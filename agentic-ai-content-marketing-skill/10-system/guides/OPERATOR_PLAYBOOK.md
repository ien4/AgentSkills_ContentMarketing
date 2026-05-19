# Practical Operator Playbook — Agentic AI Content Marketing Skill

## 1. Mục Đích
Playbook này giúp operator/đồng nghiệp dùng bộ **agentic-ai-content-marketing-skill** đúng quy trình thực chiến, không cần hiểu toàn bộ cấu trúc bên trong ngay từ đầu.

Mục tiêu vận hành:
- Chọn đúng command theo nhu cầu (post/outline/qa/content-score/ingestion).
- Đọc đúng “resource map” cần thiết.
- Bảo vệ output bằng checklist & quality gates.
- Thực thi **progressive disclosure**: chỉ ingest khi user xác nhận **exact source files**.

## 2. Ai Nên Dùng
- Content writer / content marketer
- Social media content creator
- Content marketing executive
- Founder/marketer
- AI operator dùng Blackbox/Kimi/Minimax/Antigravity/Codex
- Người quản lý muốn kiểm output content trước khi đăng

## 3. Nguyên Tắc Vận Hành Cốt Lõi
Operator vận hành theo nguyên tắc:
1. **Brief trước** (đọc mục tiêu, audience, platform, CTA).
2. **Audience trước** (xác định ai, level hiểu biết, nhu cầu).
3. Dùng **5W-1H** để mở ý (brainstorm), **không dùng làm bố cục chính**.
4. **Layout để sắp xếp ý** (chọn layout từ matrix, validate taxonomy, kiểm layout-fit).
5. **Hook để kéo chú ý** (đưa vào mở bài đúng vai trò).
6. **CTA để điều hướng hành động** (conversion component, không trang trí).
7. **QA trước khi dùng output** (logic + layout-fit + final-output checklist).
8. **Ingestion safety**: không ingest docs mới nếu user chưa xác nhận exact source files.

## 4. Bắt Đầu Nhanh Cho Operator Mới

### Nếu muốn viết Facebook post
**Đọc:**
1. `10-system/control/COMMAND_MAPPING.md`
2. `04-commands/post.md`
3. `10-system/control/PROMPT_MASTER.md`
4. `02-frameworks/content-layout-systems/00-layout-system-control/layout-selection-matrix.md`
5. `07-quality-gates/layout-fit-checklist.md`
6. `07-quality-gates/final-output-checklist.md`

**Operator cần yêu cầu user cung cấp (input tối thiểu):**
- Nội dung thô / chủ đề sản phẩm
- Mục tiêu bài viết (goal)
- Đối tượng đọc (audience)
- Nền tảng đăng (platform: Facebook/LinkedIn…)
- CTA mong muốn
- Tone giọng (nếu có)

**Output cần kiểm (must-have):**
- Audience
- Pain point
- Insight
- **5W-1H table** (nếu prompt cần mở ý)
- Selected layout + layout type
- **Taxonomy validation** (taxonomy label + evidence/guardrail)
- **10 hooks**
- Marketing outline **5 phần**
- Final post
- CTA
- QA checklist (logic + final output)

**Fail nhanh nếu thiếu:**
- Thiếu audience/pain/insight hoặc thiếu CTA → dừng và yêu cầu bổ sung trước khi post.

---

### Nếu muốn lập outline
**Đọc:**
1. `04-commands/outline.md`
2. `02-frameworks/content-layout-systems/00-layout-system-control/layout-selection-matrix.md`
3. `02-frameworks/content-layout-systems/00-layout-system-control/layout-taxonomy.md`
4. `07-quality-gates/layout-fit-checklist.md`

**Output cần kiểm:**
- Content goal
- Audience
- Selected layout + layout type
- **Taxonomy Validation Evidence** (nhãn/bằng chứng theo taxonomy)
- Marketing outline 5 phần
- CTA direction

**Luật bắt buộc:**
- Chọn layout từ matrix → validate taxonomy → kiểm layout-fit.
- Không dùng meta-framework như root layout.

