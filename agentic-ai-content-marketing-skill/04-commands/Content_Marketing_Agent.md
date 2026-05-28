# Command: @Content_Marketing_Agent

- **Alias phụ**: `@AGENT Content Marketing`

## Định dạng Gọi lệnh (Invocation Format)

```txt
@Content_Marketing_Agent
Platform: [Facebook / Blog / LinkedIn / TikTok / v.v.]
Input: [Nội dung thô / Tài liệu / Brief ý tưởng]
Goal: [Mục tiêu bài viết, ví dụ: viết bài marketing giới thiệu BBO Tech]
Tone: [Tông giọng mong muốn, ví dụ: rõ ràng, tự nhiên, chuyên gia, không sáo rỗng]
```

## Khi Nào Dùng

Dùng khi cần tạo lập bài viết tiếp thị (content marketing) hoàn chỉnh cho các nền tảng mạng xã hội hoặc blog từ các nguồn thông tin thô, ý tưởng chưa cấu trúc, hoặc các brief tiếp thị ngắn gọn.

## Input Cần Có

- **Platform**: Nền tảng đăng bài mục tiêu (Facebook, Blog, LinkedIn, TikTok, v.v.) nhằm tối ưu định dạng và nhịp điệu bài viết.
- **Input**: Đoạn văn bản thô, ghi chú hoặc outline ý tưởng sơ khởi.
- **Goal**: Mục đích truyền thông/tiếp thị cụ thể.
- **Tone**: Tông giọng và phong cách hành văn mong muốn.

---

## Quy Trình Xử Lý Tự Động (Orchestration Pipeline)

Khi nhận lệnh, Agent tự động đóng vai trò là **Bộ điều phối (Orchestrator)** xâu chuỗi các tri thức và quy trình chuyên biệt đã học để xử lý nội dung qua 6 giai đoạn sau:

### Giai đoạn 1 — Phân Tích Độc Giả & Mục Tiêu (Audience & Goal Analysis)
- Đọc hiểu mục tiêu cụ thể (`Goal`) từ người dùng.
- Nhận diện chân dung khách hàng mục tiêu (`Target Audience`).
- Trích xuất các vấn đề/nỗi đau (`Pain Points`) và động cơ sâu sắc (`Insight`) của người đọc.
- **Tài nguyên kết nối**:
  - Tra cứu các vấn đề/nỗi đau phổ biến tại `06-reference-banks/pain-point-bank.md`.
  - Sử dụng mẫu brief tại `05-templates/content-brief-template.md` để cấu trúc dữ liệu đầu vào.

### Giai đoạn 2 — Brainstorm Mở Ý Bằng 5W-1H (5W-1H Brainstorming)
- Sử dụng framework **5W-1H** (`02-frameworks/5w1h-framework.md`) để mở rộng ý tưởng thô từ hai góc nhìn song song:
  - *Marketer's Perspective* (Góc truyền tải thương hiệu).
  - *Customer's Perspective* (Góc quan tâm thực tế của khách hàng).
- Trình bày kết quả phân tích dưới dạng bảng Markdown. Các thành phần 5W-1H không được chọn đưa vào bài viết cuối cùng phải ghi nhận rõ: `N/A — Not used in final content`.
- **Tài nguyên kết nối**:
  - Tuân thủ quy trình chi tiết tại `03-workflows/5w1h-brainstorming-workflow.md`.
  - Sử dụng mẫu bảng phân tích tại `05-templates/5w1h-analysis-template.md`.
  - Đối chiếu ví dụ thực tế tại `08-examples/example-5w1h-analysis.md` để phân loại đúng góc nhìn.

