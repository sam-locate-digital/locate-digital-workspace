---
name: wrapup
description: Save the session to Sam's Supabase session memory at the end of a Claude Code session - a summary, the decisions and why, and what's still open - so the startup skill can pick it up next time. Also offers any new rule for the right CLAUDE.md and reports uncommitted work, without committing or pushing. Use when Sam says "wrapup", "wrap up", "save the session" or "end of session".
---

# Wrapup - save the session

Write one record of this session that the next `/startup` can read in 30 seconds. Be exact about what was done and what's still open. A vague summary costs the next session an hour.

## Keys

Same as startup: the Locate workspace `.env` at `G:\My Drive\Claude Code.Locate\.env`, whatever folder the session is in. Run every command with the Bash tool (Git Bash) and start each one with this block. Shell state doesn't carry between calls.

```bash
ENV_FILE="/g/My Drive/Claude Code.Locate/.env"
get_env() { local key="${@:1:1}"; sed '1s/^\xEF\xBB\xBF//' "$ENV_FILE" 2>/dev/null | grep -m1 "^${key}=" | cut -d= -f2- | tr -d '\r' | sed -e 's/^["'\'']//' -e 's/["'\'']$//'; }
SUPABASE_URL=$(get_env SUPABASE_URL); SUPABASE_URL=${SUPABASE_URL%/}; SUPABASE_URL=${SUPABASE_URL%/rest/v1}; SUPABASE_URL=${SUPABASE_URL%/}
SB_KEY=$(get_env SUPABASE_SERVICE_ROLE_KEY)
[ -n "$SUPABASE_URL" ] && echo "SUPABASE_URL set" || echo "SUPABASE_URL MISSING"
[ -n "$SB_KEY" ] && echo "SUPABASE_SERVICE_ROLE_KEY set" || echo "SUPABASE_SERVICE_ROLE_KEY MISSING"
AUTH=(-H "apikey: $SB_KEY"); case "$SB_KEY" in eyJ*) AUTH+=(-H "Authorization: Bearer $SB_KEY");; esac
```

The URL line also drops a trailing `/rest/v1`, since the commands below add it themselves. Without that, a `.env` URL copied with `/rest/v1` on the end fails with `PGRST125 Invalid path`.

The `[ -n ]` lines are the only way to look at a key. Never `echo` a key, never `${VAR:-...}` or `${VAR:+...}`, never `cat`, `grep` or open the `.env`. If either is missing, say so and stop.

## Steps

### 1. Name the project

- Inside `clients/<Name>/` → `<Name>`, spelt as the folder is (`MOSIC`, `MaxiFinancial`).
- At the workspace root or in an agency folder (`_brand/`, `_ops/`, `_skills/`…) → the client the work was for, if it was mostly for one client; otherwise `locate-digital`.
- Any other folder outside the workspace → that folder's name.

If the session did real work for more than one client, save one record per client, each with only that client's work.

### 2. Read the entire session

Start to finish, then write 3 things:

- **Summary** - what was done, for whom, and the result. Name the files made or changed. Numbers where there are numbers.
- **Decisions** - each decision and the reason behind it. The reason is the part that's useful later.
- **Open items** - everything not finished, anything started and dropped, uncommitted work, and what to do first next time.

Do a second pass. The first one always misses something.

Keep client personal details out of the record: no loan applicant names, financial figures about individuals, health details or contact details. Describe the work ("reviewed 3 loan docs for MaxiFinancial"), not the person. The record lives in the cloud.

### 3. Save the record

Write the record as JSON with the Write tool, to a file in the session's scratchpad directory (or another temp folder outside the workspace). Never build it inside a shell command, where a dollar sign or a quote silently breaks it. Get today's local date with `date +%F` and set `session_date` yourself - left out, the database stamps the UTC date, which is yesterday in Australia until 10 or 11am.

`summary` is one text string. `decisions_made` and `pending_items` are **lists of strings**, one decision or open item per entry, because the table stores them as text arrays. A single string there fails with `22P02 malformed array literal`.

```json
{"session_date": "<YYYY-MM-DD>", "project_name": "<project>", "project_path": "<full path of the session folder>",
 "summary": "<summary>",
 "decisions_made": ["<decision> - <why>", "<decision> - <why>"],
 "pending_items": ["<open item>", "<open item>"]}
```

The table has four more optional list columns, filled the same way when the session has something for them: `actions_taken`, `rules_learned`, `problems_and_solutions` and `data_discovered`. Leave them out otherwise.

Then post it, using the file's path with forward slashes. The record file is only deleted once the save succeeds, so a failed save can be fixed and retried without rewriting it:

```bash
# (key block above first)
J="<path to the json file>"
R=$(curl -s -w "\nHTTP %{http_code}" -X POST "$SUPABASE_URL/rest/v1/session_memories" "${AUTH[@]}" \
  -H "Content-Type: application/json" -H "Prefer: return=representation" --data-binary @"$J")
echo "$R" | tail -c 600
case "$R" in *"HTTP 201") rm -f "$J"; echo "saved - record file removed";; *) echo "NOT saved - record file kept for retry";; esac
```

`HTTP 201` with the saved row echoed back means it landed. Anything else - an error message, another status, nothing at all - means it didn't: read the error, fix the file, and try once more. A wrapup that didn't land is a lost day. Common errors:
- `PGRST125 Invalid path`: the URL is wrong. Check that `.env` has the plain project URL `https://<ref>.supabase.co`.
- `22P02 malformed array literal`: a list column was sent as a string. Make it a JSON list.
- `401` or `Invalid API key`: the key is wrong or is the public anon/publishable key. It must be the service role (secret) key.

### 4. Offer any new rule

If the session produced a rule or a preference - "never do X", "this client prefers Y", "always Z" - it belongs in a CLAUDE.md, where it loads every session:

- About one client: `clients/<Name>/CLAUDE.md`, under a `## Rules` heading.
- About the agency or how Sam works across clients: the workspace `CLAUDE.md`.

Show Sam the exact line and where it would go, and add it only on a yes. One line per rule.

### 5. Report what isn't committed

Don't commit or push. If the session folder is in a git repository, run `git status --short` and list the files this session changed that are still uncommitted, so Sam can commit them when ready. Leave other people's or earlier sessions' untracked files out of the list.

### 6. Confirm

2 or 3 lines: saved (project and date), any rule added and where, and what's still uncommitted.

## Rules

- Never write a secret into the record - no key, password or token. Say "rotated the OpenAI key in .env", never the value.
- Never print the Supabase key or write it into a file.
- Never commit or push as part of wrapup.
