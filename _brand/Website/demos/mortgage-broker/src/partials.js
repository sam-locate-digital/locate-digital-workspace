/*
  Shared pieces for build.js, ported from the canvas components:
  Header, Footer, Enquiry (drawer shell), ReviewRail, CtaBand, plus the page layout.
  Interactive behaviour lives in js/main.js and js/form.js.
*/
const fs = require('fs');
const path = require('path');

const root = path.join(__dirname, '..');
const attr = (s) => String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const enquire = (prefill) => `data-enquire="${attr(JSON.stringify(prefill))}"`;

const ICON = {
  arrow14: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>',
  arrow16: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>',
  phone: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"></path></svg>',
  close: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"></path></svg>',
  star: (s) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2.8 2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4L2.8 9.5l6.4-.8Z"></path></svg>`,
};

// An <img>, or a plain pale-blue box of the same shape when the photo hasn't been added yet (photos/PHOTO-LIST.md).
function photo({ src, alt = '', width, height, cls = '', loading = 'lazy' }) {
  if (fs.existsSync(path.join(root, src))) {
    return `<img${cls ? ` class="${cls}"` : ''} src="${src}" alt="${attr(alt)}" width="${width}" height="${height}" loading="${loading}">`;
  }
  const a11y = alt ? `role="img" aria-label="${attr(alt)}"` : 'aria-hidden="true"';
  return `<span${cls ? ` class="${cls}"` : ''} ${a11y} data-missing-photo="${src}" style="display:block;background:#EAF0FD;aspect-ratio:${width}/${height};width:100%"></span>`;
}

function header(C, active) {
  const cur = (k) => (active === k ? ' aria-current="page"' : '');
  const { phone, phoneHref } = C.contact;
  const hdr = enquire({ source: 'Header' });
  return `<a class="skip" href="#main">Skip to content</a>

<div class="promo" role="region" aria-label="Rate review offer" data-promo>
<p>${esc(C.promo)}</p>
<button type="button" class="promo-go" aria-label="Book a free rate review" ${enquire({ situation: 'refinance', source: 'Promo bar' })}><span>${ICON.arrow14}</span></button>
<button type="button" class="promo-x" aria-label="Dismiss this message" data-promo-x><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"></path></svg></button>
</div>

<header class="hdr" data-hdr>
<div class="wrap hdr-in">
<a class="wm" href="./" aria-label="Harlow Home Loans, home"><b>${esc(C.brand.short)}</b><i>Home Loans</i></a>

<nav class="nav" aria-label="Main">
<div class="nav-dd" data-dd>
<button type="button" class="nav-a" aria-expanded="false" aria-controls="buying-panel"${cur('buying')} data-dd-btn>Buying <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"></path></svg></button>
<div class="dd" id="buying-panel" hidden>
<a href="first-home.html"><b>First home</b><span>Deposits, schemes and pre-approval</span></a>
<a href="next-home.html"><b>Next home</b><span>Buying before you sell, bridging</span></a>
<a href="building.html"><b>Building</b><span>Construction loans, step by step</span></a>
<a href="self-employed.html"><b>Self-employed</b><span>Lenders who get business income</span></a>
</div>
</div>
<a class="nav-a" href="refinancing.html"${cur('refinancing')}>Refinancing</a>
<a class="nav-a" href="investing.html"${cur('investing')}>Investing</a>
<a class="nav-a" href="guides.html"${cur('guides')}>Guides</a>
<a class="nav-a" href="team.html"${cur('about')}>About</a>
</nav>

<button type="button" class="hdr-pill" tabindex="-1" data-pill ${hdr}>What are you planning? <span>${ICON.arrow14}</span></button>

<div class="hdr-right">
<a class="hdr-phone" href="${phoneHref}">${ICON.phone}${esc(phone)}</a>
<button type="button" class="btn btn-primary btn-sm hdr-book" ${hdr}>Book a free chat</button>
<button type="button" class="menu-btn" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu" data-menu-btn>
<svg data-ic-close hidden width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"></path></svg>
<svg data-ic-open width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"></path></svg>
</button>
</div>
</div>

<nav class="mnav" id="mobile-nav" aria-label="Mobile" hidden>
<div class="wrap">
<span class="mnav-h">Buying</span>
<a class="sub" href="first-home.html">First home <span aria-hidden="true">›</span></a>
<a class="sub" href="next-home.html">Next home <span aria-hidden="true">›</span></a>
<a class="sub" href="building.html">Building <span aria-hidden="true">›</span></a>
<a class="sub" href="self-employed.html">Self-employed <span aria-hidden="true">›</span></a>
<span class="mnav-h">More</span>
<a href="refinancing.html">Refinancing <span aria-hidden="true">›</span></a>
<a href="health-check.html">Refinance health check <span aria-hidden="true">›</span></a>
<a href="investing.html">Investing <span aria-hidden="true">›</span></a>
<a href="team.html">About and team <span aria-hidden="true">›</span></a>
<a href="reviews.html">Reviews <span aria-hidden="true">›</span></a>
<a href="guides.html">Guides <span aria-hidden="true">›</span></a>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; padding-top: 20px">
<a class="btn btn-secondary" href="${phoneHref}" style="border: 0; min-height: 52px; justify-content: center">Call us</a>
<button type="button" class="btn btn-primary" ${hdr} style="min-height: 52px">Book a free chat</button>
</div>
</div>
</nav>
</header>

<div class="callbar" role="region" aria-label="Quick contact" data-callbar hidden>
<a class="btn btn-secondary" href="${phoneHref}">${ICON.phone}Call</a>
<button type="button" class="btn btn-primary" ${hdr}>Book a free chat</button>
</div>`;
}

