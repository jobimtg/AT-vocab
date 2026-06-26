import fs from "fs";
import path from "path";

const ROOT = process.cwd();

const COURSES = [
  { dir: "lessons/ca-life", label: "Canada Life & Career English", badge: "Canada Life", accent: "#2A7A6E", order: 1 },
  { dir: "lessons/travel", label: "Travel English", badge: "Travel", accent: "#C8956C", order: 2 },
  { dir: "lessons/business", label: "Business English", badge: "Business", accent: "#1B2A4A", order: 3 }
];

const LOADER_START = "<!-- YSP_GLOBAL_NAV_LOADER_START -->";
const LOADER_END = "<!-- YSP_GLOBAL_NAV_LOADER_END -->";
const CARDS_START = "<!-- YSP_LESSON_CARDS_START -->";
const CARDS_END = "<!-- YSP_LESSON_CARDS_END -->";
const HOME_START = "<!-- YSP_HOME_FEATURED_LESSONS_START -->";
const HOME_END = "<!-- YSP_HOME_FEATURED_LESSONS_END -->";

function abs(p){ return path.join(ROOT, p); }
function exists(p){ return fs.existsSync(abs(p)); }
function read(p){ return fs.readFileSync(abs(p), "utf8"); }
function write(p,c){ fs.mkdirSync(path.dirname(abs(p)), {recursive:true}); fs.writeFileSync(abs(p), c, "utf8"); }
function escRe(s){ return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }
function escHtml(s){ return String(s || "").replace(/[&<>"']/g, ch => ({ "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;" }[ch])); }
function clean(s){
  return String(s || "")
    .replace(/<script[\s\S]*?<\/script>/gi," ")
    .replace(/<style[\s\S]*?<\/style>/gi," ")
    .replace(/<[^>]+>/g," ")
    .replace(/&amp;/g,"&")
    .replace(/&nbsp;/g," ")
    .replace(/\s+/g," ")
    .trim();
}
function isLessonHtml(rel){
  return /^lessons\/(ca-life|travel|business)\/[^/]+\.html$/i.test(rel) && !/\/index\.html$/i.test(rel);
}
function removeMarked(html,start,end){
  return html.replace(new RegExp(`${escRe(start)}[\\s\\S]*?${escRe(end)}\\s*`, "g"), "");
}
function removeLegacyInjectedStuff(html){
  html = removeMarked(html, "<!-- YSP_SITE_NAV_START -->", "<!-- YSP_SITE_NAV_END -->");
  html = removeMarked(html, "<!-- YSP_BACK_TO_LESSONS_START -->", "<!-- YSP_BACK_TO_LESSONS_END -->");
  html = removeMarked(html, "<!-- YSP_TOP_BUTTON_START -->", "<!-- YSP_TOP_BUTTON_END -->");
  html = removeMarked(html, LOADER_START, LOADER_END);
  html = html.replace(/<style id=["']ysp-auto-nav-style["'][\s\S]*?<\/style>\s*/gi, "");
  html = html.replace(/<nav[^>]*class=["'][^"']*\bysp-site-nav\b[^"']*["'][\s\S]*?<\/nav>\s*/gi, "");
  html = html.replace(/<nav[^>]*class=["'][^"']*\bysp-local-nav\b[^"']*["'][\s\S]*?<\/nav>\s*/gi, "");
  html = html.replace(/<a[^>]*class=["'][^"']*\bysp-back-lessons\b[^"']*["'][\s\S]*?<\/a>\s*/gi, "");
  html = html.replace(/<button[^>]*class=["'][^"']*\bysp-top-btn\b[^"']*["'][\s\S]*?<\/button>\s*/gi, "");
  html = html.replace(/<button[^>]*class=["'][^"']*\bysp-top\b[^"']*["'][\s\S]*?<\/button>\s*/gi, "");
  return html;
}
function prefixFor(rel){
  const depth = rel.split("/").length - 1;
  return Array(depth).fill("..").join("/") + "/";
}
function loaderBlock(rel){
  const base = prefixFor(rel);
  return `${LOADER_START}
<script src="${base}js/ysp-global-nav.js" defer data-ysp-base="${base}"></script>
${LOADER_END}`;
}
function ensureLoader(rel){
  let html = read(rel);
  html = removeLegacyInjectedStuff(html);
  const loader = loaderBlock(rel);
  if (/<\/body>/i.test(html)) {
    html = html.replace(/<\/body>/i, `${loader}\n</body>`);
  } else {
    html += `\n${loader}\n`;
  }
  write(rel, html);
}
function titleOf(rel){
  const html = read(rel);
  const h1 = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
  if (h1) return clean(h1[1]);
  const t = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  if (t) return clean(t[1]);
  return path.basename(rel, ".html");
}
function lessonOrder(rel,title){
  const file = path.basename(rel).toLowerCase();
  const m = file.match(/u(\d+)-l(\d+)/i) || title.match(/u\s*(\d+)\s*[-—]\s*l\s*(\d+)/i) || title.match(/lesson\s*(\d+)/i);
  if (!m) return 999999;
  if (m.length >= 3) return Number(m[1]) * 1000 + Number(m[2]);
  return Number(m[1]);
}
function courseOf(rel){ return COURSES.find(c => rel.startsWith(c.dir + "/")); }
function lessonFiles(){
  const out = [];
  for (const course of COURSES){
    const dir = abs(course.dir);
    if (!fs.existsSync(dir)) continue;
    for (const name of fs.readdirSync(dir)){
      const rel = `${course.dir}/${name}`.replaceAll("\\", "/");
      if (isLessonHtml(rel)) out.push(rel);
    }
  }
  return out.sort((a,b) => a.localeCompare(b, undefined, {numeric:true}));
}
function lessons(){
  return lessonFiles().map(rel => {
    const title = titleOf(rel);
    return { rel, title, order: lessonOrder(rel,title), course: courseOf(rel) };
  }).sort((a,b) => a.course.order-b.course.order || a.order-b.order || a.rel.localeCompare(b.rel, undefined, {numeric:true}));
}
function card(lesson,prefix=""){
  const href = prefix + lesson.rel.replace(/^lessons\//, "");
  return `<a class="lesson-card" href="${escHtml(href)}">
  <span class="lesson-badge" style="background:${lesson.course.accent}">${escHtml(lesson.course.badge)}</span>
  <strong>${escHtml(lesson.title)}</strong>
  <small>${escHtml(lesson.course.label)}</small>
</a>`;
}
function styleBlock(){
  return `<style id="ysp-managed-lesson-card-style">
.ysp-managed-lessons{max-width:1120px;margin:0 auto;padding:32px 20px;font-family:Montserrat,'Noto Sans TC',Arial,sans-serif}
.ysp-managed-lessons h2{color:#1B2A4A;margin:0 0 8px}
.ysp-managed-lessons p{color:#7A7A6E;margin:0 0 18px}
.lesson-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.lesson-card{display:block;text-decoration:none;color:#1B2A4A;background:#fff;border:1px solid rgba(27,42,74,.12);border-radius:18px;padding:18px;box-shadow:0 8px 24px rgba(27,42,74,.08);transition:.18s}
.lesson-card:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(27,42,74,.14)}
.lesson-card strong{display:block;font-size:16px;line-height:1.35;margin:10px 0 6px}
.lesson-card small{display:block;color:#7A7A6E;font-size:12px}
.lesson-badge{display:inline-block;color:#fff;border-radius:999px;padding:4px 9px;font-size:11px;font-weight:800}
</style>`;
}
function ensureStyle(html){
  if (html.includes('id="ysp-managed-lesson-card-style"')) return html;
  if (html.includes("</head>")) return html.replace(/<\/head>/i, styleBlock()+"\n</head>");
  return styleBlock()+"\n"+html;
}
function replaceOrAppend(html,start,end,block,title){
  const pattern = new RegExp(`${escRe(start)}[\\s\\S]*?${escRe(end)}`);
  if (html.includes(start) && html.includes(end)) return html.replace(pattern, block);
  const section = `<section class="ysp-managed-lessons" id="lessons">
<h2>${title}</h2>
<p>Choose a lesson path and continue your English practice.</p>
<div class="lesson-grid">
${block}
</div>
</section>`;
  if (html.includes("</body>")) return html.replace(/<\/body>/i, section+"\n</body>");
  return html + "\n" + section;
}
function updateLessonsIndex(all){
  const rel = "lessons/index.html";
  const block = `${CARDS_START}
${all.map(l => card(l, "")).join("\n")}
${CARDS_END}`;
  let html = exists(rel) ? read(rel) : `<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Lessons — YSP Learn & Shine</title>${styleBlock()}</head><body></body></html>`;
  html = ensureStyle(html);
  html = replaceOrAppend(html, CARDS_START, CARDS_END, block, "Lessons");
  write(rel, html);
}
function updateHomeIndex(all){
  const rel = "index.html";
  if (!exists(rel)) return;
  const block = `${HOME_START}
${all.slice(0,12).map(l => card(l, "lessons/")).join("\n")}
${HOME_END}`;
  let html = read(rel);
  html = ensureStyle(html);
  html = replaceOrAppend(html, HOME_START, HOME_END, block, "Featured Lessons");
  write(rel, html);
}

for (const rel of lessonFiles()) ensureLoader(rel);
const all = lessons();
updateLessonsIndex(all);
updateHomeIndex(all);
console.log(`Updated ${lessonFiles().length} lesson page loaders and ${all.length} lesson cards.`);
