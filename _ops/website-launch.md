# Client website launch — Locate Digital

One process for taking a demo site live for a paying client, whichever of the three situations they're in. The `/launch-site` command runs the steps marked **(Claude)**.

- Tested end to end on 6 November 2026: https://harlow-cms-test.vercel.app (see `_brand/Website Demo/demos/harlow-cms-test/HANDOVER.md`)
- Tradie sites also follow [tradie-website-sop.md](tradie-website-sop.md) for pricing, kickoff, build details, DNS, care plan and handover. Where the two differ on repos and editing, this guide wins.

---

## The one shape every client site has

| Piece | What it is | Who owns it |
|---|---|---|
| GitHub repo `site-<client>` (private) | The master copy of the site. Every change, yours or the client's, is a commit here | Locate (transferred to the client if they leave) |
| Vercel project `site-<client>` | Builds and hosts the site. Every push to `main` goes live in about a minute | Locate |
| Domain | The client's web address | **The client**, registered in their business name |
| Pages CMS access (optional) | The client's editor at app.pagescms.org | Locate invites the client |

Inside the repo:

| File or folder | Holds | Editable by the client? |
|---|---|---|
| `content/` | Words, team, guides, reviews, business details | Yes, through Pages CMS |
| `images/` | Photos as uploaded. The build shrinks big ones automatically | Yes, through Pages CMS |
| `content/pages/` | Every page built from sections (homepage, service pages, legal pages, any new page) | Yes, through Pages CMS: edit, add, remove, reorder and hide sections; create pages |
| `content/brand.json` | Brand look: colour scheme (11 presets or their own brand colour), heading font, body font, logo | Yes. Custom colours are made readable automatically |
| `.pages.yml` | What the editor shows | No |
| `site.json` | Go-live switch, live address, form endpoint | No (not in the editor at all) |
| `src/`, `js/`, `styles.css` | Layout, design, forms | No |
| `vercel.json` | Build settings, redirects, noindex on `*.vercel.app` | No |

**The local copy** lives at `clients/<client>/website/` and is a *clone* of the repo, not the other way round. The workspace ignores it (`.gitignore`: `clients/*/website/`). Always `git pull` before editing, because the client may have changed something in Pages CMS. Never use `git subtree push` for a client site: it fails the first time the client edits.

**Never run `npm install` inside Google Drive.** It fails with `EBADF`. To build locally, copy the folder to the local disk (Claude does this in its scratchpad). Vercel builds from GitHub, so day-to-day edits don't need a local build.

### Templates

| Industry | Template | Editor-ready? |
|---|---|---|
| Mortgage broker | `_brand/Website Demo/demos/harlow-cms-test/` | Yes |
| Tradie | `_brand/Website Demo/demos/tradie/` | Not yet: its content is in `config.js`. Fine for scenario 3; convert it to the `content/` shape before offering a tradie the editor |

---

## The three scenarios: what changes

The build is the same for all three. Only these rows differ.

| | 1. Moving from WordPress | 2. New site, client edits | 3. Locate runs everything |
|---|---|---|---|
| Domain | Keep theirs. Point it at Vercel at launch | Client buys one in their business name | Client buys one in their business name |
| Extra step | Keep their Google rankings (step 5) | None | None |
| Editor | Optional | Invite the client (step 7) | None. You edit through Claude or Pages CMS |
| Risk to watch | Email and DNS records at the old host | Client uploads and edits | None special |

A scenario 3 client who later wants to edit is just an invite. Nothing is rebuilt.

---

## 0. One-time setup

Done once, covers every client.

- [x] GitHub CLI installed and signed in as `sam-locate-digital` (6 Nov 2026)
- [x] Vercel connector approved for the `sam-cheng-s-projects` team (6 Nov 2026)
- [x] Pages CMS GitHub app installed on `sam-locate-digital` (6 Nov 2026). Check it's set to **Only select repositories** (GitHub → Settings → Applications → Pages CMS → Configure), so it can never touch the workspace or demos repos.
- [ ] **Vercel Pro** before the first paying client. Hobby is for non-commercial use only. One Pro seat covers every client project. Check the current price.
- [ ] Formspree, UptimeRobot and recurring billing: see tradie SOP step 0.