function footer(C) {
  const c = C.compliance;
  const { phone, phoneHref, email } = C.contact;
  return `<footer class="ftr">
<div class="wrap">
<div class="fcols">
<div class="fcol">
<a class="wm" href="./" aria-label="Harlow Home Loans, home"><b>${esc(C.brand.short)}</b><i>Home Loans</i></a>
<p style="margin-top: 12px; max-width: 340px">A small, family-run broking team helping buyers and homeowners across Melbourne.</p>
</div>
<div class="fcol">
<h4>Buying</h4>
<ul>
<li><a href="first-home.html">First home</a></li>
<li><a href="next-home.html">Next home</a></li>
<li><a href="building.html">Building</a></li>
<li><a href="self-employed.html">Self-employed</a></li>
</ul>
</div>
<div class="fcol">
<h4>Refinancing and investing</h4>
<ul>
<li><a href="refinancing.html">Refinancing</a></li>
<li><a href="health-check.html">Refinance health check</a></li>
<li><a href="investing.html">Investing</a></li>
<li><a href="guides.html">Guides</a></li>
<li><a href="reviews.html">Reviews</a></li>
</ul>
</div>
<div class="fcol">
<h4>Contact</h4>
<ul>
<li><a href="${phoneHref}">${esc(phone)}</a></li>
<li><a href="mailto:${email}">${esc(email)}</a></li>
<li><a href="team.html">Our team</a></li>
<li><a href="book.html">Book a free chat</a></li>
</ul>
<p class="small" style="margin-top: 10px; color: #5B6684">${esc(C.contact.office)} [PLACEHOLDER street address]<br>${esc(C.hours)}</p>
</div>
</div>

<div class="comp">
<p>${esc(c.entity)} ABN <span class="ph">${esc(c.abn)}</span> (Credit Representative <span class="ph">${esc(c.creditRep)}</span>) is authorised under Australian Credit Licence <span class="ph">${esc(c.acl)}</span> held by <span class="ph">${esc(c.licensee)}</span>. ${esc(c.generalInfo)}</p>
<p>${esc(c.feePolicy)} <span class="ph">[PLACEHOLDER: confirm fee policy]</span> Reviews shown on this demo site are illustrative.</p>
</div>

<div class="fbot">
<a href="credit-guide.html">Credit Guide</a>
<a href="privacy.html">Privacy Policy</a>
<a href="complaints.html">Complaints</a>
<a href="terms.html">Terms</a>
<span>© 2026 ${esc(C.brand.name)}</span>
</div>
</div>
</footer>`;
}

