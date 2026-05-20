# Layout Selection Matrix

## Purpose

Help the Agent choose a layout based on content goal, then validate the choice with `layout-taxonomy.md` and `07-quality-gates/layout-fit-checklist.md`.

## Selection Matrix

| Content goal | Recommended layout | Layout Type | Why | Avoid | Risk if wrong | Confidence | Source basis | Guardrail |
|---|---|---|---|---|---|---|---|---|
| Explain clearly | Tong phan hop | Validated root layout | Shows the main point, analyzes details, then synthesizes. | Quy nap if the audience needs the point immediately. | Reader waits too long for the answer. | High | Tong Phan Hop PDF | Validate source confidence in taxonomy. |
| Persuade | Quy nap + Dan dat thuyet phuc | Root layout + persuasive application | Builds evidence and trust before conclusion or offer. | Liet ke alone for trust-heavy persuasion. | Content lists facts without creating belief. | Medium | Quy Nap PDF | Use dan dat thuyet phuc only as application with quy nap or another root layout. |
| Tell a story | Quy nap or Moc xich | Validated root layout | Quy nap supports delayed conclusion; moc xich supports linked events. | Dien dich if curiosity must be preserved. | Conclusion appears too early or story fragments. | High | Quy Nap PDF; Moc Xich PDF | Choose one primary root layout, not both at once unless the structure is explicit. |
| Compare options | Liet ke | Validated root layout | Supports independent criteria, features, pros/cons, reviews. | Moc xich if items are independent. | Forces a false cause-effect chain. | High | Liet Ke PDF | Group list items by criteria. |
| Sell softly | Quy nap + Dan dat thuyet phuc | Root layout + persuasive application | Allows the offer to appear after trust and logic. | Dien dich if audience is defensive. | CTA appears before belief is built. | Medium | Quy Nap PDF | Validate with `quy-nap-layout.md`; do not treat persuasion flow as standalone. |
| Sell after analysis | Tong phan hop | Validated root layout | Supports CTA after complete analysis. | Liet ke if the topic needs one central argument. | CTA feels detached from the analysis. | High | Tong Phan Hop PDF | Ensure final synthesis returns to the opening message. |
| Educate in a sequence | Moc xich | Validated root layout | Each idea can lead naturally to the next lesson. | Liet ke for long learning journeys. | Lesson becomes disconnected points. | High | Moc Xich PDF | Check each transition between ideas. |
| Plan content professionally | Select a validated root layout first; then use Professional planning framework as meta-check | Root layout + meta-framework check | The meta-framework checks goal, audience, selected layout, outline, CTA, and platform fit after a real layout is chosen. | Using the meta-framework as the primary content layout. | Agent skips choosing an actual layout. | Medium | Professional Layout PDF | Use as meta-check after selecting a root layout. |
| Review products/services | Liet ke | Validated root layout | Supports criteria, pros/cons, features, and options. | Quy nap if the reader needs fast scanning. | Review becomes too indirect. | High | Liet Ke PDF | Make each item comparable. |
| Lead from problem to solution | Quy nap + Dan dat thuyet phuc | Root layout + persuasive application | Moves through situation, evidence, conclusion, action. | Dien dich if the solution should not be revealed immediately. | Jumps to solution before need is built. | Medium | Quy Nap PDF | Mark persuasive flow as application, not root layout. |
| Present many ideas clearly | Liet ke | Validated root layout | Separates independent points while keeping one shared topic. | Moc xich if ideas do not need continuity. | Forces unrelated items into a chain. | High | Liet Ke PDF | Keep one idea per item. |
| Create continuous idea-to-idea flow | Moc xich | Validated root layout | Each idea bridges to the next. | Liet ke. | Content feels disconnected. | High | Moc Xich PDF | Bridge every section. |
| Start with evidence then conclude | Quy nap | Validated root layout | Evidence comes before final point. | Dien dich. | Spoils curiosity and weakens the lead. | High | Quy Nap PDF | Conclusion must synthesize all evidence. |
| Start with conclusion then explain | Dien dich | Comparison/reference layout | Available comparison sources describe this pattern. | Quy nap if the conclusion should be delayed. | Misused when stronger source-backed layouts are required. | Medium | Tong Phan Hop PDF comparison | Needs review; use only when source confidence is acceptable. |

## Matrix Guardrails

- Always validate the selected row with `layout-taxonomy.md`.
- **Triết lý "Xây nhà"**: Chọn root layout dựa trên mục tiêu, công năng và hành vi scanning (đọc lướt) của người đọc. Không chọn layout theo cảm tính hoặc chỉ vì "nghe hay".
- **Không dùng Formula thay thế**: Tuyệt đối không chọn các công thức ứng dụng như AIDA, PAS, v.v. để thay thế cho một Root Layout thực thụ khi định hình cấu trúc.
- If `Layout Type` is meta-framework, do not use it as the primary layout.
- If `Layout Type` is application flow, pair it with a validated root layout.
- If `Confidence` is Medium or Low, disclose the risk in QA notes.
- Run `07-quality-gates/layout-fit-checklist.md` before final output.
