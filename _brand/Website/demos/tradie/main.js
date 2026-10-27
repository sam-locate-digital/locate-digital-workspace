/*
  Shared behaviour for every page: header and mega panel, footer, promo bar,
  mobile call bar, booking drawer and form, hero search, reviews carousel,
  how-it-works stepper, FAQ, suburb checker and scroll reveals.

  Business details come from config.js and reviews from reviews.json. Each
  page says what it is on <body>: data-page (home, hub, service, suburb,
  landlords, reviews, about, emergency, book, thanks, legal) and, where it
  applies, data-slug.
*/
(() => {
  'use strict';

  const C = window.CONFIG;
  const ROOT = ((document.currentScript && document.currentScript.src) || '').replace(/[^/]*$/, '');
  const PAGE = document.body.dataset.page || 'home';
  const SLUG = document.body.dataset.slug || '';
  const site = document.querySelector('.site');

  // ---------- helpers ----------
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const esc = (v) => String(v == null ? '' : v).replace(/[&<>"']/g, (ch) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch]));
  const url = (p) => ROOT + p;
  const slugify = (s) => String(s).toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  const suburbFromSlug = (slug) => C.suburbs.find((s) => slugify(s) === slug) || null;
  const matchSuburb = (v) => {
    const t = String(v || '').toLowerCase().replace(/,/g, ' ').replace(/\b(vic|victoria)\b/g, '').replace(/\b3\d{3}\b/g, '').replace(/\s+/g, ' ').trim();
    if (!t) return null;
    return C.suburbs.find((s) => s.toLowerCase() === t) || null;
  };
  const digits = (v) => { let d = String(v || '').replace(/[^\d+]/g, ''); if (d.indexOf('+61') === 0) d = '0' + d.slice(3); else if (d.indexOf('61') === 0 && d.length === 11) d = '0' + d.slice(2); return d; };
  const validMobile = (v) => /^04\d{8}$/.test(digits(v));
  const fmtMobile = (v) => { const d = digits(v); return /^04\d{8}$/.test(d) ? d.slice(0, 4) + ' ' + d.slice(4, 7) + ' ' + d.slice(7) : v; };
  const todayStr = () => { const d = new Date(); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); };
  const reduced = () => { try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } };
  const mixDark = (hex, t) => {
    const n = parseInt(hex.slice(1), 16);
    return '#' + [(n >> 16) & 255, (n >> 8) & 255, n & 255].map((x) => Math.round(x * (1 - t)).toString(16).padStart(2, '0')).join('');
  };
  const focusEl = (el) => { if (!el) return; try { el.focus({ preventScroll: true }); } catch (e) { el.focus(); } };
  const session = {
    get(k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }
  };

  // ---------- trades and display values ----------
  const trades = C.trades && C.trades.length ? C.trades : ['plumbing', 'electrical'];
  const showPl = trades.indexOf('plumbing') > -1, showEl = trades.indexOf('electrical') > -1, both = showPl && showEl;
  const showPh = C.showPlaceholders !== false;
  const jobsForTrades = () => C.jobs.filter((j) => trades.indexOf(j.t) > -1).map((j) => j.v);

  const c = {
    name: C.brand.name, phone: C.contact.phone, tel: C.contact.phone.replace(/[^\d+]/g, ''), email: C.contact.email,
    baseSuburb: C.address.suburb, base: [C.address.suburb, C.address.state, C.address.postcode].join(' '), street: C.address.street,
    weekdays: C.hours.weekdays, emergency: C.hours.emergency, promo: C.promo,
    rating: String(C.stats.rating), reviewCount: C.stats.reviewCount.toLocaleString('en-AU'), jobsDoneFmt: C.stats.jobsDone.toLocaleString('en-AU'),
    founded: String(C.brand.founded), responseTime: C.responseTime, guarantee: String(C.guaranteeYears),
    licPlumbing: C.licences.plumbing, licRec: C.licences.rec, licAbn: C.licences.abn, licInsurance: C.licences.insurance,
    tradeNoun: both ? 'Plumbers and electricians' : showPl ? 'Plumbers' : 'Electricians',
    licensedLine: both ? 'Licensed plumbers and electricians' : showPl ? 'Licensed plumbers and gas fitters' : 'Licensed electricians',
    year: String(new Date().getFullYear())
  };
  const reviewSource = showPh ? 'Sample review' : 'Google review';

  // ---------- links ----------
  const hrefFor = (page, slug) => {
    if (page === 'home') return url('');
    if (page === 'hub' || page === 'legal') return url(slug + '.html');
    if (page === 'service') return url(((C.servicePages[slug] || {}).trade || 'plumbing') + '/' + slug + '.html');
    if (page === 'suburb') return url('areas/' + slug + '.html');
    return url(page + '.html');
  };
  const svcLink = (s, trade) => {
    const href = s.page ? hrefFor('service', s.page) : s.emergency ? hrefFor('emergency') : hrefFor('hub', trade);
    return { name: s.name, desc: s.desc, href };
  };
  const svcLinks = (t) => C.services[t].map((s) => svcLink(s, t));
  const spTrade = PAGE === 'service' ? (C.servicePages[SLUG] || {}).trade : null;
  const isCurrent = {
    plumbing: (PAGE === 'hub' && SLUG === 'plumbing') || spTrade === 'plumbing',
    electrical: (PAGE === 'hub' && SLUG === 'electrical') || spTrade === 'electrical',
    landlords: PAGE === 'landlords', reviews: PAGE === 'reviews', about: PAGE === 'about'
  };

  // ---------- icons ----------
  const svg = (size, sw, paths, opts = {}) => '<svg' + (opts.cls ? ' class="' + opts.cls + '"' : '') + ' width="' + size + '" height="' + size + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="' + sw + '" stroke-linecap="round"' + (opts.round === false ? '' : ' stroke-linejoin="round"') + ' aria-hidden="true">' + paths + '</svg>';
  const PHONE = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"></path>';
  const I = {
    arrow: (s, sw, cls) => svg(s, sw, '<path d="M5 12h14M13 6l6 6-6 6"></path>', { cls }),
    chevron: (s, sw) => svg(s, sw, '<path d="m6 9 6 6 6-6"></path>'),
    close: (s, sw) => svg(s, sw, '<path d="M18 6 6 18M6 6l12 12"></path>', { round: false }),
    menu: () => svg(22, 1.6, '<path d="M4 7h16M4 12h16M4 17h16"></path>', { round: false }),
    search: () => svg(18, 1.5, '<circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path>', { round: false }),
    phone: (s, sw) => svg(s, sw, PHONE),
    check: (s, sw) => svg(s, sw, '<path d="M20 6 9 17l-5-5"></path>'),
    alert: () => svg(18, 1.8, '<circle cx="12" cy="12" r="9"></circle><path d="M12 8v5M12 16.5v.01"></path>', { round: false }),
    upload: () => svg(22, 1.5, '<path d="M12 16V4M7 9l5-5 5 5"></path><path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"></path>'),
    plus: () => svg(22, 1.5, '<path d="M12 5v14M5 12h14"></path>', { cls: 'faq-icon', round: false }),
    star: (s) => '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4l-5.9 3.1 1.2-6.5L2.5 9.4l6.6-.9z" fill="currentColor"></path></svg>'
  };

  // ---------- template copy (same for every tradie) ----------
  const STEPS = [
    { title: "Tell us what's wrong", body: 'Book online or call. Tell us the problem and when suits.', img: 'images/step-1.webp', alt: 'Homeowner booking a plumber on her phone' },
    { title: 'We confirm by text', body: "You'll get a booking text, and another when we're 30 minutes away.", img: 'images/step-2.webp', alt: 'Work ute parked outside an Edwardian home' },
    { title: 'We explain before we start', body: "We look at the problem, talk you through the options in plain English and only start once you're happy.", img: 'images/step-3.webp', alt: 'Tradie talking a couple through the job on a tablet' },
    { title: 'Fixed, cleaned up, explained', body: 'We clean up, walk you through what we did and send photos with the invoice.', img: 'images/step-4.webp', alt: 'Tradie wiping down the bench after finishing' }
  ];

  const WHY = [
    { h: 'Explained in plain English.', b: "We tell you what's wrong and what your options are before we start." },
    { h: 'On time, or we tell you first.', b: "A text when we're booked and another when we're 30 minutes away." },
    { ph: c.guarantee, h: '-year workmanship guarantee.', b: 'If our work fails, we come back and fix it.' },
    { h: 'Licensed, insured, local.', b: (both ? 'Every plumber and electrician' : showPl ? 'Every plumber' : 'Every electrician') + ' is licensed and based in the east.' },
    { h: 'We leave it cleaner.', b: 'Drop sheets down, mess gone, a walk-through before we leave.' },
    { h: 'Built for landlords too.', b: 'We deal with tenants directly and send photos and invoices to you.' }
  ];

  const FAQ = [
    { q: 'How quickly can you come out?', a: "Most call-outs are booked same day or next day. We text you a time, then again when we're 30 minutes away." },
    { q: 'Will you explain what needs doing first?', a: "Yes. We look, talk you through the options in plain English and only start once you're happy. If we find something else, we stop and ask." },
    { q: both ? 'Can you do plumbing and electrical in one visit?' : 'Can you do everything in one visit?', a: both ? 'Yes. One booking, one quote, one invoice.' : 'Most jobs, yes. One booking, one quote, one invoice.' },
    { q: 'Do you work with landlords and property managers?', a: 'Yes. We contact tenants directly and send you photos, invoices and compliance certificates.' },
    { q: 'Are you licensed?', a: 'Yes, every tradesperson is licensed and insured. Licence numbers are in the footer.' },
    { q: 'Do you do emergencies?', a: 'Yes, 24/7 for burst pipes, gas leaks, no hot water and power faults. Call ' + c.phone + '.' }
  ];

  // ---------- page shell ----------
  function applyBrand() {
    let a = String(C.accent || '#1F45D6');
    if (!/^#[0-9a-f]{6}$/i.test(a)) a = '#1F45D6';
    const ac = a.toUpperCase() === '#1F45D6'
      ? { a: '#1F45D6', h: '#1633A6', act: '#1A3CC4', b: '#1229B8' }
      : { a, h: mixDark(a, 0.22), act: mixDark(a, 0.1), b: mixDark(a, 0.18) };
    site.style.setProperty('--accent', ac.a);
    site.style.setProperty('--accent-hover', ac.h);
    site.style.setProperty('--accent-active', ac.act);
    site.style.setProperty('--accent-bevel', ac.b);
    site.classList.toggle('show-ph', showPh);

    const label = document.body.dataset.title;
    document.title = label ? label + ' · ' + c.name : c.name + ' · ' + (both ? 'Plumbing + Electrical' : showPl ? 'Plumbing' : 'Electrical');

    const ld = document.createElement('script');
    ld.type = 'application/ld+json';
    ld.textContent = JSON.stringify({
      '@context': 'https://schema.org', '@type': ['LocalBusiness'].concat(showPl ? ['Plumber'] : [], showEl ? ['Electrician'] : []),
      name: C.brand.fullName, telephone: c.phone, email: c.email,
      address: { '@type': 'PostalAddress', addressLocality: C.address.suburb, addressRegion: C.address.state, postalCode: C.address.postcode, addressCountry: 'AU' },
      openingHours: C.hours.schema, areaServed: C.suburbs, foundingDate: c.founded
    });
    document.head.appendChild(ld);
  }

  // Fill config values into static markup: data-c="key" sets the text, data-tel and data-mail set the link.
  function bindValues(root = document) {
    $$('[data-c]', root).forEach((el) => { const v = c[el.dataset.c]; if (v != null) el.textContent = v; });
    $$('[data-tel]', root).forEach((el) => { el.href = 'tel:' + c.tel; });
    $$('[data-mail]', root).forEach((el) => { el.href = 'mailto:' + c.email; });
  }

  function renderDatalist() {
    const dl = document.createElement('datalist');
    dl.id = 'suburb-list';
    dl.innerHTML = C.suburbs.map((s) => '<option value="' + esc(s) + '"></option>').join('');
    site.appendChild(dl);
  }

  function renderPromo() {
    if (!c.promo || session.get('promoDismissed')) return;
    const el = document.createElement('div');
    el.className = 'promo';
    el.setAttribute('role', 'region');
    el.setAttribute('aria-label', 'Current offer');
    el.innerHTML = '<div class="promo-in"><p>' + esc(c.promo) + '</p>' +
      '<button type="button" class="promo-go" aria-label="' + (showEl ? 'Book an electrical job' : 'Book a job') + '">' + I.arrow(16, 1.8) + '</button>' +
      '<button type="button" class="promo-x" aria-label="Dismiss offer">' + I.close(16, 1.8) + '</button></div>';
    $('.site-header').before(el);
    $('.promo-go', el).addEventListener('click', () => openBooking({ job: showEl ? 'Switchboard upgrade' : '' }));
    $('.promo-x', el).addEventListener('click', () => { session.set('promoDismissed', '1'); el.remove(); });
  }

  function renderHeader() {
    const hdr = $('.site-header');
    const cur = (k) => (isCurrent[k] ? ' is-current' : '');
    const megaBtn = (t, label) => '<li><button type="button" class="nav-link' + cur(t) + '" aria-expanded="false" aria-controls="mega" data-mega>' + label + I.chevron(16, 1.6) + '</button></li>';
    const navLink = (k, label) => '<li><a class="nav-link' + cur(k) + '" href="' + hrefFor(k) + '" data-mega-close>' + label + '</a></li>';
    const megaCol = (t, label) => '<div class="mega-col"><div class="mega-head"><span>' + label + '</span><a class="link-arrow" href="' + hrefFor('hub', t) + '">All ' + t + I.arrow(16, 1.6) + '</a></div>' +
      '<ul>' + svcLinks(t).map((s) => '<li><a class="mega-link" href="' + s.href + '">' + esc(s.name) + I.arrow(16, 1.5) + '</a></li>').join('') + '</ul></div>';
    const mm = (href, label) => '<li><a class="mm-link" href="' + href + '">' + label + I.arrow(18, 1.5) + '</a></li>';

    hdr.innerHTML =
      '<div class="wrap hdr-in">' +
        '<a class="wordmark" href="' + hrefFor('home') + '">' + esc(c.name) + '</a>' +
        '<div class="hdr-mid"><button type="button" class="pill" data-open-booking hidden>' + I.search() + '<span>What needs fixing?</span></button></div>' +
        '<nav class="main-nav" aria-label="Main"><ul>' +
          (showPl ? megaBtn('plumbing', 'Plumbing') : '') + (showEl ? megaBtn('electrical', 'Electrical') : '') +
          navLink('landlords', 'Landlords') + navLink('reviews', 'Reviews') + navLink('about', 'About') +
        '</ul></nav>' +
        '<div class="hdr-actions">' +
          '<span class="tel-wrap"><a class="tel" href="tel:' + c.tel + '">' + I.phone(18, 1.5) + esc(c.phone) + '</a><button type="button" class="copy-tip">Copy number</button></span>' +
          '<button type="button" class="btn btn-primary btn-44" data-open-booking>Book a job</button>' +
        '</div>' +
        '<button type="button" class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">' + I.menu() + '</button>' +
      '</div>' +
      '<div class="mega" id="mega" hidden><div class="wrap mega-in' + (both ? '' : ' single') + '">' +
        (showPl ? megaCol('plumbing', 'Plumbing') : '') + (showEl ? megaCol('electrical', 'Electrical') : '') +
        '<div class="mega-side"><div class="mega-photo"><img src="' + url('images/hot-water.webp') + '" alt="New continuous-flow hot water unit being installed" width="1168" height="880" loading="lazy"></div>' +
        '<p>Burst pipe, gas smell or no power? <a href="' + hrefFor('emergency') + '">We\'re on 24/7</a>.</p></div>' +
      '</div></div>' +
      '<div class="mobile-menu" id="mobile-menu" hidden><nav aria-label="Mobile"><ul>' +
        (showPl ? mm(hrefFor('hub', 'plumbing'), 'Plumbing') : '') + (showEl ? mm(hrefFor('hub', 'electrical'), 'Electrical') : '') +
        mm(hrefFor('landlords'), 'Landlords') + mm(hrefFor('reviews'), 'Reviews') + mm(hrefFor('about'), 'About') + mm(hrefFor('emergency'), 'Emergency help, 24/7') +
      '</ul></nav><div class="mm-actions">' +
        '<a class="btn btn-secondary btn-lg" href="tel:' + c.tel + '">Call ' + esc(c.phone) + '</a>' +
        '<button type="button" class="btn btn-primary btn-lg" data-open-booking>Book a job</button>' +
      '</div></div>';

    // mega panel: hover opens, click toggles (ignoring the click that follows a hover-open), Esc and leaving the header close
    const mega = $('#mega'), megaBtns = $$('[data-mega]', hdr), menuBtn = $('.menu-btn', hdr), mobile = $('#mobile-menu');
    let hoverAt = 0;
    const setMega = (open) => { mega.hidden = !open; megaBtns.forEach((b) => b.setAttribute('aria-expanded', open ? 'true' : 'false')); };
    const setMobile = (open) => {
      mobile.hidden = !open;
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      menuBtn.innerHTML = open ? I.close(22, 1.6) : I.menu();
    };
    megaBtns.forEach((b) => {
      b.addEventListener('mouseenter', () => { if (mega.hidden) { hoverAt = Date.now(); setMega(true); } });
      b.addEventListener('click', () => { if (!mega.hidden && Date.now() - hoverAt < 500) return; setMega(mega.hidden); setMobile(false); });
    });
    $$('[data-mega-close]', hdr).forEach((a) => a.addEventListener('mouseenter', () => setMega(false)));
    hdr.addEventListener('mouseleave', () => setMega(false));
    hdr.addEventListener('keydown', (e) => { if (e.key === 'Escape' && (!mega.hidden || !mobile.hidden)) { setMega(false); setMobile(false); } });
    menuBtn.addEventListener('click', () => { setMobile(mobile.hidden); setMega(false); });
    closeMenus = () => { setMega(false); setMobile(false); };

    // copy the phone number from the hover tip
    const tip = $('.copy-tip', hdr);
    let copyTimer;
    tip.addEventListener('click', () => {
      const done = () => { tip.textContent = 'Copied'; clearTimeout(copyTimer); copyTimer = setTimeout(() => { tip.textContent = 'Copy number'; }, 1800); };
      try { navigator.clipboard.writeText(c.phone).then(done, done); } catch (e) { done(); }
    });
  }
  let closeMenus = () => {};

  function renderFooter() {
    const col = (t, label) => '<nav class="f-col" aria-label="' + label + ' services"><h2>' + label + '</h2><ul>' +
      svcLinks(t).map((s) => '<li><a href="' + s.href + '">' + esc(s.name) + '</a></li>').join('') + '</ul></nav>';
    $('.footer').innerHTML =
      '<div class="wrap"><div class="f-grid">' +
        '<div class="f-col f-brand"><a class="wordmark" href="' + hrefFor('home') + '">' + esc(c.name) + '</a>' +
        '<p>Family-run plumbing and electrical for homeowners and landlords in Melbourne\'s east. Based in ' + esc(c.baseSuburb) + '.</p></div>' +
        (showPl ? col('plumbing', 'Plumbing') : '') + (showEl ? col('electrical', 'Electrical') : '') +
        '<div class="f-col"><h2>Contact</h2><ul>' +
          '<li><a href="tel:' + c.tel + '">' + esc(c.phone) + '</a></li>' +
          '<li><a href="mailto:' + esc(c.email) + '">' + esc(c.email) + '</a></li>' +
          '<li style="padding: 11px 0">Mon to Fri ' + esc(c.weekdays) + ', emergencies ' + esc(c.emergency) + '</li>' +
          '<li style="padding: 11px 0"><span class="ph">' + esc(c.street) + '</span>, ' + esc(c.base) + '</li>' +
          '<li><a href="' + hrefFor('emergency') + '">Emergency help</a></li>' +
          '<li><a href="' + hrefFor('landlords') + '">For landlords</a></li>' +
          '<li><a href="' + hrefFor('book') + '">Book online</a></li>' +
        '</ul></div>' +
      '</div><div class="f-bottom">' +
        '<span>Plumbing licence <span class="ph">' + esc(c.licPlumbing) + '</span></span>' +
        '<span>REC <span class="ph">' + esc(c.licRec) + '</span></span>' +
        '<span>ABN <span class="ph">' + esc(c.licAbn) + '</span></span>' +
        '<a href="' + hrefFor('legal', 'privacy') + '">Privacy</a>' +
        '<a href="' + hrefFor('legal', 'terms') + '">Terms</a>' +
        '<span>© ' + c.year + ' ' + esc(c.name) + '</span>' +
      '</div></div>';
  }

  let callbar;
  function renderCallbar() {
    callbar = document.createElement('div');
    callbar.className = 'callbar';
    callbar.setAttribute('aria-hidden', 'true');
    callbar.innerHTML = '<a class="btn btn-secondary" href="tel:' + c.tel + '" tabindex="-1">' + I.phone(18, 1.5) + 'Call now</a>' +
      '<button type="button" class="btn btn-primary" tabindex="-1" data-open-booking>Book a job</button>';
    site.appendChild(callbar);
  }
  function syncCallbar() {
    const show = (window.scrollY || 0) > 300 && !bk.drawer;
    callbar.classList.toggle('show', show);
    callbar.setAttribute('aria-hidden', show ? 'false' : 'true');
    $$('a,button', callbar).forEach((el) => { el.tabIndex = show ? 0 : -1; });
  }

  // ---------- reviews ----------
  const reviewsReady = fetch(url('reviews.json')).then((r) => (r.ok ? r.json() : [])).catch(() => []);
  function reviewCard(r, cls, i) {
    const n = Math.max(0, Math.min(5, Math.round(r.rating || 5)));
    return '<article class="rv-card' + (cls || '') + '"' + (i != null ? ' style="--i: ' + i + '"' : '') + '>' +
      '<div class="stars" role="img" aria-label="' + n + ' out of 5 stars">' + I.star(16).repeat(n) + '</div>' +
      '<blockquote>“' + esc(r.quote) + '”</blockquote>' +
      '<div class="rv-who"><strong>' + esc(r.name) + '</strong><span>' + esc(r.suburb) + ' · ' + esc(r.job) + '</span></div>' +
      '<div class="rv-src"><span>' + reviewSource + '</span><span>' + esc(r.date) + '</span></div></article>';
  }

  function initCarousel() {
    const track = $('#rv-track');
    if (!track) return;
    const prev = $('#rv-prev'), next = $('#rv-next');
    const ends = () => {
      prev.disabled = track.scrollLeft <= 4;
      next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
    };
    const by = (dir) => {
      const card = track.querySelector('.rv-card:not(.big)') || track.querySelector('.rv-card');
      const w = card ? card.getBoundingClientRect().width + 20 : 360;
      track.scrollBy({ left: dir * w, behavior: reduced() ? 'auto' : 'smooth' });
    };
    reviewsReady.then((list) => {
      track.innerHTML = list.map((r, i) => reviewCard(r, ' r r-right' + (i === 0 ? ' big' : ''), i)).join('');
      ends();
    });
    prev.addEventListener('click', () => by(-1));
    next.addEventListener('click', () => by(1));
    track.addEventListener('scroll', ends, { passive: true });
    window.addEventListener('resize', ends);
    track.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') { e.preventDefault(); by(1); } else if (e.key === 'ArrowLeft') { e.preventDefault(); by(-1); }
    });
    // drag to scroll with a mouse; touch uses native scrolling
    let drag = null;
    track.addEventListener('pointerdown', (e) => { if (e.pointerType !== 'mouse' || e.button !== 0) return; drag = { x: e.clientX, left: track.scrollLeft, moved: false }; });
    track.addEventListener('pointermove', (e) => {
      if (!drag) return;
      const dx = e.clientX - drag.x;
      if (!drag.moved && Math.abs(dx) > 5) { drag.moved = true; track.classList.add('dragging'); }
      if (drag.moved) track.scrollLeft = drag.left - dx;
    });
    const up = () => { if (!drag) return; const moved = drag.moved; drag = null; if (moved) track.classList.remove('dragging'); };
    ['pointerup', 'pointercancel', 'pointerleave'].forEach((t) => track.addEventListener(t, up));
  }

  // ---------- hero ----------
  function initOdometer() {
    const odo = $('#odo');
    if (!odo) return;
    odo.setAttribute('aria-label', c.jobsDoneFmt);
    const strip = '<span>0</span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span>';
    odo.innerHTML = c.jobsDoneFmt.split('').map((ch, i) => (/\d/.test(ch)
      ? '<span class="odo-col" aria-hidden="true"><span class="odo-strip" data-d="' + ch + '" style="transform: translateY(0%); transition-delay: ' + (i * 90) + 'ms">' + strip + '</span></span>'
      : '<span aria-hidden="true">' + esc(ch) + '</span>')).join('');
    setTimeout(() => { $$('.odo-strip', odo).forEach((s) => { s.style.transform = 'translateY(-' + (Number(s.dataset.d) * 10) + '%)'; }); }, 450);
  }

  function initHeroSearch() {
    const form = $('#hero-search');
    if (!form) return;
    const job = $('#hero-job'), sub = $('#hero-suburb'), list = $('#hero-sug');
    let open = false, idx = -1;
    const items = () => {
      const q = job.value.trim().toLowerCase(), all = jobsForTrades();
      if (!q) return all;
      const words = q.split(/\s+/);
      return all.filter((j) => words.every((w) => j.toLowerCase().indexOf(w) > -1));
    };
    const render = () => {
      const l = items(), show = open && l.length > 0;
      list.hidden = !show;
      list.innerHTML = show ? l.map((label, i) => '<li id="sug-' + i + '" role="option" aria-selected="' + (i === idx) + '"' + (i === idx ? ' class="on"' : '') + ' data-label="' + esc(label) + '">' + esc(label) + '</li>').join('') : '';
      job.setAttribute('aria-expanded', show ? 'true' : 'false');
      if (show && idx > -1) job.setAttribute('aria-activedescendant', 'sug-' + idx); else job.removeAttribute('aria-activedescendant');
    };
    const pick = (label) => { job.value = label; open = false; idx = -1; render(); sub.focus(); };
    closeSug = () => { open = false; idx = -1; render(); };

    job.addEventListener('input', () => { open = true; idx = -1; render(); });
    job.addEventListener('focus', () => { open = true; render(); });
    job.addEventListener('blur', () => { setTimeout(closeSug, 120); });
    job.addEventListener('keydown', (e) => {
      const l = items();
      if (e.key === 'ArrowDown') { e.preventDefault(); open = true; idx = Math.min(idx + 1, l.length - 1); render(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); idx = Math.max(idx - 1, -1); render(); }
      else if (e.key === 'Enter' && open && idx > -1 && l[idx]) { e.preventDefault(); pick(l[idx]); }
      else if (e.key === 'Escape') closeSug();
    });
    list.addEventListener('mousedown', (e) => { const li = e.target.closest('li'); if (!li) return; e.preventDefault(); pick(li.dataset.label); });

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const t = job.value.trim(), tl = t.toLowerCase(), jobs = jobsForTrades();
      const match = t ? (jobs.find((j) => j.toLowerCase() === tl) || jobs.find((j) => j.toLowerCase().indexOf(tl) > -1) || jobs.find((j) => tl.split(/\s+/).some((w) => w.length > 3 && j.toLowerCase().indexOf(w) > -1))) : null;
      openBooking({ job: match || (t ? 'Other' : ''), desc: match ? '' : t, suburb: matchSuburb(sub.value) || sub.value.trim() });
    });
  }
  let closeSug = () => {};

  // ---------- how it works ----------
  function initStepper() {
    const sec = $('#how');
    if (!sec) return;
    const media = $('.how-media', sec), list = $('.steps', sec);
    media.innerHTML = STEPS.map((s, i) => '<img src="' + url(s.img) + '" alt="' + esc(s.alt) + '"' + (i === 0 ? ' class="on"' : '') + ' width="896" height="1120" loading="lazy">').join('');
    list.innerHTML = STEPS.map((s, i) => '<li class="step"><button type="button" class="step-btn" id="step-btn-' + i + '" aria-expanded="false" aria-controls="step-body-' + i + '"><span class="step-num" aria-hidden="true">' + (i + 1) + '</span><span class="step-title">' + esc(s.title) + '</span></button></li>').join('');

    const p = { hover: false, focus: false, off: false, hidden: document.hidden };
    const paused = () => p.hover || p.focus || p.off || p.hidden;
    const sync = () => sec.classList.toggle('paused', paused());
    let step = 0;
    const setStep = (n) => {
      step = n;
      $$('img', media).forEach((im, i) => im.classList.toggle('on', i === n));
      $$('.step', list).forEach((li, i) => {
        const on = i === n;
        li.classList.toggle('on', on);
        li.firstElementChild.setAttribute('aria-expanded', on ? 'true' : 'false');
        $$('.step-body,.prog', li).forEach((x) => x.remove());
        if (on) li.insertAdjacentHTML('beforeend', '<p class="step-body" id="step-body-' + i + '">' + esc(STEPS[i].body) + '</p><div class="prog" aria-hidden="true"><div class="prog-fill"></div></div>');
      });
    };
    setStep(0);

    list.addEventListener('click', (e) => { const b = e.target.closest('.step-btn'); if (b) setStep(Number(b.id.slice(9))); });
    list.addEventListener('animationend', (e) => {
      if (!e.target.classList.contains('prog-fill') || paused() || reduced()) return;
      setStep((step + 1) % STEPS.length);
    });
    list.addEventListener('keydown', (e) => {
      const keys = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1, Home: 'first', End: 'last' };
      if (!(e.key in keys)) return;
      const id = (document.activeElement && document.activeElement.id) || '';
      if (id.indexOf('step-btn-') !== 0) return;
      e.preventDefault();
      const k = keys[e.key], n = STEPS.length;
      const nx = k === 'first' ? 0 : k === 'last' ? n - 1 : (Number(id.slice(9)) + k + n) % n;
      setStep(nx);
      document.getElementById('step-btn-' + nx).focus();
    });
    // pause on hover, keyboard focus, off screen and hidden tab
    sec.addEventListener('mouseenter', () => { p.hover = true; sync(); });
    sec.addEventListener('mouseleave', () => { p.hover = false; sync(); });
    sec.addEventListener('focusin', (e) => { let fv = false; try { fv = e.target.matches(':focus-visible'); } catch (x) {} if (fv) { p.focus = true; sync(); } });
    sec.addEventListener('focusout', (e) => { if (!e.relatedTarget || !sec.contains(e.relatedTarget)) { p.focus = false; sync(); } });
    document.addEventListener('visibilitychange', () => { p.hidden = document.hidden; sync(); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver((en) => { en.forEach((x) => { p.off = !x.isIntersecting; }); sync(); }, { threshold: 0.12 }).observe(sec);
    }
  }

  // ---------- services, why us, areas, FAQ ----------
  function renderServices() {
    const cols = $('#svc-cols');
    if (!cols) return;
    if (!both) {
      $('#svc-intro').innerHTML = showPl
        ? '<h2 id="svc-h" class="h2">Plumbing done <span class="brush">properly</span></h2><p class="lede">Hot water, drains, taps, gas and renovations, done by licensed local plumbers.</p>'
        : '<h2 id="svc-h" class="h2">Electrical done <span class="brush">properly</span></h2><p class="lede">Power faults, switchboards, lighting and safety checks, done by licensed local electricians.</p>';
    }
    const col = (t, title, img, alt, i) => '<div class="svc-col r r-rise" style="--i: ' + i + '">' +
      '<div class="svc-photo"><img src="' + url('images/' + img) + '" alt="' + alt + '" width="1168" height="880" loading="lazy"></div>' +
      '<div class="svc-col-h"><h3 class="h3">' + title + '</h3><a class="link-arrow" href="' + hrefFor('hub', t) + '">All ' + t + I.arrow(16, 1.6) + '</a></div>' +
      '<ul class="svc-list">' + svcLinks(t).map((s) => '<li><a class="svc-row" href="' + s.href + '"><span><strong>' + esc(s.name) + '</strong><span class="d">' + esc(s.desc) + '</span></span>' + I.arrow(20, 1.5, 'svc-arrow') + '</a></li>').join('') + '</ul></div>';
    cols.innerHTML = (showPl ? col('plumbing', 'Plumbing', 'hot-water.webp', 'New continuous-flow hot water unit being installed', 1) : '') +
      (showEl ? col('electrical', 'Electrical', 'electrical.webp', 'Electrician working on a home switchboard', 2) : '');
    const strip = $('#svc-strip');
    if (strip && !showPl) strip.remove();
  }

  function renderWhy() {
    const list = $('#why-list');
    if (!list) return;
    list.innerHTML = WHY.map((w, i) => '<li class="why-item r r-fade" style="--i: ' + i + '"><span class="why-num" aria-hidden="true">' + String(i + 1).padStart(2, '0') + '</span>' +
      '<h3>' + (w.ph ? '<span class="ph">' + esc(w.ph) + '</span>' : '') + esc(w.h) + '</h3><p>' + esc(w.b) + '</p></li>').join('');
  }

  function initAreas() {
    const chips = $('#area-chips');
    if (chips) chips.innerHTML = C.suburbs.map((n) => '<li><a class="chip" href="' + hrefFor('suburb', slugify(n)) + '">' + esc(n) + '</a></li>').join('');
    const form = $('#checker');
    if (!form) return;
    const inp = $('#check-in'), out = $('#check-out');
    inp.addEventListener('input', () => { out.innerHTML = ''; });
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const v = inp.value.trim();
      if (!v) { out.innerHTML = ''; return; }
      const m = matchSuburb(v);
      out.innerHTML = m
        ? '<p class="check-res check-yes">' + I.check(20, 2) + '<span>Yes, we\'re in ' + esc(m) + ' most days. <a href="' + hrefFor('suburb', slugify(m)) + '">See ' + esc(m) + '</a></span></p>'
        : '<p class="check-res check-no"><span>We may still come out. Call us on <a href="tel:' + c.tel + '">' + esc(c.phone) + '</a>.</span></p>';
    });
  }

  function renderFaq() {
    const list = $('#faq-list');
    if (!list) return;
    list.innerHTML = FAQ.map((f) => '<details><summary><span>' + esc(f.q) + '</span>' + I.plus() + '</summary><div class="faq-a"><p>' + esc(f.a) + '</p></div></details>').join('');
    // one open at a time
    list.addEventListener('click', (e) => {
      const s = e.target.closest('summary');
      if (!s) return;
      e.preventDefault();
      const d = s.parentElement, was = d.open;
      $$('details', list).forEach((x) => { x.open = false; });
      d.open = !was;
    });
  }

  // ---------- inner pages ----------
  const SIGN = svg(20, 1.5, '<circle cx="12" cy="12" r="9"></circle><path d="M12 8v5M12 16.5v.01"></path>');
  const ticks = (items, icon) => '<ul class="ticks">' + items.map((t) => '<li>' + icon + '<span>' + esc(t) + '</span></li>').join('') + '</ul>';
  const svcRows = (links) => links.map((s) => '<li><a class="svc-row" href="' + s.href + '"><span><strong>' + esc(s.name) + '</strong><span class="d">' + esc(s.desc) + '</span></span>' + I.arrow(20, 1.5, 'svc-arrow') + '</a></li>').join('');
  const chipLinks = (names) => names.map((n) => '<li><a class="chip" href="' + hrefFor('suburb', slugify(n)) + '">' + esc(n) + '</a></li>').join('');
  const findService = (name) => {
    for (const t of ['plumbing', 'electrical']) { const s = C.services[t].find((x) => x.name === name); if (s) return { s, t }; }
    return null;
  };
  const faqSection = () => '<section class="sec band-card" data-reveal="faq" aria-labelledby="faq-h"><div class="wrap r r-fade">' +
    '<h2 id="faq-h" class="h2">Questions people <span class="brush">ask</span> us</h2><div class="faq" id="faq-list"></div></div></section>';
  const bookSection = (pre, brush, post) => '<section class="sec band-w2" id="book" data-reveal="book" aria-labelledby="book-h"><div class="wrap">' +
    '<div class="intro r r-rise"><h2 id="book-h" class="h2">' + esc(pre) + '<span class="brush">' + esc(brush) + '</span>' + esc(post) + '</h2>' +
    '<p class="lede">We\'ll text you a time within <span class="ph">' + esc(c.responseTime) + '</span>, then again when we\'re 30 minutes away.</p></div>' +
    '<div class="book-grid" id="book-grid"></div></div></section>';
  const callBtn = () => '<a class="btn btn-secondary btn-lg" href="tel:' + c.tel + '">Call ' + esc(c.phone) + '</a>';

  // Service pages (plumbing/hot-water.html etc.) are built from CONFIG.servicePages.
  function renderServicePage() {
    const sp = PAGE === 'service' && C.servicePages[SLUG];
    if (!sp) return;
    const related = sp.related.map(findService).filter(Boolean).map((f) => svcLink(f.s, f.t));
    const book = (label) => '<button type="button" class="btn btn-primary btn-lg" data-open-booking data-job="' + esc(sp.job) + '">' + label + '</button>';
    $('#main').innerHTML =
      '<section class="page-hero"><div class="wrap split"><div><h1 class="h1-page">' + esc(sp.h1) + '</h1><p class="lede">' + esc(sp.intro) + '</p>' +
        '<div class="actions">' + book('Book ' + esc(sp.short)) + callBtn() + '</div></div>' +
        '<div class="photo"><img src="' + url('images/' + sp.img) + '" alt="' + esc(sp.alt) + '" width="1168" height="880"></div></div></section>' +
      '<section class="sec band-card"><div class="wrap"><div class="two-lists">' +
        '<div><h2 class="h3">Signs you need us</h2>' + ticks(sp.signs, SIGN) + '</div>' +
        '<div><h2 class="h3">What\'s included</h2>' + ticks(sp.included, I.check(20, 1.8)) + '</div></div>' +
        '<div class="note" style="margin-top: 64px"><p>' + esc(sp.note) + '</p>' + book('Book a time') + '</div></div></section>' +
      '<section class="sec" id="rg" data-rg="service"></section>' +
      '<section class="sec band-w1" aria-labelledby="rel-h"><div class="wrap"><h2 id="rel-h" class="h3">Related services</h2><ul class="svc-list" style="margin-top: 16px">' + svcRows(related) + '</ul></div></section>' +
      faqSection() + bookSection('Get ', sp.topic, ' sorted');
  }

  // Suburb pages (areas/box-hill.html etc.): local copy from CONFIG.suburbDetail, generic copy otherwise.
  function renderSuburbPage() {
    const name = PAGE === 'suburb' && suburbFromSlug(SLUG);
    if (!name) return;
    const d = C.suburbDetail[name];
    const near = (C.nearby[name] || C.suburbs.filter((x) => x !== name).slice(0, 4)).filter((x) => C.suburbs.indexOf(x) > -1);
    const h1 = (both ? 'Plumber and electrician in ' : showPl ? 'Plumber in ' : 'Electrician in ') + name;
    const para = d ? d.para : "We're in " + name + ' most weeks, fixing hot water, drains, leaks and power faults for homeowners and landlords. It is a short drive from our ' + c.baseSuburb + " workshop, and we text you when we're 30 minutes away.";
    const jobs = d ? d.jobs : ['Hot water repairs and replacement', 'Blocked drains', 'Switchboard upgrades', 'Smoke alarms for rentals'];
    $('#main').innerHTML =
      '<section class="page-hero"><div class="wrap"><h1 class="h1-page">' + esc(h1) + '</h1><p class="lede">' + esc(para) + '</p>' +
        '<div class="actions"><button type="button" class="btn btn-primary btn-lg" data-open-booking data-suburb="' + esc(name) + '">Book in ' + esc(name) + '</button>' + callBtn() + '</div></div></section>' +
      '<section class="sec band-w1"><div class="wrap split" style="align-items: start">' +
        '<div><h2 class="h3">Jobs we often do in ' + esc(name) + '</h2>' + ticks(jobs, I.check(20, 1.8)) + '</div>' +
        '<div><h2 class="h3">Nearby suburbs we cover</h2><ul class="chips" style="margin-top: 24px; list-style: none; padding: 0">' + chipLinks(near) + '</ul></div>' +
      '</div></section>' +
      '<section class="sec" id="rg" data-rg="suburb"></section>' +
      bookSection('Book a tradie in ', name, '');
  }

  function renderHubList() {
    const ul = $('#hub-list');
    if (!ul) return;
    const t = ul.dataset.trade;
    ul.innerHTML = C.services[t].map((s) => '<li class="hub-row"><div><strong>' + esc(s.name) + '</strong><span class="d">' + esc(s.desc) + '</span></div><div class="hub-btns">' +
      (s.page ? '<a class="btn btn-secondary btn-44" href="' + svcLink(s, t).href + '">Details</a>' : '') +
      '<button type="button" class="btn btn-primary btn-44" data-open-booking data-job="' + esc(s.job) + '"' + (s.job === 'Other' ? ' data-desc="' + esc(s.name) + '"' : '') + '>Book this</button></div></li>').join('');
  }

  // Review grid: data-rg is plumbing / electrical (hubs), service, suburb or all (reviews page, with filters).
  function renderReviewGrid() {
    const sec = $('#rg');
    if (!sec) return;
    const mode = sec.dataset.rg;
    sec.setAttribute('aria-label', 'Customer reviews');
    reviewsReady.then((all) => {
      let head = null, list = all, filters = null;
      if (mode === 'plumbing' || mode === 'electrical') {
        head = ['What ' + mode + ' customers ', 'say', ''];
        list = all.filter((r) => r.trade.indexOf(mode) > -1).slice(0, 3);
      } else if (mode === 'service') {
        const sp = C.servicePages[SLUG] || {};
        head = ["Neighbours who've ", 'been there', ''];
        list = all.map((r) => ({ r, sc: (r.key === sp.key ? 2 : 0) + (r.trade.indexOf(sp.trade) > -1 ? 1 : 0) })).sort((x, y) => y.sc - x.sc).map((x) => x.r).slice(0, 3);
      } else if (mode === 'suburb') {
        const name = suburbFromSlug(SLUG), near = C.nearby[name] || [];
        const here = all.filter((r) => r.suburb === name), nearList = all.filter((r) => near.indexOf(r.suburb) > -1);
        head = ['Reviews from ', here.length ? name : 'nearby', ''];
        list = here.length ? here.concat(nearList).slice(0, 3) : nearList.length ? nearList.slice(0, 3) : all.slice(0, 3);
      } else {
        const subs = [];
        all.forEach((r) => { if (subs.indexOf(r.suburb) < 0) subs.push(r.suburb); });
        filters = [{ v: 'all', label: 'All' }].concat(showPl ? [{ v: 't:plumbing', label: 'Plumbing' }] : [], showEl ? [{ v: 't:electrical', label: 'Electrical' }] : [], subs.map((x) => ({ v: 's:' + x, label: x })));
      }
      const draw = (fv) => {
        const shown = filters ? all.filter((r) => fv === 'all' || (fv.indexOf('t:') === 0 ? r.trade.indexOf(fv.slice(2)) > -1 : r.suburb === fv.slice(2))) : list;
        sec.innerHTML = '<div class="wrap">' +
          (head ? '<h2 class="h2" style="margin-bottom: 40px">' + esc(head[0]) + '<span class="brush">' + esc(head[1]) + '</span>' + esc(head[2]) + '</h2>' : '') +
          (filters ? '<div class="fchips" role="group" aria-label="Filter reviews">' + filters.map((f) => '<button type="button" class="chip" aria-pressed="' + (f.v === fv) + '" data-filter="' + esc(f.v) + '">' + esc(f.label) + '</button>').join('') + '</div>' : '') +
          '<div class="rv-grid">' + shown.map((r) => reviewCard(r)).join('') + '</div>' +
          (shown.length ? '' : '<p class="lede">No reviews for this filter yet.</p>') + '</div>';
      };
      draw('all');
      if (filters) {
        sec.addEventListener('click', (e) => {
          const b = e.target.closest('[data-filter]');
          if (!b) return;
          draw(b.dataset.filter);
          focusEl($('[data-filter="' + b.dataset.filter + '"]', sec));
        });
      }
    });
  }

  function renderTeam() {
    const ul = $('#team-rows');
    if (ul) ul.innerHTML = C.team.map((t) => '<li><strong>' + esc(t.name) + '</strong><span>' + esc(t.role) + '</span></li>').join('');
  }

  function initThanks() {
    const ref = $('#thanks-ref');
    if (!ref) return;
    let r = null;
    try { r = new URLSearchParams(location.search).get('ref'); } catch (e) {}
    ref.textContent = r || (C.bookingRefPrefix || '') + '00000';
    $('#thanks-line').textContent = r ? "We've got your details and we'll be in touch shortly." : 'This is the page customers see after they book.';
  }

  // ---------- booking form and drawer ----------
  const TIMES = ['ASAP', 'This week', 'Pick a date'];
  const ORDER = ['job', 'date', 'suburb', 'name', 'mobile', 'email', 'tmobile'];
  const blankForm = (k = {}) => ({ job: '', desc: '', time: 'ASAP', date: '', suburb: k.suburb || '', name: k.name || '', mobile: k.mobile || '', email: k.email || '', landlord: !!k.landlord, address: '', tname: '', tmobile: '', photos: [] });
  const bk = { form: blankForm(), errors: {}, submitting: false, done: null, drawer: false, opener: null };
  let bookSec, panel, scrim;
  const F = (k) => document.getElementById('f-' + k);

  if (PAGE === 'service' && C.servicePages[SLUG]) bk.form.job = C.servicePages[SLUG].job;
  if (PAGE === 'suburb' && suburbFromSlug(SLUG)) bk.form.suburb = suburbFromSlug(SLUG);
  if (PAGE === 'landlords') bk.form.landlord = true;

  function validateField(k, f) {
    const v = typeof f[k] === 'string' ? f[k].trim() : f[k];
    if (k === 'job') return v ? '' : 'Choose what needs fixing so we send the right tradie';
    if (k === 'suburb') return v ? '' : "Add your suburb so we know who's closest";
    if (k === 'date') { if (f.time !== 'Pick a date') return ''; if (!v) return 'Pick a date that suits you'; return v < todayStr() ? 'Pick a date from today onwards' : ''; }
    if (k === 'name') return v ? '' : 'Add your name';
    if (k === 'mobile') { if (!v) return 'Add a mobile so we can text you a time'; return validMobile(v) ? '' : "That doesn't look like an Australian mobile. Try 04XX XXX XXX"; }
    if (k === 'email') return !v || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? '' : 'Check the email address, or leave it blank';
    if (k === 'tmobile') { if (!f.landlord) return ''; if (!v) return "Add the tenant's mobile so we can arrange access"; return validMobile(v) ? '' : "That doesn't look like an Australian mobile. Try 04XX XXX XXX"; }
    return '';
  }

  function field(k, label, attrs, opts = {}) {
    return '<div class="field' + (opts.full ? ' full' : '') + '"><label class="lbl" for="f-' + k + '">' + label + (opts.optional ? ' <span class="opt">(optional)</span>' : '') + '</label>' +
      '<input id="f-' + k + '" class="inp" ' + attrs + (opts.check ? ' aria-invalid="false" aria-describedby="f-' + k + '-err"' : '') + '></div>';
  }

  function panelHTML() {
    const jobOpts = jobsForTrades().concat(['Other']);
    return '<div class="drawer-top" hidden><h2 id="panel-h" class="h3">' + (PAGE === 'landlords' ? 'Add a property' : 'Book a job') + '</h2>' +
        '<button type="button" class="icon-btn" id="drawer-close" aria-label="Close booking">' + I.close(20, 1.6) + '</button></div>' +
      '<form novalidate aria-label="Booking form" id="booking-form"><div class="fgrid">' +
        '<div class="field full"><label class="lbl" for="f-job">What needs fixing?</label><div class="sel-wrap">' +
          '<select id="f-job" class="inp" aria-invalid="false" aria-describedby="f-job-err"><option value="">Choose a job</option>' +
          jobOpts.map((v) => '<option value="' + esc(v) + '">' + esc(v) + '</option>').join('') + '</select>' + I.chevron(20, 1.6) +
        '</div></div>' +
        '<div class="field full"><label class="lbl" for="f-desc">Describe the problem <span class="opt">(optional)</span></label>' +
          '<textarea id="f-desc" class="inp" rows="3" placeholder="e.g. No hot water since this morning, the pilot light is out"></textarea></div>' +
        '<div class="field full"><span class="lbl" id="f-time-l">Preferred time</span>' +
          '<div class="tchips" role="group" aria-labelledby="f-time-l">' + TIMES.map((t) => '<button type="button" class="tchip" aria-pressed="false" data-time="' + t + '">' + t + '</button>').join('') + '</div>' +
          '<label class="sr-only" for="f-date" hidden>Pick a date</label>' +
          '<input id="f-date" class="inp" type="date" aria-invalid="false" aria-describedby="f-date-err" style="max-width: 260px" hidden></div>' +
        field('suburb', 'Suburb', 'type="text" list="suburb-list" autocomplete="address-level2" placeholder="e.g. Box Hill"', { check: true }) +
        field('name', 'Name', 'type="text" autocomplete="name"', { check: true }) +
        field('mobile', 'Mobile', 'type="tel" inputmode="tel" autocomplete="tel" placeholder="04XX XXX XXX"', { check: true }) +
        field('email', 'Email', 'type="email" autocomplete="email"', { check: true, optional: true }) +
        '<label class="check full"><input id="f-landlord" type="checkbox"><span>I\'m a landlord or property manager</span></label>' +
        '<div class="ll-box full" hidden>' +
          field('address', 'Property address', 'type="text" autocomplete="street-address"', { full: true, optional: true }) +
          field('tname', 'Tenant name', 'type="text"') +
          field('tmobile', 'Tenant mobile', 'type="tel" inputmode="tel" placeholder="04XX XXX XXX"', { check: true }) +
        '</div>' +
        '<div class="field full"><span class="lbl">Photos <span class="opt">(optional, up to 3)</span></span>' +
          '<label class="drop" for="f-photos">' + I.upload() + '<span>Add photos of the problem</span><input id="f-photos" class="sr-only" type="file" accept="image/*" multiple></label>' +
          '<ul class="thumbs-row" style="list-style: none; margin: 0; padding: 0" hidden></ul></div>' +
        '<div class="form-foot full"><button type="submit" class="btn btn-primary btn-lg btn-block" id="f-submit" aria-disabled="false">Send booking request</button>' +
          '<p class="cap">We\'ll text you to confirm a time.</p></div>' +
      '</div></form>' +
      '<div class="success" id="success-panel" tabindex="-1" hidden>' +
        '<div class="tick">' + svg(26, 2.2, '<path d="M20 6 9 17l-5-5"></path>') + '</div>' +
        '<h3 class="h3" id="done-h"></h3>' +
        '<p class="ref">Booking reference <strong id="done-ref"></strong></p>' +
        '<div><p class="cap" style="margin-bottom: 8px">Your confirmation text will look like this</p><p class="sms-preview" id="done-sms"></p></div>' +
        '<div class="actions" style="margin-top: 4px"><a class="btn btn-secondary" id="done-next" href="' + hrefFor('thanks') + '">What happens next</a>' +
        '<button type="button" class="btn btn-secondary" id="done-again">Book another job</button></div>' +
      '</div>' +
      '<p class="sr-only" aria-live="polite" id="bk-announce"></p>';
  }

  function talkHTML() {
    return '<aside class="talk r r-rise" style="--i: 1" aria-labelledby="talk-h"><h3 id="talk-h" class="h3">Rather talk?</h3>' +
      '<a class="big-tel" href="tel:' + c.tel + '">' + I.phone(30, 1.4) + esc(c.phone) + '</a>' +
      '<ul class="hours"><li><span>Monday to Friday</span><strong>' + esc(c.weekdays) + '</strong></li><li><span>Emergency call-outs</span><strong>' + esc(c.emergency) + '</strong></li></ul>' +
      '<p class="lede">Burst pipe, gas smell or no power? Call any time on the same number. <a href="' + hrefFor('emergency') + '">What to do while you wait</a></p></aside>';
  }

  const announce = (msg) => { $('#bk-announce').textContent = msg; };

  function setErr(k, msg) {
    if (msg) bk.errors[k] = msg; else delete bk.errors[k];
    const el = F(k);
    if (!el) return;
    el.setAttribute('aria-invalid', msg ? 'true' : 'false');
    let p = document.getElementById('f-' + k + '-err');
    if (!msg) { if (p) p.remove(); return; }
    if (!p) { p = document.createElement('p'); p.className = 'err'; p.id = 'f-' + k + '-err'; el.closest('.field').appendChild(p); }
    p.innerHTML = I.alert() + esc(msg);
  }

  function syncTime() {
    const f = bk.form, pickDate = f.time === 'Pick a date';
    $$('.tchip', panel).forEach((b) => b.setAttribute('aria-pressed', b.dataset.time === f.time ? 'true' : 'false'));
    const d = F('date');
    d.min = todayStr();
    d.hidden = !pickDate;
    $('label[for="f-date"]', panel).hidden = !pickDate;
    if (!pickDate) setErr('date', '');
  }
  const syncLandlord = () => { $('.ll-box', panel).hidden = !bk.form.landlord; };
  function syncPhotos() {
    const ph = bk.form.photos, row = $('.thumbs-row', panel);
    $('.drop', panel).hidden = ph.length >= 3;
    row.hidden = !ph.length;
    row.innerHTML = ph.map((p, i) => '<li class="thumb"><img src="' + p.url + '" alt="' + esc('Photo ' + (i + 1) + ': ' + p.name) + '">' +
      '<button type="button" aria-label="Remove photo ' + (i + 1) + '" data-remove="' + p.id + '">' + I.close(14, 2) + '</button></li>').join('');
  }
  function syncSubmit() {
    const b = F('submit');
    b.classList.toggle('is-pressed', bk.submitting);
    b.setAttribute('aria-disabled', bk.submitting ? 'true' : 'false');
    b.innerHTML = bk.submitting ? '<span class="spin" aria-hidden="true"></span>Sending…' : 'Send booking request';
  }

  // Push bk.form into the inputs (after a reset or a pre-fill from a Book button).
  function writeForm() {
    const f = bk.form, sel = F('job');
    sel.value = f.job;
    if (sel.value !== f.job) { f.job = ''; sel.value = ''; }
    ['desc', 'date', 'suburb', 'name', 'mobile', 'email', 'address', 'tname', 'tmobile'].forEach((k) => { F(k).value = f[k]; });
    F('landlord').checked = f.landlord;
    syncTime(); syncLandlord(); syncPhotos(); syncSubmit();
    ORDER.forEach((k) => setErr(k, bk.errors[k] || ''));
  }

  function setField(k, val) {
    bk.form[k] = val;
    const recheck = k === 'landlord' ? 'tmobile' : k;
    if (bk.errors[recheck] || k === 'job') setErr(recheck, validateField(recheck, bk.form));
  }
  function blurField(k) {
    const f = bk.form;
    if ((k === 'mobile' || k === 'tmobile') && f[k]) { const fm = fmtMobile(f[k]); if (fm !== f[k]) { f[k] = fm; F(k).value = fm; } }
    const has = typeof f[k] === 'string' ? f[k].trim() !== '' : !!f[k];
    if (!has && !bk.errors[k]) return;
    setErr(k, validateField(k, f));
  }
  function pickTime(t) {
    bk.form.time = t;
    syncTime();
    if (t === 'Pick a date') setTimeout(() => F('date').focus(), 30);
  }
  function addPhotos(input) {
    const files = Array.from(input.files || []).filter((f) => /^image\//.test(f.type));
    const room = 3 - bk.form.photos.length;
    const add = files.slice(0, Math.max(0, room)).map((f, i) => ({ name: f.name, url: URL.createObjectURL(f), id: Date.now() + '-' + i }));
    try { input.value = ''; } catch (x) {}
    bk.form.photos = bk.form.photos.concat(add);
    syncPhotos();
    announce(add.length ? add.length + (add.length === 1 ? ' photo' : ' photos') + ' added' : files.length ? 'You can add up to 3 photos' : '');
  }
  function removePhoto(id) {
    const p = bk.form.photos.find((x) => x.id === id);
    if (p) { try { URL.revokeObjectURL(p.url); } catch (x) {} }
    bk.form.photos = bk.form.photos.filter((x) => x.id !== id);
    syncPhotos();
    announce('Photo removed');
  }

  function showDone(on) {
    $('#booking-form').hidden = on;
    $('#success-panel').hidden = !on;
  }

  function submit(e) {
    if (e) e.preventDefault();
    if (bk.submitting) return;
    const f = bk.form, errors = {};
    ORDER.forEach((k) => { const m = validateField(k, f); if (m) errors[k] = m; });
    ORDER.forEach((k) => setErr(k, errors[k] || ''));
    const keys = ORDER.filter((k) => errors[k]);
    if (keys.length) {
      announce(keys.length + (keys.length === 1 ? ' thing needs' : ' things need') + ' fixing. ' + errors[keys[0]]);
      F(keys[0]).focus();
      return;
    }
    f.mobile = fmtMobile(f.mobile);
    f.tmobile = f.tmobile ? fmtMobile(f.tmobile) : '';
    F('mobile').value = f.mobile; F('tmobile').value = f.tmobile;
    bk.submitting = true;
    syncSubmit();
    announce('Sending your booking');

    setTimeout(() => {
      const ref = (C.bookingRefPrefix || '') + String(Math.floor(10000 + Math.random() * 90000));
      const payload = {
        ref, job: f.job, description: f.desc, preferredTime: f.time === 'Pick a date' ? f.date : f.time, suburb: f.suburb, name: f.name,
        mobile: f.mobile, email: f.email, landlord: f.landlord, propertyAddress: f.address, tenantName: f.tname, tenantMobile: f.tmobile,
        photos: f.photos.map((p) => p.name), page: PAGE + (SLUG ? '/' + SLUG : ''), submittedAt: new Date().toISOString()
      };
      if (C.formEndpoint) {
        try { fetch(C.formEndpoint, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(payload) }).catch(() => {}); } catch (x) {}
      } else {
        try { console.log('[Tradie demo] booking payload', payload); } catch (x) {}
      }
      const first = f.name.trim().split(/\s+/)[0] || 'there';
      const jobText = f.job === 'Other' ? 'your job' : f.job.toLowerCase();
      bk.submitting = false;
      bk.done = { ref };
      syncSubmit();
      $('#done-h').textContent = 'Thanks, ' + first + '. We\'ll text ' + f.mobile + ' with a time shortly.';
      $('#done-ref').textContent = ref;
      $('#done-sms').textContent = c.name + ': Hi ' + first + ", we've got your booking for " + jobText + ' (' + ref + "). We'll text you a time within " + c.responseTime + '.';
      $('#done-next').href = hrefFor('thanks') + '?ref=' + encodeURIComponent(ref);
      showDone(true);
      announce('Booking sent. Your reference is ' + ref + '.');
      focusEl($('#success-panel'));
    }, 900);
  }

  function resetForm() {
    bk.done = null;
    bk.errors = {};
    bk.form = blankForm(bk.form);
    writeForm();
    showDone(false);
    announce('');
    F('job').focus();
  }

  function setDrawer(open) {
    bk.drawer = open;
    panel.classList.toggle('is-drawer', open);
    panel.classList.toggle('r', !open);
    panel.classList.toggle('r-rise', !open);
    if (open) {
      panel.setAttribute('role', 'dialog');
      panel.setAttribute('aria-modal', 'true');
      panel.setAttribute('aria-labelledby', 'panel-h');
      bookSec.classList.add('in');
    } else {
      ['role', 'aria-modal', 'aria-labelledby'].forEach((a) => panel.removeAttribute(a));
    }
    $('.drawer-top', panel).hidden = !open;
    $('.panel-ghost', bookSec).hidden = !open;
    if (bookSec.classList.contains('book-ghost')) bookSec.hidden = !open;
    scrim.hidden = !open;
    syncCallbar();
  }

  function openBooking(o = {}) {
    bk.opener = document.activeElement;
    if (bk.done) { bk.form = blankForm(bk.form); bk.errors = {}; bk.done = null; showDone(false); }
    if (o.job != null) bk.form.job = o.job;
    if (o.desc) bk.form.desc = o.desc;
    if (o.suburb) bk.form.suburb = o.suburb;
    if (PAGE === 'landlords') bk.form.landlord = true;
    writeForm();
    closeMenus();
    closeSug();
    setDrawer(true);
    setTimeout(() => {
      const f = bk.form;
      focusEl(F(!f.job ? 'job' : !f.suburb ? 'suburb' : !f.name ? 'name' : 'mobile') || $('#drawer-close'));
    }, 80);
  }

  function closeDrawer() {
    setDrawer(false);
    if (bk.opener && bk.opener.focus) focusEl(bk.opener);
  }

  function initBooking() {
    bookSec = $('#book');
    let grid = bookSec && $('#book-grid', bookSec);
    if (!grid) {
      // pages without a booking section get a hidden one that only shows as the drawer
      bookSec = document.createElement('section');
      bookSec.className = 'sec band-w2 book-ghost';
      bookSec.id = 'book';
      bookSec.hidden = true;
      bookSec.setAttribute('aria-label', 'Booking');
      bookSec.innerHTML = '<div class="wrap"><div class="book-grid solo" id="book-grid"></div></div>';
      $('#main').appendChild(bookSec);
      grid = $('#book-grid', bookSec);
    }
    grid.innerHTML = '<div class="panel-ghost" hidden>Your booking is open in the panel. Close it to come back here.</div>' +
      '<div class="panel r r-rise" id="booking-panel">' + panelHTML() + '</div>' +
      (grid.classList.contains('solo') ? '' : talkHTML());
    panel = $('#booking-panel');

    scrim = document.createElement('button');
    scrim.type = 'button';
    scrim.className = 'scrim';
    scrim.setAttribute('aria-label', 'Close booking');
    scrim.tabIndex = -1;
    scrim.hidden = true;
    scrim.addEventListener('click', closeDrawer);
    site.appendChild(scrim);

    const form = $('#booking-form');
    form.addEventListener('input', (e) => {
      const k = (e.target.id || '').slice(2);
      if (!k || k === 'landlord' || k === 'photos' || !(k in bk.form)) return;
      setField(k, e.target.value);
    });
    form.addEventListener('change', (e) => {
      if (e.target.id === 'f-landlord') { setField('landlord', e.target.checked); syncLandlord(); }
      else if (e.target.id === 'f-photos') addPhotos(e.target);
    });
    form.addEventListener('focusout', (e) => { const k = (e.target.id || '').slice(2); if (ORDER.indexOf(k) > -1) blurField(k); });
    form.addEventListener('click', (e) => {
      const chip = e.target.closest('.tchip');
      if (chip) pickTime(chip.dataset.time);
      const rm = e.target.closest('[data-remove]');
      if (rm) removePhoto(rm.dataset.remove);
    });
    form.addEventListener('submit', submit);
    $('#done-again').addEventListener('click', resetForm);
    $('#drawer-close').addEventListener('click', closeDrawer);

    // Esc closes the drawer; Tab stays inside it
    panel.addEventListener('keydown', (e) => {
      if (!bk.drawer) return;
      if (e.key === 'Escape') { e.preventDefault(); closeDrawer(); return; }
      if (e.key !== 'Tab') return;
      const els = $$('a[href],button:not([disabled]),input:not([disabled]),select,textarea,[tabindex]:not([tabindex="-1"])', panel)
        .filter((el) => el.getClientRects().length > 0 || el.type === 'file');
      if (!els.length) return;
      const first = els[0], last = els[els.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    // any [data-open-booking] button opens the drawer; data-job, data-desc and data-suburb pre-fill it
    document.addEventListener('click', (e) => {
      const b = e.target.closest('[data-open-booking]');
      if (!b) return;
      e.preventDefault();
      openBooking({ job: b.dataset.job, desc: b.dataset.desc, suburb: b.dataset.suburb });
    });

    writeForm();
  }

  // ---------- scroll: sticky pill, header rule, call bar, reveals ----------
  function initScroll(checkReveal) {
    const pill = $('.pill');
    const limit = PAGE === 'home' ? 600 : 160;
    let raf = null;
    const onScroll = () => {
      if (raf) return;
      raf = requestAnimationFrame(() => {
        raf = null;
        const scrolled = (window.scrollY || 0) > limit;
        if (site.classList.contains('is-scrolled') !== scrolled) { site.classList.toggle('is-scrolled', scrolled); pill.hidden = !scrolled; }
        syncCallbar();
        checkReveal();
      });
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  function initReveals() {
    const els = $$('[data-reveal]');
    const check = () => {
      const h = window.innerHeight || 800;
      els.forEach((el) => {
        if (el.classList.contains('in')) return;
        const r = el.getBoundingClientRect();
        if (r.top < h * 0.92 && r.bottom > 0) el.classList.add('in');
      });
    };
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((en) => en.forEach((x) => { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } }), { threshold: 0.12 });
      els.forEach((el) => io.observe(el));
    }
    return check;
  }

  // ---------- boot ----------
  renderServicePage();
  renderSuburbPage();
  applyBrand();
  renderDatalist();
  renderHeader();
  renderPromo();
  renderFooter();
  renderCallbar();
  bindValues();
  initOdometer();
  initHeroSearch();
  initCarousel();
  initStepper();
  renderServices();
  renderWhy();
  initAreas();
  renderHubList();
  renderReviewGrid();
  renderTeam();
  initThanks();
  renderFaq();
  initBooking();

  // Hide reveal content now, then reveal what's on screen a couple of frames later so the transitions play.
  site.classList.add('js');
  const checkReveal = initReveals();
  requestAnimationFrame(() => requestAnimationFrame(() => { checkReveal(); initScroll(checkReveal); }));
})();