// The drawer shell; js/main.js opens it and js/form.js fills in the form.
const drawer = (defaults) => `<div class="drawer-wrap" data-drawer data-defaults="${attr(JSON.stringify(defaults || {}))}" hidden>
<button type="button" class="scrim" aria-label="Close" tabindex="-1" data-close></button>
<div class="drawer" role="dialog" aria-modal="true" aria-labelledby="enq-dlg-title">
<div class="drawer-h">
<b id="enq-dlg-title">Book a free 20-minute chat</b>
<button type="button" class="btn-icon arrow-btn" aria-label="Close" data-close>${ICON.close}</button>
</div>
<div data-enquiry-form data-uid="drw"></div>
</div>
</div>`;

// Inline enquiry form; js/form.js renders it.
const inlineForm = (prefill) => `<div data-enquiry-form data-uid="inl" data-prefill="${attr(JSON.stringify(prefill || {}))}"><noscript><p>Call us on the number alongside to book your free chat.</p></noscript></div>`;

function contactAside(C) {
  const { phone, phoneHref, email, office } = C.contact;
  return `<aside class="talk rv rise" style="--d: 140ms" aria-label="Contact details">
<p class="h3">Rather talk now?</p>
<a class="bigphone" href="${phoneHref}">${esc(phone)}</a>
<div class="kv">
<div><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path></svg><span>${esc(C.hours)}</span></div>
<div><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"></path><circle cx="12" cy="9.5" r="2.5"></circle></svg><span><span class="ph">[PLACEHOLDER street address]</span>, ${esc(office)}</span></div>
<div><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"></rect><path d="m3.5 6 8.5 7 8.5-7"></path></svg><a href="mailto:${email}">${esc(email)}</a></div>
</div>
<div class="map">
<svg viewBox="0 0 400 250" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="400" height="250" fill="#E6EDFB"></rect><path d="M0 70 L400 40 M0 160 L400 140 M0 225 L400 215 M80 0 L110 250 M210 0 L200 250 M320 0 L300 250" stroke="#FFFFFF" stroke-width="10" fill="none"></path><path d="M0 115 C120 100 260 120 400 95" stroke="#F8FAFF" stroke-width="16" fill="none"></path><rect x="226" y="160" width="58" height="40" rx="6" fill="#DCE5D2"></rect><rect x="20" y="180" width="44" height="30" rx="6" fill="#DCE5D2"></rect></svg>
<div class="pin"><b>Harlow Home Loans</b><svg width="28" height="34" viewBox="0 0 28 34" aria-hidden="true"><path d="M14 33s12-10.3 12-19A12 12 0 0 0 2 14c0 8.7 12 19 12 19Z" fill="#1F45D6"></path><circle cx="14" cy="14" r="4.5" fill="#fff"></circle></svg></div>
<span class="lab ph">[PLACEHOLDER map]</span>
</div>
<a class="textlink" href="https://www.google.com/maps/search/?api=1&amp;query=Box+Hill+VIC+3128">Get directions <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"></path></svg></a>
</aside>`;
}

function ctaBand(C, { hLead = "Let's work out your next ", hBrush = 'step', hTail = '', sub = 'Book a free 20-minute chat.', prefill = { source: 'Website' } } = {}) {
  return `<section class="band band-w2" aria-labelledby="cta-h" id="enquire">
<div class="wrap">
<div class="intro rv rise">
<h2 class="h2" id="cta-h">${esc(hLead)}<em class="ul">${esc(hBrush)}</em>${esc(hTail)}</h2>
<p class="lead">${esc(sub)} We'll call you back within <span class="ph">[PLACEHOLDER 1 business day]</span>.</p>
</div>
<div class="cta-grid">
<div class="rv rise" style="--d: 60ms">
${inlineForm(prefill)}
</div>
${contactAside(C)}
</div>
</div>
</section>`;
}

const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const FILTERS = [{ id: '', label: 'All' }, { id: 'first-home', label: 'First home' }, { id: 'next-home', label: 'Next home' }, { id: 'refinance', label: 'Refinance' }, { id: 'invest', label: 'Investing' }, { id: 'self-employed', label: 'Self-employed' }];