### Giai đoạn 3 — Lựa Chọn & Thẩm Định Bố Cục (Layout Selection & Validation)
- Tra cứu bảng ma trận bố cục (`02-frameworks/content-layout-systems/00-layout-system-control/layout-selection-matrix.md`) để chọn bố cục gốc phù hợp nhất (ví dụ: *Diễn dịch* cho bài quét nhanh/phủ đầu, *Quy nạp* cho bài lập luận sâu sắc, *Liệt kê* cho danh sách lợi ích/tính năng).
- Thực hiện xác thực (validate) tính hợp lý dựa trên `02-frameworks/content-layout-systems/00-layout-system-control/layout-taxonomy.md`.
- **Kiểm soát Phạm vi Kiến thức (Knowledge Coverage Guard)**:
  - Nhóm bố cục **được hỗ trợ đầy đủ**: *Liệt kê* (C1-3A), *Diễn dịch* (C1-3B), *Quy nạp* (C1-3C), *Tổng Phân Hợp* (C1-3D), *Móc xích* (C1-3E), *Đồng tâm* (C1-3F), *Vấn đề - Giải pháp* (C1-3G) có đầy đủ tài liệu chi tiết chính thức trong bộ SKILL, được khuyến nghị ưu tiên sử dụng.
  - Nhóm bố cục **chưa nạp đầy đủ (bị giới hạn)**: *Song hành / Đối xứng*. Các bố cục này chưa được nạp tài liệu chi tiết chính thức.
  - Nếu bài viết bắt buộc phải chọn nhóm bố cục chưa nạp đầy đủ này, Agent phải hiển thị một cảnh báo giới hạn kiến thức (**Knowledge Coverage Warning**) rõ ràng: *"Bố cục [Tên Layout] chưa được nạp tài liệu chi tiết chính thức. Các quy tắc cấu trúc chi tiết được áp dụng dựa trên kiến thức khái quát và có thể thiếu các hướng dẫn thực chiến nâng cao."*
- Trình bày bằng chứng **Taxonomy Validation Evidence** chứa các thông tin:
  - *Selected layout*: Tên bố cục gốc.
  - *Layout type*: Loại bố cục.
  - *Taxonomy label*: Nhãn phân loại.
  - *Confidence level*: Mức độ tin cậy.
  - *Source basis*: Nguồn gốc học liệu trong SKILL.
  - *Why this layout fits the content goal*: Giải thích sự phù hợp.
  - *Why this is not a meta-framework misuse*: Đảm bảo không lạm dụng meta-framework (như ACP hay Professional layout) làm khung bài viết chính.
  - *Knowledge Coverage Warning (nếu áp dụng)*: Ghi nhận cảnh báo giới hạn kiến thức nếu chọn bố cục chưa nạp đầy đủ, hoặc ghi "N/A - Layout fully ingested" nếu chọn bố cục đã được nạp đầy đủ (C1-3A đến C1-3G).
- **Tài nguyên kết nối**:
  - Đối chiếu ví dụ lựa chọn bố cục tại `08-examples/example-content-layout.md`.

### Giai đoạn 4 — Lập Dàn Ý Tiếp Thị 5 Phần & Sinh Hook (Outline & Hooks)
- Lồng ghép các ý đã brainstorm vào **Marketing Outline 5 phần** chuẩn:
  1. Tiêu đề (Headline)
  2. Mô tả tiêu đề (Dẫn nhập/Hook)
  3. Thân bài (Body) - cấu trúc mạch lạc theo bố cục gốc đã chọn
  4. Kết luận (Conclusion)
  5. CTA (Call To Action)
- Tạo danh sách **10 hooks gợi ý** phù hợp với nền tảng và đối tượng độc giả.
- Chọn ra hook mạnh nhất và giải thích lý do cụ thể.
- **Tài nguyên kết nối**:
  - Tuân thủ quy trình lập outline tại `03-workflows/raw-idea-to-outline-workflow.md`.
  - Sử dụng mẫu outline tại `05-templates/content-outline-template.md`.
  - Tham chiếu các hook mẫu tại `06-reference-banks/hook-bank.md` và đối chiếu ví dụ tốt/xấu tại `08-examples/good-vs-bad-outline.md`.

### Giai đoạn 5 — Viết Bài Hoàn Chỉnh & Kiểm Soát Dẫn Nguồn (Drafting & Marker Cleanup)
- Chấp bút viết bài post tiếp thị hoàn chỉnh dựa trên dàn ý và hook đã chọn.
- **Áp dụng Minimalist Content Mode (Chế độ Tối giản)**:
  - Bắt buộc tuân thủ bộ quy tắc tại `01-core-principles/content-marketing-mindset.md`.
  - **Quy tắc Lọc Văn AI (Avoid-list + Rewrite Rule)**:
    - *Avoid-list*: Cấm sử dụng các cụm từ sáo rỗng, rập khuôn mang tính liệt kê hoặc chuyển ý đậm chất AI như: "Trong bối cảnh hiện nay", "Có thể thấy rằng", "Nhìn chung", "Không thể phủ nhận rằng", "Sự thật là".
    - *Rewrite Rule*: Đi thẳng vào vấn đề (Get straight to the point), thay thế bằng văn phong đối thoại tự nhiên (Human-like conversational tone). Đoạn văn ngắn gọn, không lan man.
