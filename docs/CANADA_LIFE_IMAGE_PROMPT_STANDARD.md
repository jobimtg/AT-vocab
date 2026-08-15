# YSP Canada Life & Career English Image Prompt Standard

**Version:** 1.2

**Effective:** 2026-08-13 (America/Vancouver)

**Scope:** Canada Life & Career English lessons only

## Golden references

- Dialogue Model: `Dialogue Practice_U1L1_1.png`
- Dialogue Practice: `Dialogue Practice_U1L1_2-2.png`
- Phrases: `l01-phrases.png`
- Pronunciation: `Pronunciation_U1L1.png`
- Dialogue illustration-size references:
  - `ca-life-l02-illustration-size-SAMPLE-A-COMPACT.png`
  - `ca-life-l02-illustration-size-SAMPLE-B-BALANCED.png`
  - `ca-life-l02-illustration-size-SAMPLE-C-UPPER-RANGE.png`
- Approved published application: `ca-life-l02-d01-model-REFERENCE-v2.png`

Pronunciation also follows `YSP_PRONUNCIATION_IMAGE_STANDARD.md` and its Travel L02/L03 references.

## Mandatory routing

1. Read approved lesson JSON/HTML.
2. Read this Canada Life standard.
3. Read the shared Pronunciation standard for pronunciation.
4. Find and fully read the lesson-specific `*Image_Prompts*.md`.
5. If it is missing, STOP before image generation and warn the user. Ask for a
   Canada Life lesson prompt file following the approved lesson-prompt structure;
   never improvise the image prompts from JSON/HTML alone.
6. Use Canada Life references for non-pronunciation style.
7. Never apply Travel's modern-card style to Canada Life non-pronunciation images.

## Visual identity

- Vintage Canadian travel-poster/editorial-infographic aesthetic.
- Warm aged-paper/parchment background with subtle print grain and engraved ink texture.
- Deep navy, maple orange/rust, warm cream, restrained gold.
- Canadian mountains, evergreens, skyline, harbour, civic architecture, transit, neighbourhood, or lesson-specific landmarks.
- Maple leaves as separators and decorative anchors.
- Bold condensed/slab-serif English display titles with clear Traditional Chinese.
- Thin navy/orange borders, ribbon headings, ruled separators, and pictogram icons.
- Detailed hand-illustrated scenes with inked outlines and warm editorial shading; never photo or glossy 3D.
- Canadian context is lesson-specific, not generic tourism filler.

## Dialogue contract

- Oversized `ENGLISH DIALOGUE PRACTICE`.
- Numbered bilingual scene ribbon and Canadian panorama.
- Left: Situation plus Person A/B identity cards and small portraits.
- Center: full Model or Practice dialogue with every source line and A/B badges.
- Right: detailed Canadian-life situation illustration using the A/B/C adaptive
  illustration-size system below. A large illustration is not mandatory when it
  would reduce teaching-text size or safe margins.
- Bottom: Key Vocabulary strip with icons/Chinese.
- Bottom-right: `NOW YOU TRY! 換你說` with exact `tp` and matching vignette.
- Model/Practice retain scene and characters; Practice changes only `tp`-authorized text and only that text receives rust/orange emphasis.

## Adaptive A/B/C illustration-size system

All three approved illustration sizes are valid. Select the size from the actual
teaching-text density of each image; do not choose randomly and do not force every
lesson image into one fixed ratio.

| Level | Target illustration footprint | Use when |
| --- | --- | --- |
| A — Compact | about 29% of canvas width; about 35% of canvas height | Long dialogue, long bilingual labels, dense notes, long `tp`, or any layout where text needs maximum width |
| B — Balanced | about 33% of canvas width; about 39% of canvas height | Normal dialogue/text density; default starting choice and closest to the approved D01 Reference v2 balance |
| C — Upper-range | about 37% of canvas width; about 43% of canvas height | Short dialogue or light text density with ample safe space; use when the scene materially supports comprehension |

These percentages are visual targets, not permission to crop or stretch artwork.
Small adjustments are allowed to preserve the Golden layout, but the illustration
must remain within the A-to-C range unless the user explicitly approves an exception.

### Required selection procedure

1. Place all source-locked teaching text first: title, situation, characters, every
   dialogue line, Key Vocabulary, `NOW YOU TRY`, branding, and footer.
2. Estimate the longest lines and total line count, including Traditional Chinese.
3. Start with B. Move to A if any teaching text must shrink, wrap awkwardly, crowd a
   border, or lose safe margins. Move to C only when all text remains comfortably
   readable and the extra scene area improves instruction.
4. Text hierarchy takes priority over illustration size. Never omit, paraphrase,
   compress, or recolor source-locked text to make room for a larger illustration.
5. Model and Practice images for the same dialogue should normally use the same size
   level. They may differ by one level only when the Practice substitution materially
   changes text density; record the reason in the lesson-specific prompt.
6. The lesson-specific `Image_Prompts` file must declare `Illustration size: A`, `B`,
   or `C` for every dialogue asset, with a one-line density reason.
7. Reviewer verifies the chosen level against the final raster, readable text size,
   safe margins, and 1920x1080 gallery rendering. A larger illustration that causes
   cramped or smaller teaching text is a blocking failure.

This adaptive system applies to Canada Life non-pronunciation scene illustrations.
Pronunciation continues to follow `YSP_PRONUNCIATION_IMAGE_STANDARD.md`; Phrases,
Speaking, and Culture retain their own contracts, but may use the same principle that
teaching text and safe margins take priority over decorative illustration area.

## Phrases contract

