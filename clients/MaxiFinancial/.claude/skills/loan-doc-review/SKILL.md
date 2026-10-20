---
name: loan-doc-review
description: >-
  Pre-submission review of a mortgage/home-loan client's supporting documents for Maxi Financial.
  Given a folder of a borrower's documents (ID, payslips, tax returns, bank/credit statements,
  contract of sale, etc.), it identifies the loan scenario, checks the file against the required-docs
  checklist for that scenario, reconciles details across documents for consistency, and runs
  responsible-lending / Best Interests Duty (NCCP) compliance checks — then produces a checklist +
  flagged-issues report so the broker knows exactly what's missing or wrong before lodging to a lender.
  Use this WHENEVER Sam or a Maxi Financial user asks to review a loan file, check a client's
  documents, run a pre-lodgement or pre-submission check, verify a borrower's paperwork, build a
  supporting-docs checklist, or asks "is this file ready to submit / what am I missing" — even if they
  don't say the word "skill". Also trigger on payslip/bank-statement/tax-return review for a home loan,
  VOI/identity checks, or genuine-savings and serviceability document checks.
---

# Loan document review (Maxi Financial)

Review a borrower's supporting documents before the loan is lodged to a lender. The goal is to catch
problems while there's still time to fix them cheaply — a missing document, a name that doesn't match,
an income figure that doesn't reconcile, or a responsible-lending gap — rather than have the lender
kick the file back after submission (slow, and it erodes the client's confidence).

This is a **decision-support aid for the broker, not a credit decision.** It flags what a careful
human reviewer would flag; the broker still applies their own judgment and the specific lender's
policy. Never state or imply that a loan is approved, will be approved, or that a borrower "qualifies".

## Who uses this and how

A Maxi Financial user points Claude at a folder containing one borrower's (or a couple's) documents —
scanned PDFs and images. They want back a clear report: what's present, what's missing, and every issue
worth a second look, sorted so the most urgent thing is at the top.

## Workflow

### 1. Locate and read the documents
The user will give a folder path. Read every document in it. Most will be PDFs or images (scanned
payslips, licences, statements). For images and scanned PDFs, read the visible text carefully —
names, dates, dollar figures, addresses, account numbers, employer names. Build a short internal
inventory of what each file actually is (don't trust the filename alone — open it and confirm).

If a file is unreadable (corrupt, password-protected, blank scan), note it as an issue rather than
silently skipping it — an unreadable payslip is effectively a missing payslip.

### 2. Identify the loan scenario
The required documents depend on the scenario. Determine two axes from the documents and anything the
user has told you:

- **Income type:** PAYG (employee) or Self-employed (sole trader / company / trust director).
  A borrower with both needs both sets. A couple may have one of each — assess each applicant.
- **Loan purpose:** Owner-occupier purchase · Investment purchase · Refinance · Construction.

If the scenario genuinely can't be determined from the documents, don't guess silently — state your
best inference, list what made it ambiguous, and proceed on the most likely scenario while noting the
assumption at the top of the report.

Then read `references/document-requirements.md` and assemble the checklist: the **base requirements**
(everyone) + the **income-type** add-ons + the **loan-purpose** add-ons for this file.

### 3. Check completeness
For each required document, mark it Present, Missing, or Unreadable. "Present" means you actually saw
a document of that type in the folder — not that the user mentioned it. Currency matters: many
documents have a freshness window (payslips within ~30 days, transaction statements covering the last
~90 days, etc.). A document that's present but stale is not a clean pass — flag it. The freshness
windows are in the requirements reference.

### 4. Check consistency and compliance
Read `references/review-checks.md` and work through it. Two families of checks:

- **Consistency** — reconcile the same fact across different documents. Names, DOB, and current
  address should match across ID, payslips, and statements. Payslip income should reconcile against
  salary credits visible in the bank statements and against the YTD figure. Employer names should
  match between payslip and salary credit narration. Self-employed income should be consistent across
  tax returns, NOAs and BAS. Mismatches are where fraud, stale documents, and data-entry errors hide,
  so treat any unexplained mismatch as worth a human look.
- **Compliance / Best Interests Duty (NCCP)** — the responsible-lending essentials: is income verified
  with evidence, are living expenses verified against actual statements (not just declared), are all
  liabilities documented, does the file hold the evidence a broker needs to demonstrate the loan is
  not unsuitable and is in the client's best interests. This skill checks that the *evidence exists in
  the file*; it does not perform the serviceability calculation or make the suitability judgment.

### 5. Produce the report
Use the exact structure in "Report format" below. Lead with the scenario and a one-line readiness
verdict, then the checklist, then flagged issues sorted worst-first by severity.

## Severity tiers

Sort every flagged issue into one of three tiers, worst-first, so the user reads the deal-blockers
before the nitpicks:

- **🔴 Blocker** — the file cannot be lodged as-is. A required document is missing, unreadable, or
  expired; or a consistency mismatch is serious enough that the lender will reject or query it
  immediately (e.g. name on ID doesn't match name on application, income can't be evidenced).
- **🟠 Review** — needs a human decision before lodging. A possible compliance gap, an unexplained
  inconsistency, a stale-but-present document, or something that depends on the specific lender's
  policy. Not automatically fatal, but don't lodge without resolving it.
- **🟡 Minor** — low-risk / cosmetic. Worth tidying but won't hold up the file (e.g. a statement is
  present and current but slightly hard to read, a middle name is abbreviated on one doc).

