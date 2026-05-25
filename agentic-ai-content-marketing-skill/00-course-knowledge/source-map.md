# Source Map

## Mục Đích

File này liên kết kiến thức đã nạp với nguồn tài liệu khóa học.

## Nguồn Đã Dùng Trong Batch 001

Nguồn chính của Batch 001 là brief kiến thức do người dùng cung cấp trong yêu cầu tạo skill.

## Tài Liệu Có Trong Workspace

Các tài liệu sau được ghi nhận để xử lý ở batch sau:

- `docs/Nghệ Thuật Xây Dựng Bố Cục Nội Dung Marketing Chuẩn Xu Hướng.docx`
- `docs/Nghệ Thuật Xây Dựng Bố Cục Content Marketing Chuyên Nghiệp.pdf`
- `docs/Nghệ Thuật Sáng Tạo Nội Dung Đỉnh Cao Với 5W-1H.pdf`
- `docs/Nghệ Thuật Sáng Tạo Nội Dung Đỉnh Cao Với 5W-1H.docx`
- `docs/Nghệ thuật Sáng tạo Nội dung theo Bố cục Móc xích.pdf`
- `docs/Nghệ Thuật Làm Chủ Bố Cục Liệt Kê Trong Content Marketing.pdf`
- `docs/Nghệ Thuật Chuyển Đổi Tư Duy Viết Nội Dung Marketing Chuẩn Toàn Diện.docx`
- `docs/Nghệ Thuật Bố Cục Và Quy Trình Xây Dựng Nội Dung Chi Tiết.pdf`
- `docs/Nghệ thuật Bố cục Tổng Phân Hợp trong Sáng tạo Nội dung.pdf`
- `docs/Nghệ thuật Bố cục Quy nạp và Dẫn dắt Content Thuyết phục.pdf`
- `docs/Nghệ thuật Bố cục Quy nạp và Dẫn dắt Content Thuyết phục (1).pdf`

## External Source Directory

`docs/` là nơi chứa tài liệu nguồn thô bên ngoài skill.

Rules:

- Không sửa file trong `docs/`.
- Không xóa file trong `docs/`.
- Không di chuyển file trong `docs/`.
- Mỗi batch ingestion phải map tài liệu nguồn sang file đích trong `agentic-ai-content-marketing-skill/`.
- Source mapping phải ghi rõ tài liệu nào cung cấp kiến thức cho file nào.

## Cần Làm Ở Batch Sau

- Trích xuất nội dung từng tài liệu.
- Gắn từng ý vào file principle, framework, workflow hoặc example tương ứng.
- Ghi rõ trang, chương hoặc đoạn nguồn nếu có thể.

## Batch 2B Source Inventory — Layout Systems

