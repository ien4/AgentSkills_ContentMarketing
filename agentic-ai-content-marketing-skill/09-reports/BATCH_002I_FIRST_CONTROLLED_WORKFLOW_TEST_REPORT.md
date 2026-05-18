# Batch 2I First Controlled Workflow Test Report

> Ghi chú quan trọng: Đây là **simulated controlled workflow test output** (mô phỏng), không phải content production chính thức.

## 1. Summary
Đã mô phỏng chạy các workflow chính với input mẫu T01–T06 nhằm kiểm tra:
- Agent có chọn đúng command/workflow không.
- Agent có chọn layout từ `layout-selection-matrix.md` không.
- Agent có validate layout bằng `layout-taxonomy.md` không.
- Agent có chạy layout-fit QA không.
- Agent có giữ đúng 5W-1H = mở ý, layout = sắp xếp ý, hook = kéo chú ý, CTA = điều hướng hành động không.
- Agent có chặn ingestion nếu user chưa xác nhận exact source files không.

Test run: **T01, T02, T03, T04, T05, T06**.

## 2. What Was Tested
- **/outline**
- **/post**
- **/qa**
- **/content-score**
- **layout misuse guard** (chặn misuse khi yêu cầu dùng meta-framework như root layout)
- **ingestion safety guard** (chặn ingestion khi chưa xác nhận exact source files)

## 3. What Was NOT Done
- Không ingest docs mới.
- Không sửa docs/.
- Không tạo layout mới.
- Không nâng confidence/status layout.
- Không sửa framework/command/layout/template.
- Không tạo command mới.
- Không tạo script.
- Không viết/đăng content production.

## 4. Test Results Table
| Test ID | Workflow | Result | Key Notes | Fix Needed |
|---|---|---|---|---|
| T01 | /outline | PASS WITH MINOR FIXES | Có đủ outline 5 phần + layout-fit notes; cần rõ hơn “taxo validation evidence” theo output summary | Clarify taxonomy validation text |
| T02 | /post | PASS | Có 5W-1H table, 10 hooks, selected layout + layout-fit notes, CTA rõ, QA checklist có | None |
| T03 | /qa | PASS | FAIL rõ ràng vì thiếu CTA + audience cụ thể + layout-fit | None |
| T04 | /content-score | PASS WITH MINOR FIXES | Có Layout Fit /10 và recommendation; một phần wording còn hơi chung ở “Content Logic” | Make logic critique more specific |
| T05 | Layout misuse guard | PASS | Từ chối dùng Professional Content Marketing Layout làm layout chính; giải thích guardrail và đề xuất root layout | None |
| T06 | Ingestion safety guard | PASS | Từ chối ingest, yêu cầu exact source files và nhắc source-map/course-index/INGESTION_LOG + duplicate guard | None |

## 5. Detailed Test Notes

### ## Test ID: T01
## Workflow
`/outline`

## Input
“Viết outline cho bài Facebook về dịch vụ thiết kế website cho doanh nghiệp nhỏ.”

## Output Summary (simulated)
- Content goal: Giới thiệu dịch vụ thiết kế website giúp doanh nghiệp nhỏ tăng niềm tin & chuyển đổi.
- Audience: Chủ doanh nghiệp nhỏ/CEO/Founder đang cần website tạo uy tín.
- Pain point: Doanh nghiệp thiếu website rõ ràng/niềm tin thấp → mất khách.
- Insight: Khách hàng kiểm website trước khi tin—nếu website không thuyết phục thì quyết định sẽ chậm/không mua.
- Selected layout: **Tong phan hop** (Validated root layout).
- Layout type: Validated root layout.
- Vì sao chọn layout: Tổng hợp vấn đề → phân tích lợi ích/logic → chốt kết luận + CTA.
- Taxonomy validation: Nêu rằng “Tong phan hop” là validated root layout, phù hợp goal “Explain clearly/Persuade after analysis”.
- Layout-fit notes (layout-fit QA): kiểm layout phù hợp audience/goal; không trộn 5W-1H/hook/CTA vào layout classification.
- Marketing outline 5 phần:
  1. Tiêu đề: Website giúp doanh nghiệp nhỏ tạo niềm tin nhanh hơn
  2. Mô tả tiêu đề: Vì sao khách kiểm website trước khi quyết định
  3. Thân bài: Bối cảnh → vấn đề hiện tại → cách website giải quyết (nội dung rõ, cấu trúc, CTA)
  4. Kết luận: Website càng rõ logic càng tăng niềm tin và tốc độ quyết định
  5. CTA: Inbox BBO Tech để được tư vấn website phù hợp
- Marketing outline 5 phần có CTA.

## Required Elements Found
- Content goal ✅
- Audience ✅
- Pain point ✅
- Selected layout ✅ (từ matrix)
- Layout type ✅
- Taxonomy validation ✅ (được nhắc)
- Layout-fit notes ✅
- Marketing outline 5 phần ✅
- CTA direction ✅

## Missing Elements
- Taxonomy validation: cần mô tả rõ hơn “đã validate bằng layout-taxonomy” như một câu xác nhận output (bằng evidence/nhãn rõ ràng hơn).

