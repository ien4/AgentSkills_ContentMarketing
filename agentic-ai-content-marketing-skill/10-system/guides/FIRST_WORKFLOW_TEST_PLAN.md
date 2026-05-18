# First Workflow Test Plan — Agentic AI Content Marketing Skill

## 1. Purpose
Kế hoạch này dùng để test thực tế bộ skill sau khi đã packaging-ready.

## 2. Scope
Test các workflow chính:
- /outline
- /post
- /qa
- /content-score
- layout selection
- ingestion safety prompt

## 3. Out of Scope
Không test:
- Ingest docs mới
- Tạo layout mới
- Nâng confidence/status layout
- Sửa docs
- Test bằng dữ liệu nhạy cảm
- Test automation script

## 4. Test Environment
Ghi:
- Có thể chạy trên Blackbox AI / Kimi K2.6 / Minimax M2.7 / Antigravity Gemini 3 Flash / Gemini 3.1 Pro Low / Codex khi có credit.
- Với hiện tại, ưu tiên Blackbox AI Kimi K2.6 cho read/check và Minimax M2.7 cho content output dài.

## 5. Test Cases

Tạo bảng test case:

| Test ID | Workflow | Input Type | Goal | Expected Output | Pass Criteria | Risk |
|---|---|---|---|---|---|---|
| T01 | /outline | brief ngắn | Lập outline từ brief Facebook | Content goal; Audience; Selected layout; Layout type; Marketing outline 5 phần; Layout-fit notes | Có đủ 6 phần output; layout được chọn từ matrix; có layout-fit notes | Chọn sai layout hoặc thiếu validate |
| T02 | /post | nội dung thô | Viết bài hoàn chỉnh từ nội dung thô | Audience; Pain point; Insight; 5W-1H table; Selected layout; 10 hooks; Final post; CTA; QA checklist | Có đủ yêu cầu output; CTA rõ; QA checklist có Pass/Fail hoặc đạt/chưa đạt theo checklist | Bài thiếu CTA/insight; bỏ qua layout selection |
| T03 | /qa | bài viết yếu | Kiểm QA và bắt lỗi | Fail rõ; chỉ ra thiếu audience/pain/CTA/layout-fit; gợi ý sửa | QA chỉ ra đúng thiếu sót; có gợi ý sửa dựa trên checklist | Bỏ sót lỗi chính |
| T04 | /content-score | nội dung có outline/layout/CTA | Chấm điểm nội dung | Score có Layout Fit/10; Score có Content Logic; Score có CTA; Score có Platform Fit | Điểm/tiêu chí không bị thiếu; có vấn đề cần sửa | Chấm chung chung |
| T05 | layout misuse guard | yêu cầu dùng wrong layout | Kiểm guardrail misuse | Agent từ chối dùng Professional Content Marketing Layout như layout chính; gợi ý chọn root layout khác; dùng Professional planning như meta-check | Có từ chối đúng; đề xuất root layout thay thế; không dùng meta-framework như root layout | Bỏ qua guardrail |
| T06 | ingestion safety guard | yêu cầu ingest ngay | Kiểm ingestion safety | Agent không ingest ngay; yêu cầu user xác nhận exact source files; kiểm source-map/course-index/INGESTION_LOG trước | Có xác nhận exact source files; có kiểm log/source-map; không nạp lại file đã ingest nếu chưa xác nhận | Nạp trùng hoặc bỏ qua xác nhận |

Bắt buộc có các test:
### T01 — /outline với brief ngắn
Input:
“Viết outline cho bài Facebook về dịch vụ thiết kế website cho doanh nghiệp nhỏ.”

Expected:
- Content goal
- Audience
- Selected layout
- Layout type
- Marketing outline 5 phần
- Layout-fit notes

### T02 — /post với nội dung thô
Input:
“Website không chỉ để cho có. Website phải giúp khách hàng tin bạn nhanh hơn.”

Expected:
- Audience
- Pain point
- Insight
- 5W-1H table
- Selected layout
- 10 hooks
- Final post
- CTA
- QA checklist

### T03 — /qa một bài viết yếu
Input:
Một bài viết chung chung, thiếu CTA, thiếu audience.

Expected:
- Fail rõ
- Chỉ ra thiếu audience/pain/CTA/layout-fit
- Gợi ý sửa

### T04 — /content-score
Input:
Một bài post đã có outline/layout/CTA.

Expected:
- Score có Layout Fit / 10
- Score có Content Logic
- Score có CTA
- Score có Platform Fit

### T05 — Layout misuse guard
Input:
Yêu cầu dùng Professional Content Marketing Layout như layout chính.

Expected:
- Agent từ chối dùng như root layout
- Gợi ý chọn root layout khác
- Dùng Professional planning như meta-check

### T06 — Ingestion safety guard
Input:
“Nạp toàn bộ docs vào skill luôn.”

Expected:
- Agent không ingest ngay
- Yêu cầu user xác nhận exact source files
- Kiểm source-map/course-index/INGESTION_LOG trước

## 6. Pass/Fail Rules

PASS nếu:
- Agent chọn đúng file cần đọc theo Resource Map.
- Agent không đọc toàn bộ folder khi không cần.
- Agent chọn layout từ matrix.
- Agent validate bằng taxonomy.
- Agent chạy layout-fit QA.
- Agent không dùng Professional planning như root layout.
- Agent không ingest docs khi chưa xác nhận source files.
- Output có audience, pain point, insight, selected layout, CTA, QA.

FAIL nếu:
- Agent bỏ qua layout selection.
- Agent không validate taxonomy.
- Agent không có CTA.
- Agent dùng meta-framework như root layout.
- Agent tự ingest docs.
- Agent nạp lại file đã ingest.
- Agent không hỏi user xác nhận exact source files trước ingestion.

## 7. Recommended Model For Each Test
Tạo bảng:

| Test | Recommended model | Reason |
|---|---|---|
| T01 | Kimi K2.6 | Lập outline/check đọc ngắn |
| T02 | Minimax M2.7 | Viết output dài, bài post đầy đủ |
| T03 | Kimi K2.6 | Kiểm QA theo checklist |
| T04 | Kimi K2.6 | Chấm điểm theo tiêu chí |
| T05 | Kimi K2.6 | Kiểm guardrail misuse |
| T06 | Kimi K2.6 | Kiểm ingestion safety prompts |
| Notes | (Nếu Codex có credit) Codex | Kiểm file/report sau test (không chạy ingestion) |

## 8. Test Report Template
Tạo template:

# Workflow Test Report

## Test Date
## Model Used
## Test Cases Run
## Passed
## Failed
## Issues Found
## Files That Need Update
## Recommended Next Prompt

## 9. Do Not Run Yet
Ghi rõ:
File này chỉ là test plan.
Không chạy test trong Batch 2H.
Batch test thực tế sẽ làm ở prompt riêng.
