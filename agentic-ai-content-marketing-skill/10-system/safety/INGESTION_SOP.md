# Ingestion SOP â€” Agentic AI Content Marketing Skill

## 1. Má»¥c ÄÃ­ch

File nÃ y chuáº©n hÃ³a quy trÃ¬nh náº¡p tÃ i liá»‡u khÃ³a há»c, video, transcript, PDF hoáº·c DOCX vÃ o bá»™ Agentic AI Content Marketing Skill.

Má»¥c tiÃªu lÃ  biáº¿n tÃ i liá»‡u thÃ´ thÃ nh kiáº¿n thá»©c Ä‘Ã£ xá»­ lÃ½, cÃ³ phÃ¢n loáº¡i, cÃ³ source mapping, cÃ³ report vÃ  cÃ³ thá»ƒ dÃ¹ng á»•n Ä‘á»‹nh bá»Ÿi AI Agent.

## 2. NguyÃªn Táº¯c Báº¥t Biáº¿n

- `docs/` lÃ  nguá»“n thÃ´, khÃ´ng sá»­a.
- `agentic-ai-content-marketing-skill/` lÃ  nÆ¡i chá»©a kiáº¿n thá»©c Ä‘Ã£ xá»­ lÃ½.
- KhÃ´ng copy nguyÃªn vÄƒn tÃ i liá»‡u dÃ i vÃ o skill.
- Pháº£i trÃ­ch xuáº¥t, phÃ¢n loáº¡i, chuáº©n hÃ³a.
- Má»—i batch pháº£i cÃ³ report.
- Má»—i kiáº¿n thá»©c pháº£i cÃ³ source mapping.
- KhÃ´ng trá»™n framework vá»›i workflow.
- KhÃ´ng trá»™n 5W-1H vá»›i bá»‘ cá»¥c gá»‘c.
- KhÃ´ng trá»™n hook vá»›i CTA.
- KhÃ´ng trá»™n nguyÃªn lÃ½ ná»n táº£ng vá»›i template á»©ng dá»¥ng.

## Mandatory User Confirmation Before Ingestion

- TrÆ°á»›c má»i batch náº¡p dá»¯ liá»‡u má»›i, Agent pháº£i yÃªu cáº§u user xÃ¡c nháº­n exact source files.
- Náº¿u source file Ä‘Ã£ tá»«ng Ä‘Æ°á»£c ingest, khÃ´ng ingest láº¡i tá»± Ä‘á»™ng.
- Náº¿u cáº§n update kiáº¿n thá»©c cÅ©, pháº£i ghi rÃµ update target vÃ  lÃ½ do.
- Náº¿u khÃ´ng cháº¯c file Ä‘Ã£ ingest chÆ°a, pháº£i kiá»ƒm `source-map.md` + `INGESTION_LOG.md` trÆ°á»›c.

## 3. Quy TrÃ¬nh Náº¡p TÃ i Liá»‡u Chuáº©n

1. Scan `docs/`.
2. Chá»n file nguá»“n cho batch.
3. Äá»c tá»«ng file.
4. TÃ³m táº¯t tá»«ng file.
5. PhÃ¢n loáº¡i kiáº¿n thá»©c.
6. XÃ¡c Ä‘á»‹nh file Ä‘Ã­ch.
7. Cáº­p nháº­t Ä‘Ãºng file.
8. Cáº­p nháº­t `00-course-knowledge/course-index.md`.
9. Cáº­p nháº­t `00-course-knowledge/source-map.md`.
10. Cáº­p nháº­t `INGESTION_LOG.md`.
11. Táº¡o batch report trong `09-reports/`.
12. Kiá»ƒm tra khÃ´ng trá»™n láº«n framework.

## 4. Taxonomy PhÃ¢n Loáº¡i Kiáº¿n Thá»©c

