# Tradie website SOP — Locate Digital

How a tradie website goes from signed proposal to live site, and how it's looked after once it's live. Follow it in order, every time. The client's side of the job is in the [client guide](tradie-website-client-guide.md): send it at kickoff.

- Template: `_brand/Website Demo/demos/tradie/` (live demo: https://demo.locatedigital.io/tradie)
- Pricing: [02-pricing.md](../_brand/launch/02-pricing.md) → "Tradie website package"
- Agreement: [service-agreement.html](../_brand/launch/service-agreement.html)
- **Repos, editing and migrations:** [website-launch.md](website-launch.md) is the one process for every client site (tradie, broker, any scenario). Where they differ, it wins. In particular, step 4.1 below is replaced by its step 2: the client repo is the master copy and `clients/<client>/website/` is a clone of it, because a `git subtree push` breaks as soon as the client edits through Pages CMS.

Each phase has **Steps** and **Done when**. Don't move to the next phase until "Done when" is true. Steps marked **(Claude)** are quicker to hand to Claude Code than to do by hand.

---

## Timeline at a glance

| When | Phase | Who |
|---|---|---|
| Day 0 | 1. Signed and paid | You |
| Week 1 | 2. Kickoff | You + client |
| Weeks 2–3 | 3. Build | You |
| Week 3 | 4. Client review on a preview link | You + client |
| End of week 3 | 5. Domain, DNS and SSL | You (client may add records) |
| Launch day | 6. Launch checks | You |
| Monthly | 7. Care plan | You |
| If they leave | 8. Handover | You |

---

## 0. One-time setup (before your first paying client)

Do these once. They cover every client after that.

1. **Upgrade Vercel to Pro.** The free Hobby plan is for non-commercial use only. In Vercel: your team → Settings → Billing → upgrade to Pro. One Pro team holds every client site. Check locatedigital.io is on it too.
2. **Create a Formspree account** (formspree.io). It receives the booking form and emails it to the client. Each client gets their own form. The free plan has a monthly submission cap and no file uploads; check the current limits and move to a paid plan before your third or fourth client.
3. **Create an UptimeRobot account** (uptimerobot.com, free plan). It emails you if a client's site goes down.
4. **Set up recurring billing** in Xero (repeating invoices) or Stripe (subscriptions) for the $149, $399 and $1,800 monthly amounts, so you never invoice by hand.
5. **Update the service agreement** with the website terms: 50% of the build upfront and 50% at launch, two rounds of changes, what the $149 care plan covers, the 12-month term on the pay-monthly option, the client owns the domain, content and accounts, and the $300 handover if they stop the care plan.
6. ~~Make the template production-ready~~ **Done (28 Oct 2026).** The template now has a `production` switch in `config.js` and a `build.js` script. Together they:
   - take the noindex tags off
   - write the sitemap, robots.txt, `vercel.json`, 404 page and favicon
   - give every page its title, description and canonical address
   - load GA4 from `ga4Id`, with booking and phone-tap events
   - send real photo attachments with each booking, and show the customer an error if a booking fails to send

**Done when:** Vercel is on Pro, Formspree, UptimeRobot and billing are set up, and the agreement covers websites.

**How the template builds:** everything about a client's site is set in `config.js` (plus `reviews.json` and the photos). After any change to `config.js`, run this in the site folder:
```bash
node build.js
```
It rewrites the service and suburb pages and every page's head. With `production: false` (the demo) every page stays hidden from Google. With `production: true` it writes the files a live site needs. It prints which mode it ran in.

---

## 1. Signed and paid (day 0)

**Steps**
1. Send the service agreement with the option they chose: Website $5,999, Website and Google $4,499 + $1,800/mo, or Website paid monthly $1,999 + $399/mo for 12 months + $149 care plan.
2. Invoice the first payment: 50% of the build fee (or the $1,999 upfront on the pay-monthly option).
3. Once signed and paid, run the `client-onboarding` skill. It creates `clients/<client>/` with its `CLAUDE.md`.
4. Book the 45-minute kickoff interview for week 1.
5. Email the client the [client guide](tradie-website-client-guide.md) and ask them to start the "Before kickoff" checklist.

**Done when:** the agreement is signed, the first invoice is paid, the client folder exists and kickoff is booked.

---

## 2. Kickoff (week 1)

**Steps**
1. Run the 45-minute interview. Cover:
   - every service they do, and the 3–4 that earn the most (these become service pages)
   - the suburbs they cover, ranked by how much work comes from each (top 16 get pages)
   - what's different about how they work (on time, tidy, explain first): this becomes the hero and "Why us" copy
   - how the business started, and who's on the team, with roles
   - hours, emergency availability, response time to a booking
   - landlord and rental work, yes or no
   - any current offer for the promo bar
   - their current website, if they have one, and where the domain and email are hosted
2. Collect everything on the client guide's checklist: logo, photos, licence numbers, ABN, the email address bookings should go to.
3. Get access, by invite and never by password (see the client guide, "Giving us access"):
   - Google Business Profile (manager)
   - Google Analytics, or permission to create it in their name
   - Google Ads (Website and Google option only), following [client-access-guide.md](client-access-guide.md)
   - the domain's DNS (or agree that they'll add the records you send them)
