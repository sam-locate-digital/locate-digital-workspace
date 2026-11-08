---
name: launch-site
description: Take a Locate Digital demo website live for a paying client, the same way every time, and look after it afterwards. Covers the three situations - moving a client off WordPress while keeping their domain and Google rankings, a new site the client edits themselves through Pages CMS, and a site Locate runs entirely. Creates the client's private GitHub repo and Vercel project, fills in their content, sets up redirects for a migration, switches the site to live, checks the real domain, and invites editors. Also makes later edits to a launched client site. Use when Sam says "launch the site for [client]", "take the demo live for [client]", "set up [client]'s website", "migrate [client] off WordPress", "give [client] editing access", "edit [client]'s website", or "/launch-site". Publishing prospect demos to demo.locatedigital.io is publish-demo, and building a new demo is design-to-site.
---

# Launch a client site

The process for Sam is `G:/My Drive/Claude Code.Locate/_ops/website-launch.md`. Read it first: it has the scenario table, the intake questions and the migration rules. This skill is how Claude runs the **(Claude)** steps. For tradie sites, also read `_ops/tradie-website-sop.md`. Its DNS steps (step 5) apply to every site.

## Ground rules

- **Ask Sam first** before anything that costs money (Vercel Pro, a domain, paid plans), touches DNS, changes `site.json` to `production: true`, invites someone, or touches the demo.locatedigital.io project (`locate-digital-demos`). Each needs its own yes.
- **The client's GitHub repo is the master copy.** The local copy at `clients/<client>/website/` is a clone of it. `git pull` before every edit. Never force-push, never `git subtree push` a client site.
- **Never run npm inside Google Drive** (fails with EBADF). Build in a copy in the scratchpad (step 4).
- **Never commit** `.env` files, keys, `node_modules/` or `dist/`.
- **Never write or edit a review's words.** Never present AI images or stock as the client's staff.

## Tools

- **GitHub:** `gh`, signed in as `sam-locate-digital`. If `gh` isn't on PATH, use `"/c/Program Files/GitHub CLI/gh.exe"`. In Git Bash, prefix `gh api` calls with `MSYS_NO_PATHCONV=1`.
- **Vercel:** the Vercel connector. Team `sam-cheng-s-projects`, team id `team_9ZkiMvdyUo4ytEncnzHycOZ6`. If a call returns 403 for the team, call `authorize_team_access` and give Sam the link.
- **Git identity:** copy it from the workspace repo into each new client repo (`git config user.name` / `user.email`).

## Step 1: Work out the job

Ask Sam, or read from `clients/<client>/CLAUDE.md`:
1. Client folder name and **scenario**: 1 (from WordPress), 2 (client edits), 3 (Locate runs it).
2. Template: mortgage broker → `_brand/Website Demo/demos/harlow-cms-test/`. Tradie → `_brand/Website Demo/demos/tradie/` (not editor-ready: fine for scenario 3, but tell Sam it needs converting to the `content/` shape before scenario 2).
3. Domain, DNS host, email host (from the intake in the guide, step 1).
4. Editors' emails (scenario 2).

If `clients/<client>/` doesn't exist, run client-onboarding first.

If the site already exists (`clients/<client>/website/.git`), this is an **edit**: skip to "Editing a launched site".

## Step 2: Create the repo

```bash
cd "G:/My Drive/Claude Code.Locate/clients/<client>"
mkdir website
tar -C "<template folder>" --exclude=.git --exclude=node_modules --exclude=dist --exclude=HANDOVER.md --exclude=checks -cf - . | tar -C website -xf -
```
Then in `website/`:
1. Reset test content. For the Harlow template, compare `content/` and `images/` against the template's first commit (`git -C "<template>" show 5d3206b --stat` and `git -C "<template>" diff 5d3206b -- content images`), and remove test team members, "[TESTING]" names and test photos.
2. `site.json`: `"production": false`, `"url": ""`, `"formEndpoint": ""`.
3. `package.json` `name`: `site-<client>`.
4. Rewrite `README.md` for the client. Delete demo-only notes.
5. Check that the workspace `.gitignore` contains `clients/*/website/`. Add it if not.
6. Create the repo and push:
   ```bash
   git init -b main && git config user.name "<from workspace>" && git config user.email "<from workspace>"
   git add -A && git commit -m "feat: <Client> website from the <industry> template"
   gh repo create site-<client> --private --source . --remote origin --push
   ```
7. Confirm it's private: `gh repo view sam-locate-digital/site-<client> --json visibility`.

## Step 3: Fill in the content

