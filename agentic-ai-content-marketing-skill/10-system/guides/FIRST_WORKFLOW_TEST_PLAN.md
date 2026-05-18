# First Workflow Test Plan â€” Agentic AI Content Marketing Skill

## 1. Purpose
Káº¿ hoáº¡ch nÃ y dÃ¹ng Ä‘á»ƒ test thá»±c táº¿ bá»™ skill sau khi Ä‘Ã£ packaging-ready.

## 2. Scope
Test cÃ¡c workflow chÃ­nh:
- /outline
- /post
- /qa
- /content-score
- layout selection
- ingestion safety prompt

## 3. Out of Scope
KhÃ´ng test:
- Ingest docs má»›i
- Táº¡o layout má»›i
- NÃ¢ng confidence/status layout
- Sá»­a docs
- Test báº±ng dá»¯ liá»‡u nháº¡y cáº£m
- Test automation script

## 4. Test Environment
Ghi:
- CÃ³ thá»ƒ cháº¡y trÃªn Blackbox AI / Kimi K2.6 / Minimax M2.7 / Antigravity Gemini 3 Flash / Gemini 3.1 Pro Low / Codex khi cÃ³ credit.
- Vá»›i hiá»‡n táº¡i, Æ°u tiÃªn Blackbox AI Kimi K2.6 cho read/check vÃ  Minimax M2.7 cho content output dÃ i.

## 5. Test Cases

Táº¡o báº£ng test case:

| Test ID | Workflow | Input Type | Goal | Expected Output | Pass Criteria | Risk |
|---|---|---|---|---|---|---|
| T01 | /outline | brief ngáº¯n | Láº­p outline tá»« brief Facebook | Content goal; Audience; Selected layout; Layout type; Marketing outline 5 pháº§n; Layout-fit notes | CÃ³ Ä‘á»§ 6 pháº§n output; layout Ä‘Æ°á»£c chá»n tá»« matrix; cÃ³ layout-fit notes | Chá»n sai layout hoáº·c thiáº¿u validate |
| T02 | /post | ná»™i dung thÃ´ | Viáº¿t bÃ i hoÃ n chá»‰nh tá»« ná»™i dung thÃ´ | Audience; Pain point; Insight; 5W-1H table; Selected layout; 10 hooks; Final post; CTA; QA checklist | CÃ³ Ä‘á»§ yÃªu cáº§u output; CTA rÃµ; QA checklist cÃ³ Pass/Fail hoáº·c Ä‘áº¡t/chÆ°a Ä‘áº¡t theo checklist | BÃ i thiáº¿u CTA/insight; bá» qua layout selection |
| T03 | /qa | bÃ i viáº¿t yáº¿u | Kiá»ƒm QA vÃ  báº¯t lá»—i | Fail rÃµ; chá»‰ ra thiáº¿u audience/pain/CTA/layout-fit; gá»£i Ã½ sá»­a | QA chá»‰ ra Ä‘Ãºng thiáº¿u sÃ³t; cÃ³ gá»£i Ã½ sá»­a dá»±a trÃªn checklist | Bá» sÃ³t lá»—i chÃ­nh |
| T04 | /content-score | ná»™i dung cÃ³ outline/layout/CTA | Cháº¥m Ä‘iá»ƒm ná»™i dung | Score cÃ³ Layout Fit/10; Score cÃ³ Content Logic; Score cÃ³ CTA; Score cÃ³ Platform Fit | Äiá»ƒm/tiÃªu chÃ­ khÃ´ng bá»‹ thiáº¿u; cÃ³ váº¥n Ä‘á» cáº§n sá»­a | Cháº¥m chung chung |
| T05 | layout misuse guard | yÃªu cáº§u dÃ¹ng wrong layout | Kiá»ƒm guardrail misuse | Agent tá»« chá»‘i dÃ¹ng Professional Content Marketing Layout nhÆ° layout chÃ­nh; gá»£i Ã½ chá»n root layout khÃ¡c; dÃ¹ng Professional planning nhÆ° meta-check | CÃ³ tá»« chá»‘i Ä‘Ãºng; Ä‘á» xuáº¥t root layout thay tháº¿; khÃ´ng dÃ¹ng meta-framework nhÆ° root layout | Bá» qua guardrail |
| T06 | ingestion safety guard | yÃªu cáº§u ingest ngay | Kiá»ƒm ingestion safety | Agent khÃ´ng ingest ngay; yÃªu cáº§u user xÃ¡c nháº­n exact source files; kiá»ƒm source-map/course-index/INGESTION_LOG trÆ°á»›c | CÃ³ xÃ¡c nháº­n exact source files; cÃ³ kiá»ƒm log/source-map; khÃ´ng náº¡p láº¡i file Ä‘Ã£ ingest náº¿u chÆ°a xÃ¡c nháº­n | Náº¡p trÃ¹ng hoáº·c bá» qua xÃ¡c nháº­n |

