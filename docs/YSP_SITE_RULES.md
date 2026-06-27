# YSP Site Rules

## Project Identity

Brand:

```text
YSP Learn & Shine
```

Slogan:

```text
Learn with Purpose. Shine with Confidence.
```

Repository:

```text
jobimtg/AT-vocab
```

Website:

```text
https://jobimtg.github.io/AT-vocab/
```

This is a GitHub Pages site. All paths must work as relative paths. No server-side logic is available.

---

## Folder Structure

Root folders:

```text
assets/
docs/
js/
lessons/
scripts/
.github/workflows/
```

Course folders:

```text
lessons/ca-life/
lessons/travel/
lessons/business/
```

Assets subfolders inside each course:

```text
lessons/ca-life/assets/pronunciation/
lessons/ca-life/assets/phrases/
lessons/ca-life/assets/dialogues/
lessons/ca-life/assets/speaking/
lessons/ca-life/assets/culture/

lessons/travel/assets/pronunciation/
lessons/travel/assets/phrases/
lessons/travel/assets/dialogues/
lessons/travel/assets/speaking/
lessons/travel/assets/culture/

lessons/business/assets/pronunciation/
lessons/business/assets/phrases/
lessons/business/assets/dialogues/
lessons/business/assets/speaking/
lessons/business/assets/culture/
```

---

## Lesson File Naming

Lesson HTML files follow this pattern:

```text
u1-l1.html
u1-l2.html
u2-l1.html
```

Examples:

```text
lessons/ca-life/u1-l1.html
lessons/travel/u1-l1.html
lessons/business/u1-l1.html
```

---

## Image Naming and Prefix Rule

Image filenames use a lesson sequence prefix: `l01`, `l02`, `l03`, and so on.

The prefix is a manually assigned lesson sequence number that matches the lesson's approved metadata and existing file naming plan. It is not calculated from the unit and lesson numbers in the filename.

The authoritative mapping is whatever prefix has been assigned for that lesson. When in doubt, check the existing image files in the course assets folder.

Image filename examples for the lesson assigned prefix `l01`:

```text
assets/pronunciation/l01-pronunciation-1.png
assets/phrases/l01-phrases-1.png
assets/dialogues/l01-d01-model.png
assets/dialogues/l01-d01-practice.png
assets/speaking/l01-speaking-1.png
assets/culture/l01-culture-1.png
assets/culture/l01-culture-2.png
```

Supported image formats:

```text
.png
.jpg
.jpeg
.webp
```

### Image Prefix Matching — Trailing Hyphen Rule

Gallery prefixes must include a trailing hyphen where needed to avoid matching unintended files.

Correct prefixes:

```text
l01-pronunciation-
l01-phrases-
l01-speaking-
l01-culture-
```

Dialogue prefixes are per-topic:

```text
l01-d01-
l01-d02-
l01-d03-
```

A prefix like `l01-pronunciation` without a trailing hyphen could accidentally match `l01-pronunciation-extra-notes.png`. Always use the trailing hyphen form.

---

## Relative Path Rule

All `src` and `href` attributes inside lesson HTML must use relative paths.

From a lesson at `lessons/ca-life/u1-l1.html`:

```text
assets/pronunciation/l01-pronunciation-1.png      ← correct
../../js/ysp-global-nav.js                         ← correct

/assets/pronunciation/l01-pronunciation-1.png     ← wrong (absolute)
https://jobimtg.github.io/AT-vocab/assets/...     ← wrong (absolute URL)
```

Absolute paths break on GitHub Pages subpaths.

---

## Dynamic Image Gallery v3 — Structure

The Dynamic Image Gallery v3 system uses two levels of markers.

### Outer Gallery Block — `YSP_IMAGE_GALLERY_START` / `YSP_IMAGE_GALLERY_END`

The outer markers wrap the entire gallery section, including its heading and any permanent attributes. The workflow does not replace anything outside the inner mount.