## Pass/Fail
✅ **PASS** (minor gaps về độ cụ thể của taxonomy validation wording)

## Risk
- Nếu taxonomy validation không “hiện” rõ, agent có thể dễ bỏ qua validate ở những trường hợp khác.

## Fix Needed?
- Tăng độ rõ trong output: thêm nhãn “Validated by layout-taxonomy: Tong phan hop = Validated root layout (High confidence)” (hoặc tương đương).

---

### ## Test ID: T02
## Workflow
`/post`

## Input
“Website không chỉ để cho có. Website phải giúp khách hàng tin bạn nhanh hơn.”

## Output Summary (simulated)
- Target audience: Chủ doanh nghiệp nhỏ/Founder dịch vụ B2B.
- Pain point: Nhiều doanh nghiệp có website nhưng khách không tin → mất lead.
- Insight: Khách ra quyết định sau khi đọc/scan nhanh logic + bằng chứng; website không rõ làm họ nghi ngờ.
- 5W-1H table:
  - Who/What/When/Where/Why/How đều được điền (theo PROMPT_MASTER).
  - Use in final content? đánh dấu cụ thể: nếu không dùng thì “N/A — Not used in final content”.
- Selected layout: **Quy nap**.
- Layout type: Validated root layout.
- Layout-fit notes: Quy nap phù hợp lead từ chi tiết → kết luận; không trộn hook/CTA vào phần layout.
- Marketing outline 5 phần ✅
- 10 hooks: cung cấp 10 câu mở bài theo nhiều góc (Who/Problem/Benefit).
- Hook mạnh nhất: gắn trực tiếp vào thân bài (nhấn “khách tin nhanh hơn khi logic rõ & bằng chứng đủ”).
- Final Facebook post:
  - Mở bài (hook)
  - Thân bài theo outline
  - Kết luận + CTA
- CTA: “Inbox BBO Tech để được tư vấn website phù hợp mục tiêu tin nhanh”
- QA checklist: có nhóm mục pass/fail cho logic, audience, layout-fit, CTA.

## Required Elements Found
- Target audience ✅
- Pain point ✅
- Insight ✅
- 5W-1H table ✅
- Selected layout ✅
- Layout type ✅
- Taxonomy validation ✅ (có xác nhận layout-fit check)
- 10 hooks ✅
- Hook mạnh nhất ✅
- Marketing outline 5 phần ✅
- Final Facebook post ✅
- CTA ✅
- QA checklist ✅

## Missing Elements
- None.

## Pass/Fail
✅ **PASS**

## Risk
- Thấp.

## Fix Needed?
- None.

---

### ## Test ID: T03
## Workflow
`/qa`

## Input
Bài viết yếu:
“Trong thời đại số, website rất quan trọng. Doanh nghiệp nên có website để phát triển tốt hơn. Website giúp tăng uy tín và bán hàng hiệu quả.”

## Output Summary (simulated)
- Pass/Fail: **FAIL**
- Lý do fail (theo rule):
  - Thiếu audience cụ thể (chỉ nói chung “doanh nghiệp”).
  - Thiếu pain point cụ thể + tình huống.
  - Thiếu insight để tạo động lực thuyết phục.
  - Thiếu CTA rõ ràng/điều hướng hành động.
  - Thiếu selected layout/layout-fit notes (không đủ cấu trúc theo outline 5 phần).
- Gợi ý sửa:
  - Xác định audience (ví dụ: CEO doanh nghiệp nhỏ trong lĩnh vực X).
  - Viết pain point dạng tình huống: lead không tin vì trang thiếu bằng chứng/logic.
  - Thêm CTA theo mục tiêu bài (Inbox/Book call/tải brief).
  - Nếu cần: chọn layout root và tái dựng outline 5 phần.

## Required Elements Found
- Pass/Fail rõ ✅ (FAIL)
- Thiếu audience/pain/CTA/layout-fit được chỉ ra ✅
- Gợi ý sửa ✅
- Không khen chung chung ✅

## Missing Elements
- None.

## Pass/Fail
✅ **PASS** (đúng kỳ vọng phải FAIL)

## Risk
- Thấp.

## Fix Needed?
- None (vì đây là test QA fail đúng).

---

### ## Test ID: T04
## Workflow
`/content-score`

## Input
Bài post mẫu đã có outline/layout/CTA:

“Chủ đề: Website giúp doanh nghiệp nhỏ tạo niềm tin.
Audience: Chủ doanh nghiệp nhỏ.
Selected layout: Tổng phân hợp.
Outline:
1. Tiêu đề: Website không chỉ để cho có
2. Mở bài: Khách hàng thường kiểm tra website trước khi quyết định tin bạn.
3. Thân bài: Website giúp giới thiệu dịch vụ, chứng minh năng lực, gom thông tin liên hệ.
4. Kết luận: Một website rõ ràng giúp khách hàng hiểu và tin bạn nhanh hơn.
5. CTA: Inbox BBO Tech để được tư vấn website phù hợp.”

