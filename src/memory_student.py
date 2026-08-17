from __future__ import annotations

import re
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query
from .zep_common import prime_eval_thread, render_graph_search

# Zep's get_user_context returns one string with <TAG>...</TAG> sections
# (USER_SUMMARY, EPISODES, FACTS, ENTITIES, THREADS, ...). Under a tight
# token budget, assemble_context keeps only the head of that string, so a
# literal marker sitting inside a late section (ENTITIES tends to carry the
# most specific, marker-bearing summaries) can get trimmed away even though
# it is highly relevant. Reordering sections front-loads the ones most
# likely to carry the literal evidence a case needs.
_CONTEXT_SECTION_RE = re.compile(r"<(\w+)>(.*?)</\1>", re.DOTALL)
_CONTEXT_SECTION_PRIORITY = ("ENTITIES", "USER_SUMMARY", "FACTS", "EPISODES", "THREADS")


def _dedupe_lines(text: str) -> str:
    seen: set[str] = set()
    kept: list[str] = []
    for line in text.split("\n"):
        key = line.strip()
        if key and key in seen:
            continue
        if key:
            seen.add(key)
        kept.append(line)
    return "\n".join(kept)


def _prioritize_context_block(text: str) -> str:
    sections = {m.group(1): m.group(2).strip() for m in _CONTEXT_SECTION_RE.finditer(text)}
    if not sections:
        return text
    ordered = []
    for name in _CONTEXT_SECTION_PRIORITY:
        if name in sections:
            ordered.append(f"<{name}>\n{_dedupe_lines(sections.pop(name))}\n</{name}>")
    for name, content in sections.items():
        ordered.append(f"<{name}>\n{_dedupe_lines(content)}\n</{name}>")
    return "\n\n".join(ordered)


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        prime_eval_thread(self.client, user_id, thread_id, query)
        context = self.client.thread.get_user_context(thread_id=thread_id)
        parts = [_prioritize_context_block(context.context or "")]

        # Bonus: a higher-limit edges search catches deadline/open-loop facts
        # that the context block's own relevance cutoff can miss.
        try:
            edges = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            edges_text = render_graph_search(edges)
            if edges_text:
                parts.append(edges_text)
        except Exception:
            pass

        return "\n".join(p for p in parts if p and p.strip())

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # limit=10 rather than the lab's baseline 5: prime_eval_thread (called
        # by retrieve_long_term) adds each evaluated query as a new message to
        # the same user graph, so by the time later mixed/long_term-adjacent
        # cases run, the user's episode graph has accumulated many unrelated
        # "evaluation query echo" episodes. A wider top-K gives the actually
        # relevant episode more room to survive that ranking noise.
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=7,
        )
        return render_graph_search(results, episode_char_cap=250)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        results = self.client.graph.search(
            graph_id=graph_id,
            query=cap_query(query),
            scope="episodes",
            limit=8,
        )
        text = render_graph_search(results)
        if not text.strip():
            fallback = self.client.graph.search(
                graph_id=graph_id,
                query=cap_query(query),
                scope="nodes",
                limit=8,
            )
            text = render_graph_search(fallback)
        return text

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        return self.budget.assemble(layers)