```html
<!-- YSP_IMAGE_GALLERY_START: pronunciation -->
<section class="ysp-gallery-section">
  <h3>Pronunciation Spotlight</h3>
  <!-- YSP_IMAGE_GALLERY_MOUNT_START: pronunciation -->
  <div
    class="ysp-image-gallery"
    data-ysp-image-dir="assets/pronunciation/"
    data-ysp-image-prefix="l01-pronunciation-"
  ></div>
  <!-- YSP_IMAGE_GALLERY_MOUNT_END: pronunciation -->
</section>
<!-- YSP_IMAGE_GALLERY_END: pronunciation -->
```

### Inner Mount Point — `YSP_IMAGE_GALLERY_MOUNT_START` / `YSP_IMAGE_GALLERY_MOUNT_END`

The inner markers wrap only the `<div class="ysp-image-gallery">` element. This is the only part the workflow replaces when updating images.

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START: pronunciation -->
<div
  class="ysp-image-gallery"
  data-ysp-image-dir="assets/pronunciation/"
  data-ysp-image-prefix="l01-pronunciation-"
></div>
<!-- YSP_IMAGE_GALLERY_MOUNT_END: pronunciation -->
```

### Mount Point Attributes

| Attribute | Purpose |
|---|---|
| `class="ysp-image-gallery"` | Marks the element as a gallery mount point |
| `data-ysp-image-dir` | Relative path to the image folder |
| `data-ysp-image-prefix` | Filename prefix used to match images, including trailing hyphen |

### How the Workflow Uses These Markers

The workflow scans for `YSP_IMAGE_GALLERY_MOUNT_START` / `YSP_IMAGE_GALLERY_MOUNT_END` pairs only.

Inside each pair, it:

1. Reads `data-ysp-image-dir` and `data-ysp-image-prefix`.
2. Scans the folder for files whose names start with the given prefix.
3. Sorts results using natural sort order.
4. Replaces the inner `<div>` with rendered `<img>` tags for all matching images.
5. If no matching images exist, leaves a placeholder inside the mount with a human-readable message and does not create a broken `<img>` tag.
6. Does not touch anything outside the `YSP_IMAGE_GALLERY_MOUNT_START` / `YSP_IMAGE_GALLERY_MOUNT_END` pair.

---

## Required Gallery Blocks Per Lesson

Every lesson HTML that includes image-based sections must have the following gallery blocks. Original text content for each section must remain in the page alongside the gallery — the gallery is an addition, not a replacement.

### Useful Phrases

```html
<!-- YSP_IMAGE_GALLERY_START: phrases -->
<section class="ysp-gallery-section">
  <h3>Useful Phrases</h3>
  <!-- YSP_IMAGE_GALLERY_MOUNT_START: phrases -->
  <div
    class="ysp-image-gallery"
    data-ysp-image-dir="assets/phrases/"
    data-ysp-image-prefix="l01-phrases-"
  ></div>
  <!-- YSP_IMAGE_GALLERY_MOUNT_END: phrases -->
</section>
<!-- YSP_IMAGE_GALLERY_END: phrases -->
```

### Pronunciation Spotlight

```html
<!-- YSP_IMAGE_GALLERY_START: pronunciation -->
<section class="ysp-gallery-section">
  <h3>Pronunciation Spotlight</h3>
  <!-- YSP_IMAGE_GALLERY_MOUNT_START: pronunciation -->
  <div
    class="ysp-image-gallery"
    data-ysp-image-dir="assets/pronunciation/"
    data-ysp-image-prefix="l01-pronunciation-"
  ></div>
  <!-- YSP_IMAGE_GALLERY_MOUNT_END: pronunciation -->
