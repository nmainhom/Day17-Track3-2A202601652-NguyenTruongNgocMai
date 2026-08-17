# README_submission — Lab 17 Multi-Memory Agent

## Kết quả benchmark

- Practice: **11/11 PASS (100%)** — `reports/benchmark.md`.
- Baseline no-memory: **2/11 (18.2%)** — `reports/benchmark_no_memory.md`.
- Golden: **20/20 PASS, bonus 10/10** — `reports/golden_benchmark.md`.
- So sánh: `reports/comparison.md`.

## 3 câu bắt buộc

**1. Layer quan trọng nhất trong bộ test này?**
`long_term` quyết định 4/11 case (E02, E03, E08, E09) và tham gia E07. Layer duy nhất xử lý **recency/conflict** (E08: BLUEBIRD-42 phải TypeScript/NestJS, ghi đè preference Python cho ORCHID-27) và **user isolation** (E09: Lan chỉ thấy LOTUS-88/Java, không leak dữ liệu Minh).

**2. Trade-off Context Block (Zep) vs tự build Redis + Qdrant?**
Zep quản lý ingestion/ranking qua vài API call — nhanh, nhưng managed nên ít kiểm soát nội bộ. Tự build Redis + Qdrant cho toàn quyền schema/chi phí, đổi lại tự viết summarization, conflict resolution, extraction.

**3. Guardrail chống memory poisoning?**
`control_plane/AGENTS.md`: durable write giữ `source/timestamp/confidence/scope`; heartbeat không được tự cấp quyền hay chèn instruction mới; conflict dùng "recency + scope" thay vì xóa fact cũ, giữ provenance để audit.

## 4 câu phân tích benchmark

1. **Layer hit rate thấp nhất:** cả 4 layer đạt 100%. Rủi ro mở rộng cao nhất ở `long_term` vì phụ thuộc `USER_SUMMARY` Zep tự tổng hợp, ít kiểm soát hơn `graph.search(scope="episodes")` tường minh.
2. **Query nhiều token nhất:** E02 (long_term) — **1339 token**, do Context Block gộp USER_SUMMARY dài lẫn episode nguồn.
3. **E07 (mixed):** kết hợp `long_term` (Python của Minh) + `semantic` (Idempotency-Key). Evidence bắt buộc: `Python`, `Idempotency-Key`.
4. **Token reduction:** student **20.9%**, no-memory **81.8%** nhưng hit rate 18.2%. No-memory "giảm token" vì không retrieve gì — reduction chỉ có nghĩa khi đọc cùng hit rate.

## E08 (recency) và E10 (compaction)

- **E08:** cập nhật BLUEBIRD-42 sang TypeScript/NestJS, Context Block ưu tiên fact mới theo scope dự án; preference Python cho ORCHID-27 vẫn giữ ở scope khác — rule "recency + scope" (`control_plane/MEMORY.md`).
- **E10:** sliding window nén filler turn thành `SESSION_SUMMARY`, tách `REVIEW-DEADLINE-1600` vào `DURABLE_NOTES`; giảm `max_recent_messages` 6→4, deadline vẫn sống.

## Ghi chú golden (debug thật)

18/20 lần đầu: marker cần thiết nằm cuối chuỗi `retrieve_long_term`, bị trim mất theo budget 4% → ưu tiên khối `<ENTITIES>` lên đầu. `prime_eval_thread` ghi mỗi query vào graph user, chạy `--golden` lặp lại gây nhiễu episodic search → tăng `limit=7`, giảm `episode_char_cap=250`, seed sạch trước lần chạy chính thức → **20/20**.
