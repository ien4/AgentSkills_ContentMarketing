# Batch 2J Fix Workflow Test Issues Report

## 1. Summary
Batch 2J đã sửa **2 minor workflow issues** từ Batch 2I:

- **T01**: `/outline` thiếu “taxonomy validation evidence/label” hiển thị đủ rõ trong output để agent hiểu cần output evidence/nhãn.
- **T04**: `/content-score` phần **Content Logic** còn hơi chung, chưa chỉ ra được ý/câu mạnh-yếu để recommendation actionable hơn.

## 2. Source Issue
Dựa trên report Batch 2I:

- **T01 minor**:
  - `/outline` có taxonomy validation nhưng wording chưa thể hiện đủ “evidence/label” rõ ràng.
- **T04 minor**:
  - `/content-score` có Content Logic nhưng critique còn hơi chung, chưa cụ thể hóa ý/câu mạnh/yếu để recommendation actionable.

## 3. Files Updated
- `04-commands/outline.md` ✅
- `04-commands/content-score.md` ✅
- `INGESTION_LOG.md` ✅

## 4. Fix Details

### T01 Fix — `/outline`
- Added requirement block **Taxonomy Validation Evidence** trong output bắt buộc của `/outline`.
- Required fields:
  - Selected layout
  - Layout type
  - Taxonomy label
  - Confidence level
  - Source basis
  - Guardrail checked
  - Why this layout fits the content goal
  - Why this is not a meta-framework misuse
- Explicitly intended to clarify evidence/label wording trong output.
- **No layout/confidence/status logic changed.** (Chỉ thêm yêu cầu hiển thị evidence)

### T04 Fix — `/content-score`
- Added requirement block **Content Logic Evidence** để critique Content Logic trở nên actionable hơn.
- Required fields:
  - Strong idea/câu mạnh
  - Weak idea/câu yếu
  - Missing logic bridge
  - Why this affects persuasion
  - Recommended rewrite direction
- **No scoring category removed** và không thay đổi cách tính các nhóm score hiện có.
- Layout Fit/10 giữ nguyên.
- **No recommendation added ngoài phần hướng dẫn cụ thể hóa critique** (chỉ làm rõ dữ liệu cần có trong phần critique)

## 5. What Was NOT Done
- Không ingest docs mới.
- Không sửa `docs/`.
- Không tạo layout mới.
- Không nâng confidence/status layout.
- Không tạo command mới.
- Không chạy test thực tế lại T01–T06 trong batch này.
- Không sửa framework rộng ngoài 2 command files:
  - `04-commands/outline.md`
  - `04-commands/content-score.md`

## 6. Verification Checklist
- [x] `/outline` có **Taxonomy Validation Evidence** requirement.
- [x] `/content-score` có **Content Logic Evidence** requirement.
- [x] `INGESTION_LOG.md` có section **Batch 2J — Fix Workflow Test Issues**.
- [x] Report Batch 2J tồn tại tại đúng path.
- [x] Không sửa `docs/`.
- [x] Không ingest dữ liệu mới.
- [x] Không tạo layout mới.
- [x] Không nâng confidence/status layout.
- [x] Không tạo command mới.
- [x] Không chạy test thực tế lại trong Batch 2J.
- [x] Không bịa kết quả test mới.

## 7. Remaining Risks
- Cần chạy re-test nhẹ ở **Batch 2K** để xác minh T01/T04 minor issue đã hết hoàn toàn.
- Chưa tạo Operator Playbook trong Batch 2J (theo đúng phạm vi batch).

## 8. Recommended Next Prompt
**Batch 2K — Re-test Fixed Workflow Issues**
