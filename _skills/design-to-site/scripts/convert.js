/*
  Converts Claude Design canvas pages (*.dc.html) into page modules for a demo site's build.js.

    node convert.js <canvas-dir> <out-pages-dir> [--values values.json] Page1 Page2 ...

  For each page it writes <out-pages-dir>/<kebab-name>.js exporting
    (C, R) => ({ title, description, active, drawerDefaults, body })
  where body is the page's <main> markup with:
    - <dc-import name="X" a-b="…"> → ${component('X', { aB: … , prefill }, C, R)}   (Header/Footer/drawer imports are dropped: the layout adds them)
    - <img src="/_blob/…">         → ${photo({...})}   (pale-blue box when the file is missing)
    - other /_blob/ URLs           → local paths from asset-map.json (assets/ prefix dropped, photos/ → images/)
    - X.dc.html links              → x.html (Main → ./)
    - onClick="{{openPage}}"       → data-enquire="{}"  (opens the drawer with the page defaults)
    - {{key}} for site-wide values → ${…} expressions from the values map (defaults below, override with --values)
  Anything it can't convert (loops, conditionals, page-specific handlers) is left in place and listed
  under NEEDS HAND WORK. build.js fails on any {{ left, so nothing slips through.
*/
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const canvas = args.shift();
const outDir = args.shift();
let values = {
  phone: '${esc(C.contact.phone)}', phoneHref: '${C.contact.phoneHref}', email: '${esc(C.contact.email)}', mailHref: 'mailto:${C.contact.email}',
  hours: '${esc(C.hours)}', office: '${esc(C.contact.office)}', feePolicy: '${esc(C.compliance.feePolicy)}', entity: '${esc(C.compliance.entity)}',
  generalInfo: '${esc(C.compliance.generalInfo)}',
};
const vi = args.indexOf('--values');
if (vi !== -1) { values = Object.assign(values, JSON.parse(fs.readFileSync(args[vi + 1], 'utf8'))); args.splice(vi, 2); }
const PAGES = args;
if (!canvas || !outDir || !PAGES.length) { console.error('usage: node convert.js <canvas-dir> <out-pages-dir> [--values values.json] Page1 Page2 ...'); process.exit(1); }

