# Packaging Checklist — Agentic AI Content Marketing Skill

## 1. Purpose
Checklist này dùng trước khi đóng gói, chia sẻ, hoặc đưa bộ skill cho người khác sử dụng.

## 2. Required Root Files
Kiểm tra:
- SKILL.md
- README.md
- 10-system/control/COMMAND_MAPPING.md
- 10-system/control/PROMPT_MASTER.md
- INGESTION_LOG.md
- 10-system/safety/INGESTION_SOP.md
- 10-system/control/PACKAGING_CHECKLIST.md

## 3. SKILL.md Compliance
Checklist:
- YAML frontmatter hợp lệ.
- name lowercase + hyphen.
- description nói rõ skill làm gì và khi nào dùng.
- Có Trigger Conditions.
- Có Quick Start.
- Có Progressive Disclosure Rules.
- Có Resource Map.
- Không bắt agent đọc toàn bộ folder khi không cần.

## 4. Folder Structure
Checklist:
- 00-course-knowledge có course-index.md và source-map.md.
- 01-core-principles chứa nguyên tắc lõi.
- 02-frameworks chứa frameworks và content-layout-systems.
- 03-workflows chứa workflow.
- 04-commands chứa command prompt.
- 05-templates chứa template.
- 06-reference-banks chứa bank.
- 07-quality-gates chứa checklist/fail rules.
- 08-examples chứa ví dụ.
- 09-reports chứa report.

## 5. Layout Systems Safety
Checklist:
- Mỗi layout có file riêng.
- layout-taxonomy.md có Type / Status / Confidence / Guardrail.
- layout-selection-matrix.md có Layout Type / Guardrail / Confidence / Source basis.
- Diễn dịch không được nâng High nếu chưa có source riêng.
- Dẫn dắt thuyết phục không dùng như layout độc lập tuyệt đối.
- Professional content marketing planning không dùng như root layout.
- layout-fit-checklist.md tồn tại.

## 6. Data Ingestion Safety
Checklist:
- docs/ là source thô, không sửa.
- Mỗi batch ingestion phải cập nhật source-map.md.
- Mỗi batch ingestion phải cập nhật course-index.md.
- Mỗi batch ingestion phải cập nhật INGESTION_LOG.md.
- Mỗi batch ingestion phải tạo report.
- Trước khi ingest data mới, phải hỏi user xác nhận exact source files.
- Không ingest lại file đã ingest nếu chưa có lý do rõ.
- Không ghi đè kiến thức cũ nếu chưa audit.
- Nếu file đã được ingest, cần ghi “already ingested” hoặc “update required” trong source-map/report.

## 7. Quality Gates
Checklist:
- content-logic-checklist.md có rule chặn lan man.
- marketing-layout-checklist.md có fail rule cho thiếu CTA/outline.
- 5w1h-checklist.md có N/A rule.
- layout-fit-checklist.md có fail rule cho meta-framework misuse.
- final-output-checklist.md có selected layout/layout type/layout-fit check.

## 8. Reports
Checklist:
- Batch 001 report.
- Batch 002A report.
- Batch 002B report.
- Batch 002D report.
- Batch 002F report.
- Nếu thiếu report nào, ghi rõ thiếu.

## 9. Do Not Package If
Không package nếu:
- SKILL.md thiếu frontmatter.
- Không có Resource Map.
- Layout systems chưa có taxonomy/matrix.
- Có layout rủi ro bị nâng confidence sai.
- Professional planning bị dùng như root layout.
- INGESTION_LOG thiếu batch mới nhất.
- Chưa có rule hỏi user trước khi ingest dữ liệu mới.

## 10. Final Packaging Decision
Trạng thái:
- Ready
- Ready with notes
- Not ready
