---
name: tracking-setup
description: Build a conversion tracking plan for a Locate Digital client — GA4, Google Tag Manager, ad-platform pixels, and server-side tracking. Use when Sam asks to set up tracking, set up conversion tracking, set up GA4, set up GTM, configure the Meta pixel or Conversions API, set up server-side tracking, build a measurement plan, fix broken tracking, or check that conversions are firing. Also triggers on "tracking for [client]", "track bookings/calls/forms for [client]", "GA4 events", "CAPI", or "tag setup". Produces a tracking plan document with the event taxonomy, GTM tags/triggers, platform config, and a QA checklist.
---

# Tracking setup

Build a complete, implementation-ready conversion tracking plan for a Locate Digital client. One run = one tracking plan document that a person can follow tag by tag.

Tracking is the gate on every campaign. If you can't measure the lead, you can't prove the result, and the result is the whole product. Nothing goes live on broken tracking.

This skill produces the **plan and the implementation steps**. It documents exactly what to build in GA4, GTM, and the ad platforms. It does not click buttons in the accounts — a person (or a logged-in browser session) does that, then runs the QA checklist here to confirm.

---

## Step 1 — Load client context

Read the client's `CLAUDE.md` at `clients/<name>/CLAUDE.md` before anything. Extract:

- Business name, website URL, CMS/platform (WordPress, Wix, custom)
- Active channels (which ad platforms need conversions imported?)
- Booking / practice-management system (Cliniko, Calendly, HubSpot, phone-only)
- How leads actually come in — calls, forms, online bookings, live chat
- Locations (for call tracking by location if relevant)
- Any known tracking history or issues

If the CMS, booking system, or lead actions are unknown, ask Sam before building. Don't guess the tech stack — a tracking plan built on the wrong platform is worse than none.

---

## Step 2 — Confirm tier and inputs

Tracking depth is set by the client's package. Confirm which:

| Tier | Package | What gets built |
|---|---|---|
| **GA4** | Starter | GA4 property + key events for calls, forms, booking clicks |
| **GA4 + GTM** | Growth | The above via Tag Manager, plus Google Ads + Meta pixels firing on the right events |
| **Server-side** | Scale | The above plus server-side GTM / Meta CAPI so tracking survives ad blockers and iOS |

Also confirm (ask only if missing):

- **Lead actions to track** — phone call, form submit, online booking, email click, live chat. Default to all that apply.
- **Ad platforms** — which need conversions imported (Google Ads, Meta, other)?
- **Consent** — is there a cookie/consent banner? (Affects Consent Mode setup.)
- **Access** — is GTM installed already, or does it need adding to the site?

---

## Step 3 — Build the tracking plan

### Output format

Save to:
```
clients/<name>/tracking/tracking-plan.md
```

Structure:

```
# [Client name] — conversion tracking plan
Date: [YYYY-MM-DD]
Tier: [GA4 / GA4 + GTM / Server-side]
CMS: [platform]   Booking: [system]
Ad platforms to import: [list]

---

## Measurement plan
[The events table — what we track and why]

## GA4 setup
[Property config, key events to mark as conversions]

## GTM setup        (Growth + Scale)
[Tags, triggers, variables — one block each]

## Platform conversions
[Google Ads import + Meta pixel/CAPI config]

## Server-side       (Scale only)
[sGTM / CAPI gateway notes]

## Consent & privacy
[Consent Mode, PII handling]

## QA checklist
[The validation gate — tick before launch]
```

---

## Event taxonomy (the standard set)

Use these event names across every client so reporting stays consistent. Map the client's real lead actions onto this set.

| Event name | Fires when | Value | Primary? |
|---|---|---|---|
| `generate_lead` | Any lead action completes (umbrella) | est. lead value | ✓ |
| `phone_call` | Click-to-call tap, or tracked-number call | est. lead value | ✓ |
| `form_submit` | Contact/enquiry form success | est. lead value | ✓ |
| `booking_start` | User reaches the booking widget/page | — | — |
| `booking_confirmed` | Online booking completes | est. patient value | ✓ |
| `email_click` | Mailto click | — | — |
| `chat_started` | Live chat opened | — | — |

