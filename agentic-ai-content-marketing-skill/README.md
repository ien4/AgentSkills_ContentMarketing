# Agentic AI Content Marketing Skill

# Start Here / Navigation Hub

## If you are an AI Agent
Read:
1. `SKILL.md`
2. `10-system/control/COMMAND_MAPPING.md`
3. `10-system/control/PROMPT_MASTER.md`
4. Relevant command file in `04-commands/`
5. Relevant quality gate in `07-quality-gates/`

## If you are an Operator / Team Member
Read:
1. `10-system/guides/OPERATOR_PLAYBOOK.md`
2. `10-system/guides/USAGE_GUIDE.md`
3. `10-system/control/COMMAND_MAPPING.md`
4. `07-quality-gates/final-output-checklist.md`

## If you are maintaining the skill
Read:
1. `10-system/handoff/FINAL_PACKAGING_SNAPSHOT.md`
2. `10-system/handoff/HANDOFF_SUMMARY.md`
3. `INGESTION_LOG.md`
4. `10-system/control/PACKAGING_CHECKLIST.md`
5. `10-system/safety/DATA_INGESTION_SAFETY.md`

## If you want to ingest new knowledge
Stop first.
Read:
1. `10-system/safety/DATA_INGESTION_SAFETY.md`
2. `10-system/safety/INGESTION_SOP.md`
3. `00-course-knowledge/source-map.md`
4. `00-course-knowledge/course-index.md`
5. `INGESTION_LOG.md`

Then ask user to confirm exact source files before any ingestion.

## File Role Clarification
- **`SKILL.md`**: runtime entry file for AI agent.
- **`README.md`**: navigation hub for humans and maintainers.
- **`10-system/guides/OPERATOR_PLAYBOOK.md`**: daily operating guide.
- **`10-system/guides/USAGE_GUIDE.md`**: detailed user guide.
- **`10-system/handoff/FINAL_PACKAGING_SNAPSHOT.md`**: final state snapshot.
- **`10-system/handoff/HANDOFF_SUMMARY.md`**: handoff summary for another model/operator.
- **`09-reports/`**: audit trail and historical reports, not daily reading material.
- **`Agent_Skills.md`** (náº¿u cÃ³): reference/comparison file, not the primary runtime entry unless explicitly configured.

## Do Not Read Everything By Default
KhÃ´ng Ä‘á»c toÃ n bá»™ 90 files cho task nhá».
Chá»‰ Ä‘á»c Ä‘Ãºng file theo task:
- viáº¿t post â†’ `/post` + layout + QA
- outline â†’ `/outline` + layout taxonomy/matrix
- QA â†’ `/qa` + quality gates
- content-score â†’ `/content-score` + quality gates
- ingestion â†’ ingestion safety files first

---

## Má»¥c TiÃªu

Bá»™ skill nÃ y biáº¿n kiáº¿n thá»©c khÃ³a há»c Content Marketing thÃ nh má»™t há»‡ thá»‘ng cÃ³ thá»ƒ dÃ¹ng cho AI Agent.

Skill táº­p trung vÃ o:

- TÆ° duy láº­p outline trÆ°á»›c khi viáº¿t.
- Bá»‘ cá»¥c Marketing 5 pháº§n.
- Brainstorm báº±ng 5W-1H theo hai gÃ³c nhÃ¬n.
- Viáº¿t Facebook post, hook, CTA, rewrite vÃ  QA ná»™i dung.
- Kiá»ƒm soÃ¡t logic trÆ°á»›c khi táº¡o báº£n viáº¿t cuá»‘i.

## CÃ¡ch DÃ¹ng

KÃ­ch hoáº¡t skill khi cáº§n xá»­ lÃ½ ná»™i dung marketing tá»« brief, Ã½ tÆ°á»Ÿng thÃ´ hoáº·c tÃ i liá»‡u khÃ³a há»c.

CÃ¡c command ná»n:

- `/outline`: láº­p dÃ n Ã½.
- `/brainstorm-5w1h`: phÃ¢n tÃ­ch Ã½ tÆ°á»Ÿng báº±ng 5W-1H.
- `/post`: viáº¿t bÃ i Facebook hoáº·c social post.
- `/hook`: táº¡o hÆ°á»›ng má»Ÿ bÃ i.
- `/rewrite`: viáº¿t láº¡i ná»™i dung.
- `/content-score`: cháº¥m Ä‘iá»ƒm ná»™i dung.
- `/qa`: kiá»ƒm tra cháº¥t lÆ°á»£ng ná»™i dung.

## Cáº¥u TrÃºc ThÆ° Má»¥c

```text
agentic-ai-content-marketing-skill/
â”œâ”€â”€ 00-course-knowledge/
â”œâ”€â”€ 01-core-principles/
â”œâ”€â”€ 02-frameworks/
â”œâ”€â”€ 03-workflows/
â”œâ”€â”€ 04-commands/
â”œâ”€â”€ 05-templates/
â”œâ”€â”€ 06-reference-banks/
â”œâ”€â”€ 07-quality-gates/
â”œâ”€â”€ 08-examples/
â””â”€â”€ 09-reports/
```

