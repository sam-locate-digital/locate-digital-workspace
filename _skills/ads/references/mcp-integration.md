# MCP Integration Guide

<!-- Created: 2026-04-13 | v1.5 -->
<!-- Purpose: How to pair claude-ads with live ad platform MCP servers -->

## Overview

claude-ads works with manually provided data by default (exports, screenshots, pasted metrics). For live API access, pair it with MCP servers that connect Claude Code directly to ad platform APIs.

## Available MCP Servers

### Google Ads: cohnen/mcp-google-ads

**Repo:** https://github.com/cohnen/mcp-google-ads
**Stars:** ~395 | **Tools:** 29 GAQL-based tools

**Setup:**
1. Install: `pip install mcp-google-ads` (or clone repo)
2. Configure Google Ads API credentials (OAuth2 or service account) — use a **read-only OAuth scope** for audit work
3. **Before adding credentials to `.mcp.json`, do this first:**
   - Add `.mcp.json` to your project's `.gitignore` so the file never reaches a public repo
   - Set restrictive file permissions: `chmod 600 .mcp.json` on Unix/macOS
   - Export the credentials into your shell as environment variables (so they live in your OS keychain / `.bashrc` / `~/.config`, not in a project file):
     ```bash
     export GOOGLE_ADS_DEVELOPER_TOKEN="..."
     export GOOGLE_ADS_CLIENT_ID="..."
     export GOOGLE_ADS_CLIENT_SECRET="..."
     export GOOGLE_ADS_REFRESH_TOKEN="..."
     export GOOGLE_ADS_LOGIN_CUSTOMER_ID="..."
     ```
4. Reference the env vars in `.mcp.json` so the file itself contains no secrets:
```json
{
  "mcpServers": {
    "google-ads": {
      "command": "python",
      "args": ["-m", "mcp_google_ads"],
      "env": {
        "GOOGLE_ADS_DEVELOPER_TOKEN": "${GOOGLE_ADS_DEVELOPER_TOKEN}",
        "GOOGLE_ADS_CLIENT_ID": "${GOOGLE_ADS_CLIENT_ID}",
        "GOOGLE_ADS_CLIENT_SECRET": "${GOOGLE_ADS_CLIENT_SECRET}",
        "GOOGLE_ADS_REFRESH_TOKEN": "${GOOGLE_ADS_REFRESH_TOKEN}",
        "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "${GOOGLE_ADS_LOGIN_CUSTOMER_ID}"
      }
    }
  }
}
```

> ⚠ **Why this matters.** A Google Ads refresh token + client secret + developer token is a full-account credential bundle. Committing `.mcp.json` with inline secrets to a public repo gives every reader long-lived API access. The `${VAR}` form keeps the file itself safe to commit if needed.

**What becomes automated:**
- Search term data for G13, G16, G17, G18, G19 (wasted spend checks)
- Quality Score data for G20-G25
- Campaign structure for G01-G12
- Conversion tracking status for G42-G49
- PMax asset group data for G31-G34, G-PM1 through G-PM6
- Budget and bidding data for G36-G41

**What stays manual:**
- Landing page analysis (G59-G61): use `analyze_landing.py`
- Creative quality assessment (subjective)
- Consent Mode V2 verification (requires GTM/tag audit)

### Multi-platform: Adspirer MCP (connected in Locate's Claude setup)

**Docs:** https://www.adspirer.com/docs
**Type:** Commercial MCP server, connected as a claude.ai connector
**Platforms:** Google, Meta, TikTok, LinkedIn, Microsoft, Amazon, plus GA4, Search Console and GTM