Rules:
- **Primary events** become conversions in GA4 and get imported to the ad platforms.
- Set a sensible **value** per lead so ROAS is calculable (use the client's average lead or patient value from `CLAUDE.md`; if unknown, ask).
- Booking confirmations beat booking starts — optimise ads to the confirmed action where the booking system allows it.

---

## GA4 setup (all tiers)

1. Confirm one GA4 property exists for the site (not duplicated). Note the Measurement ID.
2. Create the key events from the taxonomy above.
3. Mark the **primary** events as key events / conversions.
4. Link GA4 to Google Ads (for import + audience sharing).
5. Set data retention to 14 months. Turn on Google signals only if consent allows.

---

## GTM setup (Growth + Scale)

For each tracked action, document the trigger, tag, and any variables.

**Pattern per event:**

```
Event: form_submit
  Trigger: [form success — element visibility on thank-you, or form-submit listener]
  Tags:
    - GA4 event tag → event name: form_submit, params: {value, currency}
    - Google Ads conversion tag → [conversion label]
    - Meta pixel → Lead
  Variables needed: [dataLayer value, form ID, page path]
```

Common triggers by CMS:
- **WordPress + form plugin** — listen for the plugin's submit event, or thank-you page view.
- **Cliniko / external booking** — track the outbound click to the booking domain (you often can't see inside their booking flow, so the booking-link click is the measurable proxy unless they support callbacks).
- **Click-to-call** — trigger on `tel:` link clicks.

Document the `dataLayer` pushes the site needs, if any. Flag where a developer is required.

---

## Platform conversions

**Google Ads:**
- Import the GA4 primary key events as conversions, OR use Google Ads conversion tags via GTM. Pick one source of truth — don't double-count.
- Set the right conversion action category (Submit lead form, Contact, Book appointment).

**Meta:**
- Pixel fires standard events: `Lead` for forms/calls, `Schedule` for bookings.
- On Growth, pixel only. On Scale, add **CAPI** (see server-side).
- Use `event_id` so pixel + CAPI events deduplicate.

---

## Server-side (Scale only)

- Stand up server-side GTM (or a CAPI gateway) on a subdomain.
- Route GA4 + Meta events server-side; keep `event_id` for dedup.
- Hash all PII (email, phone) with SHA-256 before it leaves the server. Never send raw PII.
- Target: most conversions confirmed server-side so iOS and ad blockers don't blind the account.

Reference the `.claude/skills/ads-server-side-tracking` and `ads-attribution` skills for the deep technical detail.

---

## Consent & privacy

- If there's a consent banner, set up **Consent Mode v2** — tags wait for consent, GA4 uses modelling for declined users.
- Never send raw email or phone to any platform unhashed.
- Australian Privacy Act applies — match whatever the client's privacy policy already states. If they don't have one, flag it.

---

## QA checklist (the gate — do not skip)

Tick every line before any campaign goes live. This is the whole point of the skill.

```
[ ] GA4 receiving data (Realtime shows the test session)
[ ] Each primary event fires once per action (no double-fires)
[ ] A test form submit shows as form_submit in GA4 Realtime
[ ] A test click-to-call shows as phone_call
[ ] A test booking click/confirm shows correctly
[ ] Google Ads shows the imported conversion (no "no recent conversions" warning)
[ ] Meta Test Events tool shows the pixel event
[ ] (Scale) CAPI event shows, and dedupes against the pixel via event_id
[ ] Values are attached and look right
[ ] Consent Mode behaves: tags hold before consent, fire after
[ ] No PII sent in plain text (check the network/tag payloads)
```

If any line fails, tracking is broken. Fix it before launch. No exceptions.

---

## Finalise and deliver

1. Save the plan to `clients/<name>/tracking/tracking-plan.md`.
2. Print a short summary:

```
✓ Tracking plan built: [client name]
  Tier: [GA4 / GA4 + GTM / Server-side]
  Events tracked: [list of primary events]
  Ad platforms: [list]
  File: clients/<name>/tracking/tracking-plan.md

Needs a human/developer to:
  — [e.g. install GTM container on site]
  — [e.g. add dataLayer push on form success]
  — [e.g. confirm Cliniko booking-link click is the chosen proxy]

Before any campaign launches:
  — Run the QA checklist in the plan. Every line must pass.
```