Báº¯t buá»™c cÃ³ cÃ¡c test:
### T01 â€” /outline vá»›i brief ngáº¯n
Input:
â€œViáº¿t outline cho bÃ i Facebook vá» dá»‹ch vá»¥ thiáº¿t káº¿ website cho doanh nghiá»‡p nhá».â€

Expected:
- Content goal
- Audience
- Selected layout
- Layout type
- Marketing outline 5 pháº§n
- Layout-fit notes

### T02 â€” /post vá»›i ná»™i dung thÃ´
Input:
â€œWebsite khÃ´ng chá»‰ Ä‘á»ƒ cho cÃ³. Website pháº£i giÃºp khÃ¡ch hÃ ng tin báº¡n nhanh hÆ¡n.â€

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

### T03 â€” /qa má»™t bÃ i viáº¿t yáº¿u
Input:
Má»™t bÃ i viáº¿t chung chung, thiáº¿u CTA, thiáº¿u audience.

Expected:
- Fail rÃµ
- Chá»‰ ra thiáº¿u audience/pain/CTA/layout-fit
- Gá»£i Ã½ sá»­a

### T04 â€” /content-score
Input:
Má»™t bÃ i post Ä‘Ã£ cÃ³ outline/layout/CTA.

Expected:
- Score cÃ³ Layout Fit / 10
- Score cÃ³ Content Logic
- Score cÃ³ CTA
- Score cÃ³ Platform Fit

### T05 â€” Layout misuse guard
Input:
YÃªu cáº§u dÃ¹ng Professional Content Marketing Layout nhÆ° layout chÃ­nh.

Expected:
- Agent tá»« chá»‘i dÃ¹ng nhÆ° root layout
- Gá»£i Ã½ chá»n root layout khÃ¡c
- DÃ¹ng Professional planning nhÆ° meta-check

### T06 â€” Ingestion safety guard
Input:
â€œNáº¡p toÃ n bá»™ docs vÃ o skill luÃ´n.â€

Expected:
- Agent khÃ´ng ingest ngay
- YÃªu cáº§u user xÃ¡c nháº­n exact source files
- Kiá»ƒm source-map/course-index/INGESTION_LOG trÆ°á»›c

## 6. Pass/Fail Rules

PASS náº¿u:
- Agent chá»n Ä‘Ãºng file cáº§n Ä‘á»c theo Resource Map.
- Agent khÃ´ng Ä‘á»c toÃ n bá»™ folder khi khÃ´ng cáº§n.
- Agent chá»n layout tá»« matrix.
- Agent validate báº±ng taxonomy.
- Agent cháº¡y layout-fit QA.
- Agent khÃ´ng dÃ¹ng Professional planning nhÆ° root layout.
- Agent khÃ´ng ingest docs khi chÆ°a xÃ¡c nháº­n source files.
- Output cÃ³ audience, pain point, insight, selected layout, CTA, QA.

FAIL náº¿u:
- Agent bá» qua layout selection.
- Agent khÃ´ng validate taxonomy.
- Agent khÃ´ng cÃ³ CTA.
- Agent dÃ¹ng meta-framework nhÆ° root layout.
- Agent tá»± ingest docs.
- Agent náº¡p láº¡i file Ä‘Ã£ ingest.
- Agent khÃ´ng há»i user xÃ¡c nháº­n exact source files trÆ°á»›c ingestion.

## 7. Recommended Model For Each Test
Táº¡o báº£ng:

| Test | Recommended model | Reason |
|---|---|---|
| T01 | Kimi K2.6 | Láº­p outline/check Ä‘á»c ngáº¯n |
| T02 | Minimax M2.7 | Viáº¿t output dÃ i, bÃ i post Ä‘áº§y Ä‘á»§ |
| T03 | Kimi K2.6 | Kiá»ƒm QA theo checklist |
| T04 | Kimi K2.6 | Cháº¥m Ä‘iá»ƒm theo tiÃªu chÃ­ |
| T05 | Kimi K2.6 | Kiá»ƒm guardrail misuse |
| T06 | Kimi K2.6 | Kiá»ƒm ingestion safety prompts |
| Notes | (Náº¿u Codex cÃ³ credit) Codex | Kiá»ƒm file/report sau test (khÃ´ng cháº¡y ingestion) |

## 8. Test Report Template
Táº¡o template:

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
Ghi rÃµ:
File nÃ y chá»‰ lÃ  test plan.
KhÃ´ng cháº¡y test trong Batch 2H.
Batch test thá»±c táº¿ sáº½ lÃ m á»Ÿ prompt riÃªng.
