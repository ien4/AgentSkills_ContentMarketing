# Data Ingestion Safety

## Purpose
Tài liệu này bảo vệ bộ skill khỏi lỗi nạp trùng, nạp sai, ghi đè kiến thức cũ, hoặc trộn bố cục/framework.

## Golden Rule
Trước mọi bước nạp dữ liệu kiến thức mới, Agent phải yêu cầu user xác nhận exact source files.

## Required Confirmation Before New Ingestion
Agent phải hỏi hoặc yêu cầu user cung cấp:
1. File nào cần nạp?
2. File nào đã nạp rồi?
3. Batch ID mới là gì?
4. Nạp vào folder/file đích nào?
5. Có được cập nhật kiến thức cũ không?
6. Có được đổi status/confidence không?
7. Có cần giữ bản cũ không?

## Duplicate Ingestion Guard
Trước khi nạp file mới:
- Kiểm tra source-map.md.
- Kiểm tra course-index.md.
- Kiểm tra INGESTION_LOG.md.
- Kiểm tra report gần nhất.
- Nếu file đã nạp:
  - Không nạp lại tự động.
  - Ghi “already ingested”.
  - Chỉ update nếu user xác nhận.

## No Overwrite Rule
Không ghi đè:
- Definition.
- Core Principle.
- Source Mapping.
- Confidence.
- Status.
nếu chưa có lý do rõ và chưa ghi report.

## Layout Knowledge Protection
Không trộn:
- 5W-1H với layout.
- Hook với layout.
- CTA với layout.
- Template nền tảng với layout.
- Meta-framework với root layout.

## Required Report For Every Ingestion
Mỗi batch nạp dữ liệu phải có report:
- Source files scanned.
- Source files used.
- Files updated.
- Knowledge added.
- Status/confidence changes.
- Risks remaining.
- Next recommended prompt.
