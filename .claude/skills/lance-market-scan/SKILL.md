---
name: lance-market-scan
description: The repeatable Lance market research process. Use when asked to "run a market scan", on the monthly cadence, or when the dashboard flags research as stale (>45 days). Scans the full competitive landscape (paid all-in-ones, point solutions, AND the DIY stack), current pricing, and lead messaging; flags white space and eroded differentiators; writes dated findings to /research with linked sources; updates /positioning/current.md only with an explicit stated reason.
---

# Lance Market Scan

The repeatable market research process. Output: a dated findings file in /research, and (only if warranted) an explicitly-reasoned positioning update.

## Trigger

- "Run a market scan"
- Monthly cadence (dashboard flags when the last scan is >45 days old)
- Before any major positioning or campaign decision

## Process

### 1. Check the full landscape — never assume the competitive set

Cover all three tiers every time. Do NOT default to "Bonsai vs. HoneyBook vs. Dubsado" without re-checking:

- **Paid all-in-ones:** Bonsai, HoneyBook, Dubsado, Plutio, 17hats, Agiled — and actively search for new entrants each scan
- **Point solutions:** FreshBooks, Wave (invoicing), Trello, Asana (PM)
- **The DIY stack:** Notion + Trello/Asana + FreshBooks/Wave + spreadsheets + free tools. Last research (July 2026) showed this is the most common real alternative, not a named competitor. Check whether that's still true.

### 2. Check current pricing for each

Fetch current pricing pages. Record price, billing model, and free tier/trial. Note where Lance's $29/mo sits in the band (was $20–66/mo as of July 2026).

### 3. Check what messaging each is leading with

For each competitor: what's their hero headline, what feature or outcome are they foregrounding, who are they targeting? Screenshot or quote the actual hero copy with a link.

### 4. Flag white space and eroded differentiators

- **White space:** angles or audiences nobody is leading with that Lance could own
- **Erosion check:** for each Lance differentiator (currently: no-login client approvals link), verify whether competitors now offer the same thing. If a differentiator stopped being one, say so directly — don't soften it.

### 5. Write findings to /research

File: `/research/YYYY-MM-DD-market-scan.md`. Every claim gets a linked source (URL and date accessed). No source, no claim. If something couldn't be verified, mark it "unverified" rather than dropping or asserting it.

Structure: summary of what changed since last scan → per-competitor table (price, positioning, notable changes) → white space → differentiator status → implications for positioning (explicit).

### 6. Update positioning only if warranted — and say so

If findings change the picture, update `/positioning/current.md` with an explicit stated reason, archiving the old version to `/positioning/archive/` first (date-prefixed, with the reason). If findings do NOT warrant a change, state that explicitly in the scan file ("no positioning change warranted because..."). Never silently edit positioning.

### 7. Update the dashboard data

Refresh `/dashboard/data/research.json` (last-scan date) and, if positioning changed, `/dashboard/data/positioning.json`.

## Rules

- Sources are non-negotiable. Pricing and messaging claims link to the live page they came from.
- Date everything. The value of this process is the time series.
- When new research contradicts existing positioning, say so directly in the findings and to Marina — don't quietly assume the old framing.
