# AGENTS.md — YSP Learn & Shine Shared Agent Loop

**Version:** 1.0  
**Updated:** 2026-08-08 09:37 (America/Vancouver)  
**Repository:** `jobimtg/AT-vocab`  
**Scope:** Entire repository tree unless a deeper `AGENTS.md` / `AGENTS.override.md` provides more specific instructions.

## Purpose

This file is the shared execution entrypoint for AI coding agents working on YSP Learn & Shine.

- **Codex:** reads this root `AGENTS.md` as repository instructions.
- **Claude Code:** root `CLAUDE.md` imports this file with `@AGENTS.md` so Claude Code follows the same Loop.
- Do not maintain separate copies of the Loop rules in Codex and Claude instructions. Keep this file as the shared router and keep the detailed, current rules in Notion / repository contracts.

## Source-of-truth order

Before substantive YSP work, resolve rules in this order:

1. Direct user instruction for the current task.
2. Latest dated YSP rules in Notion.
3. Repository contracts / validators.
4. This `AGENTS.md` execution router.
5. Tool-specific convenience instructions such as `CLAUDE.md`.

When older text conflicts with a newer dated addendum, the newer dated addendum wins.

## Mandatory Notion rule read

For any substantive task involving lesson content, images, HTML/JSON, validators, GitHub changes, release state, or workflow changes, first verify an authenticated Notion MCP connection and fetch the current YSP rule pages.

Required pages:

- `📋 ESL Skill Agent Loop 審核 SOP` — `3a85a561-5413-81f0-a271-fe483b3f3601`
- `🔒 ChatGPT 課程產出強制執行合約` — `3a95a561-5413-8165-8ef0-d22b0b38a367`
- `🗂️ YSP GitHub 上傳後自動整理流程與圖片資料規範` — `3af5a561-5413-8160-a774-e6ca1227ad5a`

When lesson release / validation status changes, also use:

- `📊 ESL Course Tracker` — `38d5a561-5413-8174-9ce9-dbaead7ef9d9`

For image-production work when visual rules are relevant, also fetch the current YSP image-style page if available.

A configured MCP server alone is not proof of connectivity. Perform an authenticated read/fetch. If the task requires end-to-end Notion synchronization and the required Notion connection is unavailable, stop before modifying the release package and report the blocker.

## Mandatory Agent Loop

Use this execution sequence for substantive YSP implementation work:

`Builder → independent Reviewer → applicable validators / Git checks → Notion sync → Notion read-back → local validation/release report`

The user does not need to copy terminal logs back to ChatGPT for normal completion.

### Phase 1 — Builder

Before editing, identify:

1. exact files / lesson / assets in scope;
2. source of truth for content;
3. rules that apply;
4. files and behavior explicitly out of scope;
5. validation commands that will be required.

Then make the smallest safe change. Do not rewrite locked lesson content unless the source data or user explicitly authorizes it.

### Phase 2 — Independent Reviewer

Reviewer must begin only after Builder changes are complete.

Reviewer must not trust Builder statements such as “done”, “compliant”, or “validated”. Reviewer must independently:

1. re-fetch / re-read the latest applicable formal rules;
2. re-read actual changed files and source JSON/HTML/images;
3. inspect `git diff` / changed-file scope;
4. run the applicable validators / syntax checks again;
5. re-evaluate results as `CRITICAL`, `WARNING`, or `Proposal`;
6. for final lesson images, inspect the actual final image content when tooling supports it; otherwise report `IMAGE CONTENT FIDELITY = NOT VERIFIED`.

### Stop-loss

If the same issue still fails after the second Reviewer correction attempt:

- stop automatic repair;
- do not start a third automatic correction attempt;
- record the failure and evidence in Notion;
- report the blocker for user decision.

## Validation matrix

Run only the checks applicable to the task, but when a check is applicable it must actually run before claiming PASS.

### Lesson JSON / HTML / release work

Use the current repository scripts as applicable, including:

- `python3 scripts/validate_lesson_data.py` when production JSON is created or changed and the script is present;
- `python3 scripts/ysp_lesson_contract_check.py`;
- `python3 scripts/ysp_drilling_contract_check.py`;
- `python3 scripts/ysp_validate_site.py`;
- `python3 scripts/ysp_gallery_quality_check.py`;
- `node --check` for JavaScript / extracted script syntax when applicable.

If the repository workflow defines additional blocking checks, run or verify those too.

### Image inbox / image release work

Validate at minimum:

- Before generating any lesson image, locate and fully read the lesson folder's
  `*Image_Prompts*.md` file. Treat it as the mandatory visual-production contract.
- If no lesson-specific Image_Prompts file exists, STOP before image generation,
  warn the user that the prompt contract is missing, and ask for a new prompt file
  following `L03_On_the_Airplane_Image_Prompts.md` in structure and rules. Never
  improvise lesson images from JSON/HTML alone.
- Generate every requested image from the corresponding Image_Prompts section and
  any user-designated Golden Style Reference; do not replace that specification
  with a generic shared layout.