| Loáº¡i kiáº¿n thá»©c | Äá»‹nh nghÄ©a | VÃ­ dá»¥ | NÃªn náº±m á»Ÿ folder nÃ o | KhÃ´ng nÃªn náº±m á»Ÿ folder nÃ o |
|---|---|---|---|---|
| Mindset | TÆ° duy ná»n Ä‘iá»u khiá»ƒn cÃ¡ch lÃ m content. | AI há»— trá»£ tÆ° duy, khÃ´ng thay tháº¿ tÆ° duy. | `00-course-knowledge/`, `01-core-principles/` | `05-templates/`, `06-reference-banks/` |
| Core principle | NguyÃªn táº¯c cá»‘t lÃµi cáº§n tuÃ¢n thá»§ nhiá»u láº§n. | Outline trÆ°á»›c khi viáº¿t. | `01-core-principles/` | `04-commands/`, `05-templates/` |
| Framework | Khung phÃ¢n tÃ­ch hoáº·c ra quyáº¿t Ä‘á»‹nh. | 5W-1H, audience angle. | `02-frameworks/` | `03-workflows/`, `06-reference-banks/` |
| Layout system | NguyÃªn lÃ½ sáº¯p xáº¿p Ã½ trong ná»™i dung. | Tá»•ng phÃ¢n há»£p, quy náº¡p, mÃ³c xÃ­ch. | `02-frameworks/content-layout-systems/` | `02-frameworks/5w1h-framework.md`, `05-templates/` |
| Workflow | Chuá»—i bÆ°á»›c thá»±c thi má»™t nhiá»‡m vá»¥. | Raw idea to Facebook post. | `03-workflows/` | `02-frameworks/`, `06-reference-banks/` |
| Command | Giao diá»‡n tÃ¡c vá»¥ ngÆ°á»i dÃ¹ng gá»i trá»±c tiáº¿p. | `/post`, `/qa`, `/content-score`. | `04-commands/`, `10-system/control/COMMAND_MAPPING.md` | `01-core-principles/` |
| Template | Máº«u Ä‘iá»n Ä‘á»ƒ triá»ƒn khai output. | Facebook post template. | `05-templates/` | `02-frameworks/content-layout-systems/` |
| Checklist / Quality gate | TiÃªu chÃ­ kiá»ƒm tra Ä‘áº¡t/chÆ°a Ä‘áº¡t. | Content logic checklist. | `07-quality-gates/` | `03-workflows/` |
| Example | VÃ­ dá»¥ minh há»a tá»‘t/xáº¥u hoáº·c output máº«u. | Good vs bad outline. | `08-examples/` | `01-core-principles/` |
| Reference bank | Kho cÃ¢u, hook, CTA, transition dÃ¹ng láº¡i. | Hook bank, CTA bank. | `06-reference-banks/` | `02-frameworks/content-layout-systems/` |

## 5. Rule Xá»­ LÃ½ TÃ i Liá»‡u Vá» Bá»‘ Cá»¥c

- 5W-1H lÃ  cÃ´ng cá»¥ má»Ÿ Ã½ vÃ  brainstorming.
- Bá»‘ cá»¥c gá»‘c lÃ  cÃ¡ch sáº¯p xáº¿p Ã½.
- Hook lÃ  Ä‘iá»ƒm kÃ©o sá»± chÃº Ã½.
- CTA lÃ  Ä‘iá»ƒm Ä‘iá»u hÆ°á»›ng hÃ nh Ä‘á»™ng.
- Template lÃ  máº«u triá»ƒn khai theo ná»n táº£ng.

CÃ¡c khÃ¡i niá»‡m nÃ y liÃªn quan nhÆ°ng khÃ´ng Ä‘Æ°á»£c nháº­p chung má»™t file.

Khi náº¡p tÃ i liá»‡u vá» bá»‘ cá»¥c:

- Má»—i bá»‘ cá»¥c cÃ³ file riÃªng trong `02-frameworks/content-layout-systems/`.
- KhÃ´ng Ä‘Æ°a ná»™i dung 5W-1H vÃ o file bá»‘ cá»¥c náº¿u nÃ³ chá»‰ phá»¥c vá»¥ brainstorm.
- KhÃ´ng Ä‘Æ°a hook bank hoáº·c CTA bank vÃ o file bá»‘ cá»¥c.
- KhÃ´ng biáº¿n bá»‘ cá»¥c thÃ nh template ná»n táº£ng náº¿u tÃ i liá»‡u Ä‘ang nÃ³i vá» nguyÃªn lÃ½ sáº¯p xáº¿p Ã½.
- Náº¿u tÃ i liá»‡u nguá»“n chÆ°a Ä‘á»§ rÃµ, ghi `Needs review`, khÃ´ng tá»± bá»‹a.

## 6. Checklist TrÆ°á»›c Khi Káº¿t ThÃºc Má»—i Batch

- [ ] ÄÃ£ ghi nguá»“n chÆ°a?
- [ ] ÄÃ£ ghi file Ä‘Ã­ch chÆ°a?
- [ ] CÃ³ táº¡o report chÆ°a?
- [ ] CÃ³ cáº­p nháº­t `INGESTION_LOG.md` chÆ°a?
- [ ] CÃ³ cáº­p nháº­t `course-index.md` chÆ°a?
- [ ] CÃ³ cáº­p nháº­t `source-map.md` chÆ°a?
- [ ] CÃ³ phÃ¡t hiá»‡n kiáº¿n thá»©c trÃ¹ng khÃ´ng?
- [ ] CÃ³ phÃ¡t hiá»‡n mÃ¢u thuáº«n khÃ´ng?
- [ ] CÃ³ file nÃ o bá»‹ sá»­a ngoÃ i pháº¡m vi khÃ´ng?
- [ ] CÃ³ kiá»ƒm tra khÃ´ng trá»™n láº«n framework, workflow, layout, hook, CTA vÃ  template khÃ´ng?

