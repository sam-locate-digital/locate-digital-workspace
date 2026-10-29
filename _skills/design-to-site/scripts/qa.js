/*
  QA for a demo site: full-page screenshots, overflow, overlap, console errors, broken images,
  keyboard and drawer behaviour, and prefers-reduced-motion.

    node qa.js <base-url> <site-dir> <out-dir>
    e.g. node qa.js http://localhost:5173/mortgage-broker/ "G:/.../demos/mortgage-broker" "G:/.../demos/mortgage-broker/checks"

  Needs playwright-core installed next to this script's working copy (see SKILL.md) and Google Chrome.
  Every page = every *.html in <site-dir> except 404.html. Writes <page>-390.png, <page>-1440.png and issues.txt.
  Behaviour tests only run when the page has the matching element, so they're safe on any demo.
*/
const { chromium } = require('playwright-core');
const fs = require('fs');
const path = require('path');

const [BASE, SITE, OUT] = process.argv.slice(2);
if (!BASE || !SITE || !OUT) { console.error('usage: node qa.js <base-url> <site-dir> <out-dir>'); process.exit(1); }
const CHROME = ['C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'].find((p) => fs.existsSync(p));
const PAGES = fs.readdirSync(SITE).filter((f) => f.endsWith('.html') && f !== '404.html').map((f) => f.replace(/\.html$/, '')).sort();
const issues = [];
const note = (m) => { issues.push(m); console.log('ISSUE', m); };
const has = (page, sel) => page.evaluate((s) => !!document.querySelector(s), sel);

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ executablePath: CHROME });

  // 1. Every page at 390 and 1440: screenshot, overflow, overlap, errors, broken images
  for (const w of [390, 1440]) {
    const ctx = await browser.newContext({ viewport: { width: w, height: w < 768 ? 844 : 900 } });
    for (const p of PAGES) {
      const page = await ctx.newPage();
      const errs = [];
      page.on('console', (m) => { if (m.type() === 'error') errs.push(m.text()); });
      page.on('requestfailed', (r) => errs.push('failed ' + r.url()));
      page.on('response', (r) => { if (r.status() >= 400 && !r.url().endsWith('favicon.ico')) errs.push(r.status() + ' ' + r.url()); });
      await page.goto(BASE + (p === 'index' ? '' : p + '.html'), { waitUntil: 'networkidle' });
      // Smooth scrolling stops lazy images loading during a fast scroll, so turn it off and load everything.
      await page.evaluate(async () => {
        document.documentElement.style.scrollBehavior = 'auto';
        document.querySelectorAll('img[loading="lazy"]').forEach((i) => { i.loading = 'eager'; });
        for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 40)); }
        document.querySelectorAll('.rv, .ul').forEach((el) => el.classList.add('in'));
        await Promise.all([...document.images].map((i) => (i.complete ? 0 : new Promise((r) => { i.onload = i.onerror = r; }))));
        const broken = [...document.images].filter((i) => !i.naturalWidth).map((i) => i.src);
        if (broken.length) console.error('broken images: ' + broken.join(', '));
        window.scrollTo(0, 0);
      });
      await page.waitForTimeout(1300);
      const res = await page.evaluate(() => {
        const vw = document.documentElement.clientWidth;
        const over = document.documentElement.scrollWidth - vw;
        // Content inside a clipped or scrollable box (carousels, photo frames) is meant to extend past the edge.
        const clipped = (e) => { for (let p = e.parentElement; p && p !== document.body; p = p.parentElement) { if (getComputedStyle(p).overflowX !== 'visible') return true; } return false; };
        const out = [...document.querySelectorAll('main *, header *, footer *')].filter((e) => {
          if (e.closest('[hidden], .sr, .skip') || clipped(e)) return false;
          const b = e.getBoundingClientRect(); return b.width && (b.right > vw + 1 || b.left < -1);
        }).slice(0, 4).map((e) => e.tagName.toLowerCase() + '.' + String(e.className.baseVal ?? e.className).split(' ')[0]);
        const overlaps = [];
        document.querySelectorAll('main h1, main h2, main h3, main p, main .btn, main li').forEach((a) => {
          const sib = a.nextElementSibling; if (!sib || a.closest('[hidden]')) return;
          if (getComputedStyle(sib).position === 'absolute' || getComputedStyle(a).position === 'absolute') return;
          const r1 = a.getBoundingClientRect(); const r2 = sib.getBoundingClientRect();
          if (!r1.height || !r2.height) return;
          const ix = Math.min(r1.right, r2.right) - Math.max(r1.left, r2.left); const iy = Math.min(r1.bottom, r2.bottom) - Math.max(r1.top, r2.top);
          if (ix > 4 && iy > 4) overlaps.push(a.tagName.toLowerCase() + ' / ' + sib.tagName.toLowerCase() + ' "' + a.textContent.trim().slice(0, 30) + '"');
        });
        const missing = document.querySelectorAll('[data-missing-photo]').length;
        return { over, out, overlaps: overlaps.slice(0, 3), missing };
      });
      if (res.over > 0 || res.out.length) note(`${p}@${w}: overflow ${res.over}px ${res.out.join(', ')}`);
      if (res.overlaps.length) note(`${p}@${w}: overlap ${res.overlaps.join(' | ')}`);
      if (res.missing && w === 1440) note(`${p}: ${res.missing} photo(s) still missing (pale-blue boxes)`);
      if (errs.length) note(`${p}@${w}: ${[...new Set(errs)].join(' ; ')}`);
      await page.screenshot({ path: path.join(OUT, `${p}-${w}.png`), fullPage: true });
      await page.close();
    }
    await ctx.close();
    console.log(`screenshots done at ${w} (${PAGES.length} pages)`);
  }

  // 2. Keyboard on the homepage
  {
    const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
    const page = await ctx.newPage();
    await page.goto(BASE, { waitUntil: 'networkidle' });
    await page.keyboard.press('Tab');
    const first = await page.evaluate(() => ({ text: document.activeElement.textContent.trim(), outline: getComputedStyle(document.activeElement).outlineStyle }));
    if (!/skip/i.test(first.text)) note(`keyboard: first Tab stop is "${first.text}", not a skip link`);
    if (first.outline === 'none') note('keyboard: no visible focus outline on the first Tab stop');

    const opener = (await has(page, '.hdr-book')) ? '.hdr-book' : '[data-enquire]';
    if (await has(page, '[data-drawer]') && await has(page, opener)) {
      await page.locator(opener).first().focus(); await page.keyboard.press('Enter'); await page.waitForTimeout(200);
      let escaped = 0;
      for (let i = 0; i < 40; i++) { await page.keyboard.press('Tab'); if (!(await page.evaluate(() => !!document.activeElement.closest('[data-drawer]')))) escaped++; }
      for (let i = 0; i < 10; i++) { await page.keyboard.press('Shift+Tab'); if (!(await page.evaluate(() => !!document.activeElement.closest('[data-drawer]')))) escaped++; }
      if (escaped) note(`drawer: focus left the drawer ${escaped} times while tabbing`);
      await page.keyboard.press('Escape'); await page.waitForTimeout(100);
      const after = await page.evaluate(() => ({ hidden: document.querySelector('[data-drawer]').hidden, inDrawer: !!document.activeElement.closest('[data-drawer]') }));
      if (!after.hidden) note('drawer: Esc did not close it');
      if (after.inDrawer) note('drawer: focus stayed inside the closed drawer');
    }
    if (await has(page, '[data-dd-btn]')) {
      await page.locator('[data-dd-btn]').focus(); await page.keyboard.press('Enter');
      const opened = await page.evaluate(() => document.querySelector('[data-dd-btn]').getAttribute('aria-expanded') === 'true');
      await page.keyboard.press('Escape');
      const closed = await page.evaluate(() => document.querySelector('[data-dd-btn]').getAttribute('aria-expanded') === 'false');
      if (!opened || !closed) note('dropdown: Enter/Esc did not open and close it');
    }
    if (await has(page, '.step-list .step')) {
      await page.locator('.step').first().focus(); await page.keyboard.press('ArrowDown');
      const on = await page.evaluate(() => [...document.querySelectorAll('.step')].findIndex((b) => b.getAttribute('aria-expanded') === 'true'));
      if (on !== 1) note('steps: ArrowDown did not move to the next step');
    }
    if (await has(page, 'details[name] summary')) {
      await page.locator('details[name] summary').nth(1).click();
      const open = await page.evaluate(() => document.querySelectorAll('details[name][open]').length);
      if (open > 1) note(`faq: ${open} answers open at once`);
    }
    await ctx.close();
    console.log('keyboard checks done');
  }

  // 3. Reduced motion on the homepage
  {
    const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' });
    const page = await ctx.newPage();
    await page.goto(BASE, { waitUntil: 'networkidle' });
    const r = await page.evaluate(() => ({
      odo: document.querySelector('[data-odo]')?.textContent || null,
      target: document.querySelector('[data-odo-root]')?.dataset.target || null,
      // A progress bar counts as still if neither it nor its fill has a running animation.
      progMoving: [...document.querySelectorAll('.prog, .prog *')].some((e) => { const s = getComputedStyle(e); return s.animationName !== 'none' && parseFloat(s.animationDuration) > 0.01 && s.animationPlayState === 'running'; }),
      hiddenReveals: [...document.querySelectorAll('.rv')].filter((e) => getComputedStyle(e).opacity !== '1').length,
      heroAnim: (() => { const h = document.querySelector('.hero-in'); return h ? parseFloat(getComputedStyle(h).animationDuration) : 0; })(),
    }));
    if (r.odo && r.target && !r.odo.includes(r.target)) note(`reduced motion: odometer shows ${r.odo}, not its end value`);
    if (r.progMoving) note('reduced motion: step progress bar is still animating');
    if (r.hiddenReveals) note(`reduced motion: ${r.hiddenReveals} reveal elements not fully visible`);
    if (r.heroAnim > 0.01) note(`reduced motion: hero animation still runs (${r.heroAnim}s)`);
    if (await has(page, '.step-list .step')) {
      await page.evaluate(() => document.querySelector('.step-list').scrollIntoView());
      await page.waitForTimeout(6000);
      const step = await page.evaluate(() => [...document.querySelectorAll('.step')].findIndex((b) => b.getAttribute('aria-expanded') === 'true'));
      if (step !== 0) note('reduced motion: steps auto-advanced');
    }
    await page.screenshot({ path: path.join(OUT, 'index-reduced-motion-1440.png') });
    await ctx.close();
    console.log('reduced motion checks done');
  }

  await browser.close();
  fs.writeFileSync(path.join(OUT, 'issues.txt'), issues.join('\n') || 'No issues found.');
  console.log(`\n${issues.length} issue(s). Screenshots and issues.txt in ${OUT}`);
})();