- For Travel English, also read and follow `docs/TRAVEL_IMAGE_PROMPT_STANDARD.md`.
  This standard is Travel-only and must not be reused for Canada Life or other courses.
  If a future Travel lesson lacks its lesson-specific Image_Prompts file, this shared
  Travel standard authorizes creating that file from the approved lesson JSON/HTML
  before generation. This Travel-only route is the exception to the general missing-
  prompt stop; it does not authorize generating without first creating the prompt artifact.
- For Canada Life & Career English, read and follow
  `docs/CANADA_LIFE_IMAGE_PROMPT_STANDARD.md`. It is Canada-Life-only and must not
  inherit Travel's non-pronunciation visual system.
- For pronunciation images in either Travel English or Canada Life, also read
  `docs/YSP_PRONUNCIATION_IMAGE_STANDARD.md`. This controls teaching structure;
  each course standard still controls its surface visual finish.
- exact expected image count for the lesson;
- exact 16:9 and at least 1920×1080 for final release images;
- warning for files over 2 MB;
- block files over 5 MB from formal assets;
- filename / destination mapping;
- final image content fidelity against source JSON/HTML when tooling can verify the actual image.

### Workflow / GitHub automation work

Validate:

- YAML / script syntax as applicable;
- intended trigger paths;
- idempotence where maintenance scripts are involved;
- `git diff` contains only intended files;
- GitHub Actions result after push when the task includes publishing workflow changes.

### Documentation-only work

Do not invent application PASS results. Verify the actual document diff, references, paths, instruction imports, and any syntax/format that is relevant. Do not claim unrelated validators passed unless they were actually run.

## Core YSP hard rules — quick gate

These are a compact reminder only; latest Notion rules remain authoritative.

- Lesson text is source-locked to the approved HTML/JSON: no unapproved rewrite, add, delete, reorder, summary, or simplification.
- Exactly 15 lesson images: Phrases 1 + Dialogues 10 + Pronunciation 1 + Speaking 1 + Culture 2.
- Dialogue image line count follows the actual source `lines[]`; never force 6 or 8 lines.
- Practice dialogue changes only what source `tp` authorizes; never invent answers, numbers, times, or extra dialogue.
- Pronunciation IPA must preserve the actual Unicode IPA characters.
- Final lesson images: exact 16:9, minimum 1920×1080; >2 MB WARNING; >5 MB BLOCK.
- HTML filename is unpadded (`u1-l4.html`); image prefix is two-digit padded (`l04-...`).
- Drilling keeps L1/L2/L3, full Core traversal, flip/reveal, Previous/Next.
- Drilling filters are familiarity-only: 🔴 / 🟡 / 🟢 / ⬜, multi-select; category/topic filters are forbidden.
- Familiarity marking must support toggle-off to unassessed.
- Progress Check Previously Learned is one collapsible accordion per prior lesson.
- Gallery sections must be nested in the matching `.tpn`; renderers write to dedicated content mounts only.
- Gallery images must be responsive and contained: the mount prevents overflow,
  the grid is a single `minmax(0, 1fr)` column, and rendered images use
  `width: 100%`, `max-width: 100%`, `height: auto`, `aspect-ratio: 16/9`,
  and `object-fit: contain`. Intrinsic 1920 px images must never overflow the lesson panel.
- Global nav markers use `YSP_GLOBAL_NAV_LOADER_START` / `YSP_GLOBAL_NAV_LOADER_END` and include `data-ysp-base`.
- Final tab buttons are exactly:
  - `📊 Learning Overview`
  - `📚 Core`
  - `📖 Extended`
  - `🔁 Drilling`
  - `💬 Phrases`
  - `🎯 Pronunciation Spotlight`
  - `🎭 Dialogues`
  - `🗣️ Speaking`
  - `🌍 Culture`
  - `📋 Progress Check`

## Release honesty

Never claim a state that was not directly verified:

- no actual validator run → do not claim validator PASS;
- no actual GitHub write → do not claim committed / pushed;
- no actual GitHub Actions or site read-back → do not claim deployed;
- no actual final image inspection → do not claim image-content fidelity PASS;
- no Notion write + read-back → do not claim `Notion sync = VERIFIED`.

For a publish task, a local build is not publication. Verify the intended Git commit/push, relevant Actions run, and public site/read-back before reporting published.

## Notion completion routing

At task completion, synchronize the outcome to the appropriate pages:

- rule / contract / Loop changes → `🔒 ChatGPT 課程產出強制執行合約` and/or `📋 ESL Skill Agent Loop 審核 SOP`;
- GitHub / Gallery / upload / automation changes → `🗂️ YSP GitHub 上傳後自動整理流程與圖片資料規範`;
- lesson validation / release status → `📊 ESL Course Tracker`.

Use timestamp format:

`YYYY-MM-DD HH:mm (America/Vancouver)`

After writing, read back the newly written record. Only a successful read-back allows `Notion sync = VERIFIED`.

## Required final report

Every substantive implementation / review must end with:

1. **審核對象** — exact files / lesson / image group;
2. **驗證方式** — actual reads, diffs, commands, Git/Notion evidence;
3. **逐項結果** — CRITICAL / WARNING / Proposal;
4. **修正指示** — concrete correction for every CRITICAL;
5. **狀態聲明** — distinguish actual edit/commit/push/publish/sync from review/planning only.

Keep local validation / release reports when the task workflow calls for them.
