import fs from "fs";
import path from "path";

const ROOT = process.cwd();
const targets = process.argv.slice(2);

if (!targets.length) {
  console.error("Usage: node scripts/cleanup-old-auto-injected-nav.mjs lessons/ca-life/u1-l1.html");
  process.exit(1);
}

function esc(s){ return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }
function rmMarked(html,start,end){ return html.replace(new RegExp(`${esc(start)}[\\s\\S]*?${esc(end)}\\s*`, "g"), ""); }

for (const target of targets) {
  const rel = target.replaceAll("\\", "/");
  const p = path.join(ROOT, rel);
  if (!fs.existsSync(p)) {
    console.log(`Skip missing: ${rel}`);
    continue;
  }

  let html = fs.readFileSync(p, "utf8");

  html = rmMarked(html, "<!-- YSP_SITE_NAV_START -->", "<!-- YSP_SITE_NAV_END -->");
  html = rmMarked(html, "<!-- YSP_BACK_TO_LESSONS_START -->", "<!-- YSP_BACK_TO_LESSONS_END -->");
  html = rmMarked(html, "<!-- YSP_TOP_BUTTON_START -->", "<!-- YSP_TOP_BUTTON_END -->");
  html = html.replace(/<style id=["']ysp-auto-nav-style["'][\s\S]*?<\/style>\s*/gi, "");
  html = html.replace(/<button[^>]*class=["'][^"']*ysp-top-btn[^"']*["'][\s\S]*?<\/button>\s*/gi, "");
  html = html.replace(/<a[^>]*class=["'][^"']*ysp-back-lessons[^"']*["'][\s\S]*?<\/a>\s*/gi, "");
  html = html.replace(/<nav[^>]*class=["'][^"']*ysp-site-nav[^"']*["'][\s\S]*?<\/nav>\s*/gi, "");

  fs.writeFileSync(p, html, "utf8");
  console.log(`Cleaned previous auto-injected nav from ${rel}`);
}
