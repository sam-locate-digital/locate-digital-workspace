# Swipe file — hook library

## Master source: live Google Sheet

**Title:** Hooks
**File ID:** `1QQVgwaiPaGfGMgqJ4q65k0BXYv5BkiOfva8HIf2XDj4`
**Open:** https://docs.google.com/spreadsheets/d/1QQVgwaiPaGfGMgqJ4q65k0BXYv5BkiOfva8HIf2XDj4/edit

The Sheet holds ~1000 **intro hooks** — these are the first-3-second opening lines of a reel, not full scripts. Most use fill-in-the-blank patterns (`[insert X]`) so they adapt to any topic.

### Columns to use
- **Hook** — the intro line template
- **Inspo link** — Instagram/TikTok URL of the reel that went viral with that hook (use to study the original)

### Columns to ignore
- **Brand** — ignore (was previously used to filter; no longer relevant)
- **Notes** — ignore

### Tabs (categories)
- Educational Hooks
- _(other tabs auto-detected on read)_

### How the skill reads it

1. Call `mcp__claude_ai_Google_Drive__read_file_content` with `fileId: 1QQVgwaiPaGfGMgqJ4q65k0BXYv5BkiOfva8HIf2XDj4`
2. File is large (~150k chars) — if truncation hits, use `offset`/`limit` to read in chunks of ~30k chars and search for keywords matching the requested topic
3. Pull 5–8 candidate hooks matching the topic, pick the strongest 1–3, fill in the `[insert X]` blanks with the topic specifics, reference the inspo link in output

### If Drive isn't connected
Tell Sam: "Run `/mcp` and authenticate Google Drive so I can read your hook library." Then proceed with general patterns from `SKILL.md` only.

---

## Quick captures (manual)

Reels you spot in the wild that aren't in the Sheet yet. Migrate to the master Sheet weekly.

### Entry template

```
### [creator handle] — [YYYY-MM-DD]
- Link:
- Niche: dental / physio / accountant / lawyer / osteo / salon / agency / general
- Hook (verbatim):
- Format: talking head / b-roll VO / text-on-black / screen rec / split-screen
- Why it worked: 1–2 lines
```

---

### Entries

_(none yet)_
