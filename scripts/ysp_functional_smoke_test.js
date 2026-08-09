#!/usr/bin/env node
/**
 * Runtime smoke test for current and legacy YSP lesson HTML.
 * Current JSON lessons and unknown/malformed architectures are blocking.
 * Recognized legacy pages are still fully executed, but known legacy runtime
 * defects are reported as non-blocking warnings until those lessons migrate.
 */
const fs = require('fs');
const vm = require('vm');
const ROUNDS = 8;

function decode(value) {
  return String(value).replace(/&#39;|&apos;/g, "'").replace(/&quot;/g, '"')
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
}

function attrsOf(text) {
  const attrs = {}; let match;
  const re = /([:\w-]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+)))?/g;
  while ((match = re.exec(text))) attrs[match[1].toLowerCase()] = decode(match[2] ?? match[3] ?? match[4] ?? '');
  return attrs;
}

function mockDom(html, lessonData) {
  const store = {}; let serial = 0;
  function classList(initial = '') {
    const values = new Set(String(initial).split(/\s+/).filter(Boolean));
    return {
      toggle(n, force) { if (force === undefined) values.has(n) ? values.delete(n) : values.add(n); else force ? values.add(n) : values.delete(n); return values.has(n); },
      add(...names) { names.forEach(n => values.add(n)); }, remove(...names) { names.forEach(n => values.delete(n)); },
      contains(n) { return values.has(n); }, toString() { return [...values].join(' '); },
    };
  }
  function makeEl(id = `_el_${++serial}`, attrs = {}) {
    if (store[id]) return store[id];
    const el = {
      id, tagName: (attrs.__tag || 'div').toUpperCase(), _innerHTML: '', _onclickCode: attrs.onclick || null,
      onclick: null, style: {}, textContent: '', dataset: {}, children: [], parentNode: null, classList: classList(attrs.class),
      appendChild(child) { child.parentNode = this; this.children.push(child); return child; },
      setAttribute(n, v) { if (n === 'class') this.className = v; else if (n === 'onclick') this._onclickCode = String(v); else this[n] = v; },
      getAttribute(n) { return n === 'class' ? this.className : n === 'onclick' ? this._onclickCode : this[n] ?? null; },
      removeAttribute(n) { delete this[n]; }, addEventListener(e, fn) { if (e === 'click') this.onclick = fn; },
      querySelector(s) { return query(s)[0] || null; }, querySelectorAll(s) { return query(s); },
      scrollHeight: 0, scrollIntoView() {}, getBoundingClientRect() { return { top: 0 }; },
      get nextElementSibling() { return makeEl(`_sibling_of_${id}`); },
      get innerHTML() { return this._innerHTML; }, set innerHTML(v) { this._innerHTML = String(v); register(this._innerHTML, `render_${id}`); },
    };
    Object.defineProperty(el, 'className', { get() { return el.classList.toString(); }, set(v) { el.classList = classList(v); } });
    for (const [n, v] of Object.entries(attrs)) {
      if (n.startsWith('data-')) { el.dataset[n.slice(5).replace(/-([a-z])/g, (_, c) => c.toUpperCase())] = v; el[n] = v; }
      else if (!['id', 'class', 'onclick', '__tag'].includes(n)) el[n] = v;
    }
    store[id] = el; return el;
  }
  function register(markup, owner = 'static') {
    const prefix = `_${owner}_`; let position = 0;
    for (const key of Object.keys(store)) if (key.startsWith(prefix)) delete store[key];
    const re = /<([a-z][\w-]*)\b([^>]*)>/gi; let match;
    while ((match = re.exec(markup))) { const attrs = attrsOf(match[2]); attrs.__tag = match[1]; makeEl(attrs.id || `${prefix}${position++}`, attrs); }
  }
  function query(selector) {
    const all = Object.values(store);
    selector = selector.trim().split(/\s+/).pop();
    if (selector.startsWith('#')) return store[selector.slice(1)] ? [store[selector.slice(1)]] : [];
    const match = /^(?:([a-z][\w-]*)|\.([\w-]+))?(?:\[([:\w-]+)(?:=["']?([^\]"']+)["']?)?\])?$/i.exec(selector);
    if (!match) return [];
    return all.filter(e => (!match[1] || e.tagName.toLowerCase() === match[1].toLowerCase()) && (!match[2] || e.classList.contains(match[2])) && (!match[3] || (e.getAttribute(match[3]) !== null && (match[4] === undefined || String(e.getAttribute(match[3])) === match[4]))));
  }
  register(html.replace(/<script\b[\s\S]*?<\/script>/gi, '').replace(/<style\b[\s\S]*?<\/style>/gi, ''));
  const document = {
    getElementById(id) { if (id === 'lesson-data' && lessonData !== null) return { textContent: lessonData }; return makeEl(id); },
    querySelectorAll: query, querySelector: s => query(s)[0] || null,
    addEventListener(e, fn) { if (e === 'DOMContentLoaded') document._boots.push(fn); },
    createElement: tag => makeEl(`_created_${++serial}`, { __tag: tag }), _boots: [], body: makeEl('body', { __tag: 'body' }),
  };
  return { document, store, makeEl };
}

