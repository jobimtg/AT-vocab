#!/usr/bin/env python3
"""Build Canada Life hybrid lesson cards from JSON and AI illustration scenes."""

from __future__ import annotations

import argparse
import json
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1920, 1080
NAVY = "#102A43"
RUST = "#A33F2B"
GOLD = "#C99A45"
CREAM = "#F2E2BC"
PAPER = "#E9D2A5"
INK = "#17202A"
GREEN = "#2F6B4F"
WHITE = "#FFF9E9"
FONT_LATIN = Path(r"C:\Windows\Fonts\NotoSans-Regular.TTF")
FONT_BOLD = Path(r"C:\Windows\Fonts\NotoSans-Bold.TTF")
FONT_CJK = Path(r"C:\Windows\Fonts\NotoSansTC-VF.ttf")
TAGLINE = "YSP Learn & Shine — Your Journey. Your Voice. Your Future."

VOCAB = {
    "l04": {
        1: [("SIN number", "社會保險號碼"), ("passport", "護照"), ("checking account", "支票帳戶")],
        2: [("work permit", "工作許可證"), ("passport", "護照"), ("sign", "簽名")],
        3: [("debit card", "金融卡"), ("blocked", "遭封鎖"), ("new card", "新卡")],
        4: [("mobile app", "手機應用程式"), ("log in", "登入"), ("temporary password", "臨時密碼")],
        5: [("statement", "對帳單"), ("service fee", "服務費"), ("avoid", "避免")],
    },
    "l05": {
        1: [("available", "可出租"), ("utilities", "水電費"), ("move-in date", "入住日期")],
        2: [("furnished", "附家具"), ("security deposit", "押金"), ("application", "申請表")],
        3: [("heater", "暖氣"), ("landlord", "房東"), ("schedule", "時程")],
        4: [("lease", "租約"), ("notice period", "通知期"), ("sign", "簽名")],
        5: [("neighbor", "鄰居"), ("nearby", "附近"), ("neighborhood", "社區")],
    },
}


def font(size: int, *, bold: bool = False, cjk: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_CJK if cjk else (FONT_BOLD if bold else FONT_LATIN)), size)


def fit_scene(path: Path, size: tuple[int, int]) -> Image.Image:
    with Image.open(path) as im:
        return ImageOps.fit(im.convert("RGB"), size, method=Image.Resampling.LANCZOS)


