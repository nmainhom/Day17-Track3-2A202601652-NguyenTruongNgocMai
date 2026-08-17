# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **730.5 ms**
- Average token reduction vs full source context: **14.2%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 896.1 | 148 | 67.8% |  |
| E09 | long_term | PASS | 1097.6 | 796 | 0.0% |  |
| E10 | short_term | PASS | 0.5 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1544.0 | 1311 | 0.0% |  |
| E03 | long_term | PASS | 1173.9 | 1301 | 0.0% |  |
| E04 | episodic | PASS | 232.2 | 312 | 0.0% |  |
| E05 | episodic | PASS | 223.9 | 311 | 0.0% |  |
| E07 | mixed | PASS | 1413.0 | 485 | 14.2% |  |
| E11 | semantic | PASS | 210.7 | 146 | 74.2% |  |
| E08 | long_term | PASS | 1243.6 | 1266 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata=`

### E09 - long_term

`<ENTITIES> - Name: LOTUS-88     Attributes:       name: LOTUS-88     Summary: LOTUS-88 is a project. Lan Tran is associated with LOTUS-88 and prioritizes Java and Spring Boot for backend examples, not Python.   - Name: Python     Label: Topic       name: Python     Summary: Python is not used in the backend for the LOTUS-88 project.   - Name: Lab Assistant     Label: Assistant       name: Lab Assistant     Summary: Lab Assistant is identified as LOTUS-88. Lab Assistant uses Java for backend examples. Lab Assistant uses Spring Boot for backend examples. </ENTITIES>  <USER_SUMMARY> The user's project is LOTUS-88. They prioritize Java and Spring Boot for their backend development and do not use`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<ENTITIES> - Name: Java     Label: Topic     Attributes:       name: Java     Summary: Minh Nguyen dislikes Java. Da Hieu demoed the ORCHID-27 personal demo, prioritizing Python and avoiding Java, providing a short example. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </USER_SUMMARY>  <FACTS> The timestamp shown for each fact is the reference time of the source message that introduced it — i`

### E03 - long_term

`<ENTITIES> - Name: timeout     Label: Object     Attributes:       name: timeout     Summary: Minh Nguyen attempted to increase the timeout to 60s while debugging async HTTP, but the attempt failed. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </USER_SUMMARY>  <FACTS> The timestamp shown for each fact is the reference time of the source message that introduced it — i.e. when the fact was fir`

### E04 - episodic

`EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh. EPISODE: Sep hoi chuan hoa backend du an cong ty, minh hay lan voi stack project rieng. Rieng du an cong ty cua Minh: bat buoc ngon ngu va framework nao? Python ca nhan co duoc dung backend du an do khong? Scope dung theo du an cong ty. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat `

### E05 - episodic

`EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. Ghep hai manh: stack ca nhan cua Minh, va buoc bat buoc trong playbook  EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASY`

### E07 - mixed

`<LONG_TERM> <ENTITIES> - Name: Python     Label: Topic     Attributes:       name: Python     Summary: Minh Nguyen likes Python, which is used for personal demos like ORCHID-27. For company project BLUEBIRD-42, TypeScript with NestJS is required for the backend, not Python. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </USER_SUMMARY>  <FACTS> The timestamp shown for each fact is the referenc`

### E11 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata=`

### E08 - long_term

`<ENTITIES> - Name: Minh Nguyen     Label: User     Attributes:       email:        first_name: Minh       last_name: Nguyen       name: Minh Nguyen       role_type: user       user_id: minh-lab17     Summary: For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos lik`
