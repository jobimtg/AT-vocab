# Run with: python3 scripts/ysp_validate_site.py

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
LESSONS_ROOT = ROOT / "lessons"
COURSES = ["ca-life", "travel", "business"]

ERRORS = []
WARNINGS = []
FILES_CHECKED = 0


def err(path, msg):
    ERRORS.append((str(path.relative_to(ROOT)), msg))


def warn(path, msg):
    WARNINGS.append((str(path.relative_to(ROOT)), msg))


def read(path):
    return path.read_text(encoding="utf-8", errors="ignore")


SCRIPT_BLOCK_RE = re.compile(r"<script[\s\S]*?</script>", re.I)


def strip_scripts(text):
    """Remove <script>...</script> blocks so markers inside JS are not matched."""
    return SCRIPT_BLOCK_RE.sub("", text)


# ---------------------------------------------------------------------------
# 1. Nav loader
# ---------------------------------------------------------------------------

def check_nav_loader(path, text):
    starts = text.count("<!-- YSP_GLOBAL_NAV_LOADER_START -->")
    ends = text.count("<!-- YSP_GLOBAL_NAV_LOADER_END -->")

    if starts == 0:
        err(path, "Missing YSP_GLOBAL_NAV_LOADER_START block")
    elif starts > 1:
        err(path, f"Duplicate YSP_GLOBAL_NAV_LOADER_START ({starts} found)")

    if ends == 0 and starts > 0:
        err(path, "Missing YSP_GLOBAL_NAV_LOADER_END (unmatched start)")
    elif ends > 1:
        err(path, f"Duplicate YSP_GLOBAL_NAV_LOADER_END ({ends} found)")


# ---------------------------------------------------------------------------
# 2. Legacy / hard-coded nav elements
# ---------------------------------------------------------------------------

LEGACY_START_END = [
    ("<!-- YSP_SITE_NAV_START -->",               "<!-- YSP_SITE_NAV_END -->"),
    ("<!-- YSP_BACK_TO_LESSONS_START -->",         "<!-- YSP_BACK_TO_LESSONS_END -->"),
    ("<!-- YSP_TOP_BUTTON_START -->",              "<!-- YSP_TOP_BUTTON_END -->"),
    ("<!-- YSP_LESSON_BRAND_NAV_START -->",        "<!-- YSP_LESSON_BRAND_NAV_END -->"),
    ("<!-- YSP_LESSON_BRAND_NAV_STYLE_START -->",  "<!-- YSP_LESSON_BRAND_NAV_STYLE_END -->"),
    ("<!-- YSP_CLEAN_TOP_BUTTON_START -->",        "<!-- YSP_CLEAN_TOP_BUTTON_END -->"),
    ("<!-- YSP_CLEAN_TOP_STYLE_START -->",         "<!-- YSP_CLEAN_TOP_STYLE_END -->"),
    ("<!-- YSP_PAGE_TOP_BUTTON_START -->",         "<!-- YSP_PAGE_TOP_BUTTON_END -->"),
    ("<!-- YSP_PAGE_TOP_ANCHOR_START -->",         "<!-- YSP_PAGE_TOP_ANCHOR_END -->"),
    ("<!-- YSP_LESSON_NAV_START -->",              "<!-- YSP_LESSON_NAV_END -->"),
    ("<!-- YSP_SINGLE_TOP_BUTTON_START -->",       "<!-- YSP_SINGLE_TOP_BUTTON_END -->"),
    ("<!-- YSP_AUTO_TOP_ANCHOR_START -->",         "<!-- YSP_AUTO_TOP_ANCHOR_END -->"),
    ("<!-- YSP_AUTO_TOP_BUTTON_START -->",         "<!-- YSP_AUTO_TOP_BUTTON_END -->"),
    ("<!-- YSP_LESSON_FOOTER_START -->",           "<!-- YSP_LESSON_FOOTER_END -->"),
    ("<!-- YSP_GLOBAL_LESSON_STYLE_START -->",     "<!-- YSP_GLOBAL_LESSON_STYLE_END -->"),
]

