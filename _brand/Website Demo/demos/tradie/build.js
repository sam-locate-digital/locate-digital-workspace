/*
  Builds the site from config.js. Run it after any change to config.js:
    node build.js

  - Writes the service pages (<trade>/<slug>.html) and suburb pages (areas/<slug>.html).
    Each is a small shell; main.js fills in the content when the page loads.
  - Sets every page's <title>, description, favicon and, on a live site, its canonical address.
  - CONFIG.production false (demo): every page carries noindex so Google never lists it.
    CONFIG.production true (live client site): noindex comes off (except thanks and 404),
    and sitemap.xml, robots.txt and vercel.json (clean URLs + CONFIG.redirects) are written.
  - Writes 404.html and favicon.svg.
*/
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const dir = __dirname;
const sandbox = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(dir, 'config.js'), 'utf8'), sandbox);
const C = sandbox.window.CONFIG;

const slugify = (s) => String(s).toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const attr = (s) => String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
const showPl = C.trades.includes('plumbing'), showEl = C.trades.includes('electrical'), both = showPl && showEl;
const live = C.production === true;
const siteUrl = String(C.siteUrl || '').replace(/\/?$/, '/');
const basePath = siteUrl ? new URL(siteUrl).pathname : '/';
const name = C.brand.name, suburb = C.address.suburb, phone = C.contact.phone;
const NOINDEX_ALWAYS = ['thanks', 'notfound'];

const write = (rel, text) => {
  const file = path.join(dir, rel);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, text);
  console.log('wrote', rel);
};

// ---------- 1. service and suburb shells ----------
const shell = (title, body, root) => `<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${attr(title)} · ${attr(name)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700&amp;family=Young+Serif&amp;display=swap">
<link rel="stylesheet" href="${root}styles.css">
</head>
<body ${body} data-title="${attr(title)}">
<div class="site">
<a class="skip" href="#main">Skip to content</a>

<header class="site-header"></header>

<main id="main">${body.includes('notfound') ? NOT_FOUND : ''}</main>

<footer class="footer"></footer>
</div>
<script src="${root}config.js"></script>
<script src="${root}main.js"></script>
</body>
</html>
`;

const NOT_FOUND = `
<section class="page-hero">
  <div class="wrap">
    <h1 class="h1-page">We couldn't find that page</h1>
    <p class="lede">The link may be old, or the page has moved. Everything's still here.</p>
    <div class="actions">
      <a class="btn btn-primary btn-lg" href="${basePath}">Back to home</a>
      <button type="button" class="btn btn-secondary btn-lg" data-open-booking>Book a job</button>
      <a class="btn btn-secondary btn-lg" href="tel:${phone.replace(/[^\d+]/g, '')}" data-tel>Call <span data-c="phone">${attr(phone)}</span></a>
    </div>
  </div>
</section>
`;

for (const [slug, sp] of Object.entries(C.servicePages)) {
  const svc = (C.services[sp.trade] || []).find((s) => s.page === slug);
  write(`${sp.trade}/${slug}.html`, shell(svc ? svc.name : sp.h1, `data-page="service" data-slug="${slug}"`, '../'));
}
const suburbH1 = (n) => (both ? 'Plumber and electrician in ' : showPl ? 'Plumber in ' : 'Electrician in ') + n;
for (const n of C.suburbs) write(`areas/${slugify(n)}.html`, shell(suburbH1(n), `data-page="suburb" data-slug="${slugify(n)}"`, '../'));
// The 404 page can be served at any depth, so it uses absolute paths from siteUrl.
write('404.html', shell('Page not found', 'data-page="notfound"', basePath));

// ---------- 2. favicon: the brand's first letter on its accent colour ----------
const accent = /^#[0-9a-f]{6}$/i.test(C.accent || '') ? C.accent : '#1F45D6';
write('favicon.svg', `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="${accent}"/><text x="32" y="45" font-family="Georgia, serif" font-size="40" text-anchor="middle" fill="#ffffff">${attr(name.trim()[0] || 'E')}</text></svg>\n`);

