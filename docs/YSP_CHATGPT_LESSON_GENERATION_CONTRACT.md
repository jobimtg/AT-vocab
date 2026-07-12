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
```

This blocks generated/contract-aware lesson commits when the lesson fails the content contract.
