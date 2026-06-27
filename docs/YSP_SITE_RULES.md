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

Required root folders:

```text
assets/
docs/
js/
lessons/
scripts/
.github/workflows/
```

Lesson course folders:

```text
lessons/ca-life/
lessons/travel/
lessons/business/
```

Course-level assets folders:

```text
lessons/ca-life/assets/
lessons/travel/assets/
lessons/business/assets/
```

Each course assets folder contains subfolders for image types:

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

## Lesson Naming Rule

Lesson HTML files follow this pattern:

```text
u1-l1.html
u1-l2.html
u2-l1.html
```

Full examples:

```text
lessons/ca-life/u1-l1.html
lessons/travel/u1-l1.html
lessons/business/u1-l1.html
```

---

## Image Naming Rule

Images are named using an `l01` / `l02` / `l03` prefix that maps to the lesson number.

The lesson number is derived from the lesson file stem:

```text
u1-l1.html  →  l01
u1-l2.html  →  l02
u2-l1.html  →  l03  (lesson 3 in the series, not unit 2 lesson 1)
```

Wait — the correct interpretation is simpler: the image prefix matches the lesson index within the course, counting from `l01` for the first lesson in any unit.

Preferred interpretation:

```text
u1-l1.html  →  l01
u1-l2.html  →  l02
u1-l3.html  →  l03
u2-l1.html  →  l04  (first lesson of unit 2 = fourth lesson overall, if units are sequential)
```

When in doubt, match the image prefix to the lesson sequence number confirmed in the project, not a calculated value. The authoritative mapping is whatever image files exist in `assets/pronunciation/`.

Image file naming examples for lesson u1-l1:

```text
lessons/ca-life/assets/pronunciation/l01-pronunciation-1.png
lessons/ca-life/assets/phrases/l01-phrases.png
lessons/ca-life/assets/dialogues/l01-d01-model.png
lessons/ca-life/assets/dialogues/l01-d01-practice.png
lessons/ca-life/assets/speaking/l01-speaking-questions.png
lessons/ca-life/assets/culture/l01-culture-1.png
lessons/ca-life/assets/culture/l01-culture-2.png
```

Supported image formats:

```text
.png
.jpg
.jpeg
.webp
```

---

## Relative Path Rule

All `src` and `href` attributes inside lesson HTML files must use relative paths.

From a lesson at `lessons/ca-life/u1-l1.html`:

```text
assets/pronunciation/l01-pronunciation-1.png      ← correct
assets/phrases/l01-phrases.png                    ← correct
../../js/ysp-global-nav.js                         ← correct

/assets/pronunciation/l01-pronunciation-1.png     ← wrong (absolute)
https://jobimtg.github.io/AT-vocab/assets/...     ← wrong (absolute URL)
```

Absolute paths will break on GitHub Pages subpaths.

---

## Dynamic Image Gallery v3 — Structure

The Dynamic Image Gallery v3 system replaces hard-coded single image tags with a declarative gallery mount point.

A gallery mount point looks like this:

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START: pronunciation -->
<div
  class="ysp-image-gallery"
  data-ysp-image-dir="assets/pronunciation/"
  data-ysp-image-prefix="l01-pronunciation"
></div>
<!-- YSP_IMAGE_GALLERY_MOUNT_END: pronunciation -->
```

### Attributes

| Attribute | Purpose |
|---|---|
| `class="ysp-image-gallery"` | Marks the element as a gallery mount point |
| `data-ysp-image-dir` | Relative path to the folder containing images |
| `data-ysp-image-prefix` | Filename prefix used to match images in that folder |

### Marker Comments

Every gallery mount is wrapped in:

```text
<!-- YSP_IMAGE_GALLERY_MOUNT_START: <name> -->
<!-- YSP_IMAGE_GALLERY_MOUNT_END: <name> -->
```

The `<name>` label identifies which gallery block it is. It is used by the workflow to locate and update the block without touching anything outside it.

### How the Workflow Uses These Markers

The workflow scans the lesson HTML for `YSP_IMAGE_GALLERY_MOUNT_START` / `YSP_IMAGE_GALLERY_MOUNT_END` pairs.

Inside each pair, it:

1. Reads `data-ysp-image-dir` and `data-ysp-image-prefix`.
2. Scans the course assets folder for matching image files.
3. Replaces the inner `<div>` with rendered `<img>` tags for all matching images.
4. If no matching images exist, leaves a placeholder `<div>` with a human-readable message.
5. Does not touch anything outside the marker pair.

---

## Required Gallery Blocks Per Lesson

Every lesson HTML file that includes image-based sections must have these five gallery mount blocks:

### Useful Phrases

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START: phrases -->
<div
  class="ysp-image-gallery"
  data-ysp-image-dir="assets/phrases/"
  data-ysp-image-prefix="l01-phrases"
></div>
<!-- YSP_IMAGE_GALLERY_MOUNT_END: phrases -->
```

