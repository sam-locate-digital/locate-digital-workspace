---
name: publish-demo
description: Commit and publish Locate Digital's prospect demo websites to demo.locatedigital.io. Rebuilds the changed demo, makes sure its Vercel redirect and ignore rules are in place, commits only that demo, pushes the _brand/Website/demos subtree to the Locate-digital-demos GitHub repo (Vercel deploys it automatically) and checks the live pages. Use when Sam says "publish the demo", "push the demo live", "deploy the tradie/mortgage-broker demo", "update demo.locatedigital.io", or after editing anything in _brand/Website/demos/. Building a new demo from a Claude Design handoff is design-to-site, which calls this at the end.
---

# Publish a demo

Demo sites live in `G:\My Drive\Claude Code.Locate\_brand\Website\demos\<industry>\` and are served at `https://demo.locatedigital.io/<industry>/` by one Vercel project. That project watches the private repo https://github.com/sam-locate-digital/Locate-digital-demos (git remote `demos` in the workspace repo). Pushing the `demos` folder there is the whole deploy.

Sam asking to publish is the go-ahead to commit and push. Don't ask again, but do show what will be committed.

## 1. Work out what's changing

```bash
cd "G:/My Drive/Claude Code.Locate"
git status --short -- _brand/Website/demos
```
Name the demo(s) being published. Leave everything else in the workspace alone: other untracked files, other clients, the full-size `*.png` originals in demo folders (these are deliberately never committed).

## 2. Rebuild

For each changed demo with a `build.js`:
```bash
cd "_brand/Website/demos/<industry>" && node build.js
```
It must finish without errors. For mortgage-broker-style builds that means **Checks passed**: no `/_blob/`, `.dc.html` or `{{` left, every local link resolves. Fix failures before going on. Never publish a demo whose nav links point at pages that don't exist.

Check `config.js` still says `production: false`. Demos always carry noindex.

## 3. Vercel config (new demos only)

In `_brand/Website/demos/vercel.json`, every demo needs a trailing-slash redirect, because its pages use relative paths:
```json
{ "source": "/<industry>", "destination": "/<industry>/", "permanent": true }
```
Add it to `redirects` next to the existing ones. Leave the `/` → www.locatedigital.io redirect, `cleanUrls` and the `X-Robots-Tag: noindex, nofollow` header as they are.

`_brand/Website/demos/.vercelignore` keeps working files off the web: `*.md`, `*.png`, `*/design`, `*/build.js`, `*/src`. If the demo has another source-only folder, add it there.

## 4. Commit (only the demos)

```bash
cd "G:/My Drive/Claude Code.Locate"
git add _brand/Website/demos/<industry> _brand/Website/demos/vercel.json _brand/Website/demos/.vercelignore
git diff --cached --stat
git commit -F - <<'EOF'
feat(demos): <what changed, in plain words>

<one or two lines of detail if useful>

Co-Authored-By: <the attribution line from the current session's instructions>
EOF
```
Use `fix(demos): …` for fixes. Check the staged list doesn't include `checks/` screenshots, `node_modules` or PNG originals. LF/CRLF warnings are harmless.

## 5. Push the subtree

```bash
cd "G:/My Drive/Claude Code.Locate"
git subtree split --prefix=_brand/Website/demos -b demos-deploy
git push demos demos-deploy:main
```
If the push is rejected as non-fast-forward, someone changed the demos repo directly. Stop and tell Sam rather than force-pushing.

## 6. Verify it's live

Vercel takes about 30–60 seconds. Then, in the browser pane on `https://demo.locatedigital.io/<industry>/`, run:
```js
const pages = [/* every page name without .html, e.g. 'first-home','team' */];
const res = await Promise.all(pages.map((p) => fetch(p, { cache: 'no-store' }).then((r) => [p, r.status])));
const slash = await fetch('/<industry>', { redirect: 'follow' });
({ notOk: res.filter(([, s]) => s !== 200), redirect: slash.url, robots: slash.headers.get('x-robots-tag') })
```
Expect no failing pages, the redirect ending in `/<industry>/`, and `noindex, nofollow`. A 404 straight after pushing usually means the deploy hasn't finished: wait and retry once before investigating.

## 7. Report

Give Sam the live link, the commit hash, what changed, and what was verified. If anything visible is still unfinished (pale-blue photo boxes, `[PLACEHOLDER]` text), say whether it's fine to send to prospects on its own or only for a guided demo.
