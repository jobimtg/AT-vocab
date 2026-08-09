# Run with: python3 scripts/ysp_gallery_quality_check.py

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
LESSONS_ROOT = ROOT / "lessons"
COURSES = ["ca-life", "travel", "business"]
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
WARN_BYTES = 2 * 1024 * 1024
MAX_BYTES = 5 * 1024 * 1024

ERRORS = []
WARNINGS = []
FILES_CHECKED = 0

GALLERY_SECTION_RE = re.compile(
    r"<section\b(?=[^>]*\bclass=[\"'][^\"']*\bysp-image-gallery\b[^\"']*[\"'])(?P<tag>[^>]*)>(?P<body>[\s\S]*?)</section>",
    re.I,
)
ATTR_RE = re.compile(r"([a-zA-Z_:][-a-zA-Z0-9_:.]*)\s*=\s*([\"'])(.*?)\2", re.S)
IMG_SRC_RE = re.compile(r"<img[^>]+src=[\"']([^\"']+)[\"']", re.I)
SCRIPT_BLOCK_RE = re.compile(r"<script[\s\S]*?</script>", re.I)

RESPONSIVE_IMAGE_RULES = {
    "width": "100%",
    "max-width": "100%",
    "height": "auto",
    "aspect-ratio": "16/9",
    "object-fit": "contain",
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def err(path: Path, message: str) -> None:
    ERRORS.append((rel(path), message))


def warn(path: Path, message: str) -> None:
    WARNINGS.append((rel(path), message))


def human_size(num_bytes: int) -> str:
    return f"{num_bytes / (1024 * 1024):.2f} MB"


def attrs_from_tag(tag: str) -> dict:
    attrs = {}
    for name, _quote, value in ATTR_RE.findall(tag):
        attrs[name.lower()] = value
    return attrs


def css_declarations(text: str, selector: str) -> dict:
    declarations = {}
    for body in re.findall(rf"{re.escape(selector)}\s*\{{([^}}]*)\}}", text, re.I):
        for item in body.split(";"):
            if ":" not in item:
                continue
            name, value = item.split(":", 1)
            declarations[name.strip().lower()] = re.sub(r"\s+", "", value).lower()
    return declarations


def check_gallery_blocks(path: Path, text: str) -> None:
    stripped = SCRIPT_BLOCK_RE.sub("", text)
    galleries = list(GALLERY_SECTION_RE.finditer(stripped))

    if "YSP_IMAGE_GALLERY" in stripped and not galleries:
        err(path, "Gallery markers are present, but no .ysp-image-gallery section was found outside script blocks")

    seen_gallery_ids = set()
    if galleries:
        image_css = css_declarations(text, ".ysp-image-gallery-grid img")
        for name, expected in RESPONSIVE_IMAGE_RULES.items():
            if image_css.get(name) != expected:
                err(
                    path,
                    "Gallery images are not safely contained: "
                    f".ysp-image-gallery-grid img requires {name}:{expected}",
                )

    for match in galleries:
        tag = match.group("tag")
        body = match.group("body")
        attrs = attrs_from_tag(tag)
        gallery_id = attrs.get("data-ysp-gallery", "")
        image_dir = attrs.get("data-ysp-image-dir", "")
        prefix = attrs.get("data-ysp-image-prefix", "")

        label = gallery_id or prefix or "unnamed-gallery"

        if not gallery_id:
            warn(path, f"Gallery {label!r}: missing data-ysp-gallery")
        elif gallery_id in seen_gallery_ids:
            err(path, f"Gallery {gallery_id!r}: duplicate data-ysp-gallery value")
        else:
            seen_gallery_ids.add(gallery_id)

        if not image_dir:
            err(path, f"Gallery {label!r}: missing data-ysp-image-dir")
        elif image_dir.startswith("/") or ".." in Path(image_dir).parts:
            err(path, f"Gallery {label!r}: unsafe data-ysp-image-dir {image_dir!r}")

        if not prefix:
            err(path, f"Gallery {label!r}: missing data-ysp-image-prefix")
        elif not prefix.endswith("-"):
            warn(path, f"Gallery {label!r}: data-ysp-image-prefix should end with '-'")

        if "YSP_IMAGE_GALLERY_MOUNT_START" not in body:
            err(path, f"Gallery {label!r}: missing YSP_IMAGE_GALLERY_MOUNT_START")
        if "YSP_IMAGE_GALLERY_MOUNT_END" not in body:
            err(path, f"Gallery {label!r}: missing YSP_IMAGE_GALLERY_MOUNT_END")


def check_rendered_images(path: Path, text: str) -> None:
    lesson_dir = path.parent
    for match in IMG_SRC_RE.finditer(text):
        src = match.group(1)
        if not src.startswith("assets/"):
            continue
        target = lesson_dir / src
        if not target.exists():
            err(path, f"Rendered image is missing: {src}")
            continue
        if target.suffix.lower() not in IMAGE_EXTENSIONS:
            warn(path, f"Rendered image has unusual extension: {src}")
            continue
        size = target.stat().st_size
        if size > MAX_BYTES:
            err(path, f"Rendered image exceeds 5 MB guard: {src} ({human_size(size)})")
        elif size > WARN_BYTES:
            warn(path, f"Rendered image exceeds 2 MB warning level: {src} ({human_size(size)})")


def check_top_buttons() -> None:
    lessons_index = ROOT / "lessons" / "index.html"
    if not lessons_index.exists():
        return
    text = lessons_index.read_text(encoding="utf-8", errors="ignore")
    top_buttons = len(re.findall(r"class=[\"'][^\"']*\btop-button\b", text, re.I))
    if top_buttons > 1:
        err(lessons_index, f"Duplicate .top-button elements found: {top_buttons}")


def validate_lesson(path: Path) -> None:
    global FILES_CHECKED
    FILES_CHECKED += 1
    text = path.read_text(encoding="utf-8", errors="ignore")
    check_gallery_blocks(path, text)
    check_rendered_images(path, text)


def main() -> None:
    for course in COURSES:
        folder = LESSONS_ROOT / course
        if not folder.exists():
            continue
        for html in sorted(folder.glob("*.html")):
            if html.name.lower() == "index.html":
                continue
            validate_lesson(html)

    check_top_buttons()

    print("=" * 60)
    print("YSP Gallery Quality Check")
    print("=" * 60)
    print(f"Files checked : {FILES_CHECKED}")
    print(f"Errors        : {len(ERRORS)}")
    print(f"Warnings      : {len(WARNINGS)}")
    print()

    if ERRORS:
        print("ERRORS")
        print("------")
        for file_name, message in ERRORS:
            print(f"  {file_name}")
            print(f"    ✗ {message}")
        print()

    if WARNINGS:
        print("WARNINGS")
        print("--------")
        for file_name, message in WARNINGS:
            print(f"  {file_name}")
            print(f"    ⚠ {message}")
        print()

    if not ERRORS and not WARNINGS:
        print("All gallery quality checks passed.")

    sys.exit(1 if ERRORS else 0)


if __name__ == "__main__":
    main()
