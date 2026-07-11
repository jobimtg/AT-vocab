from pathlib import Path
from html.parser import HTMLParser
import html as html_lib
import os
import re

ROOT = Path.cwd()
LESSONS_ROOT = ROOT / "lessons"
LESSONS_INDEX = LESSONS_ROOT / "index.html"
HOME_INDEX = ROOT / "index.html"
IMAGE_INBOX = ROOT / "image-inbox"

COURSES = {
    "ca-life": {
        "order": 1,
        "label": "Canada Life & Career English",
        "short": "Canada Life",
        "tag": "Canada Life",
        "anchor": "life-career",
        "accent": "#2A7A6E",
        "description": "Daily life, settling in, work, housing, appointments, and useful communication for real situations.",
    },
    "travel": {
        "order": 2,
        "label": "Travel English",
        "short": "Travel",
        "tag": "Travel",
        "anchor": "travel",
        "accent": "#C8956C",
        "description": "Travel, transportation, airports, hotels, directions, restaurants, and everyday travel communication.",
    },
    "business": {
        "order": 3,
        "label": "Business English",
        "short": "Business",
        "tag": "Business",
        "anchor": "business",
        "accent": "#1B2A4A",
        "description": "Workplace conversations, meetings, reception, professional communication, and business confidence.",
    },
}

GLOBAL_LOADER_START = "<!-- YSP_GLOBAL_NAV_LOADER_START -->"
GLOBAL_LOADER_END = "<!-- YSP_GLOBAL_NAV_LOADER_END -->"

LESSON_CARDS_START = "<!-- YSP_LESSON_CARDS_START -->"
LESSON_CARDS_END = "<!-- YSP_LESSON_CARDS_END -->"

HOME_CARDS_START = "<!-- YSP_HOME_FEATURED_LESSONS_START -->"
HOME_CARDS_END = "<!-- YSP_HOME_FEATURED_LESSONS_END -->"

GALLERY_MOUNT_START = "<!-- YSP_IMAGE_GALLERY_MOUNT_START -->"
GALLERY_MOUNT_END = "<!-- YSP_IMAGE_GALLERY_MOUNT_END -->"

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
IMAGE_SECTION_FOLDERS = {
    "pronunciation": "pronunciation",
    "phrases": "phrases",
    "speaking": "speaking",
    "culture": "culture",
}

LEGACY_BLOCKS = [
    ("<!-- YSP_SITE_NAV_START -->", "<!-- YSP_SITE_NAV_END -->"),
    ("<!-- YSP_BACK_TO_LESSONS_START -->", "<!-- YSP_BACK_TO_LESSONS_END -->"),
    ("<!-- YSP_TOP_BUTTON_START -->", "<!-- YSP_TOP_BUTTON_END -->"),
    ("<!-- YSP_LESSON_BRAND_NAV_START -->", "<!-- YSP_LESSON_BRAND_NAV_END -->"),
    ("<!-- YSP_LESSON_BRAND_NAV_STYLE_START -->", "<!-- YSP_LESSON_BRAND_NAV_STYLE_END -->"),
    ("<!-- YSP_CLEAN_TOP_BUTTON_START -->", "<!-- YSP_CLEAN_TOP_BUTTON_END -->"),
    ("<!-- YSP_CLEAN_TOP_STYLE_START -->", "<!-- YSP_CLEAN_TOP_STYLE_END -->"),
    ("<!-- YSP_PAGE_TOP_BUTTON_START -->", "<!-- YSP_PAGE_TOP_BUTTON_END -->"),
    ("<!-- YSP_PAGE_TOP_ANCHOR_START -->", "<!-- YSP_PAGE_TOP_ANCHOR_END -->"),
    ("<!-- YSP_PRONUNCIATION_IMAGE_START -->", "<!-- YSP_PRONUNCIATION_IMAGE_END -->"),
    ("<!-- YSP_PRONUNCIATION_IMAGE_STYLE_START -->", "<!-- YSP_PRONUNCIATION_IMAGE_STYLE_END -->"),
    (GLOBAL_LOADER_START, GLOBAL_LOADER_END),
]


