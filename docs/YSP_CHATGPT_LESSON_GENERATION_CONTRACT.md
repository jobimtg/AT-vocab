# YSP ChatGPT Lesson Generation Contract — v3.9

This file is the production contract for future ChatGPT/Claude-generated lesson HTML files in `AT-vocab`.

Even during workflow testing, generated lessons must match publishable lesson depth. Shallow test content is not acceptable because it causes repeated corrections and makes the production direction unclear.

## Canonical reference

Current reference lesson:

- Course: Canada Life & Career English
- File: `lessons/ca-life/u1-l3.html`
- Title: `L03 — Phone Plans & Internet 手機與網路`
- Image prefix: `l03`
- Contract marker: `data-ysp-contract="v3.9"`

Future ChatGPT-generated lessons must follow the same level of content depth and the same Golden L02 interactive architecture.

## Mandatory structure

Every generated lesson must be a single complete `.html` file.

Required:

- `html lang="zh-Hant"`
- YSP Learn & Shine header/footer
- exactly 10 tabs
- L02 short class-name system
- data-driven renderer
- `data-ysp-contract="v3.9"` on the body element
- standard global nav loader: `../../js/ysp-global-nav.js` with `data-ysp-base="../../"`

## Mandatory 10-tab order

1. `📊 Overview｜總覽`
2. `📚 Core Vocabulary｜核心單字`
3. `📖 Extended Vocabulary｜延伸單字`
4. `🔁 Drilling Practice｜句型替換練習`
5. `💬 Useful Phrases｜實用句型`
6. `🎯 Pronunciation Spotlight｜發音焦點`
7. `🎭 Dialogue Practice｜對話練習`
8. `🗣️ Speaking Questions｜口說問題`
9. `🌍 Culture Notes｜文化補充`
10. `📋 Progress Check｜學習進度`

Do not create extra tabs such as separate Warm-up, Spiral Review, or Practice tabs.

## Mandatory counts

### Canada Life & Career English

| CEFR | Core | Extended | Phrases | Dialogues | Speaking | Culture | Pronunciation |
|---|---:|---:|---:|---:|---:|---:|---|
| A2 | 25 | 30 | 5 | 5 | 5 | 2 | 1 spotlight, 3–5 words |
| B1 | 30 | 30 | 5 | 5 | 5 | 2 | 1 spotlight, 3–5 words |

### Travel English

| CEFR | Core | Extended | Phrases | Dialogues | Speaking | Culture | Pronunciation |
|---|---:|---:|---:|---:|---:|---:|---|
| A1 | 15 | 30 | 5 | 5 | 5 | 2 | 1 spotlight, 3–5 words |

### Business English

| CEFR | Core | Extended | Phrases | Dialogues | Speaking | Culture | Pronunciation |
|---|---:|---:|---:|---:|---:|---:|---|
| B2 | 40 | 30 | 5 | 5 | 5 | 2 | 1 spotlight, 3–5 words |

## Core vocabulary rules

Each Core item must include:

- English word
- Traditional Chinese meaning
- IPA / pronunciation
- category index `0–4`
- two meaning/explanation sentences
- two example sentences
- two practice blank sentences
- one inline SVG icon using `viewBox="0 0 80 80"`

Short word cards without explanations and examples are invalid.

## Drilling Practice rules

The Drilling Practice tab must use the Golden L02 interactive flip-card system. A static list of sentence patterns plus visible answers is invalid.

Required three modes:

1. `L1 單字跟唸` / `L1 跟唸`
   - Show the Core English word.
   - Show IPA/pronunciation.
   - Hidden answer reveals the Traditional Chinese meaning.
   - Teacher reads and the student repeats three times.

2. `L2 整句跟唸`
   - Show one complete Core example sentence, normally `e1`.
   - Hidden answer reveals the target Core word and Traditional Chinese meaning.
   - Teacher reads the complete sentence and the student repeats it.

3. `L3 中翻英`
   - Show the Traditional Chinese meaning.
   - Hidden answer reveals the English word and IPA.
   - Student must produce the English before revealing the answer.

Interaction requirements:

- Use one flip/reveal card at a time.
- Clicking the card must reveal/hide the answer.
- Include Previous and Next controls.
- Show the current position, for example `3 / 15`.
- Iterate through the complete Core vocabulary set, not only the first 10 words.
- Reuse the same Core fields used by the vocabulary cards: `en`, `zh`, `pr`, and `e1`.
- The required short CSS/interaction tokens are `.dzone`, `.dc`, `.da`, `.dn`, `.dbtn`, `.lt`, and `.lb`.

Forbidden shallow format:

```text
Pattern 1
Could I have a _______ room?
Answer: quiet
```

The drill must behave like a student practice tool, not an answer sheet.

## Dialogue rules

Each generated lesson must include exactly 5 dialogues.

Each dialogue must include:

- title
- Chinese title
- situation
- role A
- role B
- dialogue lines
- Now you try / role-play variation
- teacher note

Each dialogue must have at least 6 lines. The L03 reference uses 8 lines per dialogue.

Short 2–3 line dialogues are invalid.

## Gallery automation rules

Every generated lesson must pre-reserve raw HTML gallery blocks. Do not generate gallery blocks inside JavaScript strings.

Required gallery blocks:

