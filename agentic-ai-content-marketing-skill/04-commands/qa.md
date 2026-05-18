# Command: /qa

## Khi Nào Dùng

Dùng để kiểm tra bản content cuối.

## Input Cần Có

- Nội dung.
- Brief.
- Audience.
- Mục tiêu.
- Nền tảng đăng.

## Output Bắt Buộc

- Checklist đạt/chưa đạt.
- Lỗi logic.
- Lỗi audience.
- Lỗi CTA.
- Gợi ý chỉnh sửa cuối.

## QA Scope

Kiểm tra theo thứ tự:

1. Brief và mục tiêu.
2. Audience, pain point và insight.
3. 5W-1H analysis table nếu task có bước brainstorm.
4. Marketing outline 5 phần nếu task có bước lập dàn ý.
5. Layout-fit check: selected layout must match content goal and must not be a meta-framework used as root layout.
6. Hook và độ khớp với thân bài.
7. CTA và độ khớp với mục tiêu.

## Fail Conditions

- FAIL nếu thiếu audience.
- FAIL nếu thiếu pain point.
- FAIL nếu thiếu insight trong bài cần persuasion hoặc conversion.
- FAIL nếu selected layout không được validate bằng taxonomy.
- FAIL nếu dùng meta-framework như layout chính.
- FAIL nếu CTA không liên quan mục tiêu.
- FAIL nếu nội dung chung chung, không có tình huống cụ thể.