4. **If they have a current website, list its pages now**, before anything changes. Open `https://theirdomain.com.au/sitemap.xml`, or search Google for `site:theirdomain.com.au`, and save every page address in the client's `CLAUDE.md`. You need this list for the redirects in 3.8.
5. Write the interview notes, the service list, the ranked suburbs and the old page list into `clients/<client>/CLAUDE.md`.

**Done when:** the interview is written up, the assets are in, and you have access (or an agreed plan) for each account.

---

## 3. Build (weeks 2–3)

### 3.1 Copy the template
1. Copy `_brand/Website Demo/demos/tradie/` to `clients/<client>/website/`.
2. Delete what's only for the demo: `BRIEF.md`, `HANDOFF.md`, `PROMPT.md`, the `design/` folder and the full-size PNGs in the folder root.

### 3.2 Business details: `config.js`
Go through it top to bottom:
- `brand`: name, full legal trading name, founding year
- `trades`: `['plumbing', 'electrical']`, or one of them
- `accent`: their brand colour. If it isn't the default blue, `images/brush.svg` and `images/brush-hero.svg` must be recoloured to match **(Claude)**
- `showPlaceholders`: **`false`**
- `contact`, `address` (real street address), `hours`, `licences` (plumbing licence, REC, ABN, insurance cover)
- `suburbs`: their top 16 (or fewer)
- `stats`: real Google rating and review count, and a jobs-done figure only if they can stand behind it. Otherwise ask Claude to swap that stat for something true
- `guaranteeYears`, `responseTime`, `promo` (`''` hides the promo bar)
- `bookingRefPrefix`: two letters from their name, e.g. `SP-`
- `services`, `servicePages`, `suburbDetail`, `nearby`, `team`: rewritten from the interview

### 3.3 Reviews: `reviews.json`
1. Copy 6–9 of their real Google reviews: name as the reviewer shows it (first name and initial is fine), suburb, job, trade, rating, month and the quote.
2. Send the client the list to approve before it goes live.
3. Never write or edit a review's words. Trim only, and mark any trim with "…".

### 3.4 Photos: `images/`
1. Replace each photo with theirs, **keeping the same file name**. Shapes: `hero.webp` 16:9, `step-1` to `step-4` 4:5, service photos 4:3, `team.webp` and the mosaic photos 3:2.
2. Save as WebP, around 1,200–1,400px on the long side and under 250 KB each. Use squoosh.app, or ask Claude to convert a folder.
3. Update the alt text to describe each new photo: in the HTML files, and in `main.js` for the four stepper photos **(Claude)**.
4. Only real photos of their team and work. No stock, and no AI-generated people presented as their staff.

