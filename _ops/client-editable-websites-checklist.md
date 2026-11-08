# Client-editable websites: checklist to sell and deliver

Turning the Harlow test (page builder + Pages CMS + edit → preview → publish) into a service for brokers and other clients.

- Test site: https://harlow-cms-test.vercel.app (preview: https://harlow-cms-test-preview.vercel.app)
- Repo: https://github.com/sam-locate-digital/harlow-cms-test (full details in its `HANDOVER.md`)
- Launch process: [website-launch.md](website-launch.md), run by `/launch-site`

Last updated 8 November 2026.

---

## 1. Finish the product (before the first pitch)

- [ ] Clean up the test site: remove the "9999" test edits and other test content (Claire's rename, Testing Sam, Test Suzu, "[TESTING]"), pick the colour scheme you want to show, then **Publish**. Don't press Discard before publishing: it would delete the six new pages.
- [ ] Commit the workspace files from the build session (`_ops/website-launch.md`, `_skills/launch-site/`, CLAUDE.md, `.gitignore` and the rest), so `/launch-site` and the guide are safe in git.
- [ ] Run the client experience once yourself with a second email address: invite it as a collaborator, edit a page, add a section, check the preview, publish. Check the draft and live branches show "Switch back to main to edit".
- [ ] Try editing in Pages CMS on a phone (brokers will).
- [ ] Add GA4 tracking with enquiry and phone-tap events, so you can prove results.
- [ ] Add a 404 page and canonical tags.
- [ ] Test the enquiry forms against a real Formspree form (an email lands in an inbox).
- [ ] Add one page per guide, needed for clients moving off WordPress with ranking blog posts.
- [ ] Convert the tradie template to the same editable setup, if you'll pitch this to tradies too.

## 2. Accounts and costs (one-off)

- [ ] Vercel Pro before the first paying client. The free plan is non-commercial only. About US$20 a month covers all client sites (check the current price).
- [ ] A GitHub organisation (free), e.g. "locate-digital", to own client repos, so handing a site over is clean.
- [ ] Pages CMS GitHub app set to **Only select repositories** (GitHub → Settings → Applications → Pages CMS → Configure).
- [ ] Formspree plan for enquiry forms and UptimeRobot (free) for downtime alerts (see the tradie SOP).
- [ ] Decide the fallback if Pages CMS changes or shuts down. It's free and third-party; the site, repo and hosting stay yours, so you'd edit for clients through Claude until you swap editors.

## 3. Broker compliance (important)

- [ ] Ask each broker's aggregator whether website changes need compliance approval (many require it for marketing material).
- [ ] Agreement clause: the client is responsible for anything they publish themselves (rates, claims, "free" statements); you review on request.
- [ ] Keep the compliance footer and general-information warning in Business details only, and tell clients not to remove them.

## 4. Pricing and the offer

- [ ] Decide the tiers, for example:
  - Managed: you make the edits (care plan).
  - Self-edit add-on: editor setup, a 30-minute training call and a how-to guide.
  - WordPress move: migration fee covering redirects and keeping rankings.
- [ ] Decide what's included and what's quoted: new section types, new page designs, colours outside the generator.
- [ ] Update the service agreement: ownership (client owns the domain and content; the repo is transferred if they leave), rounds of changes, what the care plan covers.

## 5. Sales material

- [ ] A 2 to 3 minute screen recording: edit a heading → Save → Preview → Publish → the live site changes.
- [ ] A sandbox prospects can try: a separate copy of the demo that resets nightly, so demos don't touch the Harlow test site.
- [ ] A one-page pitch. Angle: "Edit your own website like WordPress, with none of the plugin updates, hacks or slow pages. Every change is previewed before it goes live, and nothing you do can break the design."
- [ ] Short answers to likely objections:
  - Why not Wix or WordPress? Faster, secure, nothing to update.
  - What if Locate disappears? You own the domain, and the site can be handed over in an afternoon.
  - Can I break it? No: sections are pre-designed, colours are kept readable, there's a preview, and every change can be undone.
- [ ] A client how-to guide (adapt the tradie client guide). Cover: Save goes to the preview, bookmark the preview address, Preview / Publish / Discard under Actions, pasting a colour code from any colour picker, adding and reordering sections.
- [ ] A case study after the first client goes live: before and after, page speed, enquiries.

## 6. Delivering each sale

- [ ] Run `/launch-site`: intake, repo, content, preview setup, domain, go-live, editor invites ([website-launch.md](website-launch.md)).
- [ ] Your one manual Vercel step per client: Settings → Environments → Production → Branch Tracking → `live`.
- [ ] A 30-minute training call, the how-to guide, then the handover email.

## 7. Once you have several clients

- [ ] Plan how template improvements reach existing sites. Each client site is its own copy, so template fixes don't flow through automatically. Keep a short changelog in the template and apply updates during care-plan work.
