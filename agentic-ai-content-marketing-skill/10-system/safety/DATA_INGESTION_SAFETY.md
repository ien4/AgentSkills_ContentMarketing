# Data Ingestion Safety

## Purpose
TÃ i liá»‡u nÃ y báº£o vá»‡ bá»™ skill khá»i lá»—i náº¡p trÃ¹ng, náº¡p sai, ghi Ä‘Ã¨ kiáº¿n thá»©c cÅ©, hoáº·c trá»™n bá»‘ cá»¥c/framework.

## Golden Rule
TrÆ°á»›c má»i bÆ°á»›c náº¡p dá»¯ liá»‡u kiáº¿n thá»©c má»›i, Agent pháº£i yÃªu cáº§u user xÃ¡c nháº­n exact source files.

## Required Confirmation Before New Ingestion
Agent pháº£i há»i hoáº·c yÃªu cáº§u user cung cáº¥p:
1. File nÃ o cáº§n náº¡p?
2. File nÃ o Ä‘Ã£ náº¡p rá»“i?
3. Batch ID má»›i lÃ  gÃ¬?
4. Náº¡p vÃ o folder/file Ä‘Ã­ch nÃ o?
5. CÃ³ Ä‘Æ°á»£c cáº­p nháº­t kiáº¿n thá»©c cÅ© khÃ´ng?
6. CÃ³ Ä‘Æ°á»£c Ä‘á»•i status/confidence khÃ´ng?
7. CÃ³ cáº§n giá»¯ báº£n cÅ© khÃ´ng?

## Duplicate Ingestion Guard
TrÆ°á»›c khi náº¡p file má»›i:
- Kiá»ƒm tra source-map.md.
- Kiá»ƒm tra course-index.md.
- Kiá»ƒm tra INGESTION_LOG.md.
- Kiá»ƒm tra report gáº§n nháº¥t.
- Náº¿u file Ä‘Ã£ náº¡p:
  - KhÃ´ng náº¡p láº¡i tá»± Ä‘á»™ng.
  - Ghi â€œalready ingestedâ€.
  - Chá»‰ update náº¿u user xÃ¡c nháº­n.

## No Overwrite Rule
KhÃ´ng ghi Ä‘Ã¨:
- Definition.
- Core Principle.
- Source Mapping.
- Confidence.
- Status.
náº¿u chÆ°a cÃ³ lÃ½ do rÃµ vÃ  chÆ°a ghi report.

## Layout Knowledge Protection
KhÃ´ng trá»™n:
- 5W-1H vá»›i layout.
- Hook vá»›i layout.
- CTA vá»›i layout.
- Template ná»n táº£ng vá»›i layout.
- Meta-framework vá»›i root layout.

## Required Report For Every Ingestion
Má»—i batch náº¡p dá»¯ liá»‡u pháº£i cÃ³ report:
- Source files scanned.
- Source files used.
- Files updated.
- Knowledge added.
- Status/confidence changes.
- Risks remaining.
- Next recommended prompt.
