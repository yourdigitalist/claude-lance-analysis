# Installed Skills — Provenance and Review Notes

Reviewed and installed 2026-07-14. Every SKILL.md was read in full before installing; bundled scripts were scanned (no network calls, no exec, no credential access — pure math/JSON utilities).

## From github.com/coreyhaines31/marketingskills (commit 30bc89d)

| Skill | Verdict | Notes |
|-------|---------|-------|
| content-strategy | installed | Clean marketing guidance |
| ad-creative | installed | Clean. Its grounding rules (no invented claims/stats/testimonials, every concept cites a real source) align with Lance rules. Its "Tool Integrations" section references CLI tools from its home repo that are not installed here — ignore that section |
| copywriting | installed | Clean |
| copy-editing | installed | Clean |
| product-marketing | installed | Clean. Creates `.agents/product-marketing.md` which other skills from this family read |
| cro | installed | Clean |

## From github.com/alirezarezvani/claude-skills (commit 84dc5a4)

| Skill | Verdict | Notes |
|-------|---------|-------|
| cmo-advisor | installed | Clean scripts (offline budget/growth modelers). Caveat: its "Communication" and "Context Integration" sections reference an agent-protocol ecosystem from its home repo (Internal Quality Loop, `[INVOKE:role]`, board meetings) that does not exist here — ignore those sections. The strategy frameworks and diagnostic questions are the useful part |
| marketing-ops | **skipped** | Safety review passed, but it is purely a routing skill for ~50 skills in its home ecosystem, most of which are not installed here. Installed alone it would route requests to skills that don't exist and impose its own output protocol. No value, real confusion |
| social-media-analyzer | installed | Clean scripts. Caveat: its "Engagement Value Estimates" ($0.50/like etc.) are invented industry heuristics — fine for internal relative comparison, never usable as a real ROI claim in copy (Lance rule: real proof only) |

## Precedence rule

Where any installed skill's guidance conflicts with CLAUDE.md or the lance-voice skill (e.g. generic advice to add social proof numbers, urgency angles, or specificity like "join 10,000+ teams"), **CLAUDE.md and lance-voice win**. Installed skills are frameworks; Lance's voice and compliance rules are non-negotiable.