class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_h1 = False
        self.title = []
        self.h1 = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.in_h1 = True

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if self.in_h1:
            self.h1.append(data)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_if_changed(path: Path, text: str) -> bool:
    old = read(path) if path.exists() else ""
    if text != old:
        write(path, text)
        return True
    return False


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def strip_between(text: str, start: str, end: str) -> str:
    return re.sub(re.escape(start) + r"[\s\S]*?" + re.escape(end) + r"\s*", "", text)


def remove_legacy_generated_nav(text: str) -> str:
    for start, end in LEGACY_BLOCKS:
        text = strip_between(text, start, end)

    generated_patterns = [
        r"<style id=[\"']ysp-auto-nav-style[\"'][\s\S]*?</style>\s*",
        r"<nav[^>]*class=[\"'][^\"']*\bysp-site-nav\b[^\"']*[\"'][\s\S]*?</nav>\s*",
        r"<nav[^>]*class=[\"'][^\"']*\bysp-local-nav\b[^\"']*[\"'][\s\S]*?</nav>\s*",
        r"<a[^>]*class=[\"'][^\"']*\bysp-back-lessons\b[^\"']*[\"'][\s\S]*?</a>\s*",
        r"<button[^>]*class=[\"'][^\"']*\bysp-top-btn\b[^\"']*[\"'][\s\S]*?</button>\s*",
        r"<button[^>]*class=[\"'][^\"']*\bysp-top\b[^\"']*[\"'][\s\S]*?</button>\s*",
    ]
    for pattern in generated_patterns:
        text = re.sub(pattern, "", text, flags=re.I)
    return text


def strip_managed_card_section(text: str, marker_start: str, marker_end: str) -> str:
    """Remove old auto-appended managed card sections.

    Older versions appended a ysp-managed-lessons section immediately before </body>.
    On custom pages, that put duplicate lesson cards after the footer. This cleanup
    removes only managed sections that contain the target marker pair.
    """
    section_pattern = (
        r"\n?\s*<section\b"
        r"(?=[^>]*\bclass=[\"'][^\"']*\bysp-managed-lessons\b[^\"']*[\"'])"
        r"[^>]*>[\s\S]*?"
        + re.escape(marker_start)
        + r"[\s\S]*?"
        + re.escape(marker_end)
        + r"[\s\S]*?</section>\s*"
    )
    return re.sub(section_pattern, "\n", text, flags=re.I)


def has_managed_card_section(text: str) -> bool:
    """Return True only when a real managed section exists in the HTML body.

    CSS selectors inside <style> blocks must not count as a managed card section.
    This prevents stale ysp-managed-lesson-card-style blocks from keeping
    themselves alive forever.
    """
    return re.search(
        r"<section\b(?=[^>]*\bclass=[\"'][^\"']*\bysp-managed-lessons\b[^\"']*[\"'])",
        text,
        flags=re.I,
    ) is not None


def remove_managed_card_style_if_unused(text: str) -> str:
    if has_managed_card_section(text):
        return text
    return re.sub(
        r"\n?\s*<style id=[\"']ysp-managed-lesson-card-style[\"'][\s\S]*?</style>\s*",
        "\n",
        text,
        flags=re.I,
    )


def parse_title(path: Path) -> str:
    parser = TitleParser()
    parser.feed(read(path))
    raw = clean_text(" ".join(parser.h1)) or clean_text(" ".join(parser.title)) or path.stem
    raw = re.sub(r"\s*\|\s*YSP.*$", "", raw, flags=re.I)
    raw = re.sub(r"\s*[-–—]\s*YSP.*$", "", raw, flags=re.I)
    return raw or path.stem


def lesson_code(path: Path) -> str:
    stem = path.stem.lower()
    m = re.search(r"u(\d+)[-_]?l(\d+)", stem)
    if m:
        return f"U{m.group(1)}-L{m.group(2)}"
    nums = re.findall(r"\d+", stem)
    return "L" + nums[-1] if nums else "Preview"