const mapFile = [path.join(canvas, '..', 'assets', 'asset-map.json'), path.join(canvas, 'asset-map.json')].find((f) => fs.existsSync(f));
const map = mapFile ? JSON.parse(fs.readFileSync(mapFile, 'utf8')) : {};
const local = (u) => {
  const p = map[u]; if (!p) { report.push(`unmapped ${u}`); return u; }
  return p.replace(/^photos\//, 'images/').replace(/^assets\//, '');
};
const kebab = (n) => n.replace(/([a-z0-9])([A-Z])/g, '$1-$2').toLowerCase();
const route = (n) => (n === 'Main' || n === 'Home' || n === 'Index' ? './' : kebab(n) + '.html');
const camel = (s) => s.replace(/-([a-z])/g, (_, c) => c.toUpperCase());
const attrs = (s) => { const o = {}; for (const [, k, v] of s.matchAll(/([a-zA-Z-]+)="([^"]*)"/g)) o[k] = v; return o; };
const LAYOUT_PARTS = ['Header', 'Footer'];

const report = [];
fs.mkdirSync(outDir, { recursive: true });
for (const name of PAGES) {
  const src = fs.readFileSync(path.join(canvas, name + '.dc.html'), 'utf8');
  const title = (src.match(/<title>([^<]*)<\/title>/) || [])[1] || name;
  const description = (src.match(/name="description" content="([^"]*)"/) || [])[1] || '';
  const active = (src.match(/<dc-import name="Header"[^>]*active="([^"]*)"/) || [])[1] || '';
  const script = src.slice(src.indexOf('data-dc-script'));

  // Page constants and the prefill the page passes to its inline form and drawer.
  const consts = {};
  for (const [, k, v] of script.matchAll(/\bconst ([A-Z_]+) = '([^']*)';/g)) consts[k] = v;
  const evalObj = (txt) => { try { return Function(...Object.keys(consts), 'return (' + txt + ')')(...Object.values(consts)); } catch (e) { report.push(`${name}: couldn't read ${txt}`); return {}; } };
  const inl = script.match(/inlinePrefill = (\{[^;]*\});/);
  const inlinePrefill = inl ? evalObj(inl[1]) : null;
  let defaults = {};
  const op = script.match(/open\(p\) \{[^\n]*prefill: (\{[^}]*?)\.\.\.(q|\(p \|\| \{\}\)) \}/) || script.match(/open: \(p\) => [^\n]*prefill: (\{[^}]*?)\.\.\.(q|\(p \|\| \{\}\)) \}/);
  if (op) defaults = evalObj(op[1].replace(/,\s*$/, '') + '}');

  // Body: from <main> up to the footer import.
  const start = src.indexOf('<main');
  if (start === -1) { report.push(`${name}: no <main> found, skipped`); continue; }
  const open = src.indexOf('>', start) + 1;
  let end = src.indexOf('<dc-import name="Footer"');
  if (end === -1) end = src.indexOf('</main>');
  let b = src.slice(open, end).replace('</main>', '').trim();

  b = b.replace(/`/g, '\\`').replace(/\$\{/g, '\\${');
  b = b.replace(/ hint-[a-z-]+="[^"]*"/g, '');
  b = b.replace(/<dc-import name="(\w+)"([^>]*)><\/dc-import>/g, (m, comp, a) => {
    const o = attrs(a); delete o.style;
    if (LAYOUT_PARTS.includes(comp) || (comp === 'Enquiry' && o.variant === 'drawer')) return '';
    const props = {};
    for (const [k, v] of Object.entries(o)) {
      if (/^\{\{.*\}\}$/.test(v)) {
        if (/inlinePrefill/.test(v)) props[camel(k)] = inlinePrefill;
        else if (/\{\{ *true *\}\}/.test(v)) props[camel(k)] = true;
        else if (/\{\{ *false *\}\}/.test(v)) props[camel(k)] = false;
        else report.push(`${name}: <${comp}> prop ${k}=${v} needs a value`);
      } else props[camel(k)] = v;
    }
    return '${component(' + JSON.stringify(comp) + ', ' + JSON.stringify(props) + ', C, R)}';
  });
  b = b.replace(/ onClick="\{\{openPage\}\}"/g, ' data-enquire="{}"');
  b = b.replace(/ (open|checked|disabled)="\{\{ true \}\}"/g, ' $1').replace(/ (open|checked|disabled)="\{\{ false \}\}"/g, '');
  b = b.replace(/\{\{(\w+)\}\}/g, (m, k) => (k in values ? values[k] : m));
  b = b.replace(/<img([^>]*?)src="(\/_blob\/[0-9a-f]+)"([^>]*)>/g, (m, pre, u, post) => {
    const o = attrs(pre + post);
    const opts = { src: local(u), alt: o.alt || '', width: Number(o.width) || 800, height: Number(o.height) || 600 };
    if (o.class) opts.cls = o.class;
    if (o.loading !== 'lazy') opts.loading = 'eager';
    const extra = Object.keys(o).filter((k) => !['alt', 'width', 'height', 'class', 'loading'].includes(k));
    if (extra.length) report.push(`${name}: <img> attributes dropped: ${extra.join(', ')}`);
    return '${photo(' + JSON.stringify(opts) + ')}';
  });
  b = b.replace(/\/_blob\/[0-9a-f]+/g, (u) => local(u));
  b = b.replace(/href="(\w+)\.dc\.html(#[^"]*)?"/g, (m, n, h) => `href="${route(n)}${h || ''}"`);
  const left = b.match(/\{\{[^}]*\}\}|<sc-[a-z]+|<dc-import[^>]*>|\.dc\.html|on[A-Z]\w+="/g);
  if (left) report.push(`${name}: still to convert by hand: ${[...new Set(left)].join(' ')}`);

  const used = ['esc', 'photo', 'component'].filter((f) => b.includes(f + '('));
  const mod = `// ${title.replace(/ \|.*$/, '')} (canvas/${name}.dc.html)
const { ${used.join(', ') || 'esc'} } = require('../partials');

module.exports = (C, R) => ({
  title: ${JSON.stringify(title)},
  description: ${JSON.stringify(description)},
  active: ${JSON.stringify(active)},
  drawerDefaults: ${JSON.stringify(defaults)},
  body: \`
${b}\`,
});
`;
  const file = (name === 'Main' || name === 'Home' ? 'index' : kebab(name)) + '.js';
  fs.writeFileSync(path.join(outDir, file), mod);
  console.log(`${file.padEnd(22)} active=${active || '-'} drawer=${JSON.stringify(defaults)} inline=${JSON.stringify(inlinePrefill)}`);
}
console.log(report.length ? '\nNEEDS HAND WORK:\n  ' + report.join('\n  ') : '\nEverything converted. No hand work flagged.');
