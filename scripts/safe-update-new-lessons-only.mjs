import fs from "fs";
import path from "path";
import { execSync } from "child_process";

const ROOT = process.cwd();

const COURSE_DIRS = [
  { dir: "lessons/ca-life", label: "Canada Life & Career English", badge: "CA Life", accent: "#2A7A6E" },
  { dir: "lessons/travel", label: "Travel English", badge: "Travel", accent: "#C8956C" },
  { dir: "lessons/business", label: "Business English", badge: "Business", accent: "#1B2A4A" },
];

const SITE_NAV_MARKER_START = "<!-- YSP_SITE_NAV_START -->";
const SITE_NAV_MARKER_END = "<!-- YSP_SITE_NAV_END -->";
const BACK_MARKER_START = "<!-- YSP_BACK_TO_LESSONS_START -->";
const BACK_MARKER_END = "<!-- YSP_BACK_TO_LESSONS_END -->";
const TOP_MARKER_START = "<!-- YSP_TOP_BUTTON_START -->";
const TOP_MARKER_END = "<!-- YSP_TOP_BUTTON_END -->";
const LESSON_CARDS_START = "<!-- YSP_LESSON_CARDS_START -->";
const LESSON_CARDS_END = "<!-- YSP_LESSON_CARDS_END -->";

function exists(rel) {
  return fs.existsSync(path.join(ROOT, rel));
}

function read(rel) {
  return fs.readFileSync(path.join(ROOT, rel), "utf8");
}

function write(rel, content) {
  fs.mkdirSync(path.dirname(path.join(ROOT, rel)), { recursive: true });
  fs.writeFileSync(path.join(ROOT, rel), content, "utf8");
}

function normalizeSlash(p) {
  return p.replaceAll("\\", "/");
}

function getChangedLessonHtmlFiles() {
  let output = "";
  try {
    output = execSync("git diff --name-only HEAD~1 HEAD", { cwd: ROOT, encoding: "utf8" });
  } catch {
    try {
      output = execSync("git ls-files lessons/**/*.html", { cwd: ROOT, encoding: "utf8" });
    } catch {
      output = "";
    }
  }

  return output
    .split(/\r?\n/)
    .map(s => s.trim())
    .filter(Boolean)
    .map(normalizeSlash)
    .filter(p =>
      /^lessons\/(ca-life|travel|business)\/.+\.html$/i.test(p) &&
      !/^lessons\/index\.html$/i.test(p)
    );
}

function getAllLessonHtmlFiles() {
  const files = [];
  for (const course of COURSE_DIRS) {
    const abs = path.join(ROOT, course.dir);
    if (!fs.existsSync(abs)) continue;
    for (const name of fs.readdirSync(abs)) {
      if (!name.toLowerCase().endsWith(".html")) continue;
      if (name.toLowerCase() === "index.html") continue;
      files.push(`${course.dir}/${name}`);
    }
  }
  return files.sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
}

function getTitleFromHtml(rel) {
  const html = read(rel);
  const h1 = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
  if (h1) return cleanText(h1[1]);
  const title = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  if (title) return cleanText(title[1]);
  return path.basename(rel, ".html");
}