## Ná»™i Dung Batch 001

Batch 001 Ä‘Ã£ náº¡p cÃ¡c nhÃ³m kiáº¿n thá»©c:

- Bá»‘ cá»¥c ná»™i dung Marketing 5 pháº§n.
- TÆ° duy láº­p dÃ n Ã½ trÆ°á»›c khi viáº¿t.
- CÃ´ng thá»©c 5W-1H.
- 5W-1H theo gÃ³c nhÃ¬n Marketer vÃ  khÃ¡ch hÃ ng.
- NguyÃªn táº¯c dÃ¹ng AI nhÆ° cÃ´ng cá»¥ há»— trá»£ tÆ° duy.

## CÃ¡ch Náº¡p ThÃªm TÃ i Liá»‡u Sau NÃ y

Khi cÃ³ tÃ i liá»‡u má»›i:

1. Äá»c vÃ  tÃ¡ch cÃ¡c Ã½ cÃ³ thá»ƒ biáº¿n thÃ nh nguyÃªn táº¯c, framework, workflow, command, template, checklist hoáº·c vÃ­ dá»¥.
2. Cáº­p nháº­t `00-course-knowledge/course-index.md` vÃ  `00-course-knowledge/source-map.md`.
3. Ghi batch má»›i vÃ o `INGESTION_LOG.md`.
4. Táº¡o bÃ¡o cÃ¡o theo `09-reports/ingestion-report-template.md`.
5. KhÃ´ng ghi Ä‘Ã¨ ná»™i dung cÅ© náº¿u chÆ°a kiá»ƒm tra tÃ¡c Ä‘á»™ng.

## Knowledge Ingestion Workflow

`docs/` lÃ  nguá»“n thÃ´ bÃªn ngoÃ i skill. KhÃ´ng sá»­a, khÃ´ng xÃ³a, khÃ´ng di chuyá»ƒn tÃ i liá»‡u trong `docs/` khi náº¡p kiáº¿n thá»©c.

`10-system/safety/INGESTION_SOP.md` lÃ  quy trÃ¬nh chuáº©n Ä‘á»ƒ náº¡p tÃ i liá»‡u khÃ³a há»c, video, transcript, PDF hoáº·c DOCX vÃ o bá»™ skill. Má»—i batch cáº§n trÃ­ch xuáº¥t, phÃ¢n loáº¡i, chuáº©n hÃ³a, source mapping vÃ  táº¡o report.

`02-frameworks/content-layout-systems/` lÃ  khu riÃªng cho cÃ¡c bá»‘ cá»¥c gá»‘c trong Content Marketing. ÄÃ¢y lÃ  nÆ¡i náº¡p cÃ¡c há»‡ thá»‘ng nhÆ° mÃ³c xÃ­ch, tá»•ng phÃ¢n há»£p, quy náº¡p, diá»…n dá»‹ch, liá»‡t kÃª hoáº·c dáº«n dáº¯t thuyáº¿t phá»¥c. KhÃ´ng trá»™n khu nÃ y vá»›i 5W-1H, hook bank, CTA bank hoáº·c template bÃ i post.

## Layout Selection Safety

Khi cáº§n chá»n bá»‘ cá»¥c cho content:

1. Chá»n layout tá»« `02-frameworks/content-layout-systems/layout-selection-matrix.md`.
2. Validate loáº¡i layout, tráº¡ng thÃ¡i vÃ  confidence báº±ng `02-frameworks/content-layout-systems/layout-taxonomy.md`.
3. Kiá»ƒm báº±ng `07-quality-gates/layout-fit-checklist.md`.
4. Chá»‰ dÃ¹ng meta-framework nhÆ° bÆ°á»›c kiá»ƒm tra hoáº·c planning layer sau khi Ä‘Ã£ chá»n layout cá»¥ thá»ƒ.
5. Náº¿u layout cÃ³ confidence Medium/Low, ghi rÃµ rá»§i ro trong QA notes.

KhÃ´ng dÃ¹ng Professional Content Marketing Planning Framework nhÆ° bá»‘ cá»¥c chÃ­nh. KhÃ´ng dÃ¹ng Dáº«n dáº¯t thuyáº¿t phá»¥c nhÆ° layout Ä‘á»™c láº­p khi chÆ°a validate vá»›i Quy náº¡p hoáº·c layout gá»‘c khÃ¡c.

## NguyÃªn Táº¯c Báº£o TrÃ¬

- Má»i file trong skill lÃ  Markdown.
- Ná»™i dung pháº£i cÃ³ heading rÃµ.
- KhÃ´ng thÃªm code app vÃ o skill.
- KhÃ´ng xÃ³a file cÅ© khi náº¡p tÃ i liá»‡u má»›i.
- Má»—i batch cáº§n ghi rÃµ nguá»“n, kiáº¿n thá»©c náº¡p, file cáº­p nháº­t vÃ  pháº§n cÃ²n thiáº¿u.
