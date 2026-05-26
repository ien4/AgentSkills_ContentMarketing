# Practical Operator Playbook — Agentic AI Content Marketing Skill

## 1. Mục Đích
Playbook này là tài liệu hướng dẫn vận hành thực chiến dành cho Operator khi sử dụng bộ skill **agentic-ai-content-marketing-skill**.
Hệ thống hiện tại hoạt động dựa trên 2 Agent chính:
1. **@Data_Ingestion_Agent**: Chuyên xử lý việc nạp, phân tích và trích xuất dữ liệu gốc một cách an toàn.
2. **@Content_Marketing_Agent**: Chuyên định hướng chiến lược, lựa chọn cấu trúc (layout) và sáng tạo nội dung dựa trên nền tảng kiến thức đã nạp.

## 2. Hệ Thống Kiến Thức (Production-Ready Layouts)
Hệ thống hiện tại đã nạp đầy đủ (Fully Ingested) bộ 7 Bố cục gốc cốt lõi (C1-3 Layout System), sẵn sàng cho vận hành thực tế:
1. **C1-3A — Liệt kê (Listicle)**: Trình bày nhiều ý rõ ràng, độc lập.
2. **C1-3B — Diễn dịch (Deductive)**: Đi thẳng vào kết luận trước, giải thích sau.
3. **C1-3C — Quy nạp (Inductive)**: Dẫn dắt logic, trải nghiệm trước khi chốt kết luận.
4. **C1-3D — Tổng Phân Hợp (Synthesis)**: Mở bài khái quát, phân tích sâu, kết bài đúc kết.
5. **C1-3E — Móc xích (Chain)**: Luận điểm nhân quả liên hoàn, ý trước móc vào ý sau.
6. **C1-3F — Đồng tâm (Concentric)**: Bán hàng gián tiếp, đi từ bối cảnh ngoài vào giải pháp lõi ở tâm.
7. **C1-3G — Vấn đề - Giải pháp (Problem-Solution)**: Khơi gợi nỗi đau và đưa ra giải pháp đa tầng.

*(Lưu ý: Bố cục "Song hành / Đối xứng" vẫn đang ở trạng thái hạn chế, sẽ kích hoạt Knowledge Coverage Warning nếu sử dụng).*

## 3. Quy Trình Vận Hành Thực Tế

### Quy trình 1: Nạp Kiến Thức Mới (Ingestion Process)
**Agent thực thi:** `@Data_Ingestion_Agent`

1. **Chuẩn bị:** Đọc các quy tắc an toàn trong `10-system/safety/DATA_INGESTION_SAFETY.md` và `10-system/safety/INGESTION_SOP.md`.
2. **Kích hoạt:** Gọi `@Data_Ingestion_Agent` kèm theo lệnh nạp.
3. **Khai báo bắt buộc (Progressive Disclosure):**
   - Không được tự ý nạp nếu chưa xác nhận **Exact Source Files** (File gốc cụ thể).
   - Khai báo Batch ID.
   - Định rõ file đích (target file) sẽ lưu trữ kiến thức.
4. **Cập nhật Mapping:** Agent sẽ tự động cập nhật `course-index.md`, `source-map.md`, và `INGESTION_LOG.md` sau khi trích xuất.
5. **Nghiệm thu:** Operator kiểm tra raw source markers (đảm bảo không rò rỉ số trích dẫn thô vào output).

### Quy trình 2: Tạo Content Bằng 7 Layout C1-3
**Agent thực thi:** `@Content_Marketing_Agent`

1. **Nhập Brief:** Cung cấp thông tin đầu vào (Input) gồm:
   - Topic / Nội dung thô.
   - Goal (Mục tiêu bài viết).
   - Audience (Đối tượng độc giả).
   - Platform (Nền tảng: Facebook, Tiktok, Blog...).
   - CTA (Kêu gọi hành động mong muốn).
