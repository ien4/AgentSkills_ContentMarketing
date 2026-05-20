# Layout Taxonomy

## Purpose

Track layout systems, their confidence, and their safe usage boundaries.

## Taxonomy Table

| Layout | Type | Goal | When To Use | When Not To Use | Basic Structure | Difference / Guardrail | Source File | Target File | Status | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Tong phan hop | Validated root layout | Deep analysis with clear opening and closing logic. | Long analysis, research, SEO, website/blog. | Very short content, weak evidence, surprise-first content. | Tong -> Phan -> Hop. | Main idea appears at both beginning and end. | `Nghệ thuật Bố cục Tổng Phân Hợp trong Sáng tạo Nội dung.pdf` | `tong-phan-hop-layout.md` | Ingested | High |
| Quy nap | Validated root layout | Lead from details/evidence to final conclusion. | Storytelling, complex reasoning, curiosity, soft selling. | Short announcements, fast decisions, weak evidence. | Opening hint -> evidence -> conclusion -> CTA. | Main point appears late; do not confuse with dien dich. | `Nghệ thuật Bố cục Quy nạp và Dẫn dắt Content Thuyết phục.pdf` | `quy-nap-layout.md` | Ingested | High |
| Dien dich | Comparison/reference layout, not fully validated root layout | Put the main point first, then explain. | Use only when matrix/taxonomy mark it suitable and no stronger source-backed layout is required. | Important content needing a High-confidence layout; storytelling; trust-building. | Main point -> reason -> support -> close. | Needs review; do not treat as High confidence until a direct source is ingested. | Comparison/overview sources only | `dien-dich-layout.md` | Needs review / Partially ingested | Medium |
| Moc xich | Validated root layout | Create continuous idea-to-idea progression. | Logical series, step-by-step education, storytelling, linked arguments. | Independent list items, content needing easy insertion in the middle, very short content. | Idea 1 -> bridge -> idea 2 -> bridge -> conclusion. | Different from liet ke because each idea must connect to the next. | `Nghệ thuật Sáng tạo Nội dung theo Bố cục Móc xích.pdf` | `moc-xich-layout.md` | Ingested | High |
| Liet ke | Validated root layout | Present many clear, scan-friendly points. | Tips, steps, reviews, comparisons, feature lists, summaries. | Mystery, deep layered analysis, tight cause-effect chains. | Lead-in -> list -> conclusion -> CTA. | Items can stand independently but must share a topic. | `Nghệ Thuật Làm Chủ Bố Cục Liệt Kê Trong Content Marketing.pdf` | `liet-ke-layout.md` | Ingested | High |
| Dan dat thuyet phuc | Persuasive application / argument flow, not fully independent root layout | Build trust before offer or CTA. | Persuasive content when validated with quy nap or another root layout. | As standalone layout; quick announcements; hook/CTA-only tasks. | Root layout -> trust-building reasoning -> conclusion -> CTA. | Not a replacement for quy nap; not CTA; not hook. | `Nghệ thuật Bố cục Quy nạp và Dẫn dắt Content Thuyết phục.pdf` | `dan-dat-thuyet-phuc-layout.md` | Partially ingested | Medium |
| Detailed content process | Workflow/meta-process for applying layouts | Choose a layout, build detailed outline, then write. | Turning raw idea into structured outline/content. | As a standalone article layout; pure 5W-1H brainstorm. | Choose layout -> outline -> 5W-1H support -> write -> QA. | Process file, not a root layout. | `Nghệ Thuật Bố Cục Và Quy Trình Xây Dựng Nội Dung Chi Tiết.pdf` | `detailed-content-process-layout.md` | Ingested | High |
| Professional content marketing planning framework | Meta-framework, not single root layout | Check professional planning completeness. | Use as meta-check after selecting a root layout. | As the primary content layout. | Goal -> audience -> selected layout -> outline -> content -> QA. | Must not replace matrix/taxonomy or specific layout files. | `Nghệ Thuật Xây Dựng Bố Cục Content Marketing Chuyên Nghiệp.pdf` | `professional-content-marketing-layout.md` | Partially ingested / Meta-framework | Medium |
| Dong tam | Pending root layout | Confirmed as root layout by C1 - 3, waiting detailed source C1 - 3F. | N/A (Pending detailed source) | N/A (Pending detailed source) | N/A (Pending detailed source) | Do not use or create file until detailed source is ingested. | `Kiến Trúc Bố Cục Trong Content Marketing Đột Phá C1 - 3.docx` | `dong-tam-layout.md` | Pending / Not Ingested | Low |
| Tong phan hop trong sang tao noi dung | Alias of Tong phan hop | Same as Tong phan hop. | Use `tong-phan-hop-layout.md`. | Do not create separate logic unless source differs. | Tong -> Phan -> Hop. | Alias only. | `Nghệ thuật Bố cục Tổng Phân Hợp trong Sáng tạo Nội dung.pdf` | `tong-phan-hop-layout.md` | Ingested | High |
| Moc xich trong sang tao noi dung | Alias of Moc xich | Same as Moc xich. | Use `moc-xich-layout.md`. | Do not create separate logic unless source differs. | Idea chain. | Alias only. | `Nghệ thuật Sáng tạo Nội dung theo Bố cục Móc xích.pdf` | `moc-xich-layout.md` | Ingested | High |

## Selection Rules

- Prefer High-confidence validated root layouts when content risk is high.
- Use Medium-confidence layouts only with an explicit warning in the output or QA notes.
- Use meta-frameworks only as planning checks after a root layout is selected.
- Use application flows only with a validated root layout.
- Do not mix 5W-1H, hook, CTA, or templates into layout classification.