def wrap(draw: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    lines, current = [], words[0]
    for word in words[1:]:
        candidate = current + " " + word
        if draw.textbbox((0, 0), candidate, font=f)[2] <= width:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def draw_block(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, *, width: int,
               size: int, fill: str = INK, bold: bool = False, cjk: bool = False,
               max_lines: int | None = None, spacing: int = 6) -> int:
    x, y = xy
    chosen = size
    while chosen >= 20:
        f = font(chosen, bold=bold, cjk=cjk)
        lines = wrap(draw, text, f, width)
        if max_lines is None or len(lines) <= max_lines:
            break
        chosen -= 2
    for line in lines[:max_lines]:
        draw.text((x, y), line, font=f, fill=fill)
        y += chosen + spacing
    return y


def base(title: str, zh: str, scene_path: Path, scene_box=(1240, 150, 1880, 735)):
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    d.rectangle((16, 16, W - 16, H - 16), outline=NAVY, width=14)
    d.rectangle((35, 35, W - 35, H - 35), outline=RUST, width=4)
    d.rectangle((45, 45, 195, 135), fill=NAVY, outline=GOLD, width=4)
    d.text((72, 55), "YSP", font=font(48, bold=True), fill=CREAM)
    d.text((225, 52), title, font=font(52, bold=True), fill=NAVY)
    d.text((225, 108), zh, font=font(34, cjk=True), fill=RUST)
    x1, y1, x2, y2 = scene_box
    scene = fit_scene(scene_path, (x2 - x1, y2 - y1))
    im.paste(scene, (x1, y1))
    d.rectangle(scene_box, outline=NAVY, width=7)
    d.rectangle((45, 1008, W - 45, 1042), fill=NAVY)
    tw = d.textbbox((0, 0), TAGLINE, font=font(24, bold=True))[2]
    d.text(((W - tw) // 2, 1009), TAGLINE, font=font(24, bold=True), fill=CREAM)
    return im, d


def panel(d, box, *, fill=WHITE, outline=NAVY, width=4):
    d.rounded_rectangle(box, radius=18, fill=fill, outline=outline, width=width)


def save(im: Image.Image, out: Path):
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "PNG", optimize=True)


def build_phrases(data, scene, out):
    im, d = base("USEFUL PHRASES", "實用句型", scene, (1330, 150, 1880, 890))
    top = 160
    for i, p in enumerate(data["phrases"], 1):
        y1, y2 = top + (i - 1) * 166, top + (i - 1) * 166 + 148
        panel(d, (55, y1, 1305, y2))
        badge = "In-class" if p["t"] == "core" else "Self-study"
        d.rounded_rectangle((70, y1 + 14, 245, y2 - 14), radius=14, fill=NAVY if p["t"] == "core" else RUST)
        d.text((92, y1 + 25), str(i), font=font(42, bold=True), fill=CREAM)
        d.text((82, y1 + 80), badge, font=font(22, bold=True), fill=CREAM)
        draw_block(d, (270, y1 + 12), p["en"], width=480, size=34, bold=True, max_lines=2)
        # Chinese has no spaces for the generic wrapper; shrink deterministically
        # until the complete source string fits inside its fixed column.
        zh_size = 29
        while zh_size > 20 and d.textbbox((0, 0), p["zh"], font=font(zh_size, cjk=True))[2] > 500:
            zh_size -= 1
        d.text((770, y1 + 18), p["zh"], font=font(zh_size, cjk=True), fill=INK)
        draw_block(d, (270, y1 + 92), p["note"], width=950, size=21, fill=RUST, max_lines=2)
    save(im, out)


def build_dialogue(data, dia, scene, out, prefix, practice=False):
    suffix = " — PRACTICE" if practice else " — MODEL"
    im, d = base(f"#{dia['id']} {dia['title']}{suffix}", dia["tz"], scene, (1260, 190, 1880, 700))
    panel(d, (55, 165, 1225, 270), fill=CREAM)
    d.text((78, 180), "SITUATION", font=font(27, bold=True), fill=RUST)
    draw_block(d, (270, 177), dia["sit"], width=920, size=25, max_lines=2)
    d.text((78, 232), f"A  {dia['rA']}    •    B  {dia['rB']}", font=font(22, bold=True), fill=NAVY)
    y = 285
    line_h = min(76, 530 // len(dia["lines"]))
    for idx, (speaker, line) in enumerate(dia["lines"], 1):
        panel(d, (55, y, 1225, y + line_h - 7), fill="#F8EACB", outline=NAVY, width=3)
        d.ellipse((70, y + 9, 112, y + 51), fill=RUST if speaker == "A" else NAVY)
        d.text((83, y + 12), speaker, font=font(22, bold=True), fill=WHITE)
        draw_block(d, (130, y + 9), line, width=1065, size=27 if len(dia["lines"]) <= 6 else 24,
                   bold=False, fill=INK, max_lines=2, spacing=2)
        y += line_h
    panel(d, (55, 835, 920, 985), fill=CREAM)
    d.text((78, 852), "KEY VOCABULARY", font=font(27, bold=True), fill=NAVY)
    for i, (term, zh) in enumerate(VOCAB[prefix][dia["id"]]):
        x = 85 + i * 270
        draw_block(d, (x, 905), term, width=245, size=21, bold=True, max_lines=1)
        draw_block(d, (x, 940), zh, width=245, size=20, cjk=True, max_lines=1, fill=RUST)
    panel(d, (945, 835, 1880, 985), fill="#F8EACB", outline=RUST, width=5)
    d.text((980, 853), "NOW YOU TRY!  換你說", font=font(27, bold=True, cjk=True), fill=RUST)
    draw_block(d, (980, 908), dia["tp"], width=850, size=25, bold=True, fill=RUST, max_lines=2)
    save(im, out)


def build_speaking(data, scene, out):
    im, d = base("SPEAKING QUESTIONS", "口說練習", scene, (1340, 155, 1880, 890))
    for i, item in enumerate(data["speaking"], 1):
        y1 = 160 + (i - 1) * 166
        panel(d, (55, y1, 1310, y1 + 148))
        d.ellipse((75, y1 + 30, 155, y1 + 110), fill=RUST if item["t"] > 1 else NAVY)
        d.text((96, y1 + 44), f"T{item['t']}", font=font(28, bold=True), fill=CREAM)
        draw_block(d, (180, y1 + 16), item["q"], width=1080, size=31, bold=True, max_lines=2)
        draw_block(d, (180, y1 + 88), item["h"], width=1080, size=23, fill=RUST, max_lines=2)
    save(im, out)


def build_culture(data, item, scene, out):
    im, d = base("CULTURE NOTES", "文化補充", scene, (1030, 170, 1880, 680))
    d.text((70, 175), item["title"], font=font(46, bold=True), fill=NAVY)
    d.text((70, 238), item["tz"], font=font(33, cjk=True), fill=RUST)
    panel(d, (55, 315, 995, 670), fill=CREAM)
    d.text((80, 338), "CANADA LIFE NOTE", font=font(27, bold=True), fill=NAVY)
    draw_block(d, (80, 395), item["notes"], width=865, size=30, max_lines=8, spacing=10)
    panel(d, (55, 705, 1880, 985), fill="#F8EACB", outline=RUST)
    d.text((80, 730), "DISCUSSION QUESTIONS", font=font(29, bold=True), fill=RUST)
    y = 785
    for i, q in enumerate(item["qs"], 1):
        y = draw_block(d, (90, y), f"{i}. {q}", width=1735, size=27, bold=True, max_lines=2, spacing=4) + 12
    save(im, out)


def build_pronunciation(data, scene, out):
    p = data["pronunciation"]
    im, d = base("PRONUNCIATION SPOTLIGHT", p["fz"], scene, (1390, 155, 1880, 650))
    d.text((70, 165), p["focus"], font=font(43, bold=True), fill=NAVY)
    for i, item in enumerate(p["words"], 1):
        y1 = 235 + (i - 1) * 125
        panel(d, (55, y1, 1360, y1 + 110))
        d.ellipse((72, y1 + 24, 132, y1 + 84), fill=NAVY)
        d.text((91, y1 + 30), str(i), font=font(28, bold=True), fill=CREAM)
        d.text((155, y1 + 12), item["w"], font=font(31, bold=True), fill=NAVY)
        d.text((410, y1 + 13), item["ipa"], font=font(31, bold=True), fill=INK)
        # ASCII status labels are deterministic across the supported font stack.
        d.text((690, y1 + 12), f"X  {item['bad']}", font=font(26, bold=True), fill=RUST)
        d.text((950, y1 + 12), f"OK  {item['w']}", font=font(26, bold=True), fill=GREEN)
        draw_block(d, (155, y1 + 61), item["tip"], width=1160, size=21, max_lines=2, fill=INK)
    panel(d, (1390, 680, 1880, 850), fill=CREAM)
    d.text((1420, 700), "TIP", font=font(28, bold=True), fill=RUST)
    draw_block(d, (1420, 748), p["tip"], width=420, size=20, max_lines=4, spacing=3)
    panel(d, (55, 875, 1880, 985), fill="#F8EACB", outline=RUST)
    d.text((80, 895), "PRACTICE", font=font(26, bold=True), fill=RUST)
    draw_block(d, (260, 895), p["prac"], width=1570, size=27, bold=True, max_lines=2)
    save(im, out)


def build_lesson(json_path: Path, scene_dir: Path, out_dir: Path, prefix: str):
    data = json.loads(json_path.read_text(encoding="utf-8"))
    build_phrases(data, scene_dir / f"{prefix}-phrases-1-scene.png", out_dir / f"{prefix}-phrases-1.png")
    for dia in data["dialogues"]:
        scene = scene_dir / f"{prefix}-d{dia['id']:02d}-scene.png"
        build_dialogue(data, dia, scene, out_dir / f"{prefix}-d{dia['id']:02d}-model.png", prefix)
        build_dialogue(data, dia, scene, out_dir / f"{prefix}-d{dia['id']:02d}-practice.png", prefix, practice=True)
    build_pronunciation(data, scene_dir / f"{prefix}-pronunciation-1-scene.png", out_dir / f"{prefix}-pronunciation-1.png")
    build_speaking(data, scene_dir / f"{prefix}-speaking-1-scene.png", out_dir / f"{prefix}-speaking-1.png")
    for i, item in enumerate(data["culture"], 1):
        build_culture(data, item, scene_dir / f"{prefix}-culture-{i}-scene.png", out_dir / f"{prefix}-culture-{i}.png")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", type=Path, required=True)
    ap.add_argument("--scene-dir", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--prefix", required=True)
    args = ap.parse_args()
    build_lesson(args.json, args.scene_dir, args.out_dir, args.prefix)


if __name__ == "__main__":
    main()
