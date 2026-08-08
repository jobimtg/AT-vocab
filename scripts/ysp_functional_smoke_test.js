#!/usr/bin/env node
/**
 * ysp_functional_smoke_test.js
 *
 * Runtime functional smoke test for YSP lesson HTML files. node --check only
 * catches SYNTAX errors; ysp_lesson_contract_check.py only checks static
 * structure/counts. Neither ever actually EXECUTES the interactive JS, so a
 * closure-scope bug like referencing a function-local `const p` inside an
 * onclick="" attribute (which runs in global scope at click-time, not the
 * function's scope at render-time) passed every existing check while being
 * completely broken in a real browser.
 *
 * This script builds a minimal in-memory DOM mock, boots the lesson exactly
 * as a browser would (DOMContentLoaded), then repeatedly HARVESTS every
 * onclick="..." handler currently present in any rendered element and
 * EXECUTES it — for several rounds, so state-dependent bugs (e.g. only
 * breaking after several clicks, or only breaking near an array boundary)
 * get exercised too. It does not hardcode which buttons exist, so it stays
 * useful as the UI evolves without needing to be manually updated.
 *
 * Usage: node ysp_functional_smoke_test.js <lesson-html-file> [more files...]
 * Exit code 0 = all files clean. Exit code 1 = at least one runtime error found.
 */
const fs = require('fs');
const path = require('path');

const ROUNDS = 8; // repeated harvest-and-click passes per lesson

function mockDom(lessonDataText) {
  const store = {}; // id -> mock element
  function makeClassList() {
    const set = new Set();
    return {
      toggle(name, force) {
        if (force === undefined) { set.has(name) ? set.delete(name) : set.add(name); }
        else if (force) set.add(name); else set.delete(name);
        return set.has(name);
      },
      add(name) { set.add(name); },
      remove(name) { set.delete(name); },
      contains(name) { return set.has(name); },
    };
  }
  function makeEl(id) {
    if (store[id]) return store[id];
    const el = {
      id,
      _innerHTML: '',
      style: {},
      textContent: '',
      classList: makeClassList(),
      dataset: {},
      children: [],
      setAttribute() {},
      getAttribute() { return null; },
      removeAttribute() {},
      addEventListener() {},
      // A generic sibling stub so `this.nextElementSibling.classList.toggle(...)`
      // (used by dialogue "Teacher notes" toggles, accordion headers, etc.)
      // exercises real toggle logic instead of throwing on a null sibling.
      get nextElementSibling() { return makeEl('_sibling_of_' + id); },
      querySelector() { return null; },
      querySelectorAll() { return []; },
      get innerHTML() { return this._innerHTML; },
      set innerHTML(v) { this._innerHTML = v; },
    };
    store[id] = el;
    return el;
  }
  const documentMock = {
    getElementById(id) {
      if (id === 'lesson-data') return { textContent: lessonDataText };
      return makeEl(id);
    },
    querySelectorAll() { return []; },
    querySelector() { return null; },
    addEventListener(evt, fn) {
      // Real browsers fire DOMContentLoaded once the script has finished
      // parsing; simulate that immediately so the lesson actually boots.
      if (evt === 'DOMContentLoaded') {
        documentMock._pendingBoot = fn;
      }
    },
    createElement() { return makeEl('_tmp_' + Math.random()); },
    body: makeEl('body'),
  };
  return { documentMock, store, makeEl };
}

function harvestOnclicks(store) {
  const found = [];
  const re = /onclick="([^"]*)"/g;
  for (const id of Object.keys(store)) {
    const html = store[id]._innerHTML || '';
    let m;
    const localRe = new RegExp(re);
    while ((m = localRe.exec(html))) {
      found.push(m[1]);
    }
  }
  return found;
}

function decodeHtmlEntities(s) {
  return s
    .replace(/&#39;/g, "'")
    .replace(/&quot;/g, '"')
    .replace(/&amp;/g, '&');
}

function testFile(filePath) {
  const html = fs.readFileSync(filePath, 'utf8');
  const dataMatch = html.match(/<script id="lesson-data" type="application\/json">([\s\S]*?)<\/script>/);
  const scriptMatches = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)]
    .filter(([, attrs]) => !/id="lesson-data"/.test(attrs) && !/src=/.test(attrs));
  if (!dataMatch || scriptMatches.length === 0) {
    return { file: filePath, ok: false, errors: ['could not locate lesson-data or main script block'] };
  }
  const jsBody = scriptMatches[scriptMatches.length - 1][2];
  const { documentMock, store, makeEl } = mockDom(dataMatch[1]);

  const errors = [];
  const sandbox = {
    document: documentMock,
    localStorage: { getItem: () => null, setItem() {}, removeItem() {} },
    console: { log() {}, warn() {}, error() {} },
    window: {},
    alert() {},
    // Reset Progress and similar guarded actions call confirm(); default to
    // accepting so that code path gets exercised too, not skipped.
    confirm: () => true,
  };
  const context = require('vm').createContext(sandbox);

  try {
    require('vm').runInContext(jsBody, context, { filename: path.basename(filePath) });
  } catch (e) {
    errors.push('boot (initial script execution): ' + e.message);
    return { file: filePath, ok: false, errors };
  }

  if (typeof documentMock._pendingBoot === 'function') {
    try {
      documentMock._pendingBoot();
    } catch (e) {
      errors.push('boot (DOMContentLoaded handler): ' + e.message);
      return { file: filePath, ok: false, errors };
    }
  }

  // Repeatedly harvest and execute every onclick handler currently rendered.
  // Each handler is wrapped as `function(){ <code> }` and called with a
  // generic clicked-element as `this` (matching real DOM onclick semantics)
  // plus a fresh mock `event` object in scope, so patterns like
  // `this.classList.toggle('fl')` and `event.stopPropagation()` — both
  // extremely common in this codebase — exercise real logic instead of
  // producing mock-artifact false positives that would drown out real bugs.
  for (let round = 0; round < ROUNDS; round++) {
    const handlers = harvestOnclicks(store);
    for (const raw of handlers) {
      const code = decodeHtmlEntities(raw);
      const clickedEl = makeEl('_clicked_' + Math.random());
      const wrapped = `(function(event){ ${code} }).call(__clickedEl__, __mockEvent__)`;
      sandbox.__clickedEl__ = clickedEl;
      sandbox.__mockEvent__ = { stopPropagation() {}, preventDefault() {}, target: clickedEl };
      try {
        require('vm').runInContext(wrapped, context, { filename: `${path.basename(filePath)} onclick round ${round}` });
      } catch (e) {
        errors.push(`round ${round}, handler "${code}": ${e.message}`);
      }
    }
    if (handlers.length === 0 && round === 0) {
      errors.push('no onclick handlers were ever rendered — check that DOMContentLoaded actually fired');
    }
  }

  return { file: filePath, ok: errors.length === 0, errors };
}

const files = process.argv.slice(2);
if (files.length === 0) {
  console.error('Usage: node ysp_functional_smoke_test.js <lesson-html-file> [more files...]');
  process.exit(2);
}

let anyFail = false;
console.log('='.repeat(60));
console.log('YSP Functional Smoke Test (runtime click simulation)');
console.log('='.repeat(60));
for (const f of files) {
  const result = testFile(f);
  if (result.ok) {
    console.log(`✅ ${f} — clean across ${ROUNDS} rounds of click simulation`);
  } else {
    anyFail = true;
    console.log(`❌ ${f}`);
    for (const err of result.errors) console.log('   - ' + err);
  }
}
console.log('='.repeat(60));
process.exit(anyFail ? 1 : 0);
