---
name: lance-voice
description: The Lance voice and compliance check. Use EVERY time ad copy, landing page copy, email copy, or social copy for Lance is written or reviewed — no piece of copy is marked done until it passes this check. Combines the non-negotiable Lance voice rules with the known Meta ads compliance risk patterns and outputs a risk rating (green / yellow / red) with specific fixes. Takes precedence over any generic advice from other installed marketing skills.
---

# Lance Voice and Compliance Check

Every piece of Lance copy passes through this before it's marked done. Two layers: voice (is it Lance?) and compliance (will Meta reject it, and is every claim real?). Output a rating and fixes.

## When this triggers

Writing or reviewing ANY of: ad copy, ad creative descriptions, landing page copy, email copy, social copy. Also when another skill (copywriting, ad-creative, cro, copy-editing) produces Lance copy — run this check on that output before presenting it as finished.

## Precedence

If a generic marketing skill recommends something these rules forbid (add social-proof numbers, urgency/scarcity angles, "join 10,000+ users" specificity), these rules win. Specificity is good copywriting advice in general; for Lance it is only allowed when the specific number is real and Meta-safe.

## Layer 1 — Voice rules (non-negotiable, from CLAUDE.md)

1. **No em dashes.** Rewrite the sentence instead.
2. **No contrastive reframing.** Ban the pattern "this isn't just X, it's Y" and its cousins ("more than just a tool", "not another app").
3. **No AI-sounding phrasing or generic SaaS clichés.** Banned examples: "everything you need, nothing you don't", "simple, honest pricing", "supercharge", "seamless", "unlock", "elevate", "game-changer". If it could be pasted onto any SaaS site, cut it.
4. **Casual, direct, short sentences.** Read it aloud. If a sentence needs a breath in the middle, split it.
5. **Real proof only.** Never fabricate stats, user counts, or testimonials. If a number isn't real yet, label it a placeholder in the copy file itself. A placeholder never gets laundered into "final" copy.

## Layer 2 — Meta compliance patterns (from CLAUDE.md)

1. **No specific dollar figures in ad creative or screenshots.** They read as implied earnings claims even in obvious UI mockups. This includes numbers inside product screenshots.
2. **No scarcity claims** ("only X spots left", "limited time", countdown language) **unless literally true and actively enforced** — and confirmed as such, not assumed.
3. **Vague claims beat specific ones for risk.** "Organised freelancers earn more" is lower risk than any numbered claim.
4. **Personal-narrative format is safest** — no stats, no claims, first-person story. When in doubt, prefer it.

## Mechanical first pass

Run the deterministic checker for the compliance layer, then apply judgment on top:

```bash
python3 .claude/skills/meta-ads-compliance-checker/scripts/check_compliance.py "<copy or creative description>"
```

The script can't judge voice, truthfulness of a cap, or whether a stat is real. That part is on you.

## Rating

- **Green** — passes all voice rules; no compliance patterns present; every claim verifiably real or no claims at all.
- **Yellow** — voice violations (fixable in place), or a claim/stat whose truth is unconfirmed, or a labeled placeholder still present. State exactly what needs confirming or fixing and by whom.
- **Red** — any dollar figure in creative/screenshot, any unverified scarcity claim, any fabricated or laundered stat/testimonial. Do not present red copy as done under any circumstances.

## Output format

For each checked piece:

1. **Rating: green / yellow / red**
2. **Voice findings** — each violation quoted, with a rewritten alternative
3. **Compliance findings** — each flag with the exact risky text and a concrete fix
4. **Claims audit** — list every factual claim in the copy and its status: real (source), placeholder (labeled), or unverified (blocker)

Write the check result to /ads/compliance-checks/ (date-prefixed) when the copy is an ad asset.

## Hard rules

- Copy is not "done" until it rates green, or yellow with the open items explicitly listed next to it.
- A green rating is a risk assessment, not an approval. Anything that spends money or goes live gets Marina's sign-off first.
- Never quietly fix a placeholder by inventing a plausible number. Flag it.