LEGACY_CLASS_PATTERNS = [
    (r'class=["\'][^"\']*\bysp-site-nav\b',     "Hard-coded .ysp-site-nav element"),
    (r'class=["\'][^"\']*\bysp-local-nav\b',    "Hard-coded .ysp-local-nav element"),
    (r'class=["\'][^"\']*\bysp-back-lessons\b', "Hard-coded .ysp-back-lessons element"),
    (r'class=["\'][^"\']*\bysp-top-btn\b',      "Hard-coded .ysp-top-btn element"),
    (r'class=["\'][^"\']*\bysp-top\b',          "Hard-coded .ysp-top element"),
]

DUP_GENERATED_IDS = [
    "ysp-global-top",
    "ysp-back-to-lessons",
    "ysp-global-nav",
]


def check_legacy_nav(path, text):
    for start, end in LEGACY_START_END:
        if start in text:
            warn(path, f"Legacy nav marker present: {start}")

    for pattern, label in LEGACY_CLASS_PATTERNS:
        if re.search(pattern, text, re.I):
            warn(path, label)

    # Check for duplicate generated element IDs
    for elem_id in DUP_GENERATED_IDS:
        # Match both id="..." and id='...'
        pattern = r'id=["\']' + re.escape(elem_id) + r'["\']'
        hits = len(re.findall(pattern, text, re.I))
        if hits > 1:
            err(path, f"Duplicate generated element (id={elem_id!r}, {hits} occurrences)")


# ---------------------------------------------------------------------------
# 3. Internal production notes
# ---------------------------------------------------------------------------

INTERNAL_NOTES = [
    "本分頁使用",
    "請將圖片放在",
    "完整發音教學圖",
]


def check_internal_notes(path, text):
    for note in INTERNAL_NOTES:
        if note in text:
            err(path, f"Internal production note visible in HTML: {note!r}")

    # Check for bare assets/pronunciation/... text that is NOT inside:
    # - src= attribute
    # - <code> tags (valid gallery placeholder documentation)
    # - .ysp-image-placeholder div (valid gallery placeholder container)

    # Find all occurrences of assets/pronunciation/...
    for m in re.finditer(r'assets/pronunciation/[^\s<"\']*', text, re.I):
        start_pos = m.start()

        # Check if inside a src= attribute
        pre_context = text[max(0, start_pos - 10):start_pos]
        if "src=" in pre_context:
            continue

        # Check if inside <code>...</code> tags
        code_start = text.rfind("<code", 0, start_pos)
        code_end = text.find("</code>", start_pos)
        if code_start != -1 and code_end != -1 and code_end > start_pos:
            continue

        # Check if inside .ysp-image-placeholder
        placeholder_start = text.rfind('class="ysp-image-placeholder"', 0, start_pos)
        if placeholder_start == -1:
            placeholder_start = text.rfind("class='ysp-image-placeholder'", 0, start_pos)
        if placeholder_start != -1:
            # Find the closing </div> for this placeholder
            div_start = text.rfind("<div", 0, start_pos)
            div_end = text.find("</div>", start_pos)
            if div_start != -1 and div_end != -1 and div_end > start_pos:
                continue

        # If we get here, it's a bare assets/pronunciation/... outside valid contexts
        err(path, f"Internal instruction text visible: {m.group()!r}")


# ---------------------------------------------------------------------------
# 4. Dynamic Image Gallery v3
# ---------------------------------------------------------------------------

GALLERY_OUTER_START_RE = re.compile(r"<!--\s*YSP_IMAGE_GALLERY_START:\s*(\S+)\s*-->")
GALLERY_OUTER_END_RE   = re.compile(r"<!--\s*YSP_IMAGE_GALLERY_END:\s*(\S+)\s*-->")
GALLERY_MOUNT_START_RE = re.compile(r"<!--\s*YSP_IMAGE_GALLERY_MOUNT_START(?::\s*(\S+))?\s*-->")
GALLERY_MOUNT_END_RE   = re.compile(r"<!--\s*YSP_IMAGE_GALLERY_MOUNT_END(?::\s*(\S+))?\s*-->")

GALLERY_DIV_RE = re.compile(
    r'<div[^>]+class=["\'][^"\']*ysp-image-gallery[^"\']*["\'][^>]*>',
    re.I | re.S,
)

