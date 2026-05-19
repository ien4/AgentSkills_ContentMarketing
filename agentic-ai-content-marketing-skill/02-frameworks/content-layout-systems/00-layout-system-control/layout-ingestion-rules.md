# Layout Ingestion Rules

## Mục Đích

File này khóa luật nạp tài liệu về bố cục gốc để tránh trộn lẫn với framework, workflow, hook, CTA hoặc template.

## Rules

- Mỗi bố cục phải có file riêng.
- Không gom nhiều bố cục vào một file nếu chúng có nguyên lý khác nhau.
- Không nạp 5W-1H vào file bố cục nếu nội dung đó chỉ là công cụ brainstorm.
- Không nạp hook bank vào file bố cục.
- Không nạp CTA bank vào file bố cục.
- Không biến file bố cục thành template theo nền tảng.
- Nếu tài liệu nguồn chưa đủ rõ, ghi `Needs review`, không tự bịa.

## Required Sections For Each Layout File

Mỗi file bố cục phải có:

1. Định nghĩa.
2. Mục tiêu.
3. Khi nào dùng.
4. Không nên dùng khi nào.
5. Cấu trúc.
6. Ví dụ.
7. Lỗi thường gặp.
8. Checklist.
9. So sánh với bố cục dễ nhầm.
10. Source mapping.

## Source Mapping Rule

Mỗi ý quan trọng cần chỉ ra nguồn:

- Tên file trong `docs/`.
- Phần, trang hoặc đoạn nếu trích xuất được.
- File đích trong skill.
- Trạng thái: `Ingested`, `Needs review`, hoặc `Pending`.

