---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

one of my clients, Priya (mortgage broker), noticed her website was down for about 2 hours yesterday and wants to know what happened. heres what my dev notes say, how do i explain this to her without sounding like a robot:

"Root cause: the SSL cert on the apex domain expired at 09:14 AEST because auto-renewal failed — the ACME HTTP-01 challenge could not complete after the A record was changed during the hosting migration, so the old host was still answering the challenge. Browsers threw NET::ERR_CERT_DATE_INVALID and HSTS prevented users clicking through. Fixed at 11:20 by re-pointing DNS and manually reissuing the cert. Added uptime monitoring with cert-expiry alerts at 14 days."