function cleanText(s) {
  return s
    .replace(/<[^>]+>/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&nbsp;/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function courseForFile(rel) {
  return COURSE_DIRS.find(c => rel.startsWith(c.dir + "/"));
}

function relPrefixFromFile(rel) {
  // lessons/ca-life/u1-l1.html -> ../..
  const depth = rel.split("/").length - 1;
  return Array(depth).fill("..").join("/") || ".";
}

function siteNav(prefix) {
  return `${SITE_NAV_MARKER_START}
<nav class="ysp-site-nav" aria-label="YSP site navigation">
  <a href="${prefix}/index.html">Home</a>
  <a href="${prefix}/lessons/index.html">Lessons</a>
  <a href="${prefix}/index.html#about">About</a>
  <a class="ysp-trial" href="${prefix}/index.html#book">Book a Trial Lesson</a>
</nav>
${SITE_NAV_MARKER_END}`;
}

function backToLessons(prefix) {
  return `${BACK_MARKER_START}
<a class="ysp-back-lessons" href="${prefix}/lessons/index.html">← Back to Lessons</a>
${BACK_MARKER_END}`;
}

function topButton() {
  return `${TOP_MARKER_START}
<button class="ysp-top-btn" type="button" onclick="window.scrollTo({top:0,behavior:'smooth'})">Top ↑</button>
${TOP_MARKER_END}`;
}

function navCss() {
  return `
<style id="ysp-auto-nav-style">
.ysp-site-nav{position:sticky;top:0;z-index:9999;display:flex;gap:12px;justify-content:flex-end;align-items:center;padding:10px 24px;background:#F7F0E6;border-bottom:1px solid rgba(27,42,74,.12);font-family:Montserrat,'Noto Sans TC',Arial,sans-serif}
.ysp-site-nav a{text-decoration:none;color:#1B2A4A;background:#fff;border:1px solid rgba(27,42,74,.10);border-radius:999px;padding:9px 18px;font-size:14px;font-weight:700;box-shadow:0 2px 8px rgba(27,42,74,.05)}
.ysp-site-nav a:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(27,42,74,.12)}
.ysp-site-nav .ysp-trial{background:#1B2A4A;color:#fff;border-color:#1B2A4A}
.ysp-back-lessons{display:inline-flex;margin:14px 16px 0;padding:8px 14px;border-radius:999px;text-decoration:none;background:#fff;color:#1B2A4A;border:1px solid rgba(27,42,74,.15);font-family:Montserrat,'Noto Sans TC',Arial,sans-serif;font-size:13px;font-weight:700;box-shadow:0 2px 8px rgba(27,42,74,.05)}
.ysp-back-lessons:hover{transform:translateY(-1px)}
.ysp-top-btn{position:fixed;right:18px;bottom:18px;z-index:9999;border:0;border-radius:999px;background:#1B2A4A;color:#fff;padding:10px 14px;font-family:Montserrat,'Noto Sans TC',Arial,sans-serif;font-weight:800;box-shadow:0 6px 18px rgba(27,42,74,.25);cursor:pointer}
@media(max-width:720px){.ysp-site-nav{justify-content:flex-start;overflow-x:auto;padding:8px 12px}.ysp-site-nav a{font-size:12px;padding:8px 12px}.ysp-back-lessons{margin-left:12px}.ysp-top-btn{right:12px;bottom:12px}}
</style>`;
}

function removeMarkedBlock(html, start, end) {
  const pattern = new RegExp(`${escapeRegExp(start)}[\\s\\S]*?${escapeRegExp(end)}\\s*`, "g");
  return html.replace(pattern, "");
}

function hasMarkedBlock(html, start, end) {
  return html.includes(start) && html.includes(end);
}

function escapeRegExp(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function ensureBeforeBodyEnd(html, block) {
  if (html.includes("</body>")) return html.replace(/<\/body>/i, `${block}\n</body>`);
  return `${html}\n${block}\n`;
}

function ensureHeadCss(html) {
  if (html.includes('id="ysp-auto-nav-style"')) return html;
  if (html.includes("</head>")) return html.replace(/<\/head>/i, `${navCss()}\n</head>`);
  return `${navCss()}\n${html}`;
}

/**
 * Idempotent but conservative:
 * - If a marker already exists, replace only that marked block.
 * - If no marker exists, add the navigation once.
 * - This script is only called on changed lesson pages, not every old page.
 */
function updateLessonPage(rel) {
  let html = read(rel);
  const prefix = relPrefixFromFile(rel);

  html = removeMarkedBlock(html, SITE_NAV_MARKER_START, SITE_NAV_MARKER_END);
  html = removeMarkedBlock(html, BACK_MARKER_START, BACK_MARKER_END);
  html = removeMarkedBlock(html, TOP_MARKER_START, TOP_MARKER_END);
  html = ensureHeadCss(html);

  if (html.match(/<body[^>]*>/i)) {
    html = html.replace(/<body[^>]*>/i, match => `${match}\n${siteNav(prefix)}\n${backToLessons(prefix)}`);
  } else {
    html = `${siteNav(prefix)}\n${backToLessons(prefix)}\n${html}`;
  }

  html = ensureBeforeBodyEnd(html, topButton());
  write(rel, html);
  console.log(`Updated changed lesson page only: ${rel}`);
}

function lessonCardHtml(rel) {
  const course = courseForFile(rel);
  const title = getTitleFromHtml(rel);
  const href = rel.replace(/^lessons\//, "");
  return `<a class="lesson-card" href="${href}">
  <span class="lesson-badge" style="background:${course.accent}">${course.badge}</span>
  <strong>${escapeHtml(title)}</strong>
  <small>${escapeHtml(course.label)}</small>
</a>`;
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function buildLessonsIndex() {
  const lessons = getAllLessonHtmlFiles();

  const cards = lessons.map(lessonCardHtml).join("\n");

  let indexPath = "lessons/index.html";
  let html = exists(indexPath) ? read(indexPath) : defaultLessonsIndex();

  const block = `${LESSON_CARDS_START}
${cards}
${LESSON_CARDS_END}`;

  if (html.includes(LESSON_CARDS_START) && html.includes(LESSON_CARDS_END)) {
    html = html.replace(
      new RegExp(`${escapeRegExp(LESSON_CARDS_START)}[\\s\\S]*?${escapeRegExp(LESSON_CARDS_END)}`),
      block
    );
  } else {
    // Conservative fallback: append cards near the end without trying to rewrite the existing design.
    html = html.replace(/<\/body>/i, `<section class="lesson-grid-wrap">
<h1>Lessons</h1>
<div class="lesson-grid">
${block}
</div>
</section>
</body>`);
  }

  html = ensureLessonsIndexCss(html);
  write(indexPath, html);
  console.log("Updated lessons/index.html lesson cards.");
}

function defaultLessonsIndex() {
  return `<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lessons — YSP Learn & Shine</title>
</head>
<body>
<section class="lesson-grid-wrap">
<h1>Lessons</h1>
<div class="lesson-grid">
${LESSON_CARDS_START}
${LESSON_CARDS_END}
</div>
</section>
</body>
</html>`;
}

function ensureLessonsIndexCss(html) {
  if (html.includes("id=\"ysp-lesson-index-style\"")) return html;
  const css = `<style id="ysp-lesson-index-style">
.lesson-grid-wrap{max-width:1100px;margin:0 auto;padding:32px 20px;font-family:Montserrat,'Noto Sans TC',Arial,sans-serif}
.lesson-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.lesson-card{display:block;text-decoration:none;color:#1B2A4A;background:#fff;border:1px solid rgba(27,42,74,.12);border-radius:18px;padding:18px;box-shadow:0 8px 24px rgba(27,42,74,.08);transition:.18s}
.lesson-card:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(27,42,74,.14)}
.lesson-card strong{display:block;font-size:16px;line-height:1.35;margin:10px 0 6px}
.lesson-card small{display:block;color:#7A7A6E;font-size:12px}
.lesson-badge{display:inline-block;color:#fff;border-radius:999px;padding:4px 9px;font-size:11px;font-weight:800}
</style>`;
  if (html.includes("</head>")) return html.replace(/<\/head>/i, `${css}\n</head>`);
  return `${css}\n${html}`;
}

buildLessonsIndex();

const changed = getChangedLessonHtmlFiles();
if (changed.length === 0) {
  console.log("No changed lesson HTML pages detected. Existing lesson pages were not modified.");
} else {
  for (const rel of changed) updateLessonPage(rel);
}

console.log("Safe update complete. Existing unchanged lesson pages were not touched.");
