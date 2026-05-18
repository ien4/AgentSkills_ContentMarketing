# Agentic AI Content Marketing Skill

## Start Here / Navigation Hub

### If you are an AI Agent
Read:
1. SKILL.md
2. 10-system/control/COMMAND_MAPPING.md
3. 10-system/control/PROMPT_MASTER.md
4. Relevant command file in 04-commands/
5. Relevant quality gate in 07-quality-gates/

### If you are an Operator / Team Member
Read:
1. 10-system/guides/OPERATOR_PLAYBOOK.md
2. 10-system/guides/USAGE_GUIDE.md
3. 10-system/control/COMMAND_MAPPING.md
4. 07-quality-gates/final-output-checklist.md

### If you are maintaining the skill
Read:
1. 10-system/handoff/FINAL_PACKAGING_SNAPSHOT.md
2. 10-system/handoff/HANDOFF_SUMMARY.md
3. INGESTION_LOG.md
4. 10-system/control/PACKAGING_CHECKLIST.md

### If you want to ingest new knowledge
Stop first. Read:
1. 10-system/safety/DATA_INGESTION_SAFETY.md
2. 10-system/safety/INGESTION_SOP.md
3. 00-course-knowledge/source-map.md
4. 00-course-knowledge/course-index.md
5. INGESTION_LOG.md

Then ask the user to confirm exact source files before any ingestion.

## File Role Clarification
- README.md = navigation hub for humans and maintainers.
- SKILL.md = runtime entry file for AI Agent.
- INGESTION_LOG.md = audit/history log.
- 10-system/control/ = command map, prompt master, packaging checklist.
- 10-system/safety/ = ingestion safety and SOP.
- 10-system/guides/ = daily usage guide and operator playbook.
- 10-system/handoff/ = final snapshot and handoff summary.
- 09-reports/ = historical audit trail, not daily reading material.

## Do Not Read Everything By Default
Không đọc toàn bộ hệ thống nếu task nhỏ.

- Viết Facebook post → đọc /post + layout selection + final output checklist.
- Lập outline → đọc /outline + layout taxonomy/matrix.
- QA content → đọc /qa + quality gates.
- Chấm điểm content → đọc /content-score + quality gates.
- Ingest knowledge → dừng lại và đọc safety files trước.

## What This Skill Helps With
- Phân tích brief content marketing.
- Xác định audience, pain point, insight.
- Brainstorm bằng 5W-1H.
- Chọn layout phù hợp.
- Viết outline 5 phần.
- Viết Facebook post.
- QA và chấm điểm content.
- Bảo vệ quy trình ingestion an toàn.

## Core Safety Rules
- Không ingest docs mới nếu user chưa xác nhận exact source files.
- Không dùng 5W-1H như layout chính.
- Không dùng Professional planning như root layout.
- Không nâng confidence/status layout nếu chưa có source riêng.
- Không sửa file ngoài phạm vi batch.
- Không tạo thêm file nền nếu không thật sự cần.

## Current Folder Structure
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
├── Agent_Skills.md
├── INGESTION_LOG.md
├── README.md
└── SKILL.md
```

## Next Recommended Use
Use this skill for real content work.
Do not create more foundational files.
Only plan Batch 3A after the user confirms exact source files.
