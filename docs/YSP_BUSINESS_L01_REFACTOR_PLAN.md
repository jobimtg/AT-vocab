# YSP Business L01 Refactor Plan

_Last updated: 2026-06-30_

## Current Problem

`lessons/business/u1-l1.html` exists, but it is not a safe future production template.

Current issue:

```text
iframe / base64 viewer structure
```

## Why It Must Not Be Used As Template

| Risk | Impact |
|---|---|
| Hard to inspect | Content is not easily reviewed in normal HTML structure |
| Hard to validate | Site validator can miss internal embedded structure |
| Hard to edit | Small text changes become high-risk |
| Hard to reuse | Not aligned with Golden L02 renderer architecture |
| Product risk | Business course would look inconsistent from other YSP lessons |

## Refactor Rule

Do not directly rewrite Business L01 until the target data-source workflow is ready.

Correct order:

```text
1. Create or confirm Business L01 registry row.
2. Extract Business L01 content into lesson-data/business/u1-l1.json.
3. Validate content counts against B2 rules.
4. Build from Golden L02 renderer.
5. Compare public output visually.
6. Replace existing HTML only after approval.
```

## Business Course Standard

| Field | Required Rule |
|---|---|
| Course ID | `biz-en` |
| CEFR | B2 |
| Core | 40 |
| Extended | 30 |
| Phrases | 5 |
| Dialogues | 5 |
| Speaking | 5 |
| Culture | 2 |
| Pronunciation | 1 |

## Refactor Success Criteria

Business L01 is refactor-ready only when:

```text
[ ] Source data exists.
[ ] No iframe/base64 lesson body remains.
[ ] Uses 10-tab Golden L02 order.
[ ] Uses short class names.
[ ] Uses data-driven renderer.
[ ] Uses global nav loader exactly once.
[ ] Passes site validator.
[ ] Passes Senior ESL Reviewer gate.
```

## Current Status

```text
Business L01 refactor plan complete.
Implementation not started.
```

Do not begin new Business lessons until this refactor path is approved.
