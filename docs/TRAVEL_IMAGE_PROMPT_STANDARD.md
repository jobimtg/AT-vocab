# YSP Travel English Image Prompt Standard

**Version:** 1.0

**Effective:** 2026-08-09 (America/Vancouver)

**Scope:** Travel English lessons only

**Golden lesson:** Travel English U1 L03 — On the Airplane

**Golden source prompt:** `L03_On_the_Airplane_Image_Prompts.md`

**Golden visual reference:** `travel-l03-phrases-1.png`

## 1. Mandatory routing

When the user asks to generate images for `Travel L04` or any other Travel lesson:

1. Find and fully read the lesson JSON and HTML.
2. Find and fully read this Travel standard.
3. Find the lesson folder's lesson-specific `*Image_Prompts*.md`.
4. If the lesson-specific file does not exist, create it from the fixed template in this document, using only the lesson JSON/HTML content, then present/validate it before image generation unless the user has already authorized immediate generation.
5. Generate images only from the lesson-specific prompt file plus the Travel Golden visual reference.
6. Never apply this Travel standard to Canada Life, Business English, or another course family.

If this shared standard itself cannot be found or read, STOP and warn the user. Do not improvise a replacement visual system.

## 2. Global Travel visual lock

Apply to every Travel lesson image:

- Exact final canvas: 1920×1080, horizontal 16:9.
- Illustration only; no photography.
- Premium polished flat or semi-realistic editorial illustration.
- Warm Beige `#F5F0E8`, Deep Navy `#1B2A4A`, Copper/Gold `#C8956C`, Success Green `#5B8C5A`, Alert Red `#D4735E`.
- Real YSP shield treatment at upper left.
- Copper maple-leaf decorations.
- `YSP Learn & Shine` brand line where the matching Golden layout requires it.
- Bottom tagline exactly: `YSP Learn & Shine — Your Journey. Your Voice. Your Future.`
- Asian adult characters with natural friendly expressions for dialogue scenes.
- Large, legible English and clean Traditional Chinese.
- All text must remain inside safe margins, uncropped and readable.
- No watermark, generic filler, invented copy, paraphrase, omission, or unauthorized content.

The Golden reference controls visual hierarchy, density, typography feel, borders, icon treatment, row structure, and illustration finish. A generic shared layout is not an acceptable substitute.

## 3. Fixed 15-image manifest

Every Travel lesson image package contains exactly:

1. `travel-lNN-phrases-1.png`
2. `travel-lNN-d01-model.png`
3. `travel-lNN-d01-practice.png`
4. `travel-lNN-d02-model.png`
5. `travel-lNN-d02-practice.png`
6. `travel-lNN-d03-model.png`
7. `travel-lNN-d03-practice.png`
8. `travel-lNN-d04-model.png`
9. `travel-lNN-d04-practice.png`
10. `travel-lNN-d05-model.png`
11. `travel-lNN-d05-practice.png`
12. `travel-lNN-pronunciation-1.png`
13. `travel-lNN-speaking-1.png`
14. `travel-lNN-culture-1.png`
15. `travel-lNN-culture-2.png`

`NN` is the two-digit padded lesson number. Public routed assets remove the `travel-` course prefix and retain `lNN-...`.

## 4. Lesson-specific Image_Prompts format

Each Travel lesson folder must contain one Markdown file named like:

`L04_<Lesson_Title>_Image_Prompts.md`

It must use these sections in this order:

1. Lesson identity.
2. Global production lock.
3. Phrases prompt.
4. Dialogue 1 Model prompt.
5. Dialogue 1 Practice prompt.
6. Dialogue 2 Model prompt.
7. Dialogue 2 Practice prompt.
8. Dialogue 3 Model prompt.
9. Dialogue 3 Practice prompt.
10. Dialogue 4 Model prompt.
11. Dialogue 4 Practice prompt.
12. Dialogue 5 Model prompt.
13. Dialogue 5 Practice prompt.
14. Pronunciation prompt.
15. Speaking prompt.
16. Culture 1 prompt.
17. Culture 2 prompt.
18. GitHub upload-path table.
19. Validation checklist.

Every section must name the exact output filename and include all source-controlled text verbatim.

## 5. Phrases card contract