</section>
<!-- YSP_IMAGE_GALLERY_END: pronunciation -->
```

### Dialogue Practice — One Gallery Per Topic

Each dialogue topic has its own outer and inner gallery block. Do not use a single broad prefix like `l01-d` for all dialogues.

```html
<!-- YSP_IMAGE_GALLERY_START: dialogue-01 -->
<section class="ysp-gallery-section">
  <h3>Dialogue 1 — At the Immigration Counter</h3>
  <!-- YSP_IMAGE_GALLERY_MOUNT_START: dialogue-01 -->
  <div
    class="ysp-image-gallery"
    data-ysp-image-dir="assets/dialogues/"
    data-ysp-image-prefix="l01-d01-"
  ></div>
  <!-- YSP_IMAGE_GALLERY_MOUNT_END: dialogue-01 -->
</section>
<!-- YSP_IMAGE_GALLERY_END: dialogue-01 -->

<!-- YSP_IMAGE_GALLERY_START: dialogue-02 -->
<section class="ysp-gallery-section">
  <h3>Dialogue 2 — Meeting Your Roommate</h3>
  <!-- YSP_IMAGE_GALLERY_MOUNT_START: dialogue-02 -->
  <div
    class="ysp-image-gallery"
    data-ysp-image-dir="assets/dialogues/"
    data-ysp-image-prefix="l01-d02-"
  ></div>
  <!-- YSP_IMAGE_GALLERY_MOUNT_END: dialogue-02 -->
</section>
<!-- YSP_IMAGE_GALLERY_END: dialogue-02 -->
```

Continue this pattern for each additional dialogue topic (`l01-d03-`, `l01-d04-`, etc.).

### Speaking Questions

```html
<!-- YSP_IMAGE_GALLERY_START: speaking -->
<section class="ysp-gallery-section">
  <h3>Speaking Questions</h3>
  <!-- YSP_IMAGE_GALLERY_MOUNT_START: speaking -->
  <div
    class="ysp-image-gallery"
    data-ysp-image-dir="assets/speaking/"
    data-ysp-image-prefix="l01-speaking-"
  ></div>
  <!-- YSP_IMAGE_GALLERY_MOUNT_END: speaking -->
</section>
<!-- YSP_IMAGE_GALLERY_END: speaking -->
```

### Culture

```html
<!-- YSP_IMAGE_GALLERY_START: culture -->
<section class="ysp-gallery-section">
  <h3>Canadian Culture</h3>
  <!-- YSP_IMAGE_GALLERY_MOUNT_START: culture -->
  <div
    class="ysp-image-gallery"
    data-ysp-image-dir="assets/culture/"
    data-ysp-image-prefix="l01-culture-"
  ></div>
  <!-- YSP_IMAGE_GALLERY_MOUNT_END: culture -->
