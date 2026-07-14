# claude-lance-analysis

Marketing ops workspace for Lance (getlance.app), Marina's freelancer project-management/invoicing product.

This repo is where Claude Code sessions do marketing work for Lance: competitor and market research, ad copy and creative review, positioning, and Meta ads compliance checks. `CLAUDE.md` holds the standing context (product facts, voice rules, current positioning, known compliance risks, open items) that loads automatically at the start of every session here, so work picks up where it left off instead of restarting from scratch each time.

Anything that spends money or goes live still needs Marina's sign-off — this workspace is for drafting and analysis, not autonomous publishing.

## Tools

### Meta ads compliance checker

`.claude/skills/meta-ads-compliance-checker/` — a Claude Skill (usable directly in Claude Code) that checks ad copy or a creative/screenshot description against Lance's known Meta compliance risk patterns from `CLAUDE.md`: dollar figures read as implied earnings claims, scarcity claims, unverified stats/testimonials, vague vs specific claims. Outputs a risk rating (LOW/MEDIUM/HIGH) and a suggested fix for anything flagged.

Run it directly:

```bash
python3 .claude/skills/meta-ads-compliance-checker/scripts/check_compliance.py "your ad copy or creative description here"
```

It flags risk, it doesn't clear copy for launch — anything going live still needs Marina's sign-off.
