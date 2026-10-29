---
name: design-to-site
description: Turn a Claude Design website handoff (a folder or zip with canvas/*.dc.html, assets/asset-map.json and CLAUDE.md) into a working static demo site in _brand/Website/demos/<industry>/, check it with Playwright and Lighthouse, then publish it with publish-demo. Plain HTML/CSS/JS built by node build.js, no npm. Use when Sam says "design to site", "build this Claude Design export", "turn this handoff into a site", "rebuild the canvas", "new industry demo from Claude Design", or points at a *-handoff folder or .dc.html files. For publishing changes to an existing demo, use publish-demo instead.
---

# Design to site

Rebuild a Claude Design canvas as a static demo site that matches the tradie and mortgage-broker demos, check it properly, and put it live at `demo.locatedigital.io/<industry>/`.

The reference implementation is `G:\My Drive\Claude Code.Locate\_brand\Website\demos\mortgage-broker\` (Harlow Home Loans). It was built from a canvas handoff with this exact process. Read its `build.js`, `src/partials.js`, `js/main.js` and `js/form.js` before writing anything: most new sites reuse 80% of them.

Bundled scripts (run them from their skill path):
- `$HOME/.claude/skills/design-to-site/scripts/convert.js`: canvas pages → `src/pages/*.js` modules.
- `$HOME/.claude/skills/design-to-site/scripts/qa.js`: screenshots, layout, keyboard and reduced-motion checks.
- `$HOME/.claude/skills/design-to-site/scripts/contact-sheet.ps1`: contact sheet for matching photos or reviewing screenshots.

## Rules that save hours

- **Never run npm, Astro, Vite or any framework inside Google Drive.** `npm install` on `G:` fails with EBADF / TAR_ENTRY_ERROR, and Drive refuses junctions ("Local NTFS volumes are required"). Sites are plain HTML/CSS/JS built by a dependency-free `node build.js`. Tools that need packages (Playwright, Lighthouse) install once in `%LOCALAPPDATA%\locate-qa` on the local disk.
- **Never edit the handoff's `canvas/`.** It is the spec. Copy the stylesheet into the demo and override there.
- **Keep every `[PLACEHOLDER…]` exactly** unless Sam explicitly asks for demo values instead. Keep "Illustrative reviews" notes, compliance placeholders and `production: false` (noindex on every page).
- **Respect the handoff's own CLAUDE.md**: fonts, colours, banned patterns, behaviours. It overrides anything generic here.

## Step 1: Read and plan (stop for Sam's OK)

1. Find the handoff. If it's a zip, unzip it into its own folder next to the zip. Read its `CLAUDE.md`, `canvas/canvas.json`, `assets/asset-map.json` and any `photos/PHOTO-LIST.md`.
2. Survey the canvas before reading it all:
   ```bash
   cd "<handoff>/canvas"
   for f in *.dc.html; do m=$(sed -n '/<main/,/<\/main>/p' "$f"); echo "## $f: vals=[$(echo "$m" | grep -o '{{[^}]*}}' | sort -u | tr '\n' ' ')] events=[$(echo "$m" | grep -o ' on[A-Z][a-zA-Z]*="[^"]*"' | sort -u | tr '\n' ' ')] loops=$(echo "$m" | grep -c '<sc-for')"; done
   ```
   Pages with only site-wide values and `{{openPage}}` convert automatically. Pages with loops, page-specific handlers or `componentDidMount` logic need hand work (in Harlow: the homepage, the Team list and the health check quiz).
3. Read the shared components (Header, Footer, Enquiry/EnquiryForm, carousels, CTA bands) and the homepage in full.
4. Ask Sam two things, then give a short plan:
   - The **industry slug** for the URL (`demos/<slug>/` → `demo.locatedigital.io/<slug>/`).
   - **Placeholders:** keep `[PLACEHOLDER]` markers (fine when Sam walks a prospect through it as a template), or swap in obviously fictional demo values (needed if the link will be sent to prospects on its own).
   The plan lists pages → files, which pages need hand work, the photo situation, and anything in the canvas that's unclear.

## Step 2: Set up the demo folder

1. Create `_brand/Website/demos/<slug>/` with:
   - `styles.css`: the handoff's stylesheet, copied unchanged. Put any SVGs it references with `url(...)` next to it.
   - `icons/`, `images/`: from the handoff's assets and photos. Use the asset map's file names, `photos/` → `images/`.
   - `config.js`: `window.CONFIG` (brand, contact, hours, team, compliance, `production: false`) plus `window.REVIEWS` if the design has reviews. Merge every `CONFIG` block from the canvas scripts into it.
   - `build.js`, `src/partials.js`, `src/assets.js`, `js/main.js`, `js/form.js`: start from the mortgage-broker copies and adapt them to this design's header, footer, drawer, form and components. `src/partials.js` must export `esc`, `photo`, `layout` and `component(name, props, C, R)`, which maps each canvas `<dc-import>` component to a partial.
   - `.gitignore` containing `checks/`.
2. **Photos.** If the handoff has no photos but loose images exist (e.g. `Photorealistic-*.png` beside the handoff), match them to the photo list by content:
   ```powershell
   powershell -File "$HOME\.claude\skills\design-to-site\scripts\contact-sheet.ps1" -Dir "<folder with the PNGs>" -Out "<scratchpad>\sheet.png" -Filter "*.png"
   ```
   Read the sheet, map each image to its asset id, and save it as JPG (quality 82) under the asset-map name with System.Drawing. If portraits are missing but a team photo shows the same people, crop 4:5 head-and-shoulders portraits from the full-size original and save them at 400×500. Anything still missing renders as a pale-blue box via `photo()`. Say so in the report.

## Step 3: Shell and homepage first

Build `src/partials.js` (layout, header, footer, drawer shell, shared components) and `src/pages/index.js` by hand from the canvas homepage. Port the interactive logic from the canvas `renderVals()` / class methods into vanilla JS in `js/main.js` and `js/form.js`, keeping the same class names so `styles.css` works unchanged. Patterns that worked in Harlow:
- Buttons that open the enquiry drawer carry `data-enquire='{"source":"…"}'`. The drawer merges the page's `drawerDefaults` under that prefill and resets the form each time it opens.
- Re-render forms by replacing an inner container. Keep the `aria-live` region outside it, restore focus by `data-key`, and update error messages in place while the user types.
- Reveals use `.rv` / `.ul` + IntersectionObserver, gated by `html.js-rv`. Odometers, auto-advancing steps and carousels check `prefers-reduced-motion` and jump to their end state.
- `[hidden]{display:none!important}` in the layout, because components with `display:grid/flex` otherwise ignore `hidden`.

Run `node build.js`, preview it (the `demo-tradie` launch config serves `_brand/Website/demos` on port 5173; open `http://localhost:5173/<slug>/`), and test the drawer, form steps, validation and Esc. Missing-page warnings for the pages not built yet are expected at this stage.

## Step 4: Convert the remaining pages

```bash
node "$HOME/.claude/skills/design-to-site/scripts/convert.js" "<handoff>/canvas" "_brand/Website/demos/<slug>/src/pages" PageA PageB PageC ...
```
List every page except the homepage and the hand-built ones. Add `--values values.json` (a map of `{{key}}` to `${…}` expressions) if the design uses site-wide values beyond the defaults: phone, phoneHref, email, mailHref, hours, office, feePolicy, entity, generalInfo. The script reads each page's drawer defaults and inline-form prefill from its canvas script, and prints anything it couldn't convert under **NEEDS HAND WORK**. Fix those by hand in the generated module (loops become `${C.list.map(...)}`; page-specific handlers become `data-enquire` attributes or a small page script passed in the module's `scripts: []`).

Then `node build.js` must report **Checks passed** (no `/_blob/`, `.dc.html` or `{{` left, every local link resolves). Confirm placeholders survived:
```bash
node -e 'const fs=require("fs"),C="<handoff>/canvas/",O="_brand/Website/demos/<slug>/";const k=n=>n==="Main"?"index":n.replace(/([a-z])([A-Z])/g,"$1-$2").toLowerCase();let t=0,b=0;for(const f of fs.readdirSync(C).filter(f=>f.endsWith(".dc.html"))){const o=O+k(f.slice(0,-8))+".html";if(!fs.existsSync(o))continue;const s=fs.readFileSync(C+f,"utf8"),out=fs.readFileSync(o,"utf8");for(const p of new Set(s.slice(s.indexOf("<main"),s.indexOf("</main>")).match(/\[[^\]]*PLACEHOLDER[^\]]*\]/g)||[])){t++;if(!out.includes(p)){b++;console.log(f,"missing",p)}}}console.log("placeholders",t,"missing",b)'
```

## Step 5: Check

1. One-time setup (local disk, reuses installed Chrome, no browser download):
   ```bash
   mkdir -p "$LOCALAPPDATA/locate-qa" && cd "$LOCALAPPDATA/locate-qa" && [ -d node_modules/playwright-core ] || (npm init -y >/dev/null && npm install --no-audit --no-fund playwright-core lighthouse)
   ```
2. With the preview server running:
   ```bash
   NODE_PATH="$LOCALAPPDATA/locate-qa/node_modules" node "$HOME/.claude/skills/design-to-site/scripts/qa.js" "http://localhost:5173/<slug>/" "G:/My Drive/Claude Code.Locate/_brand/Website/demos/<slug>" "G:/My Drive/Claude Code.Locate/_brand/Website/demos/<slug>/checks"
   cd "$LOCALAPPDATA/locate-qa" && npx lighthouse "http://localhost:5173/<slug>/" --only-categories=accessibility,best-practices,performance --chrome-path="C:/Program Files/Google/Chrome/Application/chrome.exe" --chrome-flags="--headless=new" --output=json --output-path=./lh.json --quiet && node -e 'const r=require("./lh.json");for(const[k,c]of Object.entries(r.categories))console.log(k,Math.round(c.score*100));for(const ref of r.categories.accessibility.auditRefs){const a=r.audits[ref.id];if(a.score!==null&&a.score<1)console.log(" a11y fail:",a.id,"-",a.title)}'
   ```
   Accessibility must be 95+. SEO is ignored, because noindex is deliberate.
3. **Look at the screenshots, don't just trust the script.** Make contact sheets (`-Filter "*-1440.png" -Cols 7 -Width 260 -Crop 2600`, and `"*-390.png" -Cols 11 -Width 160 -Crop 3000`) and read them. Things the script can't see: blank photo areas, text split into columns, sections that look nothing like the canvas.
4. Fix what's wrong, rebuild, and re-run `qa.js` until it reports 0 issues. Fixes to the handoff's CSS go at the end of the demo's `styles.css` with a one-line comment saying why.

Known traps:
- **Fades in screenshots:** headings caught mid fade-in look faded in browser-pane screenshots. That's an animation, not a bug. `qa.js` waits them out.
- **Lazy images in full-page shots:** `html{scroll-behavior:smooth}` stops lazy images loading during a fast scroll. `qa.js` already disables it and forces eager loading.
- **Flex text blocks:** a `display:flex` on a text block (Harlow's `.legal-note`) turns a sentence with inline spans into columns. Override with `display:block`.
- **Wordmark names:** wordmarks built as `<b>Name</b><i>Tagline</i>` need a space between them, or the accessible name won't match the visible text.

## Step 6: Publish and report

1. Add the demo's trailing-slash redirect and run the **publish-demo** skill (`/publish-demo`). It commits, pushes and verifies the live URL.
2. Report to Sam:
   - the live link
   - pages built
   - what was converted automatically and what was done by hand
   - photo status
   - QA results: issues found and fixed, Lighthouse scores
   - anything that couldn't match the canvas
   - whether the site is ready to send to prospects on its own: no pale-blue boxes left, and placeholders either swapped for demo values or deliberately kept for a guided demo
3. Update the `demos-deploy` memory with the new demo and anything new learned.
