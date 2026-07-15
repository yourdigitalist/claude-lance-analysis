# Landing Page Audit — 2026-07-14 — BLOCKED (partial)

**Status: could not complete.** getlance.app is unreachable from this session: the site (or its CDN) returns 403 to the fetch tooling, the environment's network policy blocks direct browser access to arbitrary domains, and archive snapshots are also unreachable. Rather than audit from memory or invent findings, this file records what CAN be said, what to check, and how to finish the audit.

## What was confirmed

- The signup page title is "Lance – Manage your business" ([getlance.app/auth](https://www.getlance.app/auth?tab=signup), surfaced via search). No other live copy could be captured.

## Known issue to check first (from CLAUDE.md, not from viewing the page)

- **"2,400+ freelancers trust Lance" is a confirmed placeholder.** If it is still on the live page, that's a red-rated item under lance-voice rule 5 (real proof only): it must be replaced with a real number or removed. This is already tracked as an open risk in /dashboard/data/risks.json regardless of audit completion.

## Audit checklist (to run when the page is accessible)

Against **lance-voice**:
- [ ] Any em dashes in page copy
- [ ] Any "isn't just X, it's Y" constructions
- [ ] Any AI-phrasing/SaaS clichés ("everything you need...", "simple, honest pricing")
- [ ] Every stat/number on the page: real, placeholder, or fabricated? ("2,400+ freelancers" especially)
- [ ] Sentence length / casual directness

Against the **pain-point map**:
- [ ] Does the hero speak to scattered feedback / chasing approvals (loudest researched pain) in the visitor's words?
- [ ] Is the DIY-stack alternative ("you're duct-taping Notion + spreadsheets + a free invoice tool") named anywhere?
- [ ] Does invoicing copy connect to approval flow (the unique combination) or sit in a generic feature grid?

Against **conversion basics** (cro skill):
- [ ] Is the approvals differentiator above the fold, or buried in a feature grid? (CLAUDE.md says foreground it)
- [ ] One clear primary CTA? What does the button say — value ("Start your 15-day free trial") or generic ("Sign up")?
- [ ] Is $29/mo + 15-day trial visible without hunting?
- [ ] Any unsubstantiated claims remaining anywhere on the page

## How to finish this audit

Run from a session with normal network access (or paste the page HTML/screenshots into the repo under /product/lp-snapshots/):

1. Capture full-page screenshot + text of getlance.app
2. Work through the checklist above
3. Rate each finding green/yellow/red per lance-voice
4. Rewrite this file with findings, keeping the date in the filename convention (new date, new file — this one stays as the record that the first attempt was blocked)
