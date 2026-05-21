# Command: @Data_Ingestion_Agent

- **Alias phụ**: `@AGENT Nạp & Xử lý dữ liệu`

## Định dạng Gọi lệnh (Invocation Format)

```txt
@Data_Ingestion_Agent
File: docs/[exact_filename].docx
Mode: plan
```

## Khi Nào Dùng

Dùng khi cần nạp thêm kiến thức hoặc tài liệu khóa học mới (dưới dạng PDF, DOCX...) từ thư mục `docs/` vào bộ kỹ năng `agentic-ai-content-marketing-skill`.

## Input Cần Có

- **File**: Đường dẫn tuyệt đối hoặc tương đối của tệp tin nguồn nằm trong thư mục `docs/` (ví dụ: `docs/Bố Cục Liệt Kê_ Vũ Khí Tối Ưu Content Marketing C1 - 3A.docx`).
- **Mode**: Chế độ chạy:
  - `plan` (hoặc `dry-run`): Chỉ trích xuất thử, chấm điểm liên quan, phát hiện xung đột và lập kế hoạch ánh xạ tệp tin đích. Tuyệt đối không được sửa đổi các tệp tin kỹ thuật/mã nguồn của SKILL ở chế độ này.
  - `execute` (hoặc `ingest`): Thực thi nạp thật sự sau khi bản kế hoạch lập ở chế độ `plan` đã được con người (user) phê duyệt.

## Output Bắt Buộc

### Đối với Mode `plan` / `dry-run`
- **Relevance Score**: Điểm số đánh giá độ liên quan của tài liệu với Content Marketing (Yêu cầu >= 40% để tiếp tục).
- **Phân loại nguồn**: (Primary, Supporting, Duplicate, v.v.).
- **Bản tóm tắt kiến thức (Knowledge Summary)**.
- **Bản thuộc tính Marketing (Marketing Attributes)**.
- **Kết quả rà soát trùng lặp/xung đột (Conflict Check)**.
- **Bản kế hoạch ánh xạ tệp tin đích (Target Mapping Plan)**: Liệt kê rõ các tệp tin sẽ sửa đổi hoặc tạo mới trong SKILL.

### Đối với Mode `execute` / `ingest`
- **Tệp tin đã cập nhật**: Nội dung kiến thức được phân khối ngữ nghĩa (Semantic Chunking) kèm theo block Metadata chuẩn hóa Vector-Ready.
- **Source Map cập nhật**: Cập nhật thông tin nguồn học liệu vào `00-course-knowledge/source-map.md`.
- **Mục lục cập nhật**: Cập nhật danh mục kiến thức đã nạp vào `00-course-knowledge/course-index.md`.
- **Nhật ký cập nhật**: Append log chi tiết batch nạp vào tệp tin `INGESTION_LOG.md`.
- **Báo cáo kết quả nạp (Ingestion Report)**: Theo mẫu báo cáo quy định tại SOP.

## Process (Quy trình thực hiện theo SOP-02)

### Chế độ `plan` / `dry-run` (Tương ứng Step 0 đến Step 6 của SOP)
1. **Step 0 — Git Check**: Đảm bảo workspace hoàn toàn sạch sẽ (`git status --short`).
2. **Step 1 — Source Check**: Xác nhận tệp tin nguồn tồn tại trong thư mục `docs/`.
3. **Step 2 — Chấm điểm Relevance**: Chấm điểm độ liên quan. Dừng khẩn cấp nếu Relevance Score < 40%.
4. **Step 3 — Trích xuất & Làm sạch**: Đọc nội dung tệp tin nguồn, kiểm tra lỗi mã hóa/mojibake.
5. **Step 4 — Tóm tắt & Tagging**: Tóm tắt các ý chính và gắn nhãn thuộc tính marketing.
6. **Step 5 — Kiểm tra xung đột**: So khớp lý thuyết mới với các bố cục và nguyên lý cũ đã có. Nếu phát hiện mâu thuẫn không thể tự giải quyết bằng timestamp, chuyển phần tranh chấp vào vùng `#Pending_Review`.
7. **Step 6 — Đề xuất Ingestion Plan**: Liệt kê các tệp tin đích sẽ chỉnh sửa. Dừng lại chờ người dùng phê duyệt (Human-in-the-loop).

### Chế độ `execute` / `ingest` (Tương ứng Step 7 đến Step 10 của SOP)
8. **Step 7 — Thực thi nạp (Actual Ingestion)**: Cập nhật nội dung vào các file đích đã đề xuất. Phân khối ngữ nghĩa (Semantic Chunking) và gắn Vector-Ready Metadata ở đầu mỗi chunk.
9. **Step 8 — Cập nhật File Quản lý**: Ghi nhận trạng thái nguồn trong `source-map.md`, cập nhật batch trong `course-index.md`, và ghi nhận lịch sử vào `INGESTION_LOG.md`.
10. **Step 9 — Kiểm tra QA (Verification)**: Thẩm định lý thuyết, phạm vi, toàn vẹn chunk, tiếng Việt UTF-8 và tính an toàn của thư mục `docs/`.
11. **Step 10 — Sửa lỗi & Tái thẩm định**: Thực hiện sửa lỗi ngay nếu phát hiện vấn đề trong lúc QA.
12. **Step 11 — Hướng dẫn Commit**: Hướng dẫn người dùng các lệnh commit cụ thể cho 4 file đã cập nhật (Tuyệt đối không tự động commit/push hoặc dùng `git add .`).

## Checklist An Toàn (Safety Rules)

- [ ] Tài liệu nguồn có Relevance Score >= 40% không?
- [ ] Đã tách biệt xung đột kiến thức vào vùng `#Pending_Review` chưa?
- [ ] Nội dung nạp có chứa Vector-Ready Metadata với đầy đủ tags marketing không?
- [ ] Thư mục `docs/` có được giữ nguyên trạng thái untracked, không bị sửa đổi/xóa file không?
- [ ] Đã dọn sạch các file trích xuất thô hoặc file tạm (.txt, .py) chưa?
- [ ] Toàn bộ hiển thị tiếng Việt có chuẩn mã hóa UTF-8, không bị lỗi font không?
- [ ] Có tuân thủ nguyên tắc Human Approval trước khi thực hiện viết thật sự không?
- [ ] Có tránh việc tự động dùng lệnh git add hàng loạt không?