- `lXX-phrases`
- `lXX-pronunciation`
- `lXX-d01`
- `lXX-d02`
- `lXX-d03`
- `lXX-d04`
- `lXX-d05`
- `lXX-speaking`
- `lXX-culture`

Each gallery block must include:

- `class="ysp-image-gallery"`
- `data-ysp-gallery`
- `data-ysp-image-dir`
- `data-ysp-image-prefix`
- `YSP_IMAGE_GALLERY_MOUNT_START`
- `YSP_IMAGE_GALLERY_MOUNT_END`

Renderer functions must update only content mount divs, for example:

```js
document.getElementById("t4c").innerHTML = h;
```

Renderer functions must never overwrite full gallery tabs:

```js
document.getElementById("t4").innerHTML = h;
```

## Image inbox filenames for L03

```text
image-inbox/ca-life-l03-phrases-1.webp
image-inbox/ca-life-l03-pronunciation-1.webp
image-inbox/ca-life-l03-d01-model.webp
image-inbox/ca-life-l03-d01-practice.webp
image-inbox/ca-life-l03-d02-model.webp
image-inbox/ca-life-l03-d02-practice.webp
image-inbox/ca-life-l03-d03-model.webp
image-inbox/ca-life-l03-d03-practice.webp
image-inbox/ca-life-l03-d04-model.webp
image-inbox/ca-life-l03-d04-practice.webp
image-inbox/ca-life-l03-d05-model.webp
image-inbox/ca-life-l03-d05-practice.webp
image-inbox/ca-life-l03-speaking-1.webp
image-inbox/ca-life-l03-culture-1.webp
```

## Image size rules

- Aspect ratio: 16:9
- Recommended size: 1600 × 900 px
- Preferred format: `.webp`
- Target file size: under 1 MB
- Warning: over 2 MB
- Block / move to `_oversize`: over 5 MB

## Blocking validation

The workflow runs:

```bash
python3 scripts/ysp_lesson_contract_check.py
python3 scripts/ysp_drilling_contract_check.py
```

These block generated/contract-aware lesson commits when lesson content or the three-mode Drilling Practice system fails the production contract.

---

## v4 Addendum — Image & Content Fidelity Contract (2026-07-26)

This addendum was added after a Travel L04 comparison between an earlier ChatGPT draft and a corrected Claude draft surfaced three gaps in this contract: dialogue line counts were not locked to source data, the image-prompt count was underspecified, and Tab 10 Previously Learned was not required to be collapsible. It extends, and does not replace, the sections above.

Full detail lives in two companion files kept in sync with this document:

- Notion: `📋 ESL Skill Backup` → `🔒 ChatGPT 課程產出強制執行合約`
- Repo: this file (source of truth for CI-facing rules) plus `scripts/ysp_lesson_contract_check.py` (blocking validator)

### Content lock

Dialogue, phrase, vocabulary, speaking-question, and culture-note **text** must come only from the user-provided lesson JSON/HTML. No rewriting, no adding or removing lines, no reordering, no summarizing. The only permitted transformation is applying the `tp` (Try again) field's described substitution in the Practice-version dialogue image, using the exact wording from `tp` — never an invented substitution.

### Mandatory fifteen image prompts

Every lesson must produce exactly 15 image prompts:

| Type | Count | Source array |
|---|---:|---|
| A — Useful Phrases | 1 | `phrases[]` |
| B — Dialogue Practice (Model + Practice × 5) | 10 | `dialogues[]` |
| C — Pronunciation Spotlight | 1 | `pronunciation` |
| D — Speaking Questions | 1 | `speaking[]` |
| E — Culture Notes (warm-up + closing) | 2 | `culture[]` |

Producing only Types A–C (12 prompts) is an incomplete delivery.

Each Dialogue Practice image must render **every line** in that dialogue's `lines[]` array — the count is whatever the source data contains (this contract does not fix it at 6 or 8; earlier text in this document illustrating "8 lines per dialogue" was a description of the L03 reference lesson, not a hard ceiling). Line-count mismatches between source data and rendered image content are a CRITICAL violation.

### Progress Check accordion (Tab 10)

`Previously Learned` must render as a collapsible accordion — one expandable/collapsible block per prior lesson (`.pvh` header + `.pvb` body, toggled via `classList.toggle('open')`) — never a fully expanded flat word list. See Notion Skill Backup §10.2 for the canonical `totalShown` safe-sum formula and reference markup.

### No generic filler sentences

Core `m1`/`m2`/`e1`/`e2` and Extended `m`/`ex` fields must never use template patterns such as:

- `"A useful [topic] word or expression for {word}."`
- `"Please help me with {word}."`

Definitions and examples must be specific, situational sentences (ideally including a name, number, place, or time), matching the standard already used in the corrected Travel L04 lesson.

### Filename dual convention

- Lesson HTML filenames: no zero-padding — `lessons/<course>/u{unit}-l{lesson}.html` (e.g. `u1-l4.html`)
- Image filename prefixes: zero-padded — `l{lesson:02d}-{section}-{n}.png` (e.g. `l04-phrases-1.png`)

Do not invent a third convention (e.g. do not name a lesson HTML file `u1-l04.html`).

### Mandatory self-check before delivery

Before delivering any lesson HTML or image prompt set, output a self-check block covering: dialogue line-count match (per dialogue), image count (must equal 15), Progress Check accordion presence, generic-filler scan result, and filename convention compliance. Any "✗" blocks delivery until fixed.