From the kickoff notes in `clients/<client>/CLAUDE.md` and anything Sam provides:
- `content/settings.json`, `content/team/*.md`, `content/reviews.json`, `content/guides/*.md`, `images/`.
- `content/pages/*.json` (Pages): every page's sections. Rewrite the copy for the client here. Keep every key that `.pages.yml` defines for that section type, and nothing else (Pages CMS drops unknown keys on save).
- `content/brand.json` (Brand look): their colour scheme (a preset, or `custom` with `customColour` like `#1F45D6` and optional `customHighlight`), `headingFont` (`same-as-body` keeps the template look), `bodyFont`, logo. The build log lists any readability adjustment to a custom colour: tell Sam. Run `npm run check-themes` in the scratch build after changing schemes or fonts.
- Every page is `content/pages/*.json` (there are no code pages). Business details fill-ins (`{phone}`, `{hours}`, `{office}`, `{feePolicy}` and so on) keep most of them in sync automatically; rewrite the rest of the wording for the client.
- `site.json` → `formEndpoint` (Formspree form URL from Sam).
- Keep the file shapes exactly as `.pages.yml` describes them. Pages CMS rewrites files from that schema when it saves, so any key that isn't in `.pages.yml` disappears on the client's first save. Locate-only settings go in `site.json`, never in `content/`.
- Then search for anything left over from the demo:
  ```bash
  grep -rniE "PLACEHOLDER|Harlow|harlowhomeloans|TESTING|Illustrative|example\.com|\.example" content src site.json | grep -v node_modules
  ```
  Anything still unknown stays as `[PLACEHOLDER ...]` and goes on a list for Sam.

## Step 4: Build and check locally (outside Drive)

```bash
B="<scratchpad>/site-<client>"
rm -rf "$B" && mkdir -p "$B"
tar -C "G:/My Drive/Claude Code.Locate/clients/<client>/website" --exclude=.git --exclude=node_modules --exclude=dist -cf - . | tar -C "$B" -xf -
cd "$B" && npm ci && npm run build
```
It must end with `Checks passed: N page(s), every local link resolves.` and `Mode: demo`. Fix any listed problem before pushing. The `photo ...: 2.1 MB → 180 KB` lines are the automatic photo shrinking, and they're expected.

Commit and push from the Drive copy (`git pull` first).

## Step 5: Vercel project and preview

1. `create_git_project` with `repo: sam-locate-digital/site-<client>`, `teamId` as above, `projectName: site-<client>`. Don't add a domain.
2. Follow the build with `list_deployments` and `list_deployment_events` (builds: 1). It should be READY with the same `Checks passed` line.
3. Check the preview at `https://site-<client>.vercel.app` in the browser pane: every page returns 200, every `<img>` loads, the stylesheet applies, and the response header is `X-Robots-Tag: noindex, nofollow`. In the browser pane:
   ```js
   const pages = ['/', /* every page and team profile, without .html */];
   const out = [];
   for (const p of pages) {
     const r = await fetch(p, { cache: 'no-store' });
     const doc = new DOMParser().parseFromString(await r.text(), 'text/html');
     const broken = [];
     await Promise.all([...doc.querySelectorAll('img')].map((i) => new Promise((ok) => { const im = new Image(); im.onload = ok; im.onerror = () => { broken.push(i.getAttribute('src')); ok(); }; im.src = new URL(i.getAttribute('src'), location.origin + p).href; })));
     out.push([p, r.status, broken]);
   }
   ({ bad: out.filter(([, s, b]) => s !== 200 || b.length), robots: (await fetch('/')).headers.get('x-robots-tag') })
   ```
4. **Draft preview** (so clients edit, preview, then publish):
   - Branch roles: `main` = the draft (Pages CMS always saves to `main`), `draft` = automatic copy of `main` for the preview, `live` = the public site. The template's `vercel.json` already stops `main` deploying by itself.
   - Create `live` from `main`: `gh api -X POST repos/sam-locate-digital/site-<client>/git/refs -f ref=refs/heads/live -f sha=$(gh api repos/sam-locate-digital/site-<client>/git/ref/heads/main --jq .object.sha)`. The first push to `main` creates `draft` (sync-draft.yml).
   - **Sam's step:** Vercel → project → Settings → Environments → Production → Branch Tracking → `live` → Save. The connector can't change this. Until it's done, the live site doesn't update.
   - Add the preview address: `add_project_domain` with name `site-<client>-preview.vercel.app` and gitBranch `draft`.
   - Make the preview open without a login: `update_project` with `ssoProtection: null`. Every `*.vercel.app` address still sends noindex (vercel.json), so it stays out of Google.
   - Turn off Vercel's feedback toolbar on previews: `update_project` with `enablePreviewFeedback: false`.
   - In `.pages.yml`, replace every `harlow-cms-test-preview.vercel.app` (header comment, the hint under the first field of each section, the Publish checkbox) with the client's preview address.
   - Test once: push a small change to `main`, confirm the preview shows it and the live site doesn't, run `publish.yml` (`gh workflow run publish.yml -R <repo> --ref main -f payload='{}'`), confirm the live site updates.
