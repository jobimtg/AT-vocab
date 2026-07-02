# YSP Phase 5 L02 Extraction Report

_Last updated: 2026-07-02_

## User Confirmation

The user confirmed:

```text
1. Golden L02 filename is correct: Yes
2. Raw Golden L02 HTML can be stored in public repo: No
```

## Safety Decision

The raw Golden L02 HTML source file must not be committed into the public GitHub repository.

Recommended safe path:

```text
Keep raw Golden L02 HTML local.
Extract lesson-data JSON locally.
Commit only validated lesson-data JSON.
```

## Extraction Source

Confirmed local source file:

```text
L02_transportation_fixed_teacher_notes.html
```

Expected target output:

```text
lesson-data/ca-life/u1-l2.json
```

## Local Extraction Result

Local extraction was performed from the confirmed Golden L02 HTML source.

Raw HTML was not committed.

Initial count validation result:

| Field | Expected | Actual | Status |
|---|---:|---:|---:|
| categories | 5 | 5 | Pass |
| core | 25 | 25 | Pass |
| extended | 30 | 30 | Pass |
| phrases | 5 | 5 | Pass |
| dialogues | 5 | 5 | Pass |
| speaking | 5 | 5 | Pass |
| culture | 2 | 2 | Pass |
| pronunciation_words | 5 | 5 | Pass |

Overall local extraction status:

```text
passed
```

## Extracted Content Summary

| Section | Extracted Count |
|---|---:|
| Categories | 5 |
| Core vocabulary | 25 |
| Extended vocabulary | 30 |
| Useful phrases | 5 |
| Dialogues | 5 |
| Speaking questions | 5 |
| Culture notes | 2 |
| Pronunciation focus | 1 |
| Pronunciation words | 5 |

## First / Last Core Vocabulary Check

```text
First Core word: bus
Last Core word: map
```

## Dialogue Titles Extracted

```text
1. Asking About the Bus
2. Riding the Bus
3. Getting Directions
4. Buying a Transit Pass
5. Talking About Commuting
```

## Useful Phrase Titles Extracted

```text
1. Excuse me, which bus goes to downtown?
2. How much is the fare?
3. Where do I transfer?
4. Is this the right bus to the mall?
5. How many stops until Main Street?
```

## Validator Added

A reusable lesson-data validator has been added:

```text
scripts/validate_lesson_data.py
```

It validates:

```text
required top-level fields
required meta fields
course / CEFR count rules
core vocabulary fields
extended vocabulary fields
phrases
dialogues and dialogue lines
speaking questions
culture notes
pronunciation fields
```

## Current Limitation

The full JSON was generated locally, but the current GitHub connector cannot safely attach a generated local file directly into the repo as a file upload.

To avoid copy/paste corruption of a large JSON file, do not manually paste the full JSON through chat.

## Recommended Next Step

Use local Codex or a local script command to commit the already-generated JSON safely:

```bash
python3 scripts/extract_l02_source_data.py \
  --input L02_transportation_fixed_teacher_notes.html \
  --output lesson-data/ca-life/u1-l2.json

python3 scripts/validate_lesson_data.py lesson-data/ca-life/u1-l2.json --pretty
```

Then commit only:

```text
lesson-data/ca-life/u1-l2.json
```

Do not commit:

```text
L02_transportation_fixed_teacher_notes.html
```

## Next Phase After JSON Commit

```text
Phase 5.3 — Store fixed L02 template / renderer
```

Do not generate or replace public lesson HTML until:

```text
1. lesson-data/ca-life/u1-l2.json exists
2. scripts/validate_lesson_data.py passes
3. fixed L02 template is stored
4. generated proof is reviewed
```
