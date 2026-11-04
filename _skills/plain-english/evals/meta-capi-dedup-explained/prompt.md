---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

I dont get this at all, explain it simpler pls:

"Your Meta setup is sending Lead events through both the browser Pixel and the Conversions API, but the event_id parameter is not being passed consistently between the two, so Meta cannot deduplicate them. As a result each lead is counted roughly twice in Events Manager (Event Match Quality is fine at 7.8, but the dedup rate shows 3%). Reported CPL is understated by about half and the campaign is optimising toward a doubled conversion signal. Fix: generate a single event_id on form submit and pass it to both the fbq() call and the server-side CAPI payload."