ATTR_DIR_RE    = re.compile(r'data-ysp-image-dir=["\']([^"\']*)["\']', re.I)
ATTR_PREFIX_RE = re.compile(r'data-ysp-image-prefix=["\']([^"\']*)["\']', re.I)
ATTR_GALLERY_RE = re.compile(r'data-ysp-gallery=["\']([^"\']*)["\']', re.I)

BROAD_DIALOGUE_RE = re.compile(r'^l\d+-d-?$', re.I)


def check_galleries(path, text):
    outer_starts = [(m.group(1), m.start()) for m in GALLERY_OUTER_START_RE.finditer(text)]
    outer_ends   = {m.group(1): m.start() for m in GALLERY_OUTER_END_RE.finditer(text)}
    mount_starts = [(m.group(1) or "_unnamed_", m.start()) for m in GALLERY_MOUNT_START_RE.finditer(text)]
    mount_ends   = {m.group(1) or "_unnamed_": m.start() for m in GALLERY_MOUNT_END_RE.finditer(text)}

    # Matched outer pairs
    for name, pos in outer_starts:
        if name not in outer_ends:
            err(path, f"YSP_IMAGE_GALLERY_START:{name} has no matching END")

    for name in outer_ends:
        if name not in dict(outer_starts):
            err(path, f"YSP_IMAGE_GALLERY_END:{name} has no matching START")

    # Matched mount pairs
    for name, pos in mount_starts:
        if name not in mount_ends:
            err(path, f"YSP_IMAGE_GALLERY_MOUNT_START:{name} has no matching END")

    for name in mount_ends:
        if name not in dict(mount_starts):
            err(path, f"YSP_IMAGE_GALLERY_MOUNT_END:{name} has no matching START")

    # If no galleries at all, nothing more to check
    if not outer_starts and not mount_starts:
        return

    # Per outer gallery: validate attributes live outside the mount region
    seen_gallery_ids = []

    for name, outer_pos in outer_starts:
        # Find the outer END position
        outer_end_pos = outer_ends.get(name)
        if outer_end_pos is None:
            continue

        outer_text = text[outer_pos:outer_end_pos]

        # Find mount region within outer block
        mount_start_m = GALLERY_MOUNT_START_RE.search(outer_text)
        mount_end_m   = GALLERY_MOUNT_END_RE.search(outer_text)

        if not mount_start_m:
            err(path, f"Gallery {name!r}: missing YSP_IMAGE_GALLERY_MOUNT_START inside outer block")
            mount_inner = ""
        else:
            if not mount_end_m:
                err(path, f"Gallery {name!r}: missing YSP_IMAGE_GALLERY_MOUNT_END inside outer block")
                mount_inner = outer_text[mount_start_m.end():]
            else:
                mount_inner = outer_text[mount_start_m.end():mount_end_m.start()]

        # Attributes should be in outer_text but OUTSIDE the mount region
        pre_mount = outer_text[:mount_start_m.start()] if mount_start_m else outer_text

        dir_m    = ATTR_DIR_RE.search(pre_mount)
        prefix_m = ATTR_PREFIX_RE.search(pre_mount)
        gid_m    = ATTR_GALLERY_RE.search(pre_mount)

        # Also check if attrs are accidentally inside the mount
        dir_in_mount    = ATTR_DIR_RE.search(mount_inner)
        prefix_in_mount = ATTR_PREFIX_RE.search(mount_inner)

        if dir_in_mount:
            err(path, f"Gallery {name!r}: data-ysp-image-dir found inside MOUNT region (should be outside)")
        if prefix_in_mount:
            err(path, f"Gallery {name!r}: data-ysp-image-prefix found inside MOUNT region (should be outside)")

        # Validate data-ysp-image-dir
        if not dir_m:
            err(path, f"Gallery {name!r}: missing data-ysp-image-dir")
        else:
            d = dir_m.group(1)
            if d.startswith("/"):
                err(path, f"Gallery {name!r}: data-ysp-image-dir must be relative, not absolute: {d!r}")
            if "https://" in d or "http://" in d:
                err(path, f"Gallery {name!r}: data-ysp-image-dir must not contain a URL: {d!r}")
            if d.endswith("/"):
                warn(path, f"Gallery {name!r}: data-ysp-image-dir should not end with a trailing slash: {d!r}")

        # Validate data-ysp-image-prefix
        if not prefix_m:
            err(path, f"Gallery {name!r}: missing data-ysp-image-prefix")
        else:
            p = prefix_m.group(1)
            if not p.endswith("-"):
                warn(path, f"Gallery {name!r}: data-ysp-image-prefix should end with a trailing hyphen: {p!r}")
            # Warn on broad dialogue prefix like l01-d
            if BROAD_DIALOGUE_RE.match(p.rstrip("-")):
                warn(path, f"Gallery {name!r}: dialogue prefix {p!r} is too broad — use per-topic prefix e.g. l01-d01-")

        # Check data-ysp-gallery attribute uniqueness
        if gid_m:
            gid = gid_m.group(1)
            if gid in seen_gallery_ids:
                err(path, f"Gallery {name!r}: data-ysp-gallery value {gid!r} is not unique on this page")
            else:
                seen_gallery_ids.append(gid)
        else:
            warn(path, f"Gallery {name!r}: missing data-ysp-gallery attribute")

        # Check ysp-image-gallery class present in outer block (outside mount)
        if not re.search(r'class=["\'][^"\']*ysp-image-gallery', pre_mount, re.I):
            warn(path, f"Gallery {name!r}: class=\"ysp-image-gallery\" not found outside mount region")