function scriptsOf(html) {
  return [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .filter(([, a]) => !/\bsrc\s*=/.test(a) && !/\btype\s*=\s*["']application\/json["']/.test(a)).map(m => m[2]);
}

function architectureOf(html) {
  if (/<script\b(?=[^>]*\bid=["']lesson-data["'])(?=[^>]*\btype=["']application\/json["'])[^>]*>/i.test(html)) return 'current-json';
  if (/document\.getElementById\(["']lesson-data["']\)|const\s+DATA\s*=\s*JSON\.parse/.test(html)) return 'malformed-current';
  if (/const\s+lessons\s*=\s*\[[\s\S]*data:text\/html;base64,/i.test(html) && /<iframe\b/i.test(html)) return 'legacy-iframe-bundle';
  if (/(?:const|let|var)\s+V\s*=/.test(html) && /DOMContentLoaded/.test(html)) return 'legacy-inline-data';
  return 'unknown';
}

function handlers(store) {
  const result = [];
  for (const el of Object.values(store)) { if (el._onclickCode) result.push({ code: el._onclickCode, el }); if (typeof el.onclick === 'function') result.push({ fn: el.onclick, el }); }
  return result;
}

function runDocument(html, label, requireArchitecture = true) {
  const architecture = requireArchitecture ? architectureOf(html) : 'legacy-embedded';
  if (architecture === 'malformed-current') return { ok: false, architecture, errors: ['current lesson references lesson-data but the required application/json block is missing'] };
  if (architecture === 'unknown') return { ok: false, architecture, errors: ['unrecognized or malformed lesson architecture'] };
  const data = html.match(/<script\b(?=[^>]*\bid=["']lesson-data["'])(?=[^>]*\btype=["']application\/json["'])[^>]*>([\s\S]*?)<\/script>/i);
  if (architecture === 'current-json') try { JSON.parse(data[1]); } catch (e) { return { ok: false, architecture, errors: [`invalid lesson-data JSON: ${e.message}`] }; }
  const scripts = scriptsOf(html);
  if (!scripts.length) return { ok: false, architecture, errors: ['no executable inline script block'] };
  const { document, store, makeEl } = mockDom(html, data ? data[1] : null);
  const sandbox = { document, localStorage: { getItem: () => null, setItem() {}, removeItem() {} }, console: { log() {}, warn() {}, error() {} }, alert() {}, confirm: () => true, setTimeout: fn => { if (typeof fn === 'function') fn(); return 1; }, clearTimeout() {}, requestAnimationFrame: fn => { if (typeof fn === 'function') fn(); return 1; }, addEventListener() {} };
  sandbox.window = sandbox;
  for (const [id, el] of Object.entries(store)) if (/^[A-Za-z_$][\w$]*$/.test(id)) sandbox[id] = el;
  const context = vm.createContext(sandbox); const errors = [];
  for (let i = 0; i < scripts.length; i++) try { vm.runInContext(scripts[i], context, { filename: `${label} script ${i + 1}` }); } catch (e) { errors.push(`boot (script ${i + 1}): ${e.message}`); return { ok: false, architecture, errors }; }
  for (const boot of document._boots) try { boot(); } catch (e) { errors.push(`boot (DOMContentLoaded): ${e.message}`); return { ok: false, architecture, errors }; }
  for (let round = 0; round < ROUNDS; round++) {
    const found = handlers(store); if (!found.length && round === 0) errors.push('no onclick handlers were found after boot');
    for (const h of found) {
      const clicked = h.el || makeEl(`_clicked_${round}`); const event = { stopPropagation() {}, preventDefault() {}, target: clicked };
      try {
        if (h.fn) h.fn.call(clicked, event);
        else { sandbox.__clickedEl__ = clicked; sandbox.__mockEvent__ = event; vm.runInContext(`(function(event){ ${decode(h.code)} }).call(__clickedEl__, __mockEvent__)`, context, { filename: `${label} onclick round ${round}` }); }
      } catch (e) { errors.push(`round ${round}, handler "${h.code || '[programmatic onclick]'}": ${e.message}`); }
    }
  }
  if (architecture === 'legacy-iframe-bundle') {
    let sources = [];
    try { sources = vm.runInContext(`lessons.map(x => x && x.src).filter(Boolean)`, context); } catch (e) { errors.push(`could not read iframe lesson sources: ${e.message}`); }
    if (!sources.length) errors.push('legacy iframe bundle did not expose lesson data URLs');
    sources.forEach((src, i) => {
      const match = /^data:text\/html;base64,([A-Za-z0-9+/=]+)$/.exec(src);
      if (!match) { errors.push(`iframe ${i + 1}: unsupported lesson source`); return; }
      const child = runDocument(Buffer.from(match[1], 'base64').toString('utf8'), `${label} iframe ${i + 1}`, false);
      child.errors.forEach(e => errors.push(`iframe ${i + 1}: ${e}`));
    });
  }
  return { ok: errors.length === 0, architecture, errors };
}

const files = process.argv.slice(2);
if (!files.length) { console.error('Usage: node ysp_functional_smoke_test.js <lesson-html-file> [more files...]'); process.exit(2); }
let failed = false;
console.log('='.repeat(60)); console.log('YSP Functional Smoke Test (runtime click simulation)'); console.log('='.repeat(60));
for (const file of files) {
  const result = runDocument(fs.readFileSync(file, 'utf8'), file);
  if (result.ok) console.log(`PASS ${file} [${result.architecture}] - clean across ${ROUNDS} rounds`);
  else if (result.architecture.startsWith('legacy-')) {
    console.log(`LEGACY WARNING ${file} [${result.architecture}] - runtime issue is non-blocking until legacy migration`);
    [...new Set(result.errors.map(e => e.replace(/^round \d+, /, 'round *, ')))].forEach(e => console.log(`   - ${e}`));
  }
  else { failed = true; console.log(`FAIL ${file} [${result.architecture}]`); result.errors.forEach(e => console.log(`   - ${e}`)); }
}
console.log('='.repeat(60)); process.exit(failed ? 1 : 0);