2. **Phân tích:** Agent sẽ trích xuất Pain Point, Insight và lập bảng 5W-1H (Chỉ dùng để brainstorm, không dùng làm bố cục).
3. **Lựa chọn Layout:** Agent tra cứu `layout-selection-matrix.md` và `layout-taxonomy.md` để chọn ra 1 trong 7 layout C1-3 phù hợp nhất.
4. **Validation Evidence:** Agent sẽ xuất bảng chứng cứ chứng minh lý do chọn layout, kèm trạng thái `N/A - Layout fully ingested` (vì 7 layout C1-3 đã hoàn thiện).
5. **Dàn ý & Viết:** Lập dàn ý 5 phần (Marketing Outline), tạo 10 hooks (chọn 1 hook mạnh nhất) và viết bản nháp cuối cùng.
6. **Grounding Check:** Agent kiểm tra bài viết không bị "drift" (lệch đề) và không chứa các tuyên bố/số liệu bịa đặt (unsupported claims).

### Quy trình 3: Kiểm Tra Quality Gate (QA & Scoring)
**Agent thực thi:** `@Content_Marketing_Agent`

- **Lệnh `/qa`:** Operator nạp bài viết và yêu cầu Agent chạy qua các file checklist (`layout-fit-checklist.md`, `content-logic-checklist.md`, `final-output-checklist.md`). Agent trả về PASS/FAIL và gợi ý sửa bám sát nguyên nhân cụ thể.
- **Lệnh `/content-score`:** Agent chấm điểm tổng hợp (Max 100) cho bài viết dựa trên logic, audience fit, hook, layout fit và nền tảng. Yêu cầu mức điểm >= 80 để xuất bản.

### Quy trình 4: Xử Lý Lỗi Thường Gặp (Common Issues)
1. **Dùng 5W-1H làm bố cục chính:**
   - *Cách xử lý:* Nhắc Agent chỉ dùng 5W-1H để mở ý. Bố cục chính phải lấy từ 7 layout C1-3.
2. **Kích hoạt sai Knowledge Coverage Warning:**
   - *Cách xử lý:* Nếu Agent báo thiếu tài liệu cho C1-3A đến C1-3G, nhắc Agent kiểm tra lại dòng 54 của `Content_Marketing_Agent.md`. Hệ thống đã nạp đủ bộ C1-3.
3. **Bịa đặt số liệu (Hallucinated Claims):**
   - *Cách xử lý:* Sử dụng QA Gate để bắt lỗi. Bắt buộc mọi số liệu % hay cam kết năng lực phải có trong Input.
4. **Lạm dụng "Dẫn dắt thuyết phục" hoặc "Professional Planning" như Root Layout:**
   - *Cách xử lý:* Nhắc Agent chọn 1 root layout thật sự (ví dụ Quy nạp, Tổng Phân Hợp) và dùng các khung kia như là meta-framework kiểm tra.
5. **Nạp file mới gây rò rỉ raw marker:**
   - *Cách xử lý:* Yêu cầu `@Data_Ingestion_Agent` dọn dẹp số trích dẫn thô ([1], [2]) khỏi văn bản chính, dồn xuống bảng Source Map.

## 4. Prompt Mẫu Sẵn Sàng (Template Prompts)

**Nạp kiến thức (Ingestion):**
```text
@Data_Ingestion_Agent, bắt đầu Batch mới. Các file nguồn cần nạp là [danh sách file]. Hãy đọc file theo SOP, trích xuất cấu trúc và cập nhật vào [file đích]. Nhớ update INGESTION_LOG.md và source-map.md. Chú ý dọn sạch raw markers.
```

**Tạo bài đăng (Content Creation):**
```text
@Content_Marketing_Agent, sử dụng lệnh /post.
Input: Topic=[...], Goal=[...], Audience=[...], Pain point=[...], Platform=[...], CTA=[...].
Yêu cầu bắt buộc: Chọn 1 trong 7 layout C1-3. Lập bảng 5W-1H, xuất Taxonomy Validation Evidence, Outline 5 phần, 10 Hooks và bài viết hoàn chỉnh. Không bịa số liệu.
```

**Chấm điểm (Scoring):**
```text
@Content_Marketing_Agent, sử dụng lệnh /content-score cho bài viết sau: [dán bài viết]. Chạy qua final-output-checklist.md và layout-fit-checklist.md để chấm điểm.
```