When unsure between two tiers, pick the higher one and say why — under-flagging a real problem costs
the client far more than an extra second of the broker's attention.

## Report format

Always use this structure:

```
# Loan Document Review — [Borrower name(s)]
**Scenario:** [Income type] · [Loan purpose]   |   **Reviewed:** [date]   |   **Files reviewed:** [N]

## Readiness: [Ready to lodge ✅ / Not ready — N blocker(s) ❌ / Ready with items to confirm ⚠️]
[One or two sentences: the headline. What's the single most important thing to do next.]

## Document checklist
| Document | Required | Status | Note |
|---|---|---|---|
| [e.g. Photo ID (licence/passport)] | Yes | ✅ Present | [e.g. Licence, current] |
| [e.g. 2 recent payslips] | Yes | ❌ Missing | [what to request] |
| [e.g. 90 days transaction statements] | Yes | ⚠️ Stale | [dated outside window] |
...

## Flagged issues
### 🔴 Blockers
1. **[Short title]** — [what's wrong, which documents, why it blocks lodgement]. → *[action]*

### 🟠 Review
1. **[Short title]** — [the inconsistency or compliance gap, evidence]. → *[action]*

### 🟡 Minor
1. **[Short title]** — [detail]. → *[action]*

## Client callback list
A plain-language list the broker can send straight to the client:
- [ ] [e.g. Two most recent payslips (last one is from 6 weeks ago — need a current one)]
- [ ] [e.g. Bank statement for the CBA account shown on your payslip — we don't have it]

## Compliance / BID note
[2–4 lines: is income verified, are living expenses verified against statements, are liabilities
documented, is the file's evidence sufficient to support a not-unsuitable / best-interests assessment.
State plainly what's still needed for the file to stand up. This is a documentation check, not a
suitability determination.]
```

If nothing is wrong in a section, keep the heading and write "None." — an empty section is a
meaningful result (it tells the broker you checked), whereas a deleted section looks like an oversight.

## Guardrails

- **Don't invent documents or figures.** If you can't read a number, say so and flag it — a guessed
  income figure is worse than a "couldn't read this" flag.
- **Don't approve or decline.** No statement that the borrower qualifies, will be approved, or is a
  good/bad risk. You surface evidence and gaps; the broker and lender decide.
- **Requirements vary by lender.** The reference reflects standard Australian practice and common
  lender expectations. Where something is genuinely lender-specific, flag it as 🟠 Review rather than
  asserting a hard rule.
- **Privacy.** This handles sensitive personal and financial data. Keep it in the review; never copy
  identifiable borrower data into any external service, and don't retain it beyond the task.
- **Scope of the two references:** `references/document-requirements.md` for what's required per
  scenario and freshness windows; `references/review-checks.md` for the consistency reconciliations
  and the NCCP/BID compliance checklist. Read the relevant one when you reach steps 2–4 above.