### Pronunciation Spotlight

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START: pronunciation -->
<div
  class="ysp-image-gallery"
  data-ysp-image-dir="assets/pronunciation/"
  data-ysp-image-prefix="l01-pronunciation"
></div>
<!-- YSP_IMAGE_GALLERY_MOUNT_END: pronunciation -->
```

### Dialogue Practice

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START: dialogues -->
<div
  class="ysp-image-gallery"
  data-ysp-image-dir="assets/dialogues/"
  data-ysp-image-prefix="l01-d"
></div>
<!-- YSP_IMAGE_GALLERY_MOUNT_END: dialogues -->
```

### Speaking Questions

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START: speaking -->
<div
  class="ysp-image-gallery"
  data-ysp-image-dir="assets/speaking/"
  data-ysp-image-prefix="l01-speaking"
></div>
<!-- YSP_IMAGE_GALLERY_MOUNT_END: speaking -->
```

### Culture

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START: culture -->
<div
  class="ysp-image-gallery"
  data-ysp-image-dir="assets/culture/"
  data-ysp-image-prefix="l01-culture"
></div>
<!-- YSP_IMAGE_GALLERY_MOUNT_END: culture -->
```

Replace `l01` with the correct lesson prefix for each lesson file.

---

## Original Text Content Rule

The original text-based lesson content — vocabulary cards, drilling exercises, dialogues, speaking prompts, culture notes — must always be preserved.

The workflow and Claude must never:

```text
delete text content sections
replace text content with images
remove vocabulary card arrays
remove JavaScript lesson data
rewrite full lesson HTML unnecessarily
```

Image gallery blocks are additions placed inside the designated tab sections. They do not replace the existing text content in those sections.

---

## Workflow Modification Boundary Rule

The workflow may only update HTML content inside `YSP_IMAGE_GALLERY_MOUNT_START` / `YSP_IMAGE_GALLERY_MOUNT_END` marker pairs.

The workflow must not modify anything outside those markers.

This means the workflow must not:

```text
rewrite lesson headings
rewrite tab labels
rewrite vocabulary card data
rewrite JavaScript lesson arrays
add nav or Top or Back buttons inline in HTML
change styles outside the gallery blocks
```

---

## Prohibited Actions — Claude and Workflow

Claude and the workflow must never:

```text
delete text content from lesson pages
replace text content with images
hard-code nav, Top button, or Back to Lessons inline in HTML
hard-code a fixed image count (do not assume 1 or 2 images per gallery)
rewrite full lesson HTML unless the user explicitly requests it
commit empty or no-change commits
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

The relative path prefix (`../../`) must match the lesson's depth in the folder tree.

All navigation rendering — the top nav bar, the Back to Lessons button, and the Top button — is handled exclusively by `js/ysp-global-nav.js`.

Lesson HTML files must not contain inline nav, Back to Lessons links, or Top buttons. Those are the responsibility of the JS file.

---

## Gallery Image Discovery Rule

When the workflow scans for gallery images:

- It reads `data-ysp-image-dir` and `data-ysp-image-prefix` from the mount point.
- It searches the resolved folder for files whose names start with the given prefix.
- It accepts `.png`, `.jpg`, `.jpeg`, and `.webp` extensions.
- It sorts results using natural sort order (so `l01-d01` comes before `l01-d02`, and `l01-culture-1` comes before `l01-culture-10`).
- It does not assume a fixed count. If three dialogue images exist, it renders three. If one exists, it renders one.
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
duplicate lesson card sections
duplicate gallery blocks
extra commits when nothing changed
```

---

## Validation Checklist Before Publishing a Lesson

Before a lesson page goes live, confirm:

```text
[ ] Lesson file is named correctly (e.g. u1-l1.html)
[ ] Lesson is in the correct course folder (lessons/ca-life/, lessons/travel/, lessons/business/)
[ ] Lesson HTML contains exactly one YSP_GLOBAL_NAV_LOADER block
[ ] No inline nav, Top button, or Back to Lessons hard-coded in HTML
[ ] No duplicate generated blocks
[ ] Original text content (vocabulary, drills, dialogues) is intact
[ ] Gallery mount blocks are present for each image-based section
[ ] data-ysp-image-dir uses a relative path (assets/..., not /assets/...)
[ ] data-ysp-image-prefix matches the correct l01 / l02 / l03 prefix for this lesson
[ ] Image files are in the correct course assets subfolder
[ ] Image files use supported formats: png, jpg, jpeg, webp
[ ] No internal production notes visible in rendered HTML
[ ] No broken image tags (src pointing to nonexistent files)
[ ] lessons/index.html lesson card is correct for this lesson
[ ] index.html featured lesson section is correct (if this lesson is featured)
[ ] Maintenance workflow runs twice without creating new commits on second run
```