- Title: `USEFUL PHRASES — 實用句型`.
- Five spacious horizontal rows.
- Each row contains number, study badge, bold English, Traditional Chinese, lightbulb tip, and a small lesson-specific context illustration.
- In-class rows use the approved orange/star treatment; Self-study rows use navy/diamond treatment when source labels require it.
- All five English, Chinese, notes, labels, and ordering come directly from lesson source data.

## 6. Dialogue card contract

Model and Practice use the same scene, characters, composition, and visual hierarchy.

Required regions:

- Top: `ENGLISH DIALOGUE PRACTICE`.
- Left: Situation and Characters panels.
- Center: numbered bilingual dialogue title and every source line.
- Right: detailed lesson-specific scene illustration.
- Bottom-left: three source-grounded Key Vocabulary terms with Traditional Chinese.
- Bottom-right: `NOW YOU TRY!` plus the exact `tp` instruction.
- Bottom: exact Travel tagline.

Dialogue line count follows source `lines[]`. Never force a fixed count.

Practice rules:

- Change only the words or lines authorized by `tp`.
- Preserve all other Model lines verbatim and in the same order.
- Only authorized substituted text is orange/bold.
- Unchanged dialogue remains black/navy.
- Never invent a response, time, number, explanation, or conversational extension.

## 7. Pronunciation card contract

- Read `YSP_PRONUNCIATION_IMAGE_STANDARD.md`; it is the structural authority shared with Canada Life.
- Match the pronunciation family established jointly by `travel-l02-pronunciation-1.png`, `travel-l03-pronunciation-1.png`, and `Pronunciation_U1L1.png`.
- Keep the Travel clean premium finish while using the shared teaching structure.
- Header: `PRONUNCIATION SPOTLIGHT｜發音焦點` and large bilingual focus title.
- Use five horizontal rows for long tips or five vertical cards for short tips and larger articulation diagrams.
- Every module includes word, source IPA, red incorrect → green correct, articulation diagram, and exact tip.
- Include overall TIP, PRACTICE sentence, and Canadian mountain/skyline/maple/landmark decoration.
- IPA format follows the approved lesson JSON/HTML exactly. Image, JSON, and HTML must match one another.
- Never silently normalize punctuation or substitute Unicode IPA marks unless the user explicitly authorizes source synchronization.

## 8. Speaking card contract

- Title: `SPEAKING QUESTIONS — 口說練習`.
- Five rows in source order.
- Each row includes T1/T2/T3 badge, exact English question, exact hint, and a small relevant illustration.
- Do not add sample answers beyond the source hint.

## 9. Culture card contract

- Title: `CULTURE NOTES — 文化補充` with the source slot label.
- Lesson-specific central illustration.
- Exact English and Traditional Chinese titles.
- Full notes verbatim.
- Exactly three source discussion questions in source order.
- Use the shared Travel brand and footer treatment.

## 10. Generation and overwrite policy

- Use one image-generation call per distinct asset.
- Use the Travel Golden reference for style and the matching lesson prompt section for content.
- Model/Practice pairs must remain visually paired.
- If the user requests replacement, overwrite only the existing expected filenames.
- Do not add variants, backup PNGs, contact sheets, or numbered alternatives inside the lesson folder.
- Review generated text before accepting the image; AI-rendered text is not trusted automatically.

## 11. Release validation gate

Before reporting PASS:

- Image_Prompts found and read in full.
- Exactly 15 final PNG files.
- Every PNG decodes.
- Every PNG is exactly 1920×1080, exact 16:9.
- Each file below 5 MB; files over 2 MB are warnings.
- All English, Traditional Chinese, IPA, notes, hints, questions, dialogue lines, Situation, Characters, Key Vocabulary, NOW YOU TRY, branding, and tagline visually checked.
- Practice substitutions match only `tp` authorization.
- Golden Travel style fidelity checked across all 15 images.
- JSON/HTML/image pronunciation data agree.
- Shared pronunciation compliance against `YSP_PRONUNCIATION_IMAGE_STANDARD.md`.
- Independent Reviewer records CRITICAL, WARNING, and Proposal findings.
- Two-failure stop-loss remains mandatory.

## 12. Course-family boundary

This file is exclusively for Travel English.

Canada Life images use the separate `CANADA_LIFE_IMAGE_PROMPT_STANDARD.md`. Do not derive Canada Life non-pronunciation style from this Travel standard. The two course families share only the teaching structure in `YSP_PRONUNCIATION_IMAGE_STANDARD.md` while retaining their own surface finishes.
