/*
  Page behaviour, ported from the canvas scripts:
  scroll reveals, header (promo bar, sticky state, dropdown, mobile menu, call bar),
  the enquiry drawer, review rail and grid, and the homepage odometer, situations and steps.
  Everything respects prefers-reduced-motion.
*/
(function () {
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const reduce = (() => { try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } })();

  // ---------- scroll reveals (harlowReveal) ----------
  (function reveal() {
    if (!('IntersectionObserver' in window)) return;
    const root = document.documentElement;
    root.classList.add('js-rv');
    const sel = '.rv:not(.in), .ul:not(.in)';
    const io = new IntersectionObserver((ents) => ents.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });
    const seen = new WeakSet();
    const scan = () => $$(sel).forEach((el) => { if (!seen.has(el)) { seen.add(el); io.observe(el); } });
    const fallback = () => { const h = window.innerHeight || 800; $$(sel).forEach((el) => { if (el.getBoundingClientRect().top < h * 0.96) el.classList.add('in'); }); };
    let t = 0;
    new MutationObserver(() => { clearTimeout(t); t = setTimeout(scan, 40); }).observe(document.body, { childList: true, subtree: true });
    window.addEventListener('scroll', fallback, { passive: true });
    window.addEventListener('beforeprint', () => $$(sel).forEach((el) => el.classList.add('in')));
    scan(); setTimeout(fallback, 900); setTimeout(fallback, 2500);
  })();

  // ---------- enquiry drawer ----------
  const drawer = $('[data-drawer]');
  let drawerOpen = false; let lastFocus = null;
  const FOCUSABLE = '.drawer a[href], .drawer button:not([disabled]), .drawer input, .drawer select, .drawer textarea, .drawer [tabindex]:not([tabindex="-1"])';
  function openDrawer(prefill) {
    if (!drawer) return;
    let defaults = {};
    try { defaults = JSON.parse(drawer.dataset.defaults || '{}'); } catch (e) { /* none */ }
    const q = Object.assign({}, prefill || {});
    if (!q.situation) delete q.situation;
    lastFocus = document.activeElement;
    window.HarlowForm.reset($('[data-enquiry-form]', drawer), Object.assign({}, defaults, q));
    drawer.hidden = false; drawerOpen = true;
    document.documentElement.style.overflow = 'hidden';
    setMenu(false); setDd(false); syncBar();
    setTimeout(() => { const el = $('.drawer button:not([tabindex="-1"]), .drawer input', drawer); if (el) el.focus({ preventScroll: true }); }, 30);
  }
  function closeDrawer() {
    if (!drawerOpen) return;
    drawer.hidden = true; drawerOpen = false;
    document.documentElement.style.overflow = '';
    syncBar();
    if (lastFocus && lastFocus !== document.body && typeof lastFocus.focus === 'function' && document.contains(lastFocus)) lastFocus.focus({ preventScroll: true });
    else if (drawer.contains(document.activeElement)) document.activeElement.blur();
  }
  window.HarlowOpen = openDrawer;
  document.addEventListener('click', (e) => {
    const el = e.target.closest('[data-enquire]');
    if (!el) return;
    e.preventDefault();
    let prefill = {};
    try { prefill = JSON.parse(el.dataset.enquire || '{}'); } catch (err) { /* keep blank */ }
    openDrawer(prefill);
  });
  if (drawer) {
    $$('[data-close]', drawer).forEach((b) => b.addEventListener('click', closeDrawer));
    drawer.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') { e.stopPropagation(); closeDrawer(); return; }
      if (e.key !== 'Tab') return;
      const list = $$(FOCUSABLE, drawer).filter((el) => el.offsetParent !== null || el === document.activeElement);
      if (!list.length) return;
      const first = list[0]; const last = list[list.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  }

  // ---------- header ----------
  const hdr = $('[data-hdr]');
  const pill = $('[data-pill]');
  const bar = $('[data-callbar]');
  let past = false; let barOn = false; let menuOpen = false;

  const promo = $('[data-promo]');
  try { if (sessionStorage.getItem('harlow-promo') === 'x' && promo) promo.remove(); } catch (e) { /* storage blocked */ }
  const promoX = promo && $('[data-promo-x]', promo);
  if (promoX) promoX.addEventListener('click', () => { try { sessionStorage.setItem('harlow-promo', 'x'); } catch (e) { /* storage blocked */ } promo.remove(); });

  function syncBar() {
    if (!bar) return;
    const show = barOn && !drawerOpen && !menuOpen;
    if (show && bar.hidden) { bar.hidden = false; bar.style.animation = 'heroUp .35s cubic-bezier(.2,.7,.2,1) both'; bar.classList.add('show'); }
    else if (!show && !bar.hidden) { bar.hidden = true; bar.classList.remove('show'); }
  }
  function onScroll() {
    const y = window.scrollY || 0;
    const hero = document.getElementById('hero');
    const p = hero ? hero.getBoundingClientRect().bottom < 80 : y > 260;
    if (p !== past) { past = p; hdr.classList.toggle('is-past', p); pill.tabIndex = p ? 0 : -1; }
    const b = y > 300;
    if (b !== barOn) { barOn = b; syncBar(); }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  onScroll();

  const dd = $('[data-dd]');
  const ddBtn = $('[data-dd-btn]');
  const panel = $('#buying-panel');
  function setDd(on) { if (!panel) return; panel.hidden = !on; ddBtn.setAttribute('aria-expanded', String(on)); }
  ddBtn.addEventListener('click', () => setDd(panel.hidden));
  dd.addEventListener('mouseleave', () => { if (!panel.hidden) setDd(false); });
  dd.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !panel.hidden) { setDd(false); ddBtn.focus(); } });
  dd.addEventListener('focusout', () => setTimeout(() => { if (!dd.contains(document.activeElement) && !panel.hidden) setDd(false); }, 0));

  const menuBtn = $('[data-menu-btn]');
  const mnav = $('#mobile-nav');
  function setMenu(on) {
    menuOpen = on; mnav.hidden = !on;
    menuBtn.setAttribute('aria-expanded', String(on));
    menuBtn.setAttribute('aria-label', on ? 'Close menu' : 'Open menu');
    $('[data-ic-close]', menuBtn).toggleAttribute('hidden', !on);
    $('[data-ic-open]', menuBtn).toggleAttribute('hidden', on);
    syncBar();
  }
  menuBtn.addEventListener('click', () => setMenu(!menuOpen));

  // ---------- reviews: rail arrows and grid filters ----------
  $$('[data-reviews="rail"]').forEach((root) => {
    const rail = $('[data-rail]', root); const prev = $('[data-prev]', root); const next = $('[data-next]', root);
    const measure = () => { prev.disabled = rail.scrollLeft <= 4; next.disabled = rail.scrollLeft + rail.clientWidth >= rail.scrollWidth - 4; };
    const by = (dir) => {
      const card = $('.rcard:not(.big)', rail) || $('.rcard', rail);
      const w = card ? card.getBoundingClientRect().width + 16 : 340;
      rail.scrollBy({ left: dir * w, behavior: reduce ? 'auto' : 'smooth' });
    };
    rail.addEventListener('scroll', measure, { passive: true });
    window.addEventListener('resize', measure, { passive: true });
    prev.addEventListener('click', () => by(-1));
    next.addEventListener('click', () => by(1));
    rail.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') { e.preventDefault(); by(1); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); by(-1); }
    });
    setTimeout(measure, 60);
  });
  $$('[data-reviews="grid"]').forEach((root) => {
    const chips = $$('[data-filter]', root);
    chips.forEach((chip) => chip.addEventListener('click', () => {
      const f = chip.dataset.filter || '';
      chips.forEach((c) => c.setAttribute('aria-pressed', String(c === chip)));
      $$('.rcard', root).forEach((card) => { card.hidden = !!f && card.dataset.sit !== f; });
    }));
  });

  // ---------- homepage: odometer ----------
  const odoRoot = $('[data-odo-root]');
  if (odoRoot) {
    const out = $('[data-odo]', odoRoot); const target = Number(odoRoot.dataset.target) || 0;
    const show = (v) => { out.textContent = '$' + v + 'm'; };
    let stop = false;
    const finish = () => { stop = true; show(target); };
    odoRoot.addEventListener('mouseenter', finish);
    odoRoot.addEventListener('focusin', finish);
    if (reduce) show(target);
    else {
      show(0);
      const t0 = performance.now() + 500; const dur = 1600;
      const tick = (now) => {
        if (stop) return;
        if (document.hidden) { finish(); return; }
        const p = Math.max(0, Math.min(1, (now - t0) / dur)); const e = 1 - Math.pow(1 - p, 3);
        show(Math.round(target * e));
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    }
  }

  // ---------- homepage: situations photo crossfade ----------
  const sit = $('[data-sit]');
  if (sit) {
    const rows = $$('.sit-row', sit); const imgs = $$('.sit-photo > *', sit);
    const pick = (i) => { rows.forEach((r, k) => r.classList.toggle('on', k === i)); imgs.forEach((m, k) => m.classList.toggle('on', k === i)); };
    rows.forEach((r, i) => { r.addEventListener('mouseenter', () => pick(i)); r.addEventListener('focus', () => pick(i)); });
  }

  // ---------- homepage: "How we work" steps ----------
  const how = $('[data-steps]');
  if (how) {
    const list = $('.step-list', how); const btns = $$('.step', list); const imgs = $$('.step-photo > *', how);
    let step = 0; let hover = false; let focus = false; let offscreen = false; let hidden = document.hidden;
    const progCls = () => 'prog' + (reduce ? ' still' : (hover || focus || offscreen || hidden) ? ' paused' : '');
    const syncProg = () => btns.forEach((b) => { const p = $('.prog', b); if (p) p.className = progCls(); });
    const render = () => {
      btns.forEach((b, i) => {
        const on = i === step;
        b.setAttribute('aria-expanded', String(on));
        $$('.step-b, .prog', b).forEach((el) => { el.hidden = !on; });
      });
      imgs.forEach((m, i) => m.classList.toggle('on', i === step));
      syncProg();
    };
    const go = (n) => { step = (n + btns.length) % btns.length; render(); };
    btns.forEach((b, i) => {
      b.addEventListener('click', () => go(i));
      $('.prog i', b).addEventListener('animationend', () => { if (!reduce && i === step) go(step + 1); });
    });
    list.addEventListener('mouseenter', () => { hover = true; syncProg(); });
    list.addEventListener('mouseleave', () => { hover = false; syncProg(); });
    list.addEventListener('focusin', () => { focus = true; syncProg(); });
    list.addEventListener('focusout', () => setTimeout(() => { if (!list.contains(document.activeElement)) { focus = false; syncProg(); } }, 0));
    list.addEventListener('keydown', (e) => {
      const k = e.key;
      if (!['ArrowDown', 'ArrowUp', 'ArrowRight', 'ArrowLeft', 'Home', 'End'].includes(k)) return;
      e.preventDefault();
      let n = step;
      if (k === 'ArrowDown' || k === 'ArrowRight') n = step + 1;
      if (k === 'ArrowUp' || k === 'ArrowLeft') n = step - 1;
      if (k === 'Home') n = 0;
      if (k === 'End') n = btns.length - 1;
      go(n); btns[step].focus();
    });
    document.addEventListener('visibilitychange', () => { hidden = document.hidden; syncProg(); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver((ents) => ents.forEach((e) => { offscreen = !e.isIntersecting; syncProg(); }), { threshold: 0.2 }).observe(how);
    }
    render();
  }
})();