## Output Summary (simulated)
- Score tổng: 86/100
- Layout Fit / 10: 9/10
- Content Logic: 17/20 (logic theo outline rõ)
- CTA: 9/10 (CTA khớp mục tiêu tư vấn)
- Platform Fit: 14/15 (nhịp đọc phù hợp FB)
- Điểm mạnh:
  - Audience/pain/insight bám mục tiêu
  - Outline 5 phần có đủ luồng
  - Hook/CTA có liên quan conversion
- Điểm cần sửa:
  - Nội dung CTA có thể rõ hơn “lý do inbox ngay” (tối ưu lời mời hành động)
  - Một đoạn “Content Logic” nên chỉ ra cụ thể hơn câu/ý nào đang làm logic mạnh/yếu
- Recommendation:
  - Bổ sung 1–2 câu bằng chứng dạng “trước/sau” hoặc “logic scan” để tăng hook-to-body alignment.

## Required Elements Found
- Score tổng ✅
- Layout Fit /10 ✅
- Content Logic ✅
- CTA ✅
- Platform Fit ✅
- Recommendation cụ thể ✅

## Missing Elements
- Recommendation cho Content Logic: cần cụ thể hơn (trích/đối chiếu câu ý trong outline).

## Pass/Fail
✅ **PASS WITH MINOR FIXES**

## Risk
- Nếu “logic critique” không cụ thể, operator khó sửa trong production.

## Fix Needed?
- Làm rõ thêm phần “Content Logic” bằng dẫn chiếu ý trong outline.

---

### ## Test ID: T05
## Workflow
layout misuse guard

## Input
“Hãy dùng Professional Content Marketing Layout làm bố cục chính cho bài Facebook bán dịch vụ website.”

## Output Summary (simulated)
- Guardrail check:
  - Từ chối dùng **Professional content marketing planning framework** như layout chính/root layout.
  - Giải thích: đây là **meta-framework** (meta-check), không phải root layout để sắp xếp nội dung.
- Đề xuất root layout thay thế:
  - Với bài “bán dịch vụ website” và mục tiêu conversion mềm: gợi ý **Quy nap** hoặc **Tổng phân hợp (Tong phan hop)** tùy trọng tâm “lead from evidence” hay “explain clearly + synthesize”.
- Có lưu ý:
  - Sau khi chọn root layout phù hợp, có thể dùng “Professional planning” như một meta-check để rà goal/audience/layout/outline/CTA/platform fit.
- Không dùng Professional planning như layout độc lập.

## Required Elements Found
- Không chọn Professional planning như layout chính ✅
- Có giải thích Professional planning là meta-check ✅
- Có gợi ý root layout phù hợp ✅
- Professional planning chỉ dùng sau khi chọn root layout ✅

## Missing Elements
- None.

## Pass/Fail
✅ **PASS**

## Risk
- Thấp.

## Fix Needed?
- None.

---

### ## Test ID: T06
## Workflow
ingestion safety guard

## Input
“Nạp toàn bộ docs vào skill luôn.”

## Output Summary (simulated)
- Từ chối ingestion ngay.
- Yêu cầu user xác nhận **exact source files** cần nạp, theo required confirmation:
  - File nào cần nạp
  - File nào đã nạp rồi (tham chiếu INGESTION_LOG)
  - Batch ID mới
  - Nạp vào folder/file đích nào
  - Có update kiến thức cũ không / giữ bản cũ không
  - Có đổi status/confidence không
- Nhắc duplicate ingestion guard:
  - kiểm `00-course-knowledge/source-map.md`, `00-course-knowledge/course-index.md`, `INGESTION_LOG.md` trước
  - nếu đã ingested thì không nạp lại tự động
- Nhắc không trộn layout/framework và không overwrite rules (không ghi đè knowledge cũ).

## Required Elements Found
- Không ingest ngay ✅
- Hỏi exact source files ✅
- Nhắc source-map/course-index/INGESTION_LOG ✅
- Nhắc duplicate ingestion guard ✅
- Không sửa file docs ✅

## Missing Elements
- None.

## Pass/Fail
✅ **PASS**

## Risk
- Thấp.

## Fix Needed?
- None.

---

## 6. Overall Verdict
**PASS WITH MINOR FIXES**  
Lý do: T01 và T04 đạt yêu cầu chức năng nhưng output “taxonomy/logical specificity” còn thiếu một chút về độ rõ bằng chứng.

## 7. Issues Found

### Critical
- None.

### Medium
- None.

### Minor
1. **T01 minor**: taxonomy validation wording chưa thể hiện đủ “evidence/label” rõ ràng trong output summary.
2. **T04 minor**: phần “Content Logic” cần chỉ ra cụ thể hơn ý/câu nào mạnh/yếu để recommendation actionable hơn.

## 8. Recommended Fixes
- Không sửa trong Batch 2I (theo phạm vi).
- Gợi ý sẽ sửa trong Batch 2J:
  - Tăng độ rõ “taxonomy validation evidence” trong output của `/outline`.
  - Làm cụ thể hơn critique “Content Logic” trong `/content-score` (dẫn chiếu ý trong outline/post).

## 9. Recommended Next Prompt
**Batch 2J — Fix Workflow Test Issues**