def lesson_order(path: Path):
    stem = path.stem.lower()
    m = re.search(r"u(\d+)[-_]?l(\d+)", stem)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    nums = [int(n) for n in re.findall(r"\d+", stem)]
    if nums:
        return (0, nums[-1])
    return (999, 999)


def lesson_summary(title: str, key: str) -> str:
    lower = title.lower()
    if "airport" in lower or "check-in" in lower:
        return "Practice useful airport and travel survival English."
    if "immigration" in lower or "security" in lower:
        return "Practice useful questions and answers for airport security and immigration."
    if "transportation" in lower or "transit" in lower:
        return "Practice useful English for transportation, transit, and getting around."
    if "welcome" in lower or "canada" in lower:
        return "Practice useful English for arrival, daily life, and first conversations."
    if "business" in lower or "meeting" in lower or "office" in lower:
        return "Practice clearer and more confident workplace communication."
    if key == "ca-life":
        return "Practice useful English for daily life, settling in, and real situations."
    if key == "travel":
        return "Practice useful English for travel situations and trip confidence."
    if key == "business":
        return "Practice useful English for workplace and professional communication."
    return "Practice useful English for real situations."


def relative_prefix_from_lesson(path: Path) -> str:
    # Example: lessons/travel/u1-l1.html -> ../../
    rel_parent = path.parent.relative_to(ROOT)
    depth = len(rel_parent.parts)
    return "../" * depth


def loader_block(path: Path) -> str:
    prefix = relative_prefix_from_lesson(path)
    return f"""{GLOBAL_LOADER_START}
<script src="{prefix}js/ysp-global-nav.js" defer data-ysp-base="{prefix}"></script>
{GLOBAL_LOADER_END}"""


def insert_before_body_end(text: str, block: str) -> str:
    if re.search(r"</body\s*>", text, flags=re.I):
        return re.sub(r"</body\s*>", block + "\n</body>", text, count=1, flags=re.I)
    return text + "\n" + block + "\n"


def parse_attrs(tag_text: str) -> dict:
    attrs = {}
    for name, value in re.findall(r"([a-zA-Z_:][-a-zA-Z0-9_:.]*)\s*=\s*([\"'])(.*?)\2", tag_text, flags=re.S):
        attrs[name.lower()] = html_lib.unescape(value)
    return attrs


def valid_gallery_image_name(filename: str, prefix: str) -> bool:
    stem = Path(filename).stem
    suffix = Path(filename).suffix.lower()
    if suffix not in IMAGE_EXTENSIONS:
        return False
    if not stem.startswith(prefix):
        return False

    rest = stem[len(prefix):]
    lower_prefix = prefix.lower()
    if re.search(r"-d\d{2}-$", lower_prefix):
        return bool(re.fullmatch(r"model|practice|extra-\d+", rest, flags=re.I))
    return bool(re.fullmatch(r"\d+", rest))


def gallery_sort_key(path: Path, prefix: str):
    stem = path.stem
    rest = stem[len(prefix):]
    m = re.fullmatch(r"(\d+)", rest)
    if m:
        return (0, int(m.group(1)), stem)
    if rest == "model":
        return (0, 0, stem)
    if rest == "practice":
        return (0, 1, stem)
    m = re.fullmatch(r"extra-(\d+)", rest)
    if m:
        return (1, int(m.group(1)), stem)
    return (9, 999, stem)


def matching_gallery_images(lesson_path: Path, image_dir_attr: str, prefix: str):
    image_dir_attr = image_dir_attr.strip().strip("/")
    if not image_dir_attr or ".." in Path(image_dir_attr).parts:
        return []

    image_dir = lesson_path.parent / image_dir_attr
    if not image_dir.exists() or not image_dir.is_dir():
        return []

    images = [
        path for path in image_dir.iterdir()
        if path.is_file() and valid_gallery_image_name(path.name, prefix)
    ]
    return sorted(images, key=lambda item: gallery_sort_key(item, prefix))


