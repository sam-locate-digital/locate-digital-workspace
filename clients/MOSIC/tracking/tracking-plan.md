# MOSIC — conversion tracking plan
Date: 2026-06-23
Tier: GA4 + GTM (Growth)
CMS: WordPress (WPBakery)   Booking: Cliniko (online booking)
Ad platforms to import: Google Ads (active). Meta — config staged, switch on if/when they run it.

> Context: MOSIC runs Google Ads but has no verified conversion tracking. This plan closes the "set up conversion tracking audit before next spend cycle" item before more budget goes out. Right now spend can't be tied to bookings, so the account is flying blind.

---

## Measurement plan

What counts as a lead for an osteo clinic, and how we catch it. Three real entry points: phone calls, website enquiry forms, and Cliniko online bookings. Telehealth books through the same Cliniko flow.

| Event | Fires when | Value | Primary? |
|---|---|---|---|
| `phone_call` | Click-to-call tap on mobile (the `tel:` links in header/footer/contact) | new-patient value | ✓ |
| `form_submit` | Website enquiry/contact form success | new-patient value | ✓ |
| `booking_start` | User clicks through to the Cliniko booking page/widget | — | — |
| `booking_confirmed` | Cliniko booking completes *(see limitation below)* | new-patient value | ✓ |
| `generate_lead` | Umbrella event on any primary action, for GA4 reporting | new-patient value | ✓ |

**Value to assign:** set a single new-patient value so Google can optimise to revenue, not just clicks. Osteo initial consults run ~$110–130, and a new patient's value across a treatment block is meaningfully higher. **Recommend starting at $120 (first-visit value) — conservative and defensible.** Confirm with MOSIC before go-live; if they'll share average new-patient lifetime value from Cliniko, use that instead.

---

## GA4 setup

1. Confirm one GA4 property for the MOSIC site (the optional GA4 in their stack — verify it exists and isn't duplicated). Record the Measurement ID.
2. Create key events: `phone_call`, `form_submit`, `booking_start`, `booking_confirmed`, `generate_lead`.
3. Mark the primary events as key events / conversions.
4. Link GA4 → Google Ads (account already active) for conversion import and audience sharing.
5. Data retention 14 months. Google signals only if the consent banner allows.

---

## GTM setup

GTM is the cleanest path here because the site is WordPress and there are several actions to track. If no container is live yet, install one (developer or a WordPress GTM plugin).

**phone_call**
```
Trigger: Click — Just Links, where Click URL contains "tel:"
Tags:
  - GA4 event → phone_call  {value: 120, currency: AUD}
  - Google Ads conversion → [Phone call conversion label]
  - Meta pixel → Lead   (staged, paused until Meta runs)
Variables: Click URL, Page Path
```

**form_submit**
```
Trigger: depends on the form plugin —
  - Gravity Forms / CF7 / Elementor: use the plugin's submit-success event
    or a Form Submission trigger validated against a thank-you state
  - Fallback: thank-you page view (Page View where Path = /thank-you)
Tags:
  - GA4 event → form_submit  {value: 120, currency: AUD}
  - Google Ads conversion → [Lead form conversion label]
  - Meta pixel → Lead   (staged)
Variables: Form ID, Page Path
Note: confirm which form plugin MOSIC uses — it sets the trigger method.
```

**booking_start (Cliniko)**
```
Trigger: Click — Just Links, where Click URL contains the Cliniko booking domain
         (e.g. "cliniko.com" / "mosic.au1.cliniko.com" — confirm exact URL)
Tags:
  - GA4 event → booking_start
Variables: Click URL
```

**booking_confirmed — limitation, read this**
Cliniko's online booking runs on Cliniko's own domain (or an embedded widget you can't see inside). GTM on the MOSIC site can't directly detect a completed booking. Three options, best first:

1. **Cliniko booking confirmation redirect** — if the booking flow can return the patient to a MOSIC thank-you/confirmation URL, fire `booking_confirmed` on that page view. Cleanest signal. Check whether Cliniko supports a post-booking redirect on their plan.
2. **Cliniko API reconciliation** — MOSIC already needs the Cliniko API for reporting. Pull new bookings server-side and reconcile against ad clicks in the monthly report. Accurate, but offline (not real-time in Google Ads).
3. **Proxy (default for now)** — treat `booking_start` (the click to Cliniko) as the optimisation signal until option 1 or 2 is wired. Acceptable to launch on; tighten later.

Start on the proxy, pursue option 1 with whoever manages Cliniko.

---

## Platform conversions

**Google Ads (active):**
- Import GA4 primary key events as conversions — single source of truth, no double-counting with standalone Ads tags.
- Conversion categories: `phone_call` → Phone calls; `form_submit` → Submit lead form; `booking_confirmed`/`booking_start` → Book appointment.
- Optimise campaigns to the strongest *confirmed* signal available (form_submit + phone_call reliably; bookings once option 1/2 lands).

**Meta (staged):**
- Pixel + standard events written into GTM but paused. Flip on the day MOSIC starts Meta. `Lead` for forms/calls, `Schedule` for bookings.

---

## Server-side

Not in scope at the Growth tier. Worth flagging to MOSIC as a Scale upgrade: server-side GTM + Google's enhanced conversions would recover iOS/ad-blocker loss and sharpen the new-patient data. Park it as an upsell, don't build it now.

---

## Consent & privacy

- If the site has a cookie/consent banner, set up **Consent Mode v2** — tags wait for consent, GA4 models the gap.
- Health data sensitivity: never pass any condition, treatment, or patient detail into events. Track *that* a booking happened, never *what for*.
- No raw email or phone in any event payload. If enhanced conversions are turned on later, Google hashes the data — confirm it's hashing, not sending plain.
- Australian Privacy Act applies. Match MOSIC's existing privacy policy; if it doesn't mention analytics/advertising cookies, flag that to update.

---

## QA checklist (the gate — do not skip)

Run before the next spend cycle. Every line passes, or tracking is broken.

```
[ ] GA4 Realtime shows a test session
[ ] tel: click fires phone_call once (no double-fire)
[ ] Test enquiry form fires form_submit once
[ ] Click to Cliniko fires booking_start
[ ] booking_confirmed fires (if redirect option live) — else proxy noted as known gap
[ ] Google Ads shows imported conversions (no "no recent conversions" warning)
[ ] Conversion values show $120 AUD (or confirmed value)
[ ] Meta tags confirmed PAUSED (not firing yet)
[ ] Consent Mode holds tags pre-consent, fires post-consent
[ ] No PII or health detail in any tag payload (check network)
```

---

## Summary

```
✓ Tracking plan built: MOSIC
  Tier: GA4 + GTM (Growth)
  Events tracked: phone_call, form_submit, booking_start, booking_confirmed, generate_lead
  Ad platforms: Google Ads (live import), Meta (staged/paused)
  File: clients/MOSIC/tracking/tracking-plan.md

Needs a human/developer to:
  — Confirm a GTM container is installed on the WordPress site (add if not)
  — Identify the form plugin so the form_submit trigger is set correctly
  — Confirm the exact Cliniko booking URL/domain for the click trigger
  — Investigate Cliniko post-booking redirect (option 1) for true booking_confirmed
  — Confirm the new-patient conversion value with MOSIC (default $120)

Before the next spend cycle:
  — Run the QA checklist above. Every line must pass. No launch on broken tracking.
```
