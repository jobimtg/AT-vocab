# YSP Canada Life & Career English Image Prompt Standard

**Version:** 1.0

**Effective:** 2026-08-09 (America/Vancouver)

**Scope:** Canada Life & Career English lessons only

## Golden references

- Dialogue Model: `Dialogue Practice_U1L1_1.png`
- Dialogue Practice: `Dialogue Practice_U1L1_2-2.png`
- Phrases: `l01-phrases.png`
- Pronunciation: `Pronunciation_U1L1.png`

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
- Right: large detailed Canadian-life situation illustration.
- Bottom: Key Vocabulary strip with icons/Chinese.
- Bottom-right: `NOW YOU TRY! 換你說` with exact `tp` and matching vignette.
- Model/Practice retain scene and characters; Practice changes only `tp`-authorized text and only that text receives rust/orange emphasis.

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
- Magnified review for English, Traditional Chinese, IPA, and numbers.
- Exact 1920×1080; over 2 MB warning, over 5 MB block.
- Validate source text, line counts, `tp`, branding, Canadian context, and style fidelity.
- Two-failure stop-loss applies.

## Course boundary

Canada Life only. Travel continues to use `TRAVEL_IMAGE_PROMPT_STANDARD.md`. Only shared pronunciation behavior comes from `YSP_PRONUNCIATION_IMAGE_STANDARD.md`.
