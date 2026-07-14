---
name: meta-ads-compliance-checker
description: Checks Lance ad copy or ad creative descriptions (including screenshot/mockup descriptions) against known Meta ads compliance risk patterns — dollar figures read as implied earnings claims, scarcity claims, unverified stats/testimonials, vague vs specific claims. Outputs a risk rating (LOW/MEDIUM/HIGH) per flag plus an overall rating and suggested fix. Use before any ad copy or creative goes to Marina for sign-off.
---

# Meta Ads Compliance Checker

Checks a piece of ad copy or a creative description against Lance's known Meta
compliance risk patterns and reports a risk rating with suggested fixes.

## When to use this

Any time new ad copy, headline, or creative/screenshot description is drafted
for Lance and needs a compliance pass before it goes further — before it's
shown to Marina for sign-off, and definitely before anything spends money or
goes live.

## How to run it

First pass, deterministic pattern scan:

```bash
python3 .claude/skills/meta-ads-compliance-checker/scripts/check_compliance.py "<ad copy or creative description>"
```

Or from a file:

```bash
python3 .claude/skills/meta-ads-compliance-checker/scripts/check_compliance.py --file path/to/copy.txt
```

Add `--json` for machine-readable output.

The script catches the mechanical patterns (dollar amounts, scarcity phrasing,
numeric social-proof claims, quote-like testimonials). It cannot judge things
that need actual context — e.g. whether "ONLY 10 SPOTS LEFT" is true and
enforced, or whether a stat is real or a placeholder. After running the
script, add judgment on top using the rules below before reporting back.

## Risk rules (from CLAUDE.md — re-check there if this drifts)

1. **Dollar figures in creative/screenshots → HIGH.** Specific dollar amounts
   read as implied earnings claims even in obvious UI mockups. This applies
   even if the number is just illustrative UI content, not a claim about the
   user's actual earnings.
2. **Scarcity claims → HIGH unless verified true and enforced.** ("only X
   spots left", "limited time", "last chance", etc.) These are a known
   rejection trigger. Never mark this safe without explicit confirmation that
   the cap is real — if it's unconfirmed, treat it as a live risk, not a pass.
3. **Unverified stats / user counts / testimonials → MEDIUM.** Real proof
   only. If a number or testimonial isn't confirmed real, it's a placeholder,
   not final copy — say so explicitly, don't launder it into a pass.
4. **Vague, non-specific claims → LOW.** ("organised freelancers earn more")
   Lower risk than specific figures or stats. Personal-narrative copy with no
   stats or claims at all is the safest, most on-brand pattern seen so far.

## Output format

For each input, report:

- **Overall risk rating**: LOW / MEDIUM / HIGH (highest of any individual flag)
- **Findings**: one entry per flagged pattern — category, rating, the exact
  matched text, why it's flagged, and a concrete suggested fix (not just "make
  it safer" — an actual rewrite or specific next step, e.g. "confirm the spot
  cap with Marina" or "drop the $4,100 figure and replace with 'get paid
  faster'")
- If nothing is flagged, say so plainly — don't invent risk to pad the report

Always close with: this is a risk flag, not a decision — anything going live
or spending money still needs Marina's sign-off.

## Notes

- This skill flags risk, it doesn't clear copy for launch. Never report
  something as "compliant" or "approved" — report it as "no known patterns
  flagged" and leave the sign-off call to Marina.
- If the copy contains a stat or figure that matches an item already listed
  under "Open items" in CLAUDE.md (e.g. the $4,100/$7,700 screenshot, the
  ONLY 10 SPOTS LEFT line, the 2,400+ freelancers stat), call that out
  explicitly as a known unresolved risk rather than treating it as new.
