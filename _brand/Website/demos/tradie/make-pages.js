/*
  Writes the service pages (<trade>/<slug>.html) and suburb pages (areas/<slug>.html)
  from config.js. Each file is a small shell; main.js fills in the content from
  CONFIG.servicePages and CONFIG.suburbDetail when the page loads.

  Run it again after adding or removing suburbs or service pages in config.js:
    node make-pages.js
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
const both = C.trades.includes('plumbing') && C.trades.includes('electrical');

const shell = (title, body) => `<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>${attr(title)} · ${attr(C.brand.name)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700&amp;family=Young+Serif&amp;display=swap">
<link rel="stylesheet" href="../styles.css">
</head>
<body ${body} data-title="${attr(title)}">
<div class="site">
<a class="skip" href="#main">Skip to content</a>

<header class="site-header"></header>

<main id="main"></main>

<footer class="footer"></footer>
</div>
<script src="../config.js"></script>
<script src="../main.js"></script>
</body>
</html>
`;

const write = (rel, html) => {
  const file = path.join(dir, rel);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, html);
  console.log('wrote', rel);
};

for (const [slug, sp] of Object.entries(C.servicePages)) {
  const svc = (C.services[sp.trade] || []).find((s) => s.page === slug);
  write(`${sp.trade}/${slug}.html`, shell(svc ? svc.name : sp.h1, `data-page="service" data-slug="${slug}"`));
}

for (const name of C.suburbs) {
  const title = (both ? 'Plumber and electrician in ' : C.trades.includes('plumbing') ? 'Plumber in ' : 'Electrician in ') + name;
  write(`areas/${slugify(name)}.html`, shell(title, `data-page="suburb" data-slug="${slugify(name)}"`));
}
