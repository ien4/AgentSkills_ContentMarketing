# Command: /outline

## Khi Nào Dùng

Dùng khi cần dàn ý trước khi viết content.

## Input Cần Có

- Ý tưởng hoặc brief.
- Mục tiêu nội dung.
- Audience.
- Nền tảng đăng nếu có.

## Output Bắt Buộc

- Target audience.
- Pain point.
- Insight.
- Selected layout.
- Layout type.
- Marketing outline 5 phần.
- Ghi chú logic.

## Taxonomy Validation Evidence

Bắt buộc output `/outline` phải có block **Taxonomy Validation Evidence** (nhằm “show evidence/label” rằng đã validate theo taxonomy), gồm các dòng/fields:

- Selected layout:
- Layout type:
- Taxonomy label:
- Confidence level:
- Source basis:
- Guardrail checked:
- Why this layout fits the content goal:
- Why this is not a meta-framework misuse:

## Process

1. Clarify content goal and audience.
2. Select layout from `02-frameworks/content-layout-systems/00-layout-system-control/layout-selection-matrix.md`.
3. Validate the selected layout with `02-frameworks/content-layout-systems/00-layout-system-control/layout-taxonomy.md`.
4. Run `07-quality-gates/layout-fit-checklist.md`.
5. Build the Marketing outline 5 phần from the selected layout.

## Checklist

- [ ] Đã chọn layout từ matrix.
- [ ] Đã validate bằng taxonomy.
- [ ] Đã kiểm layout-fit.
- [ ] Có tiêu đề.
- [ ] Có mô tả tiêu đề.
- [ ] Có thân bài.
- [ ] Có kết luận.
- [ ] Có CTA.