---

## 1. Intake (at kickoff)

Ask and record in `clients/<client>/CLAUDE.md`:

1. **Which scenario** (1, 2 or 3), and which template.
2. **Domain:** the exact address, who registered it, and the registrar. For scenario 2 or 3, get them to buy it now in their business name (a `.com.au` needs their ABN).
3. **DNS host and email host:** look the domain up at lookup.icann.org (name servers = DNS host) and note who runs their email (MX records). Scenario 1 almost always has email at the old host.
4. **Scenario 1: the old site's page list,** before anything changes (step 5.1).
5. **Who edits:** names and email addresses for Pages CMS, or "Locate only".
6. **Where enquiries go:** the email address for the Formspree form.
7. **Tracking:** GA4 and Search Console access, or permission to create them in their name (see [client-access-guide.md](client-access-guide.md)).

---

## 2. Create the client's repo **(Claude)**

1. Copy the template to `clients/<client>/website/`, leaving out `.git`, `node_modules`, `dist` and `HANDOVER.md`.
2. Reset any test content (for the Harlow template: test team members, "[TESTING]" names, test photos).
3. Make sure `site.json` says `"production": false` and `"url": ""`.
4. `git init -b main`, commit, then create the private repo and push:
   ```bash
   gh repo create site-<client> --private --source . --remote origin --push
   ```
5. Write the repo URL into the client's `CLAUDE.md`.

---

## 3. Fill in their content

- `content/settings.json`: business name, contact details, hours, homepage, compliance (licence, ABN, credit representative numbers). Remove every `[PLACEHOLDER]`.
- `content/team/`: one file per person, with real photos.
- `content/reviews.json`: real Google reviews only, approved by the client. Never write or edit a review's words.
- `content/guides/`: their articles (scenario 1: migrated posts, see 5.3).
- `site.json`: `formEndpoint` from their Formspree form.
- Photos: upload them as they are. The build resizes anything over 1600px or 300 KB.

Claude can fill most of this from the kickoff notes, then search the whole site for leftover demo text and `[PLACEHOLDER]`.

---

## 4. Preview and client sign-off **(Claude)**

1. Create the Vercel project from the repo (Vercel connector `create_git_project`, team `sam-cheng-s-projects`). Every push to `main` now deploys.
2. The site appears at `site-<client>.vercel.app`. **Any `*.vercel.app` address always sends noindex**, so previews can't end up in Google, even after launch.
3. Check every page, image and link (Claude crawls it), then send the client the link. Two rounds of changes, then written approval (tradie SOP step 4.3).

---

## 5. Scenario 1 only: keeping their Google rankings

Google's trust sits on the **domain** and on each **page address**. Keep both and the rankings follow.

### 5.1 List what they have now (before launch)
1. Every page: `https://theirdomain.com.au/sitemap.xml` (WordPress usually has `/wp-sitemap.xml` or a Yoast `/sitemap_index.xml`), plus `site:theirdomain.com.au` in Google.
2. The pages that matter: Search Console → Performance → Pages (last 12 months, by clicks), and the pages other sites link to (Ahrefs or Semrush).
3. Each page's title and meta description.
Save the list as `clients/<client>/website-migration.md`.

### 5.2 Map old addresses to new ones
- Same address wherever possible. A new page that matches an old one gets the old page's address.
- Everything else gets a **permanent redirect** in `vercel.json` → `redirects`:
  ```json
  { "source": "/our-services/home-loans/", "destination": "/first-home", "permanent": true }
  ```
- WordPress addresses end in `/`. The template already redirects `/about/` to `/about` (`trailingSlash: false`), so only list addresses whose *name* changes.
- Catch WordPress leftovers too: `/feed`, `/wp-admin`, `/category/...`, `/tag/...`, `/author/...` → redirect to the closest page or the homepage.

### 5.3 Carry the content over
- Page titles and descriptions: reuse the ones that rank.
- Blog posts that get traffic. **Template gap:** guides are currently sections of one page. A post that ranks on its own address needs its own page, so add a guide page template (like the team profile pages) before migrating a blog with ranking posts.