def gallery_placeholder(image_dir_attr: str, prefix: str) -> str:
    pattern = f"{image_dir_attr.rstrip('/')}/{prefix}*"
    return f"""<div class="ysp-image-placeholder">
      圖片尚未更新
      <code>{html_lib.escape(pattern)}</code>
    </div>"""


def gallery_grid(lesson_path: Path, images) -> str:
    lines = ['<div class="ysp-image-gallery-grid">']
    for image in images:
        src = image.relative_to(lesson_path.parent).as_posix()
        alt = image.stem
        lines.append(
            f'  <img src="{html_lib.escape(src)}" alt="{html_lib.escape(alt)}" loading="lazy">'
        )
    lines.append("</div>")
    return "\n".join(lines)


def update_image_galleries(lesson_path: Path, text: str) -> str:
    """Render existing Dynamic Image Gallery v3 mount areas.

    This function intentionally does not create new gallery sections. It only updates
    pages that already contain a persistent `.ysp-image-gallery` section with
    `data-ysp-image-dir`, `data-ysp-image-prefix`, and mount markers.
    """
    section_pattern = re.compile(
        r"(<section\b(?=[^>]*\bclass=[\"'][^\"']*\bysp-image-gallery\b[^\"']*[\"'])(?P<attrs>[^>]*)>)"
        r"(?P<body>[\s\S]*?)"
        r"(</section>)",
        flags=re.I,
    )

    def replace_section(match):
        start = match.group(1)
        attrs = parse_attrs(start)
        body = match.group("body")
        end = match.group(4)
        image_dir_attr = attrs.get("data-ysp-image-dir", "")
        prefix = attrs.get("data-ysp-image-prefix", "")

        if not image_dir_attr or not prefix:
            return match.group(0)
        if GALLERY_MOUNT_START not in body or GALLERY_MOUNT_END not in body:
            return match.group(0)

        images = matching_gallery_images(lesson_path, image_dir_attr, prefix)
        inner = gallery_grid(lesson_path, images) if images else gallery_placeholder(image_dir_attr, prefix)
        replacement = f"{GALLERY_MOUNT_START}\n    {inner}\n    {GALLERY_MOUNT_END}"
        new_body = re.sub(
            re.escape(GALLERY_MOUNT_START) + r"[\s\S]*?" + re.escape(GALLERY_MOUNT_END),
            replacement,
            body,
            count=1,
        )
        return start + new_body + end

    return section_pattern.sub(replace_section, text)


def normalize_lesson_page(path: Path) -> bool:
    original = read(path)
    text = remove_legacy_generated_nav(original)
    text = update_image_galleries(path, text)
    text = insert_before_body_end(text, loader_block(path))
    if text != original:
        write(path, text)
        return True
    return False


def discover_lessons():
    lessons = []
    if not LESSONS_ROOT.exists():
        return lessons

    for course in COURSES:
        folder = LESSONS_ROOT / course
        if not folder.exists():
            continue

        for path in folder.glob("*.html"):
            if path.name.lower() == "index.html":
                continue

            title = parse_title(path)
            href_from_lessons = os.path.relpath(path, start=LESSONS_INDEX.parent).replace(os.sep, "/")
            href_from_home = os.path.relpath(path, start=ROOT).replace(os.sep, "/")

            lessons.append({
                "path": path,
                "key": course,
                "title": title,
                "code": lesson_code(path),
                "summary": lesson_summary(title, course),
                "href_from_lessons": href_from_lessons,
                "href_from_home": href_from_home,
                "order": lesson_order(path),
            })

    lessons.sort(key=lambda item: (COURSES[item["key"]]["order"], item["order"], item["path"].name.lower()))
    return lessons


def managed_card_html(item, href_key: str) -> str:
    cfg = COURSES[item["key"]]
    accent = cfg["accent"]
    return f"""<a class="lesson-card" href="{html_lib.escape(item[href_key])}">
  <span class="lesson-badge" style="background:{accent}">{html_lib.escape(cfg["tag"])}</span>
  <strong>{html_lib.escape(item["title"])}</strong>
  <small>{html_lib.escape(cfg["label"])} · {html_lib.escape(item["code"])}</small>
  <p>{html_lib.escape(item["summary"])}</p>
</a>"""


