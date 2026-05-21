# Data Ingestion Safety Rules

## 1. Non-Negotiable Rules (Nguyên tắc không thương lượng)

- **Never Ingest Without Dry-run**: Tuyệt đối không được nạp dữ liệu trực tiếp khi chưa chạy bước Dry-run để trích xuất, tóm tắt và đánh giá chất lượng tài liệu nguồn.
- **Never Modify docs/**: Thư mục `docs/` chứa tài liệu gốc thô của khóa học, tuyệt đối không được phép chỉnh sửa, đổi tên hay xóa bất kỳ file nào trong thư mục này.
- **Never Stage docs/**: Tuyệt đối không bao giờ đưa các file trong thư mục `docs/` vào git staging.
- **Never Use git add .**: Không bao giờ chạy lệnh `git add .` hay `git add -A`. Chỉ stage chính xác các file cần cập nhật/tạo mới trong scope.
- **Never Create New Layout Without Detailed Source**: Không tự ý tạo file bố cục mới khi tài liệu nguồn chưa cung cấp cấu trúc và thông tin chi tiết đầy đủ của bố cục đó.
- **Never Mark Source as Ingested Prematurely**: Chỉ đánh dấu nguồn tài liệu đã được nạp (`Ingested` hoặc `Read / Ingested`) trong `source-map.md` khi toàn bộ nội dung cốt lõi của nó đã thực sự được tích hợp vào các file kiến thức tương ứng.
- **Never Mark Supporting/Cross-check Source as Independent Ingestion**: Nếu một file đóng vai trò đối chiếu/hỗ trợ cho file chính, nó phải được hợp nhất xử lý chung trong cùng một batch và không được tính là một lượt nạp độc lập riêng lẻ.
- **Never Continue After Failed Verification**: Khi bước Verification phát hiện ra lỗi, Agent phải dừng lại để fix triệt để, không được phép tiếp tục sang bước sau.
- **Never Auto-commit**: Quy trình commit phải được thực thi thủ công/riêng biệt theo đúng bước quy định trong pipeline, không tích hợp tự động commit chung vào bước sửa file.
- **Never Proceed Before Post-commit Audit PASS**: Không chuyển sang batch tiếp theo hoặc đề xuất bước tiếp theo cho đến khi bước kiểm toán sau commit (Post-commit Audit) đạt trạng thái PASS hoàn toàn.
- **Never Ingest Low Relevance Source**: Tuyệt đối không nạp tài liệu nếu điểm độ liên quan (Relevance Score) dưới 40% (Mục 9).
- **Never Auto-overwrite On Conflict**: Tuyệt đối không tự động ghi đè kiến thức cũ khi xảy ra mâu thuẫn/xung đột mà không có bằng chứng timestamp rõ ràng (Mục 10).
- **Never Break Semantic Chunk Integrity**: Tuyệt đối không cắt chia nhỏ khối văn bản (chunks) làm vỡ ý nghĩa câu hoặc mất đi chủ ngữ/vị ngữ (Mục 11).

## 2. Source Safety (An toàn nguồn tài liệu)

- **Exact Filename Required**: Bắt buộc phải xác nhận chính xác tên file nguồn trong `docs/`. Không sử dụng tên viết tắt hoặc phỏng đoán.
- **Source Role Required**: Phải phân loại rõ rệt vai trò của từng file tài liệu tham gia vào batch (Primary, Supporting, Duplicate, Previously Ingested, New).
- **Duplicate Check Required**: Trước khi nạp bất kỳ tài liệu nào, phải quét `source-map.md` và `INGESTION_LOG.md` để kiểm tra xem nội dung của tài liệu đó đã từng được nạp chưa.
- **Review Prior Ingestions**: Nếu phát hiện tài liệu đã từng được nạp, chỉ tiến hành review/cập nhật bổ sung khi người dùng yêu cầu, không thực hiện nạp mới lại từ đầu để tránh trùng lặp.

## 3. Knowledge Safety (An toàn nội dung kiến thức)

- **No Hallucinated Theory**: Tuyệt đối không bịa đặt hoặc tự sáng tác ra lý thuyết, thuật ngữ mới nằm ngoài tài liệu giảng dạy gốc.
- **Mark Internal Examples**: Nếu cần đưa ra ví dụ minh họa tự xây dựng để giải thích lý thuyết, phải ghi chú rõ ràng đó là "Ví dụ minh họa nội bộ của Agent" (Internal Agent Example), tránh gây nhầm lẫn với ví dụ gốc từ giảng viên.
- **No Long Verbatim Copying**: Không sao chép nguyên văn các đoạn văn dài của tài liệu thô vào bộ SKILL. Phải tóm tắt, sơ đồ hóa, cấu trúc hóa để AI dễ sử dụng và tối ưu dung lượng.
- **No Source Scope Expansion**: Chỉ tập trung trích xuất đúng phạm vi bài học được yêu cầu. Không tự ý mở rộng sang các chương/bài học khác khi chưa đến batch tương ứng.
- **No Mixing Source Lessons**: Giữ nguyên tính độc lập của từng bài học/chương. Không trộn lẫn kiến thức của bài học này sang bài học khác trong quá trình nạp.

## 4. Layout Safety (An toàn hệ thống bố cục)

- **Strict Concept Separation**: Phải phân tách rạch ròi giữa Bố cục gốc (Root Layout), Công thức viết (Formula), Framework phân tích (Framework), và Quy trình hỗ trợ (Supporting Process):
  - **5W-1H** là framework phân tích/mở ý, tuyệt đối không được coi là một layout.
  - **ACP (Architectural Content Process)** là quy trình hỗ trợ xây dựng nội dung, không phải là một root layout.
  - **AIDA / PAS** là các công thức viết bài ứng dụng (Formulas), không phải là root layouts.
- **Pending Layout Status**: Các bố cục chưa được nạp tài liệu chi tiết (như bố cục Đồng tâm, Song hành) phải được giữ ở trạng thái `Pending` trong `layout-taxonomy.md`, không được đánh dấu hoàn thành.
- **No Premature File Creation**: Không tạo bất kỳ file bố cục trống hoặc file bố cục tạm thời nào khi chưa nạp tài liệu nguồn chi tiết cho chúng.

## 5. Git Safety (An toàn kiểm soát mã nguồn)

- **Exact Staging**: Chỉ stage các file thực sự thay đổi trong scope của batch bằng lệnh chỉ định chính xác tên file.
- **No Git Wildcards**: Tuyệt đối cấm sử dụng `git add .`, `git add *`, `git add -u`.
- **No Unauthorized Git Destructive Commands**: Tuyệt đối không dùng các lệnh `git reset`, `git restore`, `git rebase`, `git merge`, `git commit --amend` trừ khi được người dùng yêu cầu trực tiếp bằng văn bản.
- **Verify-First Commits**: Chỉ commit sau khi đã chạy verification và đạt kết quả PASS.
- **Scope Verification Before Commit**: Chạy `git status` trước khi commit để rà soát danh sách file staged, đảm bảo không có file thừa hoặc file docs/ bị lọt vào commit.
- **Remote Sync Audit**: Trước khi kết thúc, đảm bảo trạng thái branch cục bộ đồng bộ hoàn toàn với remote (`origin/main`), tránh bị drift.

## 6. Pre-Batch Ingestion Safety Checklist (Checklist an toàn trước mỗi Batch)

*Trước khi bắt đầu bất kỳ Batch nạp dữ liệu nào, Agent phải tự kiểm tra và trả lời "Có" cho tất cả các câu hỏi dưới đây:*

- [ ] Workspace hiện tại có hoàn toàn sạch không (`git status` chỉ hiển thị `?? docs/`)?
- [ ] Đã có sự xác nhận của người dùng về chính xác tên file nguồn cần nạp chưa?
- [ ] Đã xác định rõ vai trò của từng file nguồn (Primary, Supporting, Duplicate...) chưa?
- [ ] Đã quét `source-map.md` để đảm bảo file nguồn chưa từng được nạp chưa?
- [ ] Đã hiểu rõ file đích cần cập nhật và taxonomy tương ứng chưa?
- [ ] Đã cam kết tuyệt đối không sửa đổi file trong `docs/` và không dùng `git add .` chưa?

---

## 7. Incident Recovery Safety Rules (Quy tắc an toàn khi xử lý sự cố)

- **Stop Immediately**: Khi phát hiện nạp sai hoặc mâu thuẫn lý thuyết, phải DỪNG NGAY LẬP TỨC. Không được cố cứu vãn bằng cách nạp tiếp các phần khác.
- **No Blind Reverts**: Không được tự ý chạy lệnh phục hồi git diện rộng như `git reset --hard` hay `git checkout .` mà không xác định cụ thể danh sách file bị ảnh hưởng, để tránh làm mất các cấu hình hoặc file untracked quan trọng của người dùng.
- **No Hiding Incidents**: Mọi sự cố nạp sai phải được ghi nhận rõ ràng vào báo cáo (report) và thông báo cho người dùng, tuyệt đối không âm thầm sửa lỗi mà không báo cáo.
- **Verify-After-Fix**: Mọi file sau khi được fix/revert do nạp sai bắt buộc phải trải qua quy trình Verification đầy đủ từ đầu.

---

## 8. Ingestion History Recovery Safety Rules (Quy tắc an toàn đối chiếu lịch sử)

- **History Integrity**: Không bao giờ được phép chỉnh sửa, xóa hoặc thay đổi lịch sử của các batch trước trong `INGESTION_LOG.md` ngoại trừ việc sửa lỗi chính tả hoặc cập nhật link file bị hỏng. Nhật ký batch cũ là bất di bất dịch.
- **No Assumption of History**: Không bao giờ giả định một tài liệu đã được nạp nếu nó chưa có mặt trong cả 3 vị trí đối chiếu chéo (`source-map.md`, `course-index.md`, `INGESTION_LOG.md`).
- **Conflict Stop**: Nếu có sự bất nhất giữa lịch sử ghi nhận trong log và nội dung thực tế ở các file đích, Agent phải coi đây là một Stop Condition (điều kiện dừng) để báo cáo.

---

## 9. Relevance Scoring Safety Rules (Quy tắc an toàn tính điểm liên quan)

- **Mandatory Score Calculation**: Bắt buộc phải tính Relevance Score cho mọi tài liệu nguồn chính (Primary Source) trước khi nạp dữ liệu.
- **Enforce Threshold Gate**: Nếu score đánh giá dưới 40%, bắt buộc phải dừng quy trình nạp, đưa ra cảnh báo lạc đề và ghi nhận vào log/báo cáo. Cấm mọi hành vi bỏ qua bước kiểm tra điểm này.

---

## 10. Conflict Resolution Safety Rules (Quy tắc an toàn giải quyết xung đột)

- **Strict Date Comparison**: Khi phát hiện mâu thuẫn lý thuyết, bắt buộc phải đối chiếu chéo thuộc tính Timestamp của hai nguồn dữ liệu.
- **Isolation of Conflict**: Nếu không có thông tin Timestamp tin cậy hoặc ngày cập nhật bằng nhau, cấm tự ý chọn một bên để ghi đè. Bắt buộc phải đóng gói vùng mâu thuẫn vào thẻ `#Pending_Review` kèm theo giải thích lý do và nguồn gốc của cả hai bên.

---

## 11. Semantic Chunking Safety Rules (Quy tắc an toàn phân khối ngữ nghĩa)

- **Grammar & Sentence Integrity**: Khi chia khối tài liệu (chunking), cấm việc chia cắt nửa chừng câu làm mất liên kết ngữ pháp cơ bản (chủ ngữ - vị ngữ).
- **Structure-Preserved Tables**: Cấm trích xuất bảng biểu thô sơ thành các dòng chữ rời rạc. Phải cấu trúc hóa bảng biểu thành dạng Markdown Table hoặc JSON format để bảo toàn mối tương quan cột/hàng.
- **Hyperlink Preservation**: Hyperlink trong tài liệu nguồn phải được bảo toàn đúng cú pháp liên kết Markdown, không được làm hỏng đường dẫn URL hoặc bỏ qua liên kết.
- **Context Attachment**: Mỗi chunk kiến thức phải đi kèm Heading Path để đảm bảo khi đọc rời rạc, AI Agent vẫn hiểu rõ ngữ cảnh của phần kiến thức đó.

---

## 12. Enrichment & Tagging Safety Rules (Quy tắc an toàn gắn thẻ dữ liệu)

- **No Over-Tagging / Fabrication**: Chỉ gắn các thẻ marketing (#Target_Audience, #Pain_Point, #Angle, #Brand_Voice, #Use_Case, #Content_Format) dựa trên thông tin thực tế được đề cập trực tiếp hoặc suy luận logic mạnh từ nội dung bài học. Cấm tự chế các tag không liên quan để tránh làm nhiễu công cụ tìm kiếm ngữ nghĩa.
- **Standard Tag Format**: Các marketing tag phải tuân theo đúng định dạng chữ thường, ngăn cách bằng dấu gạch dưới (ví dụ: `#audience_b2b`, `#painpoint_bi_y_tuong`).