# ---------------------------------------------------------------------------
# 5. Rendered image references
# ---------------------------------------------------------------------------

IMG_SRC_RE = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.I)


def check_image_refs(path, text):
    lesson_dir = path.parent

    for m in IMG_SRC_RE.finditer(text):
        src = m.group(1)

        if src.startswith("/assets/"):
            err(path, f"img src uses absolute path: {src!r}")
            continue

        if src.startswith("https://") or src.startswith("http://"):
            if "jobimtg.github.io" in src and "/assets/" in src:
                err(path, f"img src uses full GitHub Pages URL: {src!r}")
            continue

        if src.startswith("assets/"):
            target = lesson_dir / src
            if not target.exists():
                err(path, f"img src points to missing file: {src!r}")


# ---------------------------------------------------------------------------
# 6. Validate a single lesson HTML file
# ---------------------------------------------------------------------------

def validate_lesson(path):
    global FILES_CHECKED
    FILES_CHECKED += 1
    text = read(path)
    # Strip <script> blocks so markers inside JS template literals are not matched
    stripped = strip_scripts(text)

    check_nav_loader(path, stripped)
    check_legacy_nav(path, stripped)
    check_internal_notes(path, stripped)
    check_galleries(path, stripped)
    check_image_refs(path, text)  # Keep full text: img tags are real HTML


# ---------------------------------------------------------------------------
# 7. Top-level index files
# ---------------------------------------------------------------------------

def check_index_files():
    for rel in ["lessons/index.html", "index.html"]:
        p = ROOT / rel
        if not p.exists():
            warn(ROOT / rel, f"Expected file missing: {rel}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    for course in COURSES:
        folder = LESSONS_ROOT / course
        if not folder.exists():
            warn(LESSONS_ROOT / course, f"Course folder missing: lessons/{course}/")
            continue
        for html in sorted(folder.glob("*.html")):
            if html.name.lower() == "index.html":
                continue
            validate_lesson(html)

    check_index_files()

    # ---- Output ----
    print("=" * 60)
    print("YSP Site Validator")
    print("=" * 60)
    print(f"Files checked : {FILES_CHECKED}")
    print(f"Errors        : {len(ERRORS)}")
    print(f"Warnings      : {len(WARNINGS)}")
    print()

    if ERRORS:
        print("ERRORS")
        print("------")
        by_file = {}
        for f, msg in ERRORS:
            by_file.setdefault(f, []).append(msg)
        for f, msgs in sorted(by_file.items()):
            print(f"  {f}")
            for msg in msgs:
                print(f"    ✗ {msg}")
        print()

    if WARNINGS:
        print("WARNINGS")
        print("--------")
        by_file = {}
        for f, msg in WARNINGS:
            by_file.setdefault(f, []).append(msg)
        for f, msgs in sorted(by_file.items()):
            print(f"  {f}")
            for msg in msgs:
                print(f"    ⚠ {msg}")
        print()

    if not ERRORS and not WARNINGS:
        print("All checks passed.")

    sys.exit(1 if ERRORS else 0)


if __name__ == "__main__":
    main()