function reviewRail(R, { hLead = "Clients who've ", hBrush = 'made', hTail = ' their move', sub = '', filterKey, filterVal, mode = 'rail' } = {}) {
  const mentions = (r) => {
    if (!filterKey || !filterVal) return false;
    if (filterKey === 'broker') return r.broker === filterVal || r.quote.toLowerCase().includes(filterVal.toLowerCase());
    return r[filterKey] === filterVal;
  };
  let list = R.reviews.slice();
  if (mode === 'rail' && filterKey && filterVal) list = list.filter(mentions).concat(list.filter((r) => !mentions(r)));
  const card = (r, i, extra = '') => {
    const d = new Date(r.date + 'T12:00:00');
    const cls = mode === 'rail' ? 'rcard rv from-r' + (i === 0 ? ' big' : '') : 'rcard';
    const style = mode === 'rail' ? ` style="--d: ${Math.min(i, 4) * 80}ms"` : '';
    return `<article class="${cls}"${style}${extra}>
<div class="stars" role="img" aria-label="${r.rating} out of 5 stars">${ICON.star(18).repeat(r.rating)}</div>
<blockquote>“${esc(r.quote)}”</blockquote>
<footer><b>${esc(r.name)}</b><span class="cap">${esc(r.suburb)} · ${esc(r.situationLabel)}</span></footer>
<div class="rmeta"><span>Google review</span><span>${d.getDate()} ${MON[d.getMonth()]} ${d.getFullYear()}</span></div>
</article>`;
  };
  const arrows = mode === 'rail' ? `<div class="row" style="gap: 8px">
<button type="button" class="arrow-btn" aria-label="Previous reviews" disabled data-prev><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path></svg></button>
<button type="button" class="arrow-btn" aria-label="Next reviews" data-next><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg></button>
</div>` : '';
  const body = mode === 'grid'
    ? `<div class="filters" role="group" aria-label="Filter reviews">
${FILTERS.map((f) => `<button type="button" class="chip" aria-pressed="${f.id === '' ? 'true' : 'false'}" data-filter="${f.id}">${f.label}</button>`).join('')}
</div>
<div class="rgrid">
${list.map((r, i) => card(r, i, ` data-sit="${r.situation}"`)).join('\n')}
</div>`
    : `<div class="rv-rail" tabindex="0" aria-label="Client reviews, scroll sideways" role="region" data-rail>
${list.map((r, i) => card(r, i)).join('\n')}
</div>`;
  return `<div data-reviews="${mode}">
<div class="intro intro-row">
<div>
<h2 class="h2">${esc(hLead)}<em class="ul">${esc(hBrush)}</em>${esc(hTail)}</h2>
${sub ? `<p class="lead">${esc(sub)}</p>` : ''}
</div>
<div class="row" style="gap: 16px">
<p class="small" style="display: flex; align-items: center; gap: 8px; color: #2E3A5C"><span class="stars" aria-hidden="true">${ICON.star(16)}</span><b class="ink">${R.average.toFixed(1)}</b> average on Google <span class="ph">[PLACEHOLDER]</span></p>
${arrows}
</div>
</div>
${body}
<p class="cap" style="margin-top: 8px">Illustrative reviews for this demo. A live site only shows genuine reviews, used with permission.</p>
</div>`;
}

function layout(C, { title, description, active = '', drawerDefaults = {}, jsonLd, body }) {
  return `<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)}</title>
${description ? `<meta name="description" content="${attr(description)}">\n` : ''}${C.production ? '' : '<meta name="robots" content="noindex, nofollow">\n'}<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gloock&amp;family=Hanken+Grotesk:wght@400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="styles.css">
${jsonLd ? `<script type="application/ld+json">${JSON.stringify(jsonLd)}</script>\n` : ''}<style>[hidden]{display:none!important}</style>
</head>
<body>
<div class="page" style="font-family: 'Hanken Grotesk', 'Helvetica Neue', Arial, sans-serif; color: #46506A">
${header(C, active)}

<main id="main">
${body}
</main>

${footer(C)}
${drawer(drawerDefaults)}
</div>
<script src="config.js"></script>
<script src="js/form.js"></script>
<script src="js/main.js"></script>
</body>
</html>
`;
}

module.exports = { attr, esc, enquire, ICON, photo, ctaBand, contactAside, inlineForm, reviewRail, layout };
