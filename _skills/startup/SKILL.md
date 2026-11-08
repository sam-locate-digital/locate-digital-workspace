---
name: startup
description: Load Sam's session memory at the start of a Claude Code session. Pulls the last sessions for the current client or project from the Supabase session_memories table and recaps where things stand and what's still open. Also searches past sessions by keyword ("when did we…", "find the session where…"). Use when Sam says "startup", "start up", "load memory", "load context" or "where did we leave off". Saving a session is the wrapup skill's job.
---

# Startup - load the session memory

Pull the recent sessions for the project Sam is working on and give a short recap of where things were left. Fetch, read, summarise. Never dump raw JSON at Sam.

## Keys

The keys live in one place: the Locate workspace `.env` at `G:\My Drive\Claude Code.Locate\.env` (git-ignored). It doesn't matter which folder the session is in.

- `SUPABASE_URL` - e.g. `https://abc123.supabase.co`
- `SUPABASE_SERVICE_ROLE_KEY` - the project's secret key (`sb_secret_...`) or the legacy service_role key (`eyJ...`)

Run every command below with the Bash tool (Git Bash), and start each one with this block. Shell state doesn't carry between calls, so a command without it has no keys.

```bash
ENV_FILE="/g/My Drive/Claude Code.Locate/.env"
get_env() { local key="${@:1:1}"; sed '1s/^\xEF\xBB\xBF//' "$ENV_FILE" 2>/dev/null | grep -m1 "^${key}=" | cut -d= -f2- | tr -d '\r' | sed -e 's/^["'\'']//' -e 's/["'\'']$//'; }
SUPABASE_URL=$(get_env SUPABASE_URL); SUPABASE_URL=${SUPABASE_URL%/}; SUPABASE_URL=${SUPABASE_URL%/rest/v1}; SUPABASE_URL=${SUPABASE_URL%/}
SB_KEY=$(get_env SUPABASE_SERVICE_ROLE_KEY)
[ -n "$SUPABASE_URL" ] && echo "SUPABASE_URL set" || echo "SUPABASE_URL MISSING"
[ -n "$SB_KEY" ] && echo "SUPABASE_SERVICE_ROLE_KEY set" || echo "SUPABASE_SERVICE_ROLE_KEY MISSING"
AUTH=(-H "apikey: $SB_KEY"); case "$SB_KEY" in eyJ*) AUTH+=(-H "Authorization: Bearer $SB_KEY");; esac
```

The `[ -n ]` lines are the only way to look at a key. Never `echo` a key, never `${VAR:-...}` or `${VAR:+...}`, never `cat`, `grep` or open the `.env`.

If either is missing, say "I can't find your Supabase keys in the workspace .env" and stop. Don't guess and don't fall back to anything else.

## Steps

### 1. Name the project

Work it out from the folder the session is in:

- Inside `clients/<Name>/` (at any depth) → `<Name>`, exactly as the folder is spelt: `MOSIC`, `MaxiFinancial`, `BrightenHomeLoans`.
- The workspace root, or an agency folder (`_brand/`, `_ops/`, `_skills/`, `_services/`…) → `locate-digital`.
- Any other folder outside the workspace → that folder's name.

If Sam names a client or project ("startup for MOSIC"), use that instead, spelt as its `clients/` folder is.

### 2. Pull the last 10 sessions

For a client or project:

```bash
# (key block above first)
curl -s -G -w "\nHTTP %{http_code}\n" "$SUPABASE_URL/rest/v1/session_memories" "${AUTH[@]}" \
  --data-urlencode "project_name=eq.<PROJECT>" \
  --data-urlencode "select=session_date,project_name,summary,decisions_made,pending_items" \
  --data-urlencode "order=session_date.desc,created_at.desc" \
  --data-urlencode "limit=10"
```

When the project is `locate-digital` (a session started at the workspace root), Sam may be about to work on anything. Run the same query without the `project_name` line, so the recap covers the latest sessions across every client, grouped by project.

`[]` with `HTTP 200` means nothing is saved for this project yet. Say so and carry on.

Anything else - an error message, a status that isn't 200, or no response at all - means the URL or the key is wrong (a 401 points at the key, a failed connection at the URL). Say which and stop. Never read a failed call as an empty project.

### 3. Recap

Under 10 lines:

- Where the project stands, from the newest session.
- What's still open. Read the pending items across all the sessions and drop anything a later session closed.
- Any decision that still shapes today's work.

Then ask what Sam wants done by the end of this session.

Client facts and rules live in the CLAUDE.md files and load on their own. Don't fetch them here.

## When Sam asks about the past

"When did we…", "find the session where…" - search every session by keyword:

```bash
# (key block above first)
curl -s -G -w "\nHTTP %{http_code}\n" "$SUPABASE_URL/rest/v1/session_memories" "${AUTH[@]}" \
  --data-urlencode "tsv=wfts.<search terms>" \
  --data-urlencode "select=session_date,project_name,summary" \
  --data-urlencode "order=session_date.desc" \
  --data-urlencode "limit=10"
```

## Rules

- Never print the key and never write it into a file.
- Recap, don't replay. Sam wants to start working, not re-read last week.