5. Give Sam the preview link for client review. Write the repo, Vercel project and preview URL into `clients/<client>/CLAUDE.md`.

## Step 6: Scenario 1 - migration

Follow the guide's step 5. Claude's part:
1. **Inventory:** fetch the old site's sitemap (`/sitemap.xml`, `/wp-sitemap.xml` or `/sitemap_index.xml`) and list every address with its title and meta description. Add the top pages from Search Console if Sam has given access. Save it to `clients/<client>/website-migration.md` as a table: old address, title, new address, action (keep / redirect).
2. **Redirects:** add one entry per changed address to `vercel.json` → `redirects`:
   ```json
   { "source": "/old-page/", "destination": "/new-page", "permanent": true }
   ```
   `trailingSlash: false` already sends `/about/` to `/about`, so only list addresses whose name changes. Point every WordPress leftover (`/feed`, `/category/:slug*`, `/tag/:slug*`, `/author/:slug*`, `/wp-admin`, `/wp-login.php`) somewhere sensible. Don't chain redirects.
3. **Ranking posts:** if a blog post has real traffic, it needs its own page. Guides are currently one page, so tell Sam the guide page template must be built first.
4. After pushing, test every redirect on the vercel.app preview: each must be a single 308 to a page that returns 200.

## Step 7: Go live (Sam's yes required)

1. Confirm with Sam: the client has approved the site, the domain is decided (www or bare as the main address), and DNS access is sorted.
2. Set `site.json` to `"production": true` and `"url": "https://<main address>"`, without a trailing slash. Build locally (step 4): it must say `Mode: LIVE` and write `sitemap.xml`. Push.
3. **DNS is Sam's step, or done with Sam watching.** Walk them through tradie SOP step 5: add both domains in Vercel (or `add_project_domain` after Sam's yes), copy Vercel's records, replace only A and CNAME records, never touch MX or TXT, never change name servers, then check that email still works.
4. Once Vercel shows Valid Configuration, check the real domain:
   ```bash
   D=https://<main address>
   curl -sS -o /dev/null -D - "$D/" | grep -iE "^HTTP|x-robots"        # 200, and NO x-robots-tag
   curl -sS "$D/" | grep -c 'name="robots"'                             # 0
   curl -sS "$D/robots.txt"; curl -sS "$D/sitemap.xml" | head -5          # sitemap on the real domain
   curl -sS -o /dev/null -D - "https://site-<client>.vercel.app/" | grep -i x-robots   # still noindex
   ```
   Plus the image and page check from step 5 on the real domain, the other domain variant redirecting to the main one, and (scenario 1) ten old addresses redirecting.
5. Remind Sam of the manual launch items: test enquiry, Search Console plus sitemap, GA4, Google Business Profile link, UptimeRobot, invoicing (tradie SOP step 6).

## Step 8: Editing access

- **Scenario 2:** Sam invites the client in Pages CMS (Admin → Collaborators) and adds `site-<client>` to the Pages CMS GitHub app's repository list. Claude writes the client a short how-to email in Sam's voice for Sam to send. Include: saving updates the preview at `site-<client>-preview.vercel.app` (bookmark it) and Publish (sidebar → Actions) puts it live, sections can be added, dragged, hidden, click the photo and press Select after uploading, saving publishes in about a minute, renaming keeps the page address, deleting a person deletes their page.
- **Scenario 3:** nothing to set up.
- Record who has access in `clients/<client>/CLAUDE.md`.

## Editing a launched site

1. `git pull` in `clients/<client>/website/` (on `main`). `main` is the draft: Locate edits show on the preview and go live with the next Publish (run `publish.yml`, which also publishes any client edits waiting in the draft). Tell Sam if there are unpublished client edits before publishing.
2. Edit `content/` (words, people, reviews), `images/`, `vercel.json` (redirects) or `src/` (layout, only if Sam asks).
3. Build in the scratchpad (step 4) if `src/`, `build.js` or `vercel.json` changed. Content-only edits can go straight to push.
4. Commit with a plain-words message, `git pull --rebase` if the push is rejected, then push.
5. Run Publish if it should go live now, then check the production deployment (from `live`) is READY and the change shows on the live page. Report the commit and what changed.

## Report back

Give Sam: the live or preview URL, the repo URL, what was done, what was checked (with numbers), anything left as `[PLACEHOLDER]`, and the next step that's Sam's to do.
