/*
  Builds the Harlow Home Loans demo from config.js and src/. Run it after any change:
    node build.js

  - Writes one .html page per module in src/pages/ (src/pages/first-home.js → first-home.html).
    Header, footer, drawer, reviews and the closing call to action come from src/partials.js.
  - CONFIG.production false (demo): every page carries noindex.
  - Writes favicon.svg.
  - Then checks the output: no /_blob/ URLs, .dc.html links or {{ left, and every local
    src/href points at a file that exists. Exits with an error if anything fails.
*/
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const dir = __dirname;
const sandbox = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(dir, 'config.js'), 'utf8'), sandbox);
const C = sandbox.window.CONFIG;
const R = sandbox.window.REVIEWS;
const { layout } = require('./src/partials');

const write = (rel, text) => { fs.writeFileSync(path.join(dir, rel), text); console.log('wrote', rel); };

// ---------- 1. pages ----------
const pagesDir = path.join(dir, 'src', 'pages');
const built = [];
for (const file of fs.readdirSync(pagesDir).filter((f) => f.endsWith('.js')).sort()) {
  const page = require(path.join(pagesDir, file))(C, R);
  const out = file.replace(/\.js$/, '.html');
  write(out, layout(C, page));
  built.push(out);
}

// ---------- 2. favicon ----------
write('favicon.svg', `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1F45D6"/><text x="32" y="45" font-family="Georgia, serif" font-size="38" text-anchor="middle" fill="#fff">H</text></svg>\n`);

// ---------- 3. checks ----------
const problems = [];
for (const out of built) {
  const html = fs.readFileSync(path.join(dir, out), 'utf8');
  if (html.includes('/_blob/')) problems.push(`${out}: contains a /_blob/ URL`);
  if (html.includes('.dc.html')) problems.push(`${out}: links to a .dc.html file`);
  if (html.includes('{{')) problems.push(`${out}: contains {{`);
  for (const [, url] of html.matchAll(/(?:src|href)="([^"#?]+)"/g)) {
    if (/^(https?:|tel:|mailto:|data:)/.test(url) || url === './') continue;
    if (!fs.existsSync(path.join(dir, url))) problems.push(`${out}: links to ${url}, which doesn't exist yet`);
  }
}
const unique = [...new Set(problems)];
if (unique.length) {
  console.warn(`\n${unique.length} problem(s):\n  ` + unique.join('\n  '));
  process.exitCode = 1;
} else {
  console.log(`\nChecks passed: ${built.length} page(s), no /_blob/, .dc.html or {{ left, every local link resolves.`);
}