---

### Nếu muốn QA bài viết
**Đọc:**
1. `04-commands/qa.md`
2. `07-quality-gates/content-logic-checklist.md`
3. `07-quality-gates/layout-fit-checklist.md`
4. `07-quality-gates/final-output-checklist.md`

**Output cần kiểm:**
- PASS/FAIL rõ
- Lỗi audience/pain/insight (nếu có)
- Lỗi layout-fit (nếu có)
- Lỗi CTA (nếu có)
- Gợi ý sửa cụ thể theo thứ tự ưu tiên

**Nguyên tắc xử lý fail:**
- Không đoán nguyên nhân; phải bám checklist/lỗi cụ thể.

---

### Nếu muốn chấm điểm content
**Đọc:**
1. `04-commands/content-score.md`
2. `07-quality-gates/layout-fit-checklist.md`
3. `07-quality-gates/final-output-checklist.md`

**Output cần kiểm:**
- Total score
- Layout Fit / 10
- **Content Logic Evidence**
- CTA score
- Platform fit
- Recommendation cụ thể

---

### Nếu muốn nạp tài liệu mới (ingestion)
**Đọc trước (bắt buộc):**
1. `10-system/safety/DATA_INGESTION_SAFETY.md`
2. `10-system/safety/INGESTION_SOP.md`
3. `00-course-knowledge/source-map.md`
4. `00-course-knowledge/course-index.md`
5. `INGESTION_LOG.md`

**Bắt buộc hỏi user (không ingest nếu chưa trả lời):**
- Exact source files nào cần ingest?
- File nào đã ingest rồi?
- Batch ID mới là gì?
- Nạp vào file/folder nào?
- Có được update kiến thức cũ không?
- Có được đổi status/confidence không?

**Safety stop:**
- Nếu user chưa xác nhận exact source files → dừng ingestion và yêu cầu xác nhận.

## 5. Quy Trình Vận Hành Hàng Ngày
Workflow thực tế cho operator (lặp mỗi task):

1. Nhận yêu cầu từ user.
2. Xác định loại task:  
   - `/post` | `/outline` | `/qa` | `/content-score` | ingestion
3. Tra `10-system/control/COMMAND_MAPPING.md` để biết input/output contract.
4. Chọn command phù hợp.
5. Đọc đúng file theo resource map của SKILL (chỉ “đủ dùng”, không audit toàn folder).
6. Nếu viết content: phân tích audience/pain/insight.
7. Nếu cần mở ý: dùng **5W-1H** (5W-1H để brainstorm, không làm layout).
8. Chọn layout từ `layout-selection-matrix.md`.
9. Validate layout bằng `layout-taxonomy.md`.
10. Tạo outline 5 phần (hoặc viết post theo outline).
11. Viết output (hoặc rewrite nếu được yêu cầu).
12. QA bằng checklist:
    - content logic
    - layout fit
    - final output checklist
13. Nếu fail: sửa theo checklist, không đoán.
14. Nếu task là ingestion: dừng và hỏi exact source files theo ingestion safety.

## 6. Cây Quyết Định (Decision Tree)
- User muốn viết bài hoàn chỉnh?
  → Dùng `/post`
- User chỉ muốn dàn ý?
  → Dùng `/outline`
- User muốn kiểm/bắt lỗi bài?
  → Dùng `/qa`
- User muốn chấm điểm content?
  → Dùng `/content-score`
- User yêu cầu nạp tài liệu khóa học mới?
  → Dừng → đọc `10-system/safety/DATA_INGESTION_SAFETY.md` → hỏi **exact source files** → chỉ tiếp tục khi user xác nhận
- User yêu cầu dùng “Professional planning” như layout chính?
  → Không dùng như root layout → dùng như meta-check sau khi đã chọn layout đúng

## 7. Checklist Kiểm Tra Output
Checklist operator trước khi giao output cho người dùng/đưa lên publish:

- Có đúng command không?
- Có audience rõ không?
- Có pain point không?
- Có insight không?
- Có 5W-1H nếu cần brainstorm không?
- Có selected layout không?
- Có **Taxonomy Validation Evidence** không?
- Có marketing outline 5 phần không?
- Có hook đủ (nếu case /post) không?
- Có CTA không?
- Có QA notes / PASS-FAIL checklist không?
- Có cảnh báo nếu user yêu cầu ingestion docs (nhớ rule “exact source files”) không?

## 8. Lỗi Thường Gặp Và Cách Tránh
1. **Dùng 5W-1H như bố cục chính**  
   - Vì sao sai: 5W-1H là công cụ mở ý, không thay layout.  
   - Cách đúng: chọn layout + taxonomy validation, dùng 5W-1H trong brainstorm.

2. **Dùng Professional planning như root layout**  
   - Vì sao sai: sai vai trò meta-framework.  
   - Cách đúng: dùng như meta-check; root layout vẫn là layout đã chọn từ matrix.

3. **Bỏ qua taxonomy validation**  
   - Vì sao sai: layout-fit và guardrail yêu cầu taxonomy evidence.  
   - Cách đúng: layout-selection-matrix → layout-taxonomy → layout-fit checklist.

4. **Bài có hook nhưng không có CTA**  
   - Vì sao sai: CTA là conversion component bắt buộc.  
   - Cách đúng: đảm bảo CTA khớp logic & final-output checklist.

5. **Chấm điểm content nhưng không có evidence**  
   - Vì sao sai: recommendation không actionable.  
   - Cách đúng: đảm bảo có Content Logic Evidence, bridge cho recommendation.

6. **QA quá chung chung**  
   - Vì sao sai: không chỉ rõ lỗi nào thuộc checklist nào.  
   - Cách đúng: đưa lỗi theo checklist mục (audience/pain/insight/layout-fit/CTA…).

7. **Tự ingest docs khi user chưa xác nhận exact source files**  
   - Vì sao sai: vi phạm ingestion safety golden rule.  
   - Cách đúng: dừng ingestion, yêu cầu user xác nhận exact source files + batch controls.

8. **Sửa framework/command/layout khi chỉ cần tạo output**  
   - Vì sao sai: vượt phạm vi task vận hành.  
   - Cách đúng: chỉ tạo/QA output theo command contract.

9. **Nâng confidence/status layout khi chưa có source**  
   - Vì sao sai: layout confidence cần căn cứ.  
   - Cách đúng: ghi rủi ro trong QA notes, không nâng High nếu nguồn chưa đủ.

10. **Đọc toàn bộ folder cho task nhỏ**  
   - Vì sao sai: vi phạm progressive disclosure & làm chậm.  
   - Cách đúng: đọc “đủ dùng” theo resource map.

## 9. Đề Xuất Model Sử Dụng
Bảng gợi ý chọn model theo vai trò (operator dùng khi cấu hình prompt):

| Task | Recommended model | Reason |
|---|---|---|
| Scan/audit nhanh các file .md | Kimi K2.6 | Đọc nhanh, bám cấu trúc checklist |
| Viết content dài/sáng tạo | Minimax M2.7 | Output sáng tạo và mạch lạc |
| Scan folder nhanh (nếu cần) | Gemini 3 Flash | Tốc độ cao cho đọc lướt |
| Review kiến trúc cuối (QA/logic) | Gemini 3.1 Pro Low | Rà logic và consistency |
| File edit khi có credit | Codex | Tối ưu viết patch theo format |
| Không dùng model sáng tạo để tự ý ingest docs | — | Luôn enforce ingestion safety |

## 10. Giao Thức Bàn Giao An Toàn (Safe Handoff)
Khi chuyển việc cho model khác/operator khác, luôn gửi gói handoff tối thiểu:

Template:

Current state:
Batch:
Verdict:
Last report:
Files created:
Files updated:
Not done:
Next step:
Safety:
Do not ingest docs unless user confirms exact source files.