### 5.4 After launch
- Submit the sitemap in Search Console, and use the **Change of address** tool only if the domain itself changed (normally it doesn't).
- Test 10 old addresses: each should redirect once, straight to the right page.
- Watch Search Console → Pages → "Not found (404)" weekly for a month and add redirects for anything missed.
- Keep the old WordPress hosting, switched off but not deleted, for 30 days. Don't cancel it until you've confirmed it doesn't also run their email or DNS.

A dip for a week or two is normal. It recovers if the redirects are right.

---

## 6. Go live

1. **(Claude)** In `site.json`: `"production": true` and `"url": "https://www.theirdomain.com.au"` (the version that will be the main address). Push. The build log says `Mode: LIVE`, writes `sitemap.xml` and points `robots.txt` at it.
2. **Domain, DNS and SSL:** follow tradie SOP **step 5** exactly. In short: add both the bare domain and `www` in Vercel → Settings → Domains, copy the records Vercel shows, replace only the website records (A and CNAME) at the DNS host, never touch MX or TXT, never change the name servers, and check their email still works afterwards.
3. **(Claude)** Checks on the real domain:
   - every page 200, no broken images or links
   - no `noindex` tag or `X-Robots-Tag` header on the real domain (the `*.vercel.app` address should still have one)
   - `/sitemap.xml` lists the real domain
   - scenario 1: old addresses redirect
   - a test enquiry reaches the client
4. Search Console: add a Domain property, verify it, submit `sitemap.xml`.
5. Tracking, Google Business Profile link, UptimeRobot, invoicing: tradie SOP step 6.

---

## 7. Editing access

### Scenario 2: the client edits
1. Pages CMS → the repo → **Admin → Collaborators** → enter the client's email → **Invite**. No GitHub account needed.
2. Add the repo to the Pages CMS GitHub app (GitHub → Settings → Applications → Pages CMS → Configure → add `site-<client>`), so the editor can save to it.
3. Send them a short how-to. Things that catch people out:
   - After uploading a photo, **click it and press Select**, or it isn't attached.
   - Saving updates the **preview**, not the live site. Check it at the preview link, then press **Publish to live site** (sidebar → Actions). **Discard draft changes** starts again.
   - Their preview address is `site-<client>-preview.vercel.app`. They bookmark it. Pages CMS also shows it in the editor.
   - Renaming a person keeps their web address. Deleting a person deletes their page.
4. What they can't touch: layout, forms, `site.json`, redirects, and any colour or font outside the Brand look lists. Brand look lets them pick a preset scheme or type their own brand colour (made readable automatically), choose heading and body fonts, and upload a logo. Pages lets them change every word and add, remove, reorder or hide sections. Their exact brand colour no longer needs Locate: Custom in Brand look. Their edits are saved as `pages-cms[bot]` commits, so you can see and undo any of them in GitHub.

### Scenario 3: Locate edits
Either open Pages CMS yourself, or ask Claude: it pulls the repo, edits `content/`, pushes, and checks the live page.

---

## 8. If the client leaves

Tradie SOP step 8 applies to every site: transfer the Vercel project and the GitHub repo to them (or send a ZIP), they keep their domain, and you remove your access. Remove the repo from the Pages CMS app and remove the collaborators.

---

## Known gaps in the mortgage-broker template

Fix these before the first broker launch:

- **No GA4 or conversion events** yet (the tradie template has them).
- **No canonical tags or 404 page** yet.
- **Guides are one page, not one page each** (matters for scenario 1 blogs, see 5.3).
- Forms post to `formEndpoint` but haven't been tested against a real Formspree form.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| Client saved but the site didn't change | Build still running, or it failed | Vercel → Deployments. A failed build leaves the previous version live. Claude can read the build log |
| Client's edit broke a page | Bad content, e.g. a deleted required field | Revert that commit in GitHub (or ask Claude); Vercel redeploys |
| Push from the local copy rejected | The client edited since your last pull | `git pull`, then push again. Never force-push |
| Photo shows as a pale blue box | Photo uploaded but not selected, or the file is missing | Edit the entry, pick the photo, Save |
| Real domain shows noindex | `site.json` still `production: false` | Set it to `true`, push |
| `npm install` fails with EBADF | Running inside Google Drive | Build a copy on the local disk |
