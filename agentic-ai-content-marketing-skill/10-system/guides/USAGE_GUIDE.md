# Usage Guide — Agentic AI Content Marketing Skill

## 1. Mục đích
Bộ skill này giúp Agentic AI hỗ trợ xây content marketing theo quy trình:  
brief → audience → 5W-1H → chọn layout → outline → viết content → QA.

## 2. Ai nên dùng
- Content writer
- Content marketing executive
- Social media content creator
- Founder/marketer muốn tự xây content
- AI agent/operator dùng Codex/Blackbox/Antigravity

## 3. Khi nào dùng skill này
- Khi cần viết Facebook post
- Khi cần lập outline
- Khi cần brainstorm ý tưởng bằng 5W-1H
- Khi cần chọn bố cục content
- Khi cần QA content
- Khi cần nạp tài liệu khóa học mới vào skill
- Khi cần kiểm tra content có đúng logic marketing không

## 4. Cách dùng nhanh cho người mới

### Case 1 — Viết bài Facebook từ nội dung thô
Người dùng đưa:
- Nội dung thô
- Mục tiêu bài
- Đối tượng đọc
- Nền tảng
- CTA mong muốn

Agent cần đọc:
1. 10-system/control/COMMAND_MAPPING.md
2. 04-commands/post.md
3. 10-system/control/PROMPT_MASTER.md
4. layout-selection-matrix.md
5. final-output-checklist.md

Output mong đợi:
- Target audience
- Pain point
- Insight
- 5W-1H analysis
- Selected layout
- Marketing outline 5 phần
- Final post
- CTA
- QA checklist

### Case 2 — Chỉ muốn lập outline
Agent đọc:
1. 04-commands/outline.md
2. layout-selection-matrix.md
3. layout-taxonomy.md
4. layout-fit-checklist.md

Output:
- Content goal
- Selected layout
- Layout type
- Outline 5 phần
- Layout-fit notes

### Case 3 — Chọn bố cục content
Agent đọc:
1. layout-selection-matrix.md
2. layout-taxonomy.md
3. file layout cụ thể
4. layout-fit-checklist.md

Output:
- Recommended layout
- Why it fits
- Risks
- Guardrails
- When not to use

### Case 4 — QA content
Agent đọc:
1. 04-commands/qa.md
2. layout-fit-checklist.md
3. content-logic-checklist.md
4. final-output-checklist.md

Output:
- Pass/Fail
- Điểm mạnh
- Lỗi logic
- Lỗi layout-fit
- Cách sửa

### Case 5 — Nạp tài liệu khóa học mới
Ghi rõ:
Trước khi nạp, Agent phải đọc:
1. 10-system/safety/DATA_INGESTION_SAFETY.md
2. 10-system/safety/INGESTION_SOP.md
3. source-map.md
4. course-index.md
5. INGESTION_LOG.md

Agent phải hỏi user xác nhận exact source files trước khi ingest.

## 5. Quy trình chuẩn khi viết content
Flow:
1. Hiểu brief
2. Xác định audience
3. Xác định pain point
4. Brainstorm 5W-1H
5. Chọn layout
6. Validate layout bằng taxonomy
7. Lập Marketing outline 5 phần
8. Viết content
9. Thêm CTA
10. QA bằng checklist

## 6. Quy tắc chọn layout
- 5W-1H dùng để mở ý.
- Layout system dùng để sắp xếp ý.
- Hook dùng để kéo chú ý.
- CTA dùng để điều hướng hành động.
- Professional planning chỉ là meta-check, không phải root layout.

## 7. Những điều không được làm
- Không nạp docs mới nếu user chưa xác nhận exact source files.
- Không đọc toàn bộ folder nếu task nhỏ.
- Không dùng Professional planning như root layout.
- Không nâng confidence/status layout nếu chưa có source phù hợp.
- Không dùng Dẫn dắt thuyết phục như layout độc lập nếu chưa validate.
- Không dùng Diễn dịch như High confidence nếu chưa có source riêng.
- Không trộn 5W-1H/hook/CTA/template vào layout.

## 8. Prompt mẫu cho người dùng
### Prompt mẫu 1 — Viết Facebook post
“Viết Facebook post về: [chủ đề]. Mục tiêu: [mục tiêu]. Audience: [đối tượng]. Nền tảng: Facebook. Nội dung thô: [nội dung thô]. CTA mong muốn: [CTA]. Tone: [tone].”

### Prompt mẫu 2 — Lập outline
“Lập outline cho bài: [chủ đề]. Content goal: [mục tiêu]. Audience: [đối tượng]. Nền tảng: Facebook/LinkedIn. Các ý chính có sẵn: [bullet thô].”

### Prompt mẫu 3 — Chọn layout
“Gợi ý layout phù hợp cho content: [mục tiêu/brief ngắn]. Audience: [đối tượng]. Lý do nên chọn layout nào? Rủi ro nếu chọn sai?”

### Prompt mẫu 4 — QA content
“QA bài viết sau trước khi đăng: [dán nội dung]. Brief/mục tiêu: [mục tiêu]. Audience: [đối tượng]. Nền tảng: [nền tảng]. Yêu cầu: đánh giá Pass/Fail và gợi ý sửa.”

### Prompt mẫu 5 — Chuẩn bị nạp tài liệu mới
“Tôi muốn nạp tài liệu khóa học mới vào skill. Source files cần nạp là: [danh sách file]. Những file nào đã ingest rồi: [danh sách]. Batch ID mới: [id]. Nạp vào folder/file đích nào: [đích]. Có update kiến thức cũ không: [có/không].”

## 9. Checklist trước khi dùng output
- Có audience chưa?
- Có pain point chưa?
- Có insight chưa?
- Có selected layout chưa?
- Layout có validate chưa?
- Có CTA chưa?
- Có QA chưa?
