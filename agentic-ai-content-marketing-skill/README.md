# Agentic AI Content Marketing Skill

## Bắt đầu tại đây / Trung tâm điều hướng

### Dành cho AI Agent
Đọc:
1. SKILL.md
2. 10-system/control/COMMAND_MAPPING.md
3. 10-system/control/PROMPT_MASTER.md
4. Relevant command file in 04-commands/
5. Relevant quality gate in 07-quality-gates/

### Dành cho Operator / Team Member
Đọc:
1. 10-system/guides/OPERATOR_PLAYBOOK.md
2. 10-system/guides/USAGE_GUIDE.md
3. 10-system/control/COMMAND_MAPPING.md
4. 07-quality-gates/final-output-checklist.md

### Dành cho người bảo trì skill (Maintainer)
Đọc:
1. 10-system/handoff/FINAL_PACKAGING_SNAPSHOT.md
2. 10-system/handoff/HANDOFF_SUMMARY.md
3. INGESTION_LOG.md
4. 10-system/control/PACKAGING_CHECKLIST.md

### Nếu bạn muốn nạp kiến thức mới (ingestion)
Dừng lại. Đọc trước:
1. 10-system/safety/DATA_INGESTION_SAFETY.md
2. 10-system/safety/INGESTION_SOP.md
3. 00-course-knowledge/source-map.md
4. 00-course-knowledge/course-index.md
5. INGESTION_LOG.md

Sau đó, yêu cầu người dùng xác nhận exact source files trước khi nạp.

## Phân định vai trò các file
- README.md = trung tâm điều hướng cho người dùng và maintainer.
- SKILL.md = file khởi chạy (runtime entry) cho AI Agent.
- INGESTION_LOG.md = nhật ký nạp kiến thức/lịch sử.
- 10-system/control/ = bản đồ lệnh, prompt gốc, checklist đóng gói.
- 10-system/safety/ = quy tắc an toàn nạp dữ liệu và SOP.
- 10-system/guides/ = hướng dẫn sử dụng hàng ngày và playbook cho operator.
- 10-system/handoff/ = bản ghi trạng thái cuối và tóm tắt bàn giao.
- 09-reports/ = lịch sử report, không cần đọc hàng ngày.

## Không đọc toàn bộ hệ thống mặc định
Không đọc toàn bộ hệ thống nếu task nhỏ.

- Viết Facebook post → đọc /post + layout selection + final output checklist.
- Lập outline → đọc /outline + layout taxonomy/matrix.
- QA content → đọc /qa + quality gates.
- Chấm điểm content → đọc /content-score + quality gates.
- Ingest knowledge → dừng lại và đọc safety files trước.

## Bộ Skill này hỗ trợ gì
- Phân tích brief content marketing.
- Xác định audience, pain point, insight.
- Brainstorm bằng 5W-1H.
- Chọn layout phù hợp.
- Viết outline 5 phần.
- Viết Facebook post.
- QA và chấm điểm content.
- Bảo vệ quy trình ingestion an toàn.

## Quy tắc an toàn cốt lõi
- Không ingest docs mới nếu user chưa xác nhận exact source files.
- Không dùng 5W-1H như layout chính.
- Không dùng Professional planning như root layout.
- Không nâng confidence/status layout nếu chưa có source riêng.
- Không sửa file ngoài phạm vi batch.
- Không tạo thêm file nền nếu không thật sự cần.

## Cấu trúc thư mục hiện tại
```text
agentic-ai-content-marketing-skill/
├── 00-course-knowledge/
├── 01-core-principles/
├── 02-frameworks/
├── 03-workflows/
├── 04-commands/
├── 05-templates/
├── 06-reference-banks/
├── 07-quality-gates/
├── 08-examples/
├── 09-reports/
├── 10-system/
├── 10-system/reference/Agent_Skills.md
├── INGESTION_LOG.md
├── README.md
└── SKILL.md
```

## Bước sử dụng tiếp theo
Sử dụng skill này cho công việc content thực tế.
Không tạo thêm file nền tảng.
Chỉ lên kế hoạch Batch 3A sau khi user xác nhận exact source files.