// ---------- 3. every page's head ----------
const tradeWords = both ? 'plumbers and electricians' : showPl ? 'plumbers' : 'electricians';
const describe = (page, slug) => {
  if (page === 'home') return `${C.brand.fullName}: licensed ${tradeWords} based in ${suburb}. Book online or call ${phone}.`;
  if (page === 'hub' && slug === 'plumbing') return `Hot water, blocked drains, leaks, gas and renovations. Licensed plumbers from ${name}, based in ${suburb}.`;
  if (page === 'hub') return `Power faults, switchboards, lights and smoke alarms. Licensed electricians from ${name}, based in ${suburb}.`;
  if (page === 'service') return (C.servicePages[slug] || {}).intro || '';
  if (page === 'suburb') { const n = C.suburbs.find((s) => slugify(s) === slug) || ''; return `${suburbH1(n)}. ${name} works in ${n} most weeks. Book online or call ${phone}.`; }
  if (page === 'landlords') return `One booking for every job at your rentals. ${name} deals with your tenant and sends you photos, invoices and certificates.`;
  if (page === 'reviews') return `What customers say about ${name}: ${C.stats.rating} average from ${C.stats.reviewCount} Google reviews.`;
  if (page === 'about') return `${name} is a family business run from ${suburb}. Meet the licensed team who'll turn up for your job.`;
  if (page === 'emergency') return `Burst pipe, gas smell or power fault? Call ${name} on ${phone}, day or night, and see what to do while you wait.`;
  if (page === 'book') return `Book a job with ${name} online. Tell us what's wrong and when suits, and we'll text you a time.`;
  if (page === 'legal') return `The ${slug === 'terms' ? 'terms of service' : 'privacy policy'} for ${name}.`;
  return '';
};

const htmlFiles = [];
(function walk(rel) {
  for (const entry of fs.readdirSync(path.join(dir, rel), { withFileTypes: true })) {
    const r = rel ? rel + '/' + entry.name : entry.name;
    if (entry.isDirectory()) { if (!['design', 'node_modules', 'images'].includes(entry.name) && !entry.name.startsWith('.')) walk(r); }
    else if (entry.name.endsWith('.html')) htmlFiles.push(r);
  }
})('');

const sitemap = [];
for (const rel of htmlFiles) {
  const file = path.join(dir, rel);
  let html = fs.readFileSync(file, 'utf8');
  const body = (html.match(/<body([^>]*)>/) || [])[1] || '';
  const data = (k) => ((body.match(new RegExp(`data-${k}="([^"]*)"`)) || [])[1] || '');
  const page = data('page') || 'home', slug = data('slug');
  const root = '../'.repeat(rel.split('/').length - 1);
  const cleanPath = rel === 'index.html' ? '' : rel.replace(/\.html$/, '');
  const indexable = live && !NOINDEX_ALWAYS.includes(page);

  // Strip what this script manages, then add it back for this build.
  html = html.replace(/^<meta name="(robots|description)"[^>]*>\n/gm, '').replace(/^<link rel="(canonical|icon)"[^>]*>\n/gm, '');
  const title = page === 'home'
    ? `${name} · ${both ? 'Plumbing + Electrical' : showPl ? 'Plumbing' : 'Electrical'}`
    : `${data('title').replace(/&amp;/g, '&')} · ${name}`;
  html = html.replace(/<title>[^<]*<\/title>/, `<title>${attr(title)}</title>`);
  const desc = describe(page, slug);
  const head = [
    indexable ? '' : '<meta name="robots" content="noindex, nofollow">',
    desc ? `<meta name="description" content="${attr(desc)}">` : '',
    indexable ? `<link rel="canonical" href="${siteUrl}${cleanPath}">` : '',
    `<link rel="icon" href="${page === 'notfound' ? basePath : root}favicon.svg" type="image/svg+xml">`
  ].filter(Boolean).map((l) => l + '\n').join('');
  html = html.replace(/(<meta name="viewport"[^>]*>\n)/, `$1${head}`);
  fs.writeFileSync(file, html);
  if (indexable) sitemap.push(siteUrl + cleanPath);
}
console.log(`updated the head of ${htmlFiles.length} pages (${live ? 'production' : 'demo: noindex on every page'})`);

// ---------- 4. production-only files ----------
if (live) {
  const today = new Date().toISOString().slice(0, 10);
  write('sitemap.xml', `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${sitemap.sort().map((u) => `  <url><loc>${u}</loc><lastmod>${today}</lastmod></url>`).join('\n')}\n</urlset>\n`);
  write('robots.txt', `User-agent: *\nAllow: /\n\nSitemap: ${siteUrl}sitemap.xml\n`);
  const redirects = (C.redirects || []).filter((r) => r && r.from && r.to).map((r) => ({ source: r.from, destination: r.to, permanent: true }));
  write('vercel.json', JSON.stringify({ cleanUrls: true, redirects }, null, 2) + '\n');
}
