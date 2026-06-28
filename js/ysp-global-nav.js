/*
YSP Global Nav Component v2
Single source of truth for course-page navigation.
It creates exactly one website nav, one Back to Lessons, and one Top button.
It also removes legacy duplicated buttons from older workflows.
*/
(function () {
  "use strict";

  var currentScript = document.currentScript;
  var base = (currentScript && currentScript.getAttribute("data-ysp-base")) || "../../";

  function ready(fn) {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", fn);
    else fn();
  }

  function removeAll(selector) {
    document.querySelectorAll(selector).forEach(function (el) { el.remove(); });
  }

  ready(function () {
    removeAll("#ysp-global-nav");
    removeAll("#ysp-back-to-lessons");
    removeAll("#ysp-global-top");
    removeAll(".ysp-site-nav");
    removeAll(".ysp-local-nav");
    removeAll(".ysp-back-lessons");
    removeAll(".ysp-top-btn");
    removeAll(".ysp-top");
    removeAll("button[onclick*='scrollTo'][class*='top']");
    removeAll("button[onclick*='scrollTo'][class*='Top']");

    var oldStyle = document.getElementById("ysp-global-nav-style");
    if (oldStyle) oldStyle.remove();

    var style = document.createElement("style");
    style.id = "ysp-global-nav-style";
    style.textContent = [
      "#ysp-global-nav{position:sticky;top:0;z-index:9999;display:flex;gap:12px;justify-content:center;align-items:center;flex-wrap:wrap;padding:12px 16px;background:#F7F0E6;border-bottom:1px solid rgba(27,42,74,.12);font-family:Montserrat,'Noto Sans TC',Arial,sans-serif}",
      "#ysp-global-nav a{text-decoration:none;color:#1B2A4A;background:#fff;border:1px solid rgba(27,42,74,.12);border-radius:999px;padding:8px 15px;font-size:13px;font-weight:800;box-shadow:0 2px 8px rgba(27,42,74,.06)}",
      "#ysp-global-nav a:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(27,42,74,.12)}",
      "#ysp-global-nav .trial{background:#1B2A4A;color:#fff;border-color:#1B2A4A}",
      "#ysp-back-to-lessons{position:fixed;left:18px;bottom:18px;z-index:10000;text-decoration:none;color:#1B2A4A;background:#fff;border:1px solid rgba(27,42,74,.15);border-radius:999px;padding:10px 14px;font-family:Montserrat,'Noto Sans TC',Arial,sans-serif;font-size:13px;font-weight:800;box-shadow:0 6px 18px rgba(27,42,74,.18)}",
      "#ysp-global-top{position:fixed;right:18px;bottom:18px;z-index:10000;border:0;border-radius:999px;background:#1B2A4A;color:#fff;padding:10px 14px;font-family:Montserrat,'Noto Sans TC',Arial,sans-serif;font-size:13px;font-weight:900;box-shadow:0 6px 18px rgba(27,42,74,.25);cursor:pointer}",
      "@media(max-width:720px){#ysp-global-nav{justify-content:flex-start;overflow-x:auto;flex-wrap:nowrap;padding:8px 10px}#ysp-global-nav a{white-space:nowrap;font-size:12px;padding:7px 11px}#ysp-back-to-lessons{left:10px;bottom:12px;font-size:12px;padding:8px 10px}#ysp-global-top{right:10px;bottom:12px;font-size:12px;padding:8px 10px}}"
    ].join("\n");
    document.head.appendChild(style);

    var nav = document.createElement("nav");
    nav.id = "ysp-global-nav";
    nav.setAttribute("aria-label", "YSP website navigation");
    nav.innerHTML = [
      '<a href="' + base + 'index.html">Home</a>',
      '<a href="' + base + 'lessons/index.html">Lessons</a>',
      '<a href="' + base + 'index.html#about">About</a>',
      '<a class="trial" href="' + base + 'index.html#book">Book a Trial Lesson</a>'
    ].join("");
    document.body.insertBefore(nav, document.body.firstChild);

    var back = document.createElement("a");
    back.id = "ysp-back-to-lessons";
    back.href = base + "lessons/index.html";
    back.textContent = "← Back to Lessons";
    document.body.appendChild(back);

    var top = document.createElement("button");
    top.id = "ysp-global-top";
    top.type = "button";
    top.textContent = "Top ↑";
    top.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });
    document.body.appendChild(top);
  });
})();