## 11. Khi Nào Cần Dừng Lại Hỏi User
Operator phải dừng và hỏi user khi:
- User yêu cầu ingestion docs nhưng chưa nói **file nguồn cụ thể**.
- File đã từng ingest nhưng user muốn nạp lại/overwrite.
- User muốn đổi status/confidence layout.
- Muốn biến meta-framework thành root layout.
- Thiếu audience/goal/CTA quan trọng.
- Output có thể làm hỏng cấu trúc skill (ví dụ trộn sai 5W-1H/layout/hook/CTA).
- Model/agent đề xuất hành động ngoài phạm vi (chỉnh command/framework/layout, chạy test mới, v.v.).

## 12. Prompt Mẫu Sẵn Sàng Copy

### 1) Prompt dùng `/post`
**Input cần điền:**
- Topic:
- Goal:
- Audience:
- Pain point:
- Insight (nếu có):
- Platform:
- CTA:
- Tone:

**Prompt:**
“Bạn là Agentic AI Content Marketing Skill operator. Hãy dùng command `/post`.  
Input: Topic=[...], Goal=[...], Audience=[...], Pain point=[...], Insight=[...], Platform=[...], CTA=[...], Tone=[...].  
Yêu cầu output bắt buộc: Target audience, Pain point, Insight, 5W-1H table, Selected layout + layout type + layout-fit notes, Marketing outline 5 phần, 10 hooks, Hook mạnh nhất, Final post, CTA, QA checklist.  
Luôn validate layout qua matrix + taxonomy và chạy checklist PASS/FAIL trước khi trả output.”

### 2) Prompt dùng `/outline`
**Prompt:**
“Bạn là Agentic AI Content Marketing Skill operator. Hãy dùng command `/outline`.  
Input: Content goal=[...], Audience=[...], Topic/Idea=[...], Platform=[...].  
Output bắt buộc: Target audience, Pain point hoặc nhu cầu, Insight sơ bộ, Selected layout + layout type, Layout-fit notes, Taxonomy Validation Evidence, Marketing outline 5 phần, CTA direction.  
Không dùng 5W-1H làm bố cục chính.”

### 3) Prompt dùng `/qa`
**Prompt:**
“Bạn là Agentic AI Content Marketing Skill operator. Hãy dùng command `/qa`.  
Input: Final content=[dán nội dung], Brief/mục tiêu=[...], Audience=[...], Platform=[...].  
Output bắt buộc: Checklist PASS/FAIL rõ, lỗi logic/audience/insight/CTA, lỗi layout-fit (nếu có), gợi ý sửa cụ thể bám checklist.”

### 4) Prompt dùng `/content-score`
**Prompt:**
“Bạn là Agentic AI Content Marketing Skill operator. Hãy dùng command `/content-score`.  
Input: Content=[dán nội dung], Goal=[...], Platform=[...], Audience=[...].  
Output bắt buộc: Total score, score theo tiêu chí (logic/audience fit/hook/body/CTA/platform fit), vấn đề cần sửa, Recommendation theo evidence (Content Logic Evidence), và kiểm Layout Fit / 10.”

### 5) Prompt chuẩn bị ingestion an toàn
**Prompt:**
“Bạn là Agentic AI Content Marketing Skill operator. Task là ingestion.  
Trước khi ingest, hãy hỏi user theo ingestion safety:  
(1) Exact source files nào cần ingest?  
(2) File nào đã ingest rồi?  
(3) Batch ID mới là gì?  
(4) Nạp vào folder/file đích nào?  
(5) Có update kiến thức cũ không?  
(6) Có đổi status/confidence không?  
(7) Có giữ bản cũ không?  
Chỉ tiếp tục sau khi user xác nhận exact source files. Không đọc/sửa ngoài phạm vi.”

## 13. Quy Tắc Vận Hành Cuối Cùng
- Không ưu tiên làm nhanh hơn làm đúng.
- Không ingest dữ liệu mới khi chưa có xác nhận exact source files.
- Không sửa file ngoài phạm vi batch.
- Không đoán nếu thiếu evidence (taxonomy/layout-fit/final-output QA).
- Nếu đầu ra fail → sửa theo checklist; không tự “ước lượng bằng niềm tin”.
