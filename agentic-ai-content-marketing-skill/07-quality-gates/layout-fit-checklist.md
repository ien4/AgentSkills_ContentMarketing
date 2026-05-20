# Layout Fit Checklist

## Purpose

Kiểm tra layout được chọn có phù hợp với mục tiêu content không.

## Required Checks

- [ ] Content goal đã rõ chưa?
- [ ] Content có đi từ Audience, Pain point, và Insight cụ thể không?
- [ ] Đã có dàn ý thô (keywords/5W-1H) có logic rõ ràng trước khi chọn layout chưa?
- [ ] Layout được chọn từ `02-frameworks/content-layout-systems/00-layout-system-control/layout-selection-matrix.md` chưa?
- [ ] Layout đã được validate lại bằng `02-frameworks/content-layout-systems/00-layout-system-control/layout-taxonomy.md` chưa?
- [ ] Layout là root layout, meta-framework, application flow hay reference layout?
- [ ] Đã chọn Root Layout theo triết lý "Xây nhà" (công năng đi trước, sáng tạo đi sau) chưa?
- [ ] Cấu trúc bài viết có hỗ trợ thói quen scanning (đọc lướt) của người đọc (sử dụng heading, in đậm, chia đoạn) không?
- [ ] Đảm bảo KHÔNG dùng công thức ứng dụng (Formulas như AIDA, PAS...) thay thế cho Root Layout?
- [ ] Bố cục bài viết có tuân thủ 5 phần chuẩn Marketing (Mở bài -> Dẫn nhập -> Thân bài -> Kết luận -> CTA) thay vì văn học 3 phần không?
- [ ] Nếu layout confidence Medium/Low, Agent có ghi cảnh báo không?
- [ ] Nếu dùng Professional Content Marketing Planning Framework, có dùng như meta-check thay vì layout chính không?
- [ ] Nếu dùng Dẫn dắt thuyết phục, có validate với Quy nạp hoặc root layout khác không?
- [ ] Nếu dùng Diễn dịch, có ghi Needs review nếu nguồn chưa đủ không?
- [ ] CTA (Call To Action) của content có phù hợp với mục tiêu chưa?

## Fail Rules

FAIL nếu:

- Chọn layout mà không có content goal.
- Chọn layout mà không kiểm taxonomy.
- Dùng Professional Content Marketing Planning Framework như layout gốc duy nhất.
- Dùng Dẫn dắt thuyết phục như layout độc lập khi chưa validate.
- Dùng Diễn dịch như layout High confidence khi source chưa đủ.
- Trộn 5W-1H vào layout.
- Trộn hook vào layout.
- Trộn CTA vào layout.
- Trộn template nền tảng vào layout.

## Output Format

Khi QA layout fit, Agent phải trả:

- Selected layout.
- Layout type.
- Source confidence.
- Why this layout fits.
- Risks.
- Pass/Fail.
- Required adjustment.

