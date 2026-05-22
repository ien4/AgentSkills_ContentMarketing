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

### Giai đoạn 2 — Brainstorm Mở Ý Bằng 5W-1H (5W-1H Brainstorming)
- Sử dụng framework **5W-1H** (`02-frameworks/5w1h-framework.md`) để mở rộng ý tưởng thô từ hai góc nhìn song song:
  - *Marketer's Perspective* (Góc truyền tải thương hiệu).
  - *Customer's Perspective* (Góc quan tâm thực tế của khách hàng).
- Trình bày kết quả phân tích dưới dạng bảng Markdown. Các thành phần 5W-1H không được chọn đưa vào bài viết cuối cùng phải ghi nhận rõ: `N/A — Not used in final content`.

### Giai đoạn 3 — Lựa Chọn & Thẩm Định Bố Cục (Layout Selection & Validation)
- Tra cứu bảng ma trận bố cục (`02-frameworks/content-layout-systems/00-layout-system-control/layout-selection-matrix.md`) để chọn bố cục gốc phù hợp nhất (ví dụ: *Diễn dịch* cho bài quét nhanh/phủ đầu, *Quy nạp* cho bài lập luận sâu sắc, *Liệt kê* cho danh sách lợi ích/tính năng).
- Thực hiện xác thực (validate) tính hợp lý dựa trên `02-frameworks/content-layout-systems/00-layout-system-control/layout-taxonomy.md`.
- **Kiểm soát Phạm vi Kiến thức (Knowledge Coverage Guard)**:
  - Nhóm bố cục **được hỗ trợ đầy đủ**: *Liệt kê* (C1-3A) và *Diễn dịch* (C1-3B) có đầy đủ tài liệu chi tiết chính thức trong bộ SKILL, được khuyến nghị ưu tiên sử dụng.
  - Nhóm bố cục **chưa nạp đầy đủ (bị giới hạn)**: *Quy nạp* (C1-3C), *Tổng Phân Hợp* (C1-3D), *Móc xích* (C1-3E), *Đồng tâm* (C1-3F), *Vấn đề - Giải pháp* (C1-3G), *Song hành / Đối xứng*. Các bố cục này chưa được nạp tài liệu chi tiết chính thức.
  - Nếu bài viết bắt buộc phải chọn nhóm bố cục chưa nạp đầy đủ này, Agent phải hiển thị một cảnh báo giới hạn kiến thức (**Knowledge Coverage Warning**) rõ ràng: *"Bố cục [Tên Layout] chưa được nạp tài liệu chi tiết chính thức (chưa chạy Batch C1-3C đến C1-3G). Các quy tắc cấu trúc chi tiết được áp dụng dựa trên kiến thức khái quát và có thể thiếu các hướng dẫn thực chiến nâng cao."*
- Trình bày bằng chứng **Taxonomy Validation Evidence** chứa các thông tin:
  - *Selected layout*: Tên bố cục gốc.
  - *Layout type*: Loại bố cục.
  - *Taxonomy label*: Nhãn phân loại.
  - *Confidence level*: Mức độ tin cậy.
  - *Source basis*: Nguồn gốc học liệu trong SKILL.
  - *Why this layout fits the content goal*: Giải thích sự phù hợp.
  - *Why this is not a meta-framework misuse*: Đảm bảo không lạm dụng meta-framework (như ACP hay Professional layout) làm khung bài viết chính.
  - *Knowledge Coverage Warning (nếu áp dụng)*: Ghi nhận cảnh báo giới hạn kiến thức nếu chọn bố cục chưa nạp đầy đủ, hoặc ghi "N/A - Layout fully ingested" nếu chọn Diễn dịch hoặc Liệt kê.

### Giai đoạn 4 — Lập Dàn Ý Tiếp Thị 5 Phần & Sinh Hook (Outline & Hooks)
- Lồng ghép các ý đã brainstorm vào **Marketing Outline 5 phần** chuẩn:
  1. Tiêu đề (Headline)
  2. Mô tả tiêu đề (Dẫn nhập/Hook)
  3. Thân bài (Body) - cấu trúc mạch lạc theo bố cục gốc đã chọn
  4. Kết luận (Conclusion)
  5. CTA (Call To Action)
- Tạo danh sách **10 hooks gợi ý** phù hợp với nền tảng và đối tượng độc giả.
- Chọn ra hook mạnh nhất và giải thích lý do cụ thể.

### Giai đoạn 5 — Viết Bài Hoàn Chỉnh & Kiểm Soát Dẫn Nguồn (Drafting & Marker Cleanup)
- Chấp bút viết bài post tiếp thị hoàn chỉnh dựa trên dàn ý và hook đã chọn.
- **Quy tắc dọn sạch ký hiệu dẫn nguồn thô (Raw Source Marker Cleanliness)**:
  - Tuyệt đối cấm giữ lại các chữ số trần dẫn nguồn từ việc trích xuất tài liệu (như `1`, `3`, `[1]`, v.v.) trong phần bài viết chính.
  - Gom toàn bộ thông tin đối chiếu nguồn gốc xuống bảng **Source Mapping Table** ở cuối bài viết.

### Giai đoạn 6 — Tự Thẩm Định Chất Lượng & Chấm Điểm (Self-Audit & Scoring)
- Tự động đối chiếu chất lượng bài viết với checklist `07-quality-gates/final-output-checklist.md` và `04-commands/qa.md`.
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
- **Knowledge Coverage Warning (nếu áp dụng)**: [Chỉ bắt buộc nếu chọn layout chưa nạp đầy đủ bao gồm Quy nạp C1-3C, Tổng Phân Hợp C1-3D, Móc xích C1-3E, Đồng tâm C1-3F, Vấn đề - Giải pháp C1-3G, Song hành / Đối xứng. Ghi rõ cảnh báo giới hạn kiến thức chi tiết và khuyến nghị fallback nếu cần thiết. Nếu chọn Diễn dịch hoặc Liệt kê thì ghi "N/A - Layout fully ingested"]

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
- [x] CTA phù hợp và rõ ràng.

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
- [ ] Nếu chọn các bố cục chưa nạp đầy đủ (Quy nạp, Tổng Phân Hợp, Móc xích, Đồng tâm, Vấn đề - Giải pháp, Song hành / Đối xứng), đã bổ sung cảnh báo giới hạn kiến thức (Knowledge Coverage Warning) và lý do sử dụng thay vì fallback sang Diễn dịch/Liệt kê chưa?