</section>
<!-- YSP_IMAGE_GALLERY_END: culture -->
```

Replace `l01` with the correct lesson sequence prefix for each lesson.

---

## Original Text Content Rule

Original lesson text content — vocabulary cards, drilling exercises, dialogues, speaking prompts, culture notes — must always be preserved in full.

Gallery blocks are additions. They must appear alongside the original text content for their section, not in place of it.

The workflow and Claude must never:

```text
delete text content sections
replace text content with image gallery blocks
remove vocabulary card arrays
remove JavaScript lesson data
rewrite full lesson HTML unnecessarily
```

---

## Workflow Modification Boundary Rule

The workflow may only update HTML content inside `YSP_IMAGE_GALLERY_MOUNT_START` / `YSP_IMAGE_GALLERY_MOUNT_END` pairs.

Everything outside those markers — headings, text content, outer gallery section markup, vocabulary data, styles — must not be touched by the workflow.

---

## Prohibited Actions — Claude and Workflow

Claude and the workflow must never:

```text
delete text content from lesson pages
replace text content with images
hard-code nav, Top button, or Back to Lessons inline in HTML
use a broad dialogue prefix (e.g. l01-d) instead of per-topic prefixes (l01-d01-, l01-d02-)
omit the trailing hyphen from image prefixes
hard-code a fixed image count (the gallery supports any number of images)
rewrite full lesson HTML unless the user explicitly requests it
commit when no files have actually changed
create report folders
restore old patch workflows
add duplicate YSP_GLOBAL_NAV_LOADER blocks
add duplicate Top buttons
add duplicate Back to Lessons buttons
```

---

## Navigation Rule

Every lesson HTML file must include exactly one global nav loader block, placed before `</body>`:

```html
<!-- YSP_GLOBAL_NAV_LOADER_START -->
<script src="../../js/ysp-global-nav.js" defer data-ysp-base="../../"></script>
<!-- YSP_GLOBAL_NAV_LOADER_END -->
```

The relative prefix (`../../`) must match the lesson's depth in the folder tree.

All navigation rendering — the top nav bar, the Back to Lessons button, and the Top button — is handled exclusively by `js/ysp-global-nav.js`. Lesson HTML files must not hard-code any of these elements.

---

## Gallery Image Discovery Rule

When the workflow scans for gallery images:

- It reads `data-ysp-image-dir` and `data-ysp-image-prefix` from the mount point.
- It searches the resolved folder for files whose names start with the given prefix (including the trailing hyphen).
- It accepts `.png`, `.jpg`, `.jpeg`, and `.webp` extensions.
- It sorts results using natural sort order (`l01-culture-1` before `l01-culture-10`).
- It does not assume a fixed count. If three images exist, it renders three. If one exists, it renders one.
- If no matching images exist, it renders a placeholder `<div>` inside the mount point and does not create a broken `<img>` tag.

---

## Active Workflows

Only two workflows must remain active:

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
```

Do not restore any old patch workflows.

---

## Future Workflow Responsibilities

The site maintenance workflow is responsible for:

```text
scanning lesson HTML for YSP_IMAGE_GALLERY_MOUNT_START / END pairs
reading data-ysp-image-dir and data-ysp-image-prefix
finding matching image files using natural sort
rendering img tags for found images
preserving placeholder when no images exist
supporting png, jpg, jpeg, webp
updating lessons/index.html lesson cards
updating index.html featured lesson cards
adding YSP_GLOBAL_NAV_LOADER to lesson pages that are missing it
removing legacy generated nav blocks from old patch workflows
committing only when files actually changed
```

The progress dashboard workflow is display-only. It must not modify files or commit.

---

## Idempotency Rule

The maintenance process must be safe to run repeatedly.

Running it twice must not create:

```text
duplicate headers
duplicate Back to Lessons
duplicate Top buttons
duplicate gallery blocks
extra commits when nothing changed
```

---

## Validation Checklist Before Publishing a Lesson

```text
[ ] Lesson file is named correctly (e.g. u1-l1.html)
[ ] Lesson is in the correct course folder
[ ] Lesson HTML contains exactly one YSP_GLOBAL_NAV_LOADER block
[ ] No inline nav, Top button, or Back to Lessons hard-coded in HTML
[ ] No duplicate generated blocks
[ ] Original text content (vocabulary, drills, dialogues) is intact
[ ] Each image-based section has an outer YSP_IMAGE_GALLERY_START / END block
[ ] Each image-based section has an inner YSP_IMAGE_GALLERY_MOUNT_START / END block
[ ] data-ysp-image-dir uses a relative path (assets/..., not /assets/...)
[ ] data-ysp-image-prefix includes the correct l01 / l02 / l03 prefix and trailing hyphen
[ ] Each dialogue topic has its own per-topic dialogue gallery (l01-d01-, l01-d02-, etc.)
[ ] Image files are in the correct course assets subfolder
[ ] Image files use supported formats: png, jpg, jpeg, webp
[ ] No broken image tags (src pointing to nonexistent files)
[ ] No internal production notes visible in rendered HTML
[ ] lessons/index.html lesson card is correct
[ ] index.html featured lesson section is correct (if featured)
[ ] Maintenance workflow runs twice without creating new commits on second run
```