- **Quy tắc Bám sát Dữ liệu đầu vào (Input Grounding & Unsupported Claim Prevention)**:
  - **Bám sát sản phẩm/dịch vụ**: Phải viết chính xác về sản phẩm, dịch vụ hoặc chủ đề cốt lõi được cung cấp trong `Input` của người dùng. Tuyệt đối không tự ý thay đổi chủ đề hoặc tráo đổi sang sản phẩm/dịch vụ khác (ví dụ: nếu người dùng yêu cầu viết về tối ưu quảng cáo Facebook/chăm sóc khách hàng tự động, tuyệt đối không được tự ý đổi sang Agentic AI Coding / lập trình tự động).
  - **Không tự thêm số liệu (No Hallucinated Claims)**: Không được tự ý đưa vào các số liệu định lượng (như tăng doanh số 30%, tối ưu 50% chi phí, nhanh gấp 3 lần, v.v.) trừ khi các con số này được cung cấp trực tiếp trong `Input` của người dùng hoặc có bằng chứng cụ thể từ nguồn học liệu đã được nạp chính thức.
  - **Không tự claim năng lực cho thương hiệu**: Không tự tiện gán ghép hoặc khẳng định năng lực công nghệ/dịch vụ của BBO Tech trừ khi thông tin này nằm trong `Input` hoặc được dẫn xuất chính xác từ nguồn học liệu trong hệ thống.
- **Quy tắc dọn sạch ký hiệu dẫn nguồn thô (Raw Source Marker Cleanliness)**:
  - Tuyệt đối cấm giữ lại các chữ số trần dẫn nguồn từ việc trích xuất tài liệu (như `1`, `3`, `[1]`, v.v.) trong phần bài viết chính.
  - Gom toàn bộ thông tin đối chiếu nguồn gốc xuống bảng **Source Mapping Table** ở cuối bài viết.
- **Tài nguyên kết nối**:
  - Tuân thủ quy trình chuyển thể tại `03-workflows/outline-to-content-workflow.md` và `03-workflows/raw-idea-to-facebook-post-workflow.md`.
  - Sử dụng mẫu định dạng phù hợp tại `05-templates/facebook-post-template.md` (nếu platform là Facebook), hoặc tham khảo `05-templates/carousel-template.md` / `05-templates/short-video-script-template.md` khi có yêu cầu riêng biệt.
  - Tra cứu các thư viện viết sẵn tại `06-reference-banks/opening-description-bank.md` (dẫn nhập), `06-reference-banks/transition-bank.md` (chuyển tiếp ý), `06-reference-banks/conclusion-bank.md` (kết luận) và `06-reference-banks/cta-bank.md` (CTA).
  - Đối chiếu với ví dụ thực chiến tại `08-examples/good-vs-bad-facebook-post.md` và bài viết mẫu tại `08-examples/example-final-output.md`.

### Giai đoạn 6 — Tự Thẩm Định Chất Lượng & Chấm Điểm (Self-Audit & Scoring)
- Tự động đối chiếu chất lượng bài viết với checklist `07-quality-gates/final-output-checklist.md` và `04-commands/qa.md`.
- **Rà soát Grounding & Tuyên bố không căn cứ (Grounding & Unsupported Claim Audit)**:
  - **Input Grounding Check**: Đối chiếu bài viết với `Input` ban đầu để xác nhận toàn bộ thông tin cốt lõi đều bám sát thực tế, không bị lệch hoặc đổi chủ đề.
  - **Unsupported Claim Check**: Kiểm tra xem bài viết có chứa bất kỳ con số, cam kết hay khẳng định năng lực nào tự tạo không có nguồn gốc từ đầu vào hoặc tài liệu nạp không. Nếu có, bắt buộc phải loại bỏ hoặc thay thế.