- Oversized `USEFUL PHRASES — 實用句型`.
- Mountain shield plus lesson-specific Canadian panorama.
- Five horizontal rows with number, In-class/Self-study badge, exact English/Chinese/tip, and context illustration.
- In-class uses orange/star; Self-study uses navy/book/diamond when source labels require it.
- Exact branded footer and maple separators.

## Pronunciation contract

Use `YSP_PRONUNCIATION_IMAGE_STANDARD.md` structurally. Canada Life adds aged-paper texture, inked editorial illustration, mountain shield, Canada panorama, vintage typography/borders, and lesson-specific Canadian footer. Use vertical modules for short tips or horizontal rows for long tips.

## Speaking and Culture

- Speaking: five source questions with badges, exact hints, Canadian-life vignettes.
- Culture: large topic illustration, exact bilingual title/notes/questions, Canadian daily-life or landmark context, vintage information-panel hierarchy.
- Never import Travel's clean modern row-card system.

## Package and validation

- Exactly 15 images: Phrases 1, Dialogue Model/Practice 10, Pronunciation 1, Speaking 1, Culture 2.
- Current padded `lNN-...` convention and repository routing apply.
- One generation call per asset, using its Golden reference and exact lesson prompt.
- No generic template, variants, or contact sheets inside the lesson folder.
- A deterministic text-only/card template is not an acceptable substitute for the
  required vintage Canadian editorial illustration. Dimension, file-size, and text
  checks cannot produce a style-fidelity PASS by themselves.
- When a lesson folder already contains content-approved Golden raster artwork, the
  Builder may preserve that artwork and perform only lossless/high-quality resizing
  to the required canvas. It must not redraw it as a generic template.
- Reviewer evidence must include an actual visual reopen of every final raster and a
  comparison with the declared Golden reference. Style fidelity is a blocking gate.
- Magnified review for English, Traditional Chinese, IPA, and numbers.
- Before release, visually reopen all 15 final images. Every border, title, teaching row, right-side note, bottom panel, branding mark, and footer must remain fully inside the 1920x1080 canvas; intrinsic crop or edge overflow is BLOCKING.
- After routing images into lesson HTML, inspect every rendered gallery image at desktop and narrow/mobile widths. The image bounding box and scroll width must remain within its gallery mount; source-dimension checks alone are insufficient.
- Exact 1920×1080; over 2 MB warning, over 5 MB block.
- Validate source text, line counts, `tp`, branding, Canadian context, and style fidelity.
- Two-failure stop-loss applies.

## Stop-loss-only hybrid production fallback

The `AI illustration scene + local deterministic Unicode typesetting` workflow is
authorized for Canada Life only after the same image-content or text-fidelity problem
has failed Reviewer verification following two AI generation/correction attempts and
the mandatory stop-loss has been recorded. It is not a first-round shortcut, and it
does not authorize a third AI correction attempt for the same problem.

Once unlocked, the hybrid workflow is a separately identified fallback cycle:

1. AI generation supplies only the hand-illustrated Canada Life scene, panorama,
   pictograms, non-text decoration, parchment texture, and vintage editorial finish.
2. A local program reads the approved lesson JSON and typesets every source-locked
   text element: all titles, English, Traditional Chinese, dialogue lines, IPA,
   incorrect/correct forms, tips, notes, hints, questions, labels, badges,
   Situation/Characters, Key Vocabulary, `NOW YOU TRY`, branding, and footer/tagline.
3. The renderer uses Unicode-capable fonts; source values must come directly from
   JSON wherever available, not from manual retyping or OCR.
4. Canada Life A/B/C illustration sizing remains binding. Text is placed first;
   AI artwork is fitted into the declared illustration footprint without shrinking,
   crowding, or cropping the teaching hierarchy.

Hybrid output must still match the Canada Life Golden vintage illustrated system.
A generic deterministic text-only/card template remains prohibited. Model/Practice
pairs must retain the same scene and characters, and Practice may change only the
`tp`-authorized text. The full final package must pass two sequential, complete visual
review rounds. Pass 1 reopens every image individually at full resolution and checks
magnified JSON-to-raster text/IPA, Canada Life Golden style, scene relevance,
intrinsic crop and safe margins. Pass 2 may begin only after all pass-1 findings are
resolved; it must independently reopen and recheck every image again from source and
Golden references. Sampling, carrying forward pass-1 conclusions, or using a contact
sheet instead of individual full-resolution inspection is forbidden. Upload and
publication remain prohibited until pass 2 passes, followed by desktop/mobile gallery
containment verification. If
the hybrid fallback repeats the same blocking problem after two correction attempts,
stop again and request user direction.

## Post-review user-discovered error escalation

If the user finds an image content, style, text, crop, pairing, or consistency error
after both required review passes were recorded as complete, immediately retract the
affected lesson's image-style VERIFIED status and freeze further image publication.
Do not silently patch only the reported raster and do not claim the existing review
mechanism is sufficient. Produce an evidence-backed miss analysis covering the exact
file, missed rule, why pass 1 and pass 2 failed to catch it, likely sibling-image
exposure, and the proposed new per-image evidence/check method. Discuss that redesigned
review mechanism with the user and obtain an explicit decision before implementing it.
Only after the mechanism is agreed may the Builder update rules/content, reconstruct
images, rerun the newly approved review cycle across the user-approved scope, and
synchronize the outcome to repository standards and Notion with read-back.

## Course boundary

Canada Life only. Travel continues to use `TRAVEL_IMAGE_PROMPT_STANDARD.md`. Only shared pronunciation behavior comes from `YSP_PRONUNCIATION_IMAGE_STANDARD.md`.