def static_lesson_card_html(item) -> str:
    cfg = COURSES[item["key"]]
    code = html_lib.escape(item["code"])
    return f"""<article class="lesson-card">
  <span class="tag">{html_lib.escape(cfg["tag"])} · {code}</span>
  <h3>{html_lib.escape(item["title"])}</h3>
  <p>{html_lib.escape(item["summary"])}</p>
  <a href="{html_lib.escape(item["href_from_lessons"])}">View Preview →</a>
</article>"""


def card_style() -> str:
    return """<style id="ysp-managed-lesson-card-style">
.ysp-managed-lessons{max-width:1120px;margin:0 auto;padding:32px 20px;font-family:Inter,'Noto Sans TC','Microsoft JhengHei',Arial,sans-serif}
.ysp-managed-lessons h2{color:#1B2A4A;margin:0 0 8px}
.ysp-managed-lessons p{color:#7A7A6E;margin:0 0 18px;line-height:1.65}
.lesson-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.lesson-card{display:block;text-decoration:none;color:#1B2A4A;background:#fff;border:1px solid rgba(27,42,74,.12);border-radius:18px;padding:18px;box-shadow:0 8px 24px rgba(27,42,74,.08);transition:.18s}
.lesson-card:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(27,42,74,.14)}
.lesson-card strong{display:block;font-size:16px;line-height:1.35;margin:10px 0 6px}
.lesson-card small{display:block;color:#7A7A6E;font-size:12px}
.lesson-badge{display:inline-block;color:#fff;border-radius:999px;padding:4px 9px;font-size:11px;font-weight:800}
</style>"""


def ensure_card_style(text: str) -> str:
    if 'id="ysp-managed-lesson-card-style"' in text or "id='ysp-managed-lesson-card-style'" in text:
        return text
    if re.search(r"</head\s*>", text, flags=re.I):
        return re.sub(r"</head\s*>", card_style() + "\n</head>", text, count=1, flags=re.I)
    return card_style() + "\n" + text


def replace_or_append_cards(
    text: str,
    start: str,
    end: str,
    block: str,
    title: str,
    append_if_missing: bool = False,
) -> str:
    full_block = f"{start}\n{block}\n{end}"
    if start in text and end in text:
        return re.sub(re.escape(start) + r"[\s\S]*?" + re.escape(end), full_block, text)

    if not append_if_missing:
        return text

    section = f"""<section class="ysp-managed-lessons" id="lessons">
  <h2>{html_lib.escape(title)}</h2>
  <p>Choose a lesson path and continue your English practice.</p>
  <div class="lesson-grid">
{full_block}
  </div>
</section>"""
    if re.search(r"</body\s*>", text, flags=re.I):
        return re.sub(r"</body\s*>", section + "\n</body>", text, count=1, flags=re.I)
    return text + "\n" + section + "\n"


def replace_course_lesson_grid(text: str, anchor: str, cards: str):
    pattern = re.compile(
        r"(<section\b(?=[^>]*\bid=[\"']" + re.escape(anchor) + r"[\"'])(?=[^>]*\bclass=[\"'][^\"']*\bcourse-section\b[^\"']*[\"'])[^>]*>[\s\S]*?"
        r"<div\b(?=[^>]*\bclass=[\"'][^\"']*\blesson-grid\b[^\"']*[\"'])[^>]*>)"
        r"[\s\S]*?"
        r"(</div>\s*</section>)",
        flags=re.I,
    )
    return pattern.subn(r"\1\n" + cards + r"\n\2", text, count=1)