| Source file name | File type | Related layout/topic | Read status | Target skill file | Notes |
|---|---|---|---|---|---|
| `Nghệ thuật Bố cục Quy nạp và Dẫn dắt Content Thuyết phục.pdf` | PDF | Quy nạp; dẫn dắt thuyết phục | Read | `02-frameworks/content-layout-systems/01-core-layouts/quy-nap-layout.md`; `02-frameworks/content-layout-systems/02-supporting-frameworks/dan-dat-thuyet-phuc-layout.md` | Primary source used. |
| `Nghệ thuật Bố cục Quy nạp và Dẫn dắt Content Thuyết phục (1).pdf` | PDF | Quy nạp; dẫn dắt thuyết phục | Read | Same as primary quy nạp target files | Extracted text matches the primary quy nạp PDF; used for duplicate cross-check only. |
| `Nghệ thuật Bố cục Tổng Phân Hợp trong Sáng tạo Nội dung.pdf` | PDF | Tổng phân hợp; partial diễn dịch comparison | Read | `02-frameworks/content-layout-systems/01-core-layouts/tong-phan-hop-layout.md`; `02-frameworks/content-layout-systems/01-core-layouts/dien-dich-layout.md` | Used for Tổng - Phân - Hợp and limited source basis for diễn dịch. |
| `Nghệ thuật Sáng tạo Nội dung theo Bố cục Móc xích.pdf` | PDF | Móc xích | Read | `02-frameworks/content-layout-systems/01-core-layouts/moc-xich-layout.md` | Primary source used. |
| `Nghệ Thuật Làm Chủ Bố Cục Liệt Kê Trong Content Marketing.pdf` | PDF | Liệt kê | Read | `02-frameworks/content-layout-systems/01-core-layouts/liet-ke-layout.md` | Primary source used. |
| `Nghệ Thuật Bố Cục Và Quy Trình Xây Dựng Nội Dung Chi Tiết.pdf` | PDF | Quy trình xây dựng nội dung chi tiết; bố cục gốc overview | Read | `02-frameworks/content-layout-systems/02-supporting-frameworks/detailed-content-process-layout.md`; `02-frameworks/content-layout-systems/02-supporting-frameworks/professional-content-marketing-layout.md`; `02-frameworks/content-layout-systems/01-core-layouts/dien-dich-layout.md` | Used for meta-process and source confirmation that diễn dịch is a listed bố cục gốc. |
| `Nghệ Thuật Xây Dựng Bố Cục Content Marketing Chuyên Nghiệp.pdf` | PDF | Professional content marketing layout; bố cục gốc overview | Read | `02-frameworks/content-layout-systems/02-supporting-frameworks/professional-content-marketing-layout.md`; `02-frameworks/content-layout-systems/02-supporting-frameworks/detailed-content-process-layout.md`; `02-frameworks/content-layout-systems/01-core-layouts/dien-dich-layout.md` | Used for professional meta-framework and layout-system boundaries. |
| `Nghệ Thuật Sáng Tạo Nội Dung Đỉnh Cao Với 5W-1H.docx` | DOCX | 5W-1H | Read / Ingested (Batch 3A-2I-2) | `02-frameworks/5w1h-framework.md`; `07-quality-gates/5w1h-checklist.md` | Primary source. Extracted và integrated. |
| `Nghệ Thuật Sáng Tạo Nội Dung Đỉnh Cao Với 5W-1H.pdf` | PDF | 5W-1H | Read / Cross-checked (Batch 3A-2I-2) | Same as DOCX above | Supporting/cross-check source. Nội dung trùng khớp với DOCX; PDF extraction kém hơn (ngắt dòng từng từ). Merge để tránh double-ingest. |
| `Nghệ Thuật Xây Dựng Bố Cục Nội Dung Marketing Chuẩn Xu Hướng.docx` | DOCX | Mindset; Marketing outline 5 phần; Outline workflow | Read / Ingested (Batch 3A-2I-1) | `01-core-principles/content-marketing-mindset.md`; `01-core-principles/marketing-layout-5-parts.md`; `02-frameworks/content-outline-framework.md` | Primary source. Extracted and integrated. |
| `Nghệ Thuật Chuyển Đổi Tư Duy Viết Nội Dung Marketing Chuẩn Toàn Diện.docx` | DOCX | Mindset; Marketing outline 5 phần; Outline workflow | Read / Ingested (Batch 3A-2I-1) | Same as primary source above | Supporting/cross-check source. Content nearly identical to primary source; merged to avoid double-ingest. |
| `Kiến Trúc Bố Cục Trong Content Marketing Đột Phá C1 - 3.docx` | DOCX | Layout Architecture; Triết lý Xây nhà; 6 Root Layouts; ACP | Read / Ingested (Batch 3A-3I-1A) | `README.md` (layout systems); `layout-taxonomy.md`; `layout-selection-matrix.md`; `detailed-content-process-layout.md`; `layout-fit-checklist.md` | Primary source. Extracted and integrated. Đồng tâm confirmed as pending root layout. |
| `Bố Cục Liệt Kê_ Vũ Khí Tối Ưu Content Marketing C1 - 3A.docx` | DOCX | Bố cục Liệt kê | Read / Ingested (Batch 3A-3I-1B) | `02-frameworks/content-layout-systems/01-core-layouts/liet-ke-layout.md` | Primary source. Extracted & integrated Listicle Conversion Model framework and logic sequencing. |
| `Làm Chủ Bố Cục Diễn Dịch Trong Content Marketing C1 - 3B.docx` | DOCX | Bố cục Diễn dịch | Read / Ingested (Batch 3A-3I-1C) | `02-frameworks/content-layout-systems/01-core-layouts/dien-dich-layout.md` | Primary source. Extracted & integrated Deductive Persuasion Content (DPC) framework and logic sequencing. |
| `Làm Chủ Bố Cục Quy Nạp_ Nghệ Thuật Dẫn Dắt Chuyển Đổi C1 -3C.docx` | DOCX | Bố cục Quy nạp | Read / Ingested (Batch 3A-3I-1D) | `02-frameworks/content-layout-systems/01-core-layouts/quy-nap-layout.md` | Primary source. Extracted & integrated Inductive Discovery Model framework and logic sequencing. |

