# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **3316.0 ms**
- Average token reduction vs full source context: **5.8%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.5 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G06 | long_term | PASS | 44044.2 | 779 | 0.0% |  |
| G09 | semantic | PASS | 264.9 | 365 | 20.5% |  |
| G10 | semantic | PASS | 302.3 | 217 | 52.7% |  |
| G14 | mixed | PASS | 1633.1 | 553 | 0.0% |  |
| G03 | long_term | PASS | 1439.6 | 1316 | 0.0% |  |
| G04 | long_term | PASS | 1397.7 | 1316 | 0.0% |  |
| G07 | episodic | PASS | 266.4 | 264 | 0.0% |  |
| G08 | episodic | PASS | 249.6 | 234 | 0.0% |  |
| G11 | mixed | PASS | 1727.1 | 569 | 0.0% |  |
| G13 | mixed | PASS | 879.2 | 500 | 11.5% |  |
| G15 | mixed | PASS | 2858.9 | 831 | 0.0% |  |
| G16 | mixed | PASS | 2646.3 | 581 | 0.0% |  |
| G17 | mixed | PASS | 1758.4 | 581 | 0.0% |  |
| G18 | mixed | PASS | 586.6 | 500 | 11.5% |  |
| G19 | mixed | PASS | 1639.2 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1405.0 | 1299 | 0.0% |  |
| G12 | mixed | PASS | 1610.1 | 507 | 19.8% |  |
| G20 | mixed | PASS | 1610.3 | 756 | 0.0% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<ENTITIES> - Name: Lan Tran     Label: User     Attributes:       email:        first_name: Lan       last_name: Tran       name: Lan Tran       role_type: user       user_id: lan-lab17     Summary: The user's project is LOTUS-88. They prioritize Java and Spring Boot for their backend development and do not use Python for backend examples.   - Name: Spring Boot     Label: Topic       name: Spring Boot     Summary: Spring Boot is a framework.   - Name: Python       name: Python     Summary: Python is not used in the backend for the LOTUS-88 project.   - Name: LOTUS-88       name: LOTUS-88     Summary: LOTUS-88 is a project.   - Name: Java       name: Java     Summary: Java is a programming la`

### G09 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use expone`

### G10 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.","source":"lab-design-note","updated_at":"2026-08-13T00:00:00Z"} metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove`

### G14 - mixed

`<LONG_TERM> <ENTITIES> - Name: Lan Tran     Label: User     Attributes:       email:        first_name: Lan       last_name: Tran       name: Lan Tran       role_type: user       user_id: lan-lab17     Summary: The user's project is LOTUS-88. They prioritize Java and Spring Boot for their backend development and do not use Python for backend examples.   - Name: Spring Boot     Label: Topic       name: Spring Boot     Summary: Spring Boot is a framework.   - Name: Python       name: Python     Summary: Python is not used in the backend for the LOTUS-88 project.   - Name: LOTUS-88       name: LOTUS-88     Summary: LOTUS-88 is a project.   - Name: Java       name: Java     Summary: Java is a pr`

### G03 - long_term

`<ENTITIES> - Name: Minh Nguyen     Label: User     Attributes:       email:        first_name: Minh       last_name: Nguyen       name: Minh Nguyen       role_type: user       user_id: minh-lab17     Summary: For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos lik`

### G04 - long_term

`<ENTITIES> - Name: benchmark report     Label: Topic     Attributes:       name: benchmark report     Summary: Minh Nguyen has to complete the benchmark report before Friday at 16:00. This is open loop LAB-REPORT-1600. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </USER_SUMMARY>  <FACTS> The timestamp shown for each fact is the reference time of the source message that introduced it — i.e. w`

### G07 - episodic

`EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScr`

### G08 - episodic

`EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISOD`

### G11 - mixed

`<LONG_TERM> <ENTITIES> - Name: timeout     Label: Object     Attributes:       name: timeout     Summary: Minh Nguyen tried increasing the timeout to 60s while debugging async HTTP, but it still failed. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </USER_SUMMARY>  <FACTS> The timestamp shown for each fact is the reference time of the source message that introduced it — i.e. when the fact was`

### G13 - mixed

`<EPISODIC> EPISODE: Mai hop mentor, toi nay minh muon don open-loop. Liet ke viec chua dong, deadline, va ma dinh danh task. Can du ba manh de ghi vao note hop. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Pyth`

### G15 - mixed

`<LONG_TERM> <ENTITIES> - Name: async HTTP     Label: Topic     Attributes:       name: async HTTP     Summary: Minh Nguyen was debugging async HTTP. Minh tried increasing the timeout to 60s, but it still failed. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </USER_SUMMARY>  <FACTS> The timestamp shown for each fact is the reference time of the source message that introduced it — i.e. when the`

### G16 - mixed

`<LONG_TERM> <ENTITIES> - Name: benchmark report     Label: Topic     Attributes:       name: benchmark report     Summary: Minh Nguyen has to complete the benchmark report before Friday at 16:00. This is open loop LAB-REPORT-1600. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </USER_SUMMARY>  <FACTS> The timestamp shown for each fact is the reference time of the source message that introduced`

### G17 - mixed

`<LONG_TERM> <ENTITIES> - Name: Task     Label: Topic     Attributes:       name: Task     Summary: Minh Nguyen is learning async/await and sometimes confuses coroutine with Task. Minh requested an explanation of this topic using a timeline if encountered in the future. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </USER_SUMMARY>  <FACTS> The timestamp shown for each fact is the reference tim`

### G18 - mixed

`<EPISODIC> EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh thuc trong lab. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. Ghep hai manh: stack ca nhan cua Minh, va buoc bat buoc trong playbook  EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi`

### G19 - mixed

`<LONG_TERM> <ENTITIES> - Name: async HTTP     Label: Topic     Attributes:       name: async HTTP     Summary: Minh Nguyen was debugging async HTTP. Minh tried increasing the timeout to 60s, but it still failed. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </USER_SUMMARY>  <FACTS> The timestamp shown for each fact is the reference time of the source message that introduced it — i.e. when the`

### G05 - long_term

`<ENTITIES> - Name: Minh Nguyen     Label: User     Attributes:       email:        first_name: Minh       last_name: Nguyen       name: Minh Nguyen       role_type: user       user_id: minh-lab17     Summary: For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos lik`

### G12 - mixed

`<LONG_TERM> <ENTITIES> - Name: Minh Nguyen     Label: User     Attributes:       email:        first_name: Minh       last_name: Nguyen       name: Minh Nguyen       role_type: user       user_id: minh-lab17     Summary: For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27.  The user prefers Python for personal demos, specifically the ORCHID-27 project. The user likes Python and dislikes Java. </ENTITIES>  <USER_SUMMARY> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for person`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