def default_lessons_index() -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lessons — YSP Learn & Shine</title>
{card_style()}
</head>
<body>
</body>
</html>"""


def update_lessons_index(lessons):
    cards_by_course = {course: [] for course in COURSES}
    for item in lessons:
        cards_by_course[item["key"]].append(item)

    created_default = not LESSONS_INDEX.exists()
    text = read(LESSONS_INDEX) if LESSONS_INDEX.exists() else default_lessons_index()
    text = strip_managed_card_section(text, LESSON_CARDS_START, LESSON_CARDS_END)

    custom_sections_updated = 0
    for course, cfg in COURSES.items():
        course_lessons = cards_by_course.get(course, [])
        if not course_lessons:
            continue
        cards = "\n".join(static_lesson_card_html(item) for item in course_lessons)
        text, count = replace_course_lesson_grid(text, cfg["anchor"], cards)
        custom_sections_updated += count

    if custom_sections_updated == 0:
        cards = "\n".join(managed_card_html(item, "href_from_lessons") for item in lessons)
        if not cards:
            cards = '<article class="lesson-card"><span class="lesson-badge" style="background:#1B2A4A">Coming Soon</span><strong>New lessons are coming soon</strong><small>YSP Learn & Shine</small></article>'

        if created_default or (LESSON_CARDS_START in text and LESSON_CARDS_END in text):
            text = ensure_card_style(text)
        text = replace_or_append_cards(
            text,
            LESSON_CARDS_START,
            LESSON_CARDS_END,
            cards,
            "Lessons",
            append_if_missing=created_default,
        )
        text = remove_managed_card_style_if_unused(text)

    return write_if_changed(LESSONS_INDEX, text)


def update_home_index(lessons):
    """Update only explicitly managed home lesson card blocks.

    The current homepage has custom curated cards and no managed markers. To avoid
    overwriting that design, this function updates the homepage only when the
    YSP_HOME_FEATURED_LESSONS markers are present.
    """
    if not HOME_INDEX.exists():
        return False

    text = read(HOME_INDEX)
    if HOME_CARDS_START not in text or HOME_CARDS_END not in text:
        return False

    featured = lessons[:12]
    cards = "\n".join(managed_card_html(item, "href_from_home") for item in featured)
    if not cards:
        return False

    text = strip_managed_card_section(text, HOME_CARDS_START, HOME_CARDS_END)
    text = ensure_card_style(text)
    text = replace_or_append_cards(
        text,
        HOME_CARDS_START,
        HOME_CARDS_END,
        cards,
        "Featured Lessons",
        append_if_missing=False,
    )
    text = remove_managed_card_style_if_unused(text)
    return write_if_changed(HOME_INDEX, text)


def parse_inbox_lesson_html(path: Path):
    """Parse lesson HTML files uploaded to image-inbox.

    Supported names:
    - ca-life-u1-l3.html
    - travel-u1-l2.html
    - business-u2-l1.html

    Existing lesson HTML files are never overwritten by this automation.
    """
    if path.suffix.lower() != ".html":
        return None

    stem = path.stem.lower()
    for course in sorted(COURSES.keys(), key=len, reverse=True):
        prefix = f"{course}-"
        if not stem.startswith(prefix):
            continue

        rest = stem[len(prefix):]
        if not re.fullmatch(r"u\d+-l\d+", rest):
            return None

        return {
            "course": course,
            "filename": f"{rest}.html",
        }

    return None


def process_lesson_html_inbox():
    moved = []
    skipped = []
    if not IMAGE_INBOX.exists():
        return moved, skipped

    for path in sorted(IMAGE_INBOX.iterdir()):
        if not path.is_file() or path.suffix.lower() != ".html":
            continue

        parsed = parse_inbox_lesson_html(path)
        if not parsed:
            skipped.append((path.name, "filename must match <course>-u<number>-l<number>.html"))
            continue

        content = read(path)
        if not re.search(r"<html\b", content, flags=re.I) or not re.search(r"</html\s*>", content, flags=re.I):
            skipped.append((path.name, "file does not look like a complete HTML document"))
            continue

        dest_dir = LESSONS_ROOT / parsed["course"]
        dest_path = dest_dir / parsed["filename"]
        if dest_path.exists():
            skipped.append((path.name, f"target already exists: {dest_path.relative_to(ROOT).as_posix()}"))
            continue

        dest_dir.mkdir(parents=True, exist_ok=True)
        path.replace(dest_path)
        moved.append((path.name, dest_path.relative_to(ROOT).as_posix()))

    return moved, skipped


def parse_inbox_image(path: Path):
    ext = path.suffix.lower()
    if ext not in IMAGE_EXTENSIONS:
        return None

    stem = path.stem.lower()
    for course in sorted(COURSES.keys(), key=len, reverse=True):
        prefix = f"{course}-"
        if not stem.startswith(prefix):
            continue

        rest = stem[len(prefix):]
        m = re.fullmatch(r"(l\d{2})-(pronunciation|phrases|speaking|culture)-(\d+)", rest)
        if m:
            lesson_prefix, section, number = m.groups()
            return {
                "course": course,
                "folder": IMAGE_SECTION_FOLDERS[section],
                "filename": f"{lesson_prefix}-{section}-{number}{ext}",
            }

        m = re.fullmatch(r"(l\d{2})-(d\d{2})-(model|practice|extra-\d+)", rest)
        if m:
            lesson_prefix, dialogue, suffix = m.groups()
            return {
                "course": course,
                "folder": "dialogues",
                "filename": f"{lesson_prefix}-{dialogue}-{suffix}{ext}",
            }

    return None


def process_image_inbox():
    moved = []
    skipped = []
    if not IMAGE_INBOX.exists():
        return moved, skipped

    for path in sorted(IMAGE_INBOX.iterdir()):
        if not path.is_file():
            continue
        if path.suffix.lower() == ".html":
            continue

        parsed = parse_inbox_image(path)
        if not parsed:
            skipped.append((path.name, "filename does not match supported YSP image-inbox rules"))
            continue

        dest_dir = LESSONS_ROOT / parsed["course"] / "assets" / parsed["folder"]
        dest_path = dest_dir / parsed["filename"]
        if dest_path.exists():
            skipped.append((path.name, f"target already exists: {dest_path.relative_to(ROOT).as_posix()}"))
            continue

        dest_dir.mkdir(parents=True, exist_ok=True)
        path.replace(dest_path)
        moved.append((path.name, dest_path.relative_to(ROOT).as_posix()))

    return moved, skipped


def main():
    js_file = ROOT / "js" / "ysp-global-nav.js"
    if not js_file.exists():
        print("WARNING: js/ysp-global-nav.js does not exist.")
        print("The loader will be added, but navigation buttons will not appear until js/ysp-global-nav.js is uploaded.")

    moved_lessons, skipped_lessons = process_lesson_html_inbox()
    moved_images, skipped_images = process_image_inbox()

    lessons = discover_lessons()
    changed_pages = []

    for item in lessons:
        if normalize_lesson_page(item["path"]):
            changed_pages.append(item["path"].relative_to(ROOT).as_posix())

    lessons_index_changed = update_lessons_index(lessons)
    home_index_changed = update_home_index(lessons)

    print("YSP Site Maintenance")
    print("====================")
    print(f"Lesson HTML inbox files published: {len(moved_lessons)}")
    for source, dest in moved_lessons:
        print(f"- {source} -> {dest}")
    if skipped_lessons:
        print(f"Lesson HTML inbox files skipped: {len(skipped_lessons)}")
        for source, reason in skipped_lessons:
            print(f"- {source}: {reason}")
    print(f"Lessons discovered: {len(lessons)}")
    print("Scanned folders: lessons/ca-life, lessons/travel, lessons/business")
    print(f"Image inbox files moved: {len(moved_images)}")
    for source, dest in moved_images:
        print(f"- {source} -> {dest}")
    if skipped_images:
        print(f"Image inbox files skipped: {len(skipped_images)}")
        for source, reason in skipped_images:
            print(f"- {source}: {reason}")
    print(f"Lesson pages with loader/gallery updated: {len(changed_pages)}")
    for path in changed_pages:
        print(f"- {path}")
    print(f"Updated: lessons/index.html ({'changed' if lessons_index_changed else 'no changes'})")
    if HOME_INDEX.exists():
        print(f"Updated: index.html ({'changed' if home_index_changed else 'no changes'})")


if __name__ == "__main__":
    main()
