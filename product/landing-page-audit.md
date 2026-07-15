# Landing Page Audit — 2026-07-15 — COMPLETED

**Source:** full-page screenshot provided by Marina 2026-07-15, plus her notes (hero noun rotates through audience segments: freelancers, copywriters, designers, web developers...; hero image is a video intro of the app). First attempt 2026-07-14 was blocked (page unreachable from the research environment) — that's why this is a day late.

**Resolution caveat:** body copy is too small to read in the screenshot, so line-level voice checks (em dashes, sentence rhythm) could not be run. The section headings and major claims ARE legible and are audited below. To finish the line-level pass: export the copy from the landing page CMS (/admin/landing-content per the tech doc) into /product/lp-snapshots/ and run lance-voice on it.

## Overall rating: RED (one hard voice violation)

**Update 2026-07-15 (later same day):** Marina confirmed contracts WITH e-signatures exist in the product — the tech/journey docs are stale, not the page. That finding is resolved below; the remaining hard violation is the pricing heading.

## Findings

### RED — "Simple, honest pricing." section heading
This is verbatim on the banned list in CLAUDE.md (voice rules: no generic SaaS clichés, with "simple, honest pricing" named explicitly). It must change. On-voice alternatives to consider: "One plan. $29." / "What it costs." / "No tiers, no add-ons." (all pass lance-voice; Marina picks).

### RESOLVED — "Signed contracts without the back-and-forth." section
Flagged 2026-07-15 because neither the technical build doc nor the user journey doc documents a contracts/e-signature feature. **Marina confirmed same day: contracts with e-signatures exist in the product — the docs are stale.** Page claim is legitimate. Follow-up: update the product docs (and the extracts in /product/reference/) so future audits don't re-flag this.

### YELLOW — "The average freelancer pays $75/month to run their business."
Specific stat, no visible source. If $75 is the sum of the actual tool prices listed in the comparison table next to it, it's defensible arithmetic — but then (a) verify those listed prices are current (our 2026-07-14 market scan has sourced prices to check against) and (b) say "adds up to" rather than "the average freelancer pays", which claims survey data we don't have. If it's not the table sum, it's an invented stat and has to go.

### YELLOW — "What our beta testers say." testimonials (8 cards)
Real-proof-only rule: confirm each quote is from a real beta tester who agreed to be quoted. If yes, green (and consider adding first names/roles for credibility). If any are illustrative placeholders, they must be labeled or removed.

### GREEN (verify) — "2,400+ freelancers trust Lance" appears to be GONE
The placeholder stat is not visible anywhere in the screenshot. If it was removed deliberately: excellent, close the open item in CLAUDE.md. There is small text under the hero CTAs I can't read — confirm it isn't hiding there.

### Conversion findings (cro pass)

1. **The differentiator is buried.** Approvals ("Client feedback that's actually useful." / "Give clients a window. Not your inbox.") is the 8th-9th feature section, far below the fold. CLAUDE.md says foreground it. The hero's general angle (matches Arm A) is a fair choice, but at minimum the approvals feature deserves the first feature-section slot, not a mid-list position. This also sets up the Arm A/Arm B ad test nicely: if Arm B (approvals angle) wins, the hero should follow.
2. **Hero is on-positioning.** "Organised [audience] earn more." with the rotating noun is exactly the current hero angle, personalized per segment. Good execution of the general angle.
3. **"Your entire freelance stack. $29/month."** — strong, concrete, on-voice second section. The price-anchored comparison against the DIY stack matches the market scan finding (DIY stack is the real competitor).
4. **Final CTA "Ready to cancel six subscriptions?"** — on-voice, names the enemy, good. Verify "six" matches the comparison table count so the page doesn't contradict itself.
5. **One primary CTA per screen** — hero shows two buttons (trial + watch demo); acceptable pattern with the video, keep trial visually primary.
6. **Video intro as hero media** — good; ensure it has a poster frame and doesn't autoplay with sound (couldn't check from a static screenshot).

### Voice notes on legible headings (pass)
"Every client relationship, properly managed." / "Projects that don't fall apart mid-way." / "Every hour logged. Every hour billed." / "Invoices that go out fast..." / "Proposals your clients actually read." / "Every brief, idea, and meeting note in one place." / "From kickoff to paid." — all short, direct, concrete, no clichés. These pass lance-voice as headings. "Everything that needs doing, nothing forgotten." sits close to the banned "everything you need, nothing you don't" construction family — passable, but if it ever gets flagged by Meta reviewers or feels templated, "Tasks that don't slip." is the same idea, safer.

## Action list (for Marina)

1. Replace "Simple, honest pricing." heading — hard rule violation
2. ~~Confirm contracts feature exists~~ Done: confirmed real (e-signatures included). Update the stale product docs
3. Source or reframe the $75/month claim
4. Confirm beta testimonials are real and permitted
5. Confirm "2,400+" placeholder is fully removed (including small print)
6. Consider moving approvals to first feature slot
7. Export CMS copy for the line-level lance-voice pass