- Trình bày chứng cứ logic **Content Logic Evidence** để đảm bảo tính liên kết chặt chẽ của lập luận (không nhảy cóc ý, không rời rạc):
  - *Strong idea/câu mạnh*: ...
  - *Weak idea/câu yếu*: ...
  - *Missing logic bridge*: ...
  - *Why this affects persuasion*: ...
  - *Recommended rewrite direction*: ...
- Tính điểm đánh giá tự động dựa trên tiêu chí của `/content-score` và xuất bảng điểm:
  - *Logic (Max 15)*
  - *Audience fit (Max 10)*
  - *Pain point và insight (Max 15)*
  - *Hook (Max 10)*
  - *Marketing outline 5 phần (Max 15)*
  - *Layout Fit (Max 10)*
  - *CTA (Max 10)*
  - *Platform fit (Max 15)*
  - **TỔNG ĐIỂM (Max 100)** (Mức điểm >= 80 mới đạt yêu cầu xuất bản).
- **Tài nguyên kết nối**:
  - Tuân thủ quy trình kiểm định tại `03-workflows/content-qa-workflow.md` và tối ưu lại câu chữ tại `03-workflows/content-rewrite-workflow.md`.
  - Tra cứu các checklists tương ứng trong `07-quality-gates/` để tự chấm điểm chính xác (gồm `5w1h-checklist.md`, `content-logic-checklist.md`, `layout-fit-checklist.md`, `marketing-layout-checklist.md`, `platform-fit-checklist.md`).
  - Kiểm tra và tránh lặp lại các lỗi nghiêm trọng đã được sửa đổi và ghi nhận trong lịch sử các báo cáo tại `09-reports/` (như `09-reports/BATCH_002I_FIRST_CONTROLLED_WORKFLOW_TEST_REPORT.md` và `09-reports/BATCH_002K_RETEST_FIXED_WORKFLOW_ISSUES_REPORT.md`).

---

## Output Bắt Buộc (Required Output Format)

Khi trả về kết quả cho người dùng, Agent phải trình bày theo đúng định dạng cấu trúc sau:

```markdown
# [AGENT OUTPUT] BẢN THẢO CONTENT MARKETING CỦA @Content_Marketing_Agent

## 1. Phân Tích Độc Giả & Mục Tiêu (Audience & Goal Analysis)
- **Target Audience**: ...
- **Pain Point**: ...
- **Insight**: ...

## 2. Bảng Phân Tích 5W-1H (5W-1H Analysis Table)
| Thành phần | Góc nhìn Marketer | Góc nhìn Khách hàng | Trạng thái |
|---|---|---|---|
| **Who** | ... | ... | Active |
| **What** | ... | ... | Active |
| **When** | ... | ... | [Active / N/A — Not used in final content] |
| **Where** | ... | ... | [Active / N/A — Not used in final content] |
| **Why** | ... | ... | Active |
| **How** | ... | ... | Active |

## 3. Thẩm Định Bố Cục (Layout Validation)
### Taxonomy Validation Evidence
- **Selected layout**: ...
- **Layout type**: ...
- **Taxonomy label**: ...
- **Confidence level**: ...
- **Source basis**: ...
- **Why this layout fits the content goal**: ...
- **Why this is not a meta-framework misuse**: ...
- **Knowledge Coverage Warning (nếu áp dụng)**: [Chỉ bắt buộc nếu chọn layout chưa nạp đầy đủ như Song hành / Đối xứng. Ghi rõ cảnh báo giới hạn kiến thức chi tiết và khuyến nghị fallback nếu cần thiết. Nếu chọn các layout từ C1-3A đến C1-3G thì ghi "N/A - Layout fully ingested"]

## 4. Dàn Ý Tiếp Thị 5 Phần (Marketing Outline)
- **Tiêu đề**: ...
- **Mô tả tiêu đề (Hook)**: ...
- **Thân bài (cấu trúc theo [Tên Layout])**: ...
- **Kết luận**: ...
- **CTA**: ...

## 5. Danh Sách Hook Gợi Ý (10 Suggested Hooks)
1. ...
...
10. ...
* **Hook mạnh nhất được chọn**: Hook số X
* **Lý do chọn**: ...

## 6. Bài Viết Hoàn Chỉnh (Final Content)
> [Nội dung văn bản sạch, mạch lạc, không chứa bất kỳ chữ số dẫn nguồn thô nào]

---

### Kêu Gọi Hành Động (CTA)
> [CTA tách biệt rõ ràng]

---

### Source Mapping Table
| Section | Key Knowledge / Statement | Source File | Source Marker / Paragraph | Confidence |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 7. Kết Quả Thẩm Định Chất Lượng (Quality Gate & Self-Score)
### QA Checklist
- [x] Đã chọn layout từ matrix và validate bằng taxonomy.
- [x] Đầy đủ cấu trúc Marketing outline 5 phần.
- [x] Không chứa ký hiệu dẫn nguồn thô trong văn bản chính.
- [x] Đạt yêu cầu về bám sát đầu vào (Input Grounding Check - không đổi chủ đề/sản phẩm).
- [x] Không chứa số liệu tự chế hay tuyên bố không có căn cứ (Unsupported Claim Check).
- [x] Đã áp dụng Minimalist Content Mode, đi thẳng vào vấn đề, loại bỏ hoàn toàn các từ ngữ "văn AI" trong Avoid-list.
- [x] CTA phù hợp và rõ ràng.

### Grounding & Claim Audit Evidence
- **Input Grounded Elements**: [Liệt kê cụ thể các thông tin chính từ Input được dùng trong bài viết]
- **Unsupported Claims Found & Resolved**: [Ghi rõ "None" nếu không có lỗi, hoặc liệt kê các lỗi phát hiện và cách đã chỉnh sửa/loại bỏ]

### Content Logic Evidence
- **Strong idea/câu mạnh**: ...
- **Weak idea/câu yếu**: ...
- **Missing logic bridge**: ...
- **Why this affects persuasion**: ...
- **Recommended rewrite direction**: ...

### Bảng Điểm Tự Chấm (Self-Score Table)
- **Logic**: X / 15
- **Audience fit**: X / 10
- **Pain point & Insight**: X / 15
- **Hook**: X / 10
- **Marketing outline**: X / 15
- **Layout Fit**: X / 10
- **CTA**: X / 10
- **Platform fit**: X / 15
- **TỔNG ĐIỂM**: **XX / 100**
```

---

## Cổng Kiểm Soát An Toàn (Safety Rules)

- [ ] Bài viết cuối cùng có loại bỏ hoàn toàn các ký hiệu dẫn nguồn thô (`1`, `3`, `[1]`) khỏi phần body văn bản chính không?
- [ ] Bố cục được chọn có nằm trong danh mục bố cục gốc hợp lệ của `layout-selection-matrix.md` không (Tuyệt đối không dùng meta-framework ACP hay Professional layout làm bố cục chính)?
- [ ] Bảng 5W-1H có ghi nhận rõ lý do `N/A` cho các yếu tố không dùng không?
- [ ] Có xuất đầy đủ block bằng chứng **Taxonomy Validation Evidence** và **Content Logic Evidence** không?
- [ ] Điểm tự đánh giá tổng hợp có đạt từ 80/100 trở lên để đủ điều kiện xuất bản không?
- [ ] Điểm `Layout Fit` có đạt tối thiểu từ 7/10 trở lên không?
- [ ] Nếu chọn các bố cục chưa nạp đầy đủ (như Song hành / Đối xứng), đã bổ sung cảnh báo giới hạn kiến thức (Knowledge Coverage Warning) và lý do sử dụng thay vì fallback sang các bố cục đã nạp (C1-3A đến C1-3G) chưa?
- [ ] Bài viết có bám sát sản phẩm, dịch vụ và chủ đề thực tế từ `Input` không (Tuyệt đối không tự ý đổi chủ đề/sản phẩm)?
- [ ] Toàn bộ số liệu định lượng và tuyên bố về năng lực có căn cứ xác thực từ `Input` hoặc tài liệu chính thức không (Tuyệt đối không tự chế số liệu)?
- [ ] Bài viết đã được "khử AI" theo rule Avoid-list, không lan man, sử dụng văn phong đối thoại tự nhiên theo Minimalist Content Mode chưa?