**Using it:**
- `get_connections_status` to see which accounts are linked (reuse a recent result, don't re-check before every call)
- `get_campaign_performance` (Google) and `get_meta_campaign_performance` (Meta) for performance pulls
- Everything else sits behind platform routers (`google_ads`, `meta_ads`, `tiktok_ads`, `linkedin_ads`, `microsoft_ads`, `amazon_ads`). Find the right inner tool with `search_tools`, get its exact inputs with `get_tool_schema`, then call the router with `action: "execute"`, `tool_name` and `arguments`. Never guess a tool name, parameter or account ID
- `get_usage_status` if calls start failing; on exhausted quota, say so and fall back to exports rather than retrying
- Budget inputs are account-currency decimal amounts, not cents or micros. Confirm the live schema and account currency before preparing any write

**What becomes automated:**
- Campaign performance data for M11-M18 (structure)
- Creative metrics for M25-M32 (fatigue detection)
- Audience overlap for M19 (overlap check)
- EMQ scores for M04 (requires Events Manager access)
- Google campaign, search term and keyword data for the G-checks listed above

**Alternative: Direct Meta API:**
No bundled fetcher ships with claude-ads. For a free, self-hosted option, write
a thin wrapper around the Meta Marketing API (Graph API) and import its JSON
output via the standard data-collection flow.

### LinkedIn Ads: Multiple Options

**GrowthSpree MCP:** https://www.growthspreeofficial.com/blogs/connect-linkedin-ads-to-claude-mcp
**Adzviser MCP:** https://adzviser.com/mcp/linkedin-ads

Both provide campaign data access for LinkedIn Ads analysis. Setup follows standard MCP patterns.

### TikTok Ads

Adspirer (above) covers this platform if the account is linked. Otherwise use:
- TikTok Ads Manager exports (CSV)
- TikTok Business API (custom integration via scripts)

### Microsoft Ads

Adspirer (above) covers this platform if the account is linked. Otherwise use:
- Microsoft Ads Editor exports
- Google Ads import data (if mirrored)
- Microsoft Advertising API (custom integration)

### Apple Ads

No Adspirer or dedicated MCP server for Apple Ads as of October 2026. Use:
- Apple Ads dashboard exports
- Apple Ads API (custom integration)

## Hybrid Workflow

The recommended approach combines MCP live data with claude-ads structured analysis:

```
1. Connect MCP server(s) for available platforms
2. Run /ads audit (claude-ads auto-detects MCP data sources)
3. For platforms without MCP, provide exports manually
4. claude-ads merges all data into unified audit
5. Health Score calculated across all platforms regardless of data source
```

## Live Account Rules

These apply whenever a skill reads a real ad account through an MCP server
(Adspirer or any other). Sub-skills point here.

### Scope every pull
- One account at a time. Locate runs many client accounts: if the request
  doesn't name the account, ask which one before pulling anything
- Use **complete days only** (exclude today). Default windows: last 30
  complete days for reviews, last 7 vs previous 7 for change checks
- State the account's **timezone, currency, date window and conversion
  definition** (which conversion actions count as primary) at the top of
  every output
- Never add up amounts in different currencies. Never treat Google, Meta and
  LinkedIn "conversions" as the same thing: their windows and definitions differ

### Separate what you saw from what you think
Every finding is labelled one of:
- **Observed**: a number pulled from the account
- **Possible cause**: a hypothesis that would explain it, with the evidence for it
- **Recommendation**: what to do, and how we'd know it worked

Period-over-period comparisons list the biggest observed changes first, then
possible causes. Don't present a cause as fact.

### Don't overstate waste or wins
- Zero conversions is not automatic proof of waste. Check for tracking gaps,
  conversion lag (lead gen often reports days late) and recently changed
  conversion actions before calling spend wasted
- Report "spend affected", not "savings". Pausing a campaign doesn't save its
  whole budget if some of its conversions were real
- Platform-attributed revenue is not causal lift. Say "attributed" unless an
  incrementality test backs it

### Changing an account
Audits and analysis are **read-only**. Kill lists, reallocations and fixes are
recommendations for Sam to approve, never applied during the audit. For a
later change Sam asks for:
1. Read the current state first
2. Show the account, the exact change, and any budget with its currency
3. Get explicit approval for that change (approval for one change doesn't cover the next)
4. Create new campaigns **paused**. Turning anything on, or raising spend, needs its own approval
5. Read the change back from the account before reporting it done

### When calls fail
Say what failed and what that leaves unverified. Never fill gaps with
estimated or benchmark numbers presented as account data, and don't repeat a
failing call blindly.

## Security Notes

- **MCP servers run locally** — no data leaves your machine except the API calls each server makes to its target ad platform.
- **Never inline credentials in committed files.** Add `.mcp.json` to `.gitignore`, set `chmod 600 .mcp.json` on Unix, and use `${ENV_VAR}` interpolation so the file contains references — not values. See the Google Ads setup above for the canonical pattern; the same applies to Meta, LinkedIn, and any future MCP server.
- **Use read-only OAuth scopes** for audit work. A refresh token issued for `https://www.googleapis.com/auth/adwords` allows campaign mutations; for audit-only the read scope is sufficient.
- **Rotate any token that was ever committed to a public repo**, even briefly. Treat the credential as compromised — search-engine caches and forks make deletion unreliable.
- **For write operations** (campaign changes, budget edits), see the CEP safety protocol discussion in the itallstartedwithaidea/google-ads-skills repo. Claude Ads itself is audit-only by design.