### 3.5 Copy that lives in the pages
`config.js` holds the details, but some demo copy is written straight into the HTML. Rewrite each of these for the client:
- `index.html`: hero headline and subline, the team strip ("A family business since…")
- `about.html`: the founding story and the "people who'll turn up" intro
- `plumbing.html` / `electrical.html`: the intro paragraph and mosaic alt text
- `landlords.html`: **remove or replace the "Raj K." quote** (it's a demo sample). Use a real landlord review, or delete the quote section
- `privacy.html` / `terms.html`: replace the placeholder text with their real policy and terms
- `emergency.html`: check the advice matches what they actually want customers to do

If they only do one trade, delete the other trade's hub and service page files, and let `build.js` regenerate the rest.

### 3.6 Booking form
1. In Formspree, create a new form named after the client, with the notification email set to the address they gave you.
2. Copy the form's endpoint (`https://formspree.io/f/xxxxxxx`) into `formEndpoint` in `config.js`.
3. **Photos:** the form attaches up to three photos, shrunk on the customer's phone to about 100–300 KB each. Formspree only accepts attachments on a paid plan. On a plan without them, the booking still arrives, with a note saying the customer added photos and asking the tradie to get them by text. Tell the client which they're getting.

### 3.7 Switch it from demo to live
In `config.js`:
1. `production: true`
2. `siteUrl`: their live address, ending in `/`. Use the version you'll make the main address in 5.3, e.g. `'https://www.smithplumbing.com.au/'`
3. `ga4Id`: their GA4 measurement ID (3.9), e.g. `'G-AB12CD34EF'`

Then run `node build.js`. Check that it says **production**, and that the site folder now has `sitemap.xml`, `robots.txt` and `vercel.json`.

The favicon is their first initial on their brand colour. If they have a logo mark that works at small sizes, replace `favicon.svg` with it.

### 3.8 Redirects from their old website
For every old page you listed in 2.4, add a line to `redirects` in `config.js`, pointing to the closest new page:
```js
redirects: [
  { from: '/services/hot-water-repairs.php', to: '/plumbing/hot-water' },
  { from: '/contact-us', to: '/book' }
],
```
Run `node build.js` again to write them into `vercel.json`. Without these, their existing Google rankings can drop at launch.

### 3.9 Tracking
1. Create a GA4 property in the client's name, with you as admin. Copy its measurement ID (Admin → Data streams → their web stream) into `ga4Id` (3.7).
2. The site sends two events by itself: `generate_lead` when a booking is sent, and `phone_call_click` when a phone number is tapped. Once each has appeared in GA4 (send a test booking and tap the number after launch), mark both as **key events** (Admin → Events).
3. Website and Google option: import those two key events into Google Ads as conversions.

### 3.10 Regenerate after any config change
Any time you change `config.js` (suburbs, services, details, the switches above), run `node build.js` again. Delete any `areas/` or service page left over for a suburb or service they no longer cover.

### 3.11 Check it before the client sees it
Run the preview locally and check:
- [ ] Every page loads, with no broken links or images (ask Claude to crawl it)
- [ ] No yellow placeholder highlights, sample reviews, "Eastside Trades", "HC-" or demo names left anywhere (ask Claude to search for them)
- [ ] `node build.js` says **production**, and there's no noindex left on any page except Thanks and 404 (ask Claude to check)
- [ ] A test booking sent from the site, with a photo attached, arrives in the client's inbox (check spam too)
- [ ] Phone numbers dial the right number on a real phone
- [ ] The mobile call bar, booking drawer, menu and FAQ all work on a phone
- [ ] No sideways scrolling on a phone

**Done when:** every box above is ticked.

---

## 4. Client review on a preview link (week 3)

### 4.1 Put the site in its own repo
1. In GitHub (signed in as sam-locate-digital), create a new **private** repository named `site-<client>`, with nothing added (no README, licence or .gitignore).
2. Commit the site in the workspace, then push just that folder to the new repo **(Claude)**:
```bash
git remote add site-<client> https://github.com/sam-locate-digital/site-<client>.git
git subtree split --prefix=clients/<client>/website -b site-<client>-deploy
git push site-<client> site-<client>-deploy:main
```
3. Write the remote name and the push commands into the client's `CLAUDE.md`, so later edits use the same steps.

### 4.2 Connect it to Vercel
1. Go to vercel.com/new, choose **Import** next to `site-<client>`.
2. Framework preset: **Other**. Leave the build and output settings empty. Click **Deploy**.
3. Vercel gives it an address ending in `.vercel.app`. That's the preview link.

### 4.3 Get their feedback
1. Send the preview link with a short note: what to look at, and that you need one list of changes per round (see the client guide, "Reviewing your site").
2. Round 1: make the changes, push again (Vercel updates within a minute), send the link back.
3. Round 2: same again. Anything beyond two rounds, or anything that's a new page rather than a change, is quoted as an add-on.
4. Get a written "approved for launch" from the client.

**Done when:** the client has approved the site in writing.

---

## 5. Domain, DNS and SSL (end of week 3)

This is the step that can break a client's email. Go slowly and follow it exactly.

### 5.1 Find out who controls their DNS
The company they bought the domain from isn't always the one running its DNS.
1. Look the domain up at lookup.icann.org. Note the **registrar** and the **name servers**.
2. The name servers show who runs the DNS. For example `ns1.ventraip.net.au` means VentraIP, `ns-cloud-x.googledomains.com` means Google, and the old web designer's name means them.
3. Log in there yourself (if they invited you), or arrange a 15-minute screen-share where the client logs in and you talk them through it.

### 5.2 Save every existing record first
1. Screenshot (or export) every DNS record, and save it in `clients/<client>/`.
2. Note the **MX** records (their email), and the **TXT** records (SPF, DKIM, DMARC and service verifications, which email also relies on). You will not touch these.

### 5.3 Add the domain in Vercel
1. Open the client's Vercel project → **Settings → Domains**.
2. Add `theirdomain.com.au` and `www.theirdomain.com.au`. Choose www as the main one, so the bare domain redirects to it (or the other way around: pick one and stay consistent with the sitemap).
3. Vercel shows the records it needs: usually an **A** record for the bare domain and a **CNAME** for www. Copy the exact values it shows. They can differ from project to project.

### 5.4 Change the records at their DNS host
1. For the bare domain (host `@` or blank): **replace** the existing A record that points to the old website with Vercel's A record. Don't leave both.
2. For `www`: replace the existing CNAME or A record with Vercel's CNAME.
3. **Don't change** MX, TXT or any other record, and **never change the name servers**. Changing the name servers wipes every record, email included.
4. If there's a **CAA** record, it must allow `letsencrypt.org`, or the security certificate can't be issued. If there's none, that's fine.

### 5.5 Wait for it to connect
1. In Vercel's Domains page, both entries turn to **Valid Configuration**. That usually takes minutes, occasionally an hour or more.
2. Vercel then issues the security certificate (SSL) by itself. You don't buy, install or renew anything. Expect a few minutes where https fails before the certificate arrives.
3. Check `https://theirdomain.com.au` and `https://www.theirdomain.com.au` both open the new site, with the padlock showing.

### 5.6 Check their email still works
Send an email to the client's business address and ask them to confirm it arrived, and that they can still send. If it fails, compare the MX and TXT records against your screenshots from 5.2 and put back anything that changed.

**Done when:** both addresses open the new site over https, and the client has confirmed their email works.

---

## 6. Launch checks (launch day)

- [ ] Send a test booking from the live site and confirm it reaches the client
- [ ] GA4 → Reports → Realtime shows your visit, and the booking and phone-tap events
- [ ] Search Console: add a **Domain** property for their domain, verify it with the TXT record it gives you (add it at their DNS host), then submit `sitemap.xml`
- [ ] Old page addresses from 2.4 redirect to the new pages (try three or four)
- [ ] Google Business Profile → website link set to the new site
- [ ] Website and Google option: Google Ads ads point at the matching service and suburb pages, and conversions are recording
- [ ] UptimeRobot: add an HTTPS monitor for the homepage, alerting your email
- [ ] Invoice the second 50% of the build, and start the monthly subscription ($149, $399 + $149, or $1,800)
- [ ] Send the client the launch email: the site is live, how bookings will reach them, how to ask for edits (client guide, "After launch")
- [ ] Tell the client **not** to cancel their old hosting yet (see below)
- [ ] Update `clients/<client>/CLAUDE.md`: launch date, repo, Vercel project, Formspree form, GA4 ID, DNS host

**The old hosting:** after two weeks with no problems, confirm whether the old host also runs their email or DNS (check the MX records and name servers). If it runs neither, tell the client it's safe to cancel. If it runs either, it must stay, or the email or DNS must be moved first.

**Done when:** every box is ticked and the client has the launch email.

---

## 7. Care plan ($149/month)

**Monthly**
1. Make any small edits they've asked for, up to one hour in total: new reviews, hours, the promo bar, a photo swap. Edit, commit, push (as in 4.1). Vercel publishes within a minute.
2. Add any good new Google reviews to `reviews.json` (with the client's OK).
3. Send one test booking and confirm it arrives. Form services and spam filters change.
4. Check UptimeRobot for any downtime.
5. Send the short monthly email: calls and bookings from the site (from GA4), any edits made, anything they need to know.

**Every few months**
- Check the domain's renewal date at the registrar. It's the client's domain and their renewal, but remind them a month before it's due. An expired domain takes the site and their email down.
- Check the Formspree plan still covers your total monthly submissions across all clients.

**Out of scope for the care plan:** new pages, rewrites, new photography, a redesign. Quote these as add-ons (extra service page $250, extra suburb page $150).

---

## 8. Handover, if they leave the care plan

1. Invoice the $300 handover fee.
2. Ask where they want the site to go:
   - **Their own Vercel account:** in Vercel, the client project → Settings → **Transfer project** to their team.
   - **Somewhere else:** download the repo as a ZIP from GitHub and send it. Any static host will run it as-is.
3. Transfer the GitHub repo to them if they want it (repo → Settings → **Transfer ownership**).
4. If the hosting moves, they (or their new provider) update the DNS records. You don't touch them after handover.
5. Once they confirm the new setup works, remove your access from their GA4, Google Business Profile, Google Ads, DNS and Formspree form. Pause the UptimeRobot monitor and cancel the subscription.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| Vercel says "Invalid Configuration" | Records not saved, or the old A or CNAME record is still there next to the new one | Recheck 5.4. Delete the old record, leave only Vercel's |
| Domain connected but https fails | Certificate still being issued, or a CAA record blocks Let's Encrypt | Wait 10–15 minutes. Then check for a CAA record (5.4) |
| Client's email stopped working | An MX or TXT record changed or was deleted, or the name servers were changed | Restore from the 5.2 screenshots |
| Bookings aren't arriving | Wrong `formEndpoint`, Formspree not confirmed, or landing in spam | Check `config.js`, confirm the form in Formspree, check spam and mark as "not spam" |
| Site shows the demo, placeholders or "Eastside Trades" | Steps in 3.2 or 3.5 missed | Search the site folder for demo text (Claude) and fix |
| Google isn't listing the site | `production` still `false`, or `build.js` not rerun | Recheck 3.7, run `node build.js`, push, resubmit the sitemap in Search Console. New sites can take a few weeks to appear |
| Customer sees "We couldn't send your booking" | Formspree is down, the endpoint is wrong, or the monthly limit is used up | Check the form in Formspree and its usage. The customer was shown your number, so check for missed calls too |
| Change pushed but not showing | Browser cache, or the push didn't reach the client repo | Hard refresh. Check the deployment in Vercel |
