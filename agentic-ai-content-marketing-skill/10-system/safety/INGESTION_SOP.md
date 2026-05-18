# Ingestion SOP — Agentic AI Content Marketing Skill

## 1. Mục Đích

File này chuẩn hóa quy trình nạp tài liệu khóa học, video, transcript, PDF hoặc DOCX vào bộ Agentic AI Content Marketing Skill.

Mục tiêu là biến tài liệu thô thành kiến thức đã xử lý, có phân loại, có source mapping, có report và có thể dùng ổn định bởi AI Agent.

## 2. Nguyên Tắc Bất Biến

- `docs/` là nguồn thô, không sửa.
- `agentic-ai-content-marketing-skill/` là nơi chứa kiến thức đã xử lý.
- Không copy nguyên văn tài liệu dài vào skill.
- Phải trích xuất, phân loại, chuẩn hóa.
- Mỗi batch phải có report.
- Mỗi kiến thức phải có source mapping.
- Không trộn framework với workflow.
- Không trộn 5W-1H với bố cục gốc.
- Không trộn hook với CTA.
- Không trộn nguyên lý nền tảng với template ứng dụng.

## Mandatory User Confirmation Before Ingestion

- Trước mọi batch nạp dữ liệu mới, Agent phải yêu cầu user xác nhận exact source files.
- Nếu source file đã từng được ingest, không ingest lại tự động.
- Nếu cần update kiến thức cũ, phải ghi rõ update target và lý do.
- Nếu không chắc file đã ingest chưa, phải kiểm `source-map.md` + `INGESTION_LOG.md` trước.

## 3. Quy Trình Nạp Tài Liệu Chuẩn

1. Scan `docs/`.
2. Chọn file nguồn cho batch.
3. Đọc từng file.
4. Tóm tắt từng file.
5. Phân loại kiến thức.
6. Xác định file đích.
7. Cập nhật đúng file.
8. Cập nhật `00-course-knowledge/course-index.md`.
9. Cập nhật `00-course-knowledge/source-map.md`.
10. Cập nhật `INGESTION_LOG.md`.
11. Tạo batch report trong `09-reports/`.
12. Kiểm tra không trộn lẫn framework.

## 4. Taxonomy Phân Loại Kiến Thức

| Loại kiến thức | Định nghĩa | Ví dụ | Nên nằm ở folder nào | Không nên nằm ở folder nào |
|---|---|---|---|---|
| Mindset | Tư duy nền điều khiển cách làm content. | AI hỗ trợ tư duy, không thay thế tư duy. | `00-course-knowledge/`, `01-core-principles/` | `05-templates/`, `06-reference-banks/` |
| Core principle | Nguyên tắc cốt lõi cần tuân thủ nhiều lần. | Outline trước khi viết. | `01-core-principles/` | `04-commands/`, `05-templates/` |
| Framework | Khung phân tích hoặc ra quyết định. | 5W-1H, audience angle. | `02-frameworks/` | `03-workflows/`, `06-reference-banks/` |
| Layout system | Nguyên lý sắp xếp ý trong nội dung. | Tổng phân hợp, quy nạp, móc xích. | `02-frameworks/content-layout-systems/` | `02-frameworks/5w1h-framework.md`, `05-templates/` |
| Workflow | Chuỗi bước thực thi một nhiệm vụ. | Raw idea to Facebook post. | `03-workflows/` | `02-frameworks/`, `06-reference-banks/` |
| Command | Giao diện tác vụ người dùng gọi trực tiếp. | `/post`, `/qa`, `/content-score`. | `04-commands/`, `10-system/control/COMMAND_MAPPING.md` | `01-core-principles/` |
| Template | Mẫu điền để triển khai output. | Facebook post template. | `05-templates/` | `02-frameworks/content-layout-systems/` |
| Checklist / Quality gate | Tiêu chí kiểm tra đạt/chưa đạt. | Content logic checklist. | `07-quality-gates/` | `03-workflows/` |
| Example | Ví dụ minh họa tốt/xấu hoặc output mẫu. | Good vs bad outline. | `08-examples/` | `01-core-principles/` |
| Reference bank | Kho câu, hook, CTA, transition dùng lại. | Hook bank, CTA bank. | `06-reference-banks/` | `02-frameworks/content-layout-systems/` |

## 5. Rule Xử Lý Tài Liệu Về Bố Cục

- 5W-1H là công cụ mở ý và brainstorming.
- Bố cục gốc là cách sắp xếp ý.
- Hook là điểm kéo sự chú ý.
- CTA là điểm điều hướng hành động.
- Template là mẫu triển khai theo nền tảng.

Các khái niệm này liên quan nhưng không được nhập chung một file.

Khi nạp tài liệu về bố cục:

- Mỗi bố cục có file riêng trong `02-frameworks/content-layout-systems/`.
- Không đưa nội dung 5W-1H vào file bố cục nếu nó chỉ phục vụ brainstorm.
- Không đưa hook bank hoặc CTA bank vào file bố cục.
- Không biến bố cục thành template nền tảng nếu tài liệu đang nói về nguyên lý sắp xếp ý.
- Nếu tài liệu nguồn chưa đủ rõ, ghi `Needs review`, không tự bịa.

## 6. Checklist Trước Khi Kết Thúc Mỗi Batch

- [ ] Đã ghi nguồn chưa?
- [ ] Đã ghi file đích chưa?
- [ ] Có tạo report chưa?
- [ ] Có cập nhật `INGESTION_LOG.md` chưa?
- [ ] Có cập nhật `course-index.md` chưa?
- [ ] Có cập nhật `source-map.md` chưa?
- [ ] Có phát hiện kiến thức trùng không?
- [ ] Có phát hiện mâu thuẫn không?
- [ ] Có file nào bị sửa ngoài phạm vi không?
- [ ] Có kiểm tra không trộn lẫn framework, workflow, layout, hook, CTA và template không?

