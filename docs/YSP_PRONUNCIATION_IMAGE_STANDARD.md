# YSP Shared Pronunciation Image Standard

**Version:** 1.1

**Effective:** 2026-08-13 (America/Vancouver)

**Applies to:** Travel English and Canada Life & Career English pronunciation images only

## Golden reference set

- `travel-l02-pronunciation-1.png`
- `travel-l03-pronunciation-1.png`
- `Pronunciation_U1L1.png`

These three images jointly define the pronunciation image family. No single reference overrides source-controlled lesson content.

## Shared visual behavior

- Exact 1920×1080 horizontal 16:9 final canvas.
- Prominent `PRONUNCIATION SPOTLIGHT` and Traditional Chinese `發音焦點`.
- YSP shield branding, navy/copper palette, maple leaves, Canadian mountain/city/landmark decoration.
- One large bilingual pronunciation-focus title.
- Exactly five source-controlled pronunciation modules.
- Every module includes numbered position, target word, source IPA, red incorrect form with X, arrow, green correct form with check, articulation diagram, and exact tip.
- One overall TIP panel and one PRACTICE sentence panel.
- Strong instructional hierarchy; IPA and articulation visuals remain readable at normal webpage width.

## Layout family

1. **Five horizontal teaching rows** — preferred for longer English tips; follow Travel L02/L03.
2. **Five vertical teaching cards** — allowed for short tips and larger articulation diagrams; follow `Pronunciation_U1L1.png`.

Choose from content density, not course identity. Never omit or paraphrase content to force a layout.

## Course-specific finish

- Travel uses the clean premium finish in `TRAVEL_IMAGE_PROMPT_STANDARD.md`.
- Canada Life uses the textured Canadian editorial/poster finish in `CANADA_LIFE_IMAGE_PROMPT_STANDARD.md`.
- Teaching structure remains the same even when surface texture differs.

## Content lock

- JSON/HTML controls word, IPA, incorrect form, tip, overall tip, and practice sentence.
- Image, JSON, and HTML agree exactly.
- Preserve source punctuation and Unicode IPA; never normalize without explicit user authorization.
- Use a font that visibly supports every IPA glyph.
- AI-rendered IPA requires magnified visual inspection.
- After the same pronunciation text/IPA fidelity problem fails two AI
  generation/correction attempts and stop-loss is recorded, the course standard's
  hybrid fallback may be used. AI supplies only illustration and non-text visual
  treatment; a local Unicode-capable renderer must typeset all titles, Chinese,
  words, IPA, incorrect/correct forms, tips, practice text, labels, branding, and
  footer directly from approved JSON. This is a separate fallback path, not a third
  AI correction attempt.

## Lesson prompt block

Include exact filename; bilingual focus; five complete word/IPA/incorrect/correct/tip records; articulation diagram requirement; overall tip; practice sentence; selected row/card layout with content-density reason; course finish; exact branding/tagline.

## Reviewer gate

- Five modules present in source order.
- Every IPA visually exact.
- Wrong/correct forms visually distinct.
- Articulation diagrams match the target.
- Tips, overall tip, and practice sentence exact.
- No clipping, missing glyph, or punctuation drift unless source-authorized.
- The full header, all five teaching modules, right-side tips/diagrams, TIP panel, PRACTICE panel, and footer must be visibly inside the canvas safe area. A 1920x1080 file with internally cropped content is a BLOCKING failure.
- Reopen and inspect the final PNG at magnification, then verify its rendered desktop and narrow/mobile gallery bounds before release.
- Dimensions/file-size gates pass.
- Two-failure stop-loss applies.

If the user finds a pronunciation-image error after both required review passes were
recorded as complete, retract VERIFIED status and freeze publication. Document the
missed glyph/content/style evidence and why both reviews missed it, assess sibling
pronunciation images, and discuss a redesigned per-image review mechanism with the
user. Do not reconstruct or update the review rules until the user approves the new
mechanism; after approval, execute it and synchronize the updated standards and status.
