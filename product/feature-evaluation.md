# Feature Evaluation — 2026-07-15 (v2)

**v2 note:** the 2026-07-14 version missed features. Corrected against the technical build doc and user journey doc Marina provided 2026-07-15: Lance also has **Proposals** (token-based public view, accept lifecycle, service line items), **Services** (priced service library with default tasks), **dashboard analytics**, **global search**, and **notifications with invoice reminders**. Also corrected: the "no contracts" gap is nuanced — proposals with client Accept exist; contracts/e-signatures do NOT appear in the product docs (yet the landing page has a "Signed contracts" section — flagged in the LP audit for Marina to reconcile).

Scores each feature against the pain-point map. Scale: strong / moderate / weak. "Table stakes" = every paid competitor has it.

| Feature | Pains addressed | Strength | Table stakes? | Honest read |
|---|---|---|---|---|
| **File approvals / client reviews** (no-login token link, comments, versions, statuses) | 1 scattered feedback, 2 version confusion, 3 delayed approvals, 7 vague feedback | **Strong** | No — unique in the all-in-one category | Still the differentiator. Version numbers on review files confirmed in the journey doc, so the version-confusion claim is safe to make. Claim it as approvals inside the all-in-one (see market scan erosion note) |
| **Proposals** (public token view, one-click Accept, service line items, defaults) | 5 scope creep, 9 contracts (partially) | **Strong** (missed in v1) | Bonsai/HoneyBook/Dubsado have proposals too | The Accept lifecycle (draft→sent→read→accepted) gives a scope paper trail before work starts. NOT a contract/e-signature — don't market it as one. Combined with per-proposal service line items it directly answers scope creep |
| **Invoicing** (+ reminders, overdue notifications, unbilled-time import) | 4 unpaid invoices, 10 time-to-invoice | **Strong** | Yes | Upgraded from v1: send-reminder and overdue notifications (in-app + email) are confirmed, so the chasing-payment claim is real. Note: Lance does NOT process client payments (manual mark-as-paid, wire instructions) — no transaction fees ever, but no card collection either. That cuts both ways vs HoneyBook's 2.9%+$0.25: "no fees" is honest, "get paid faster" needs care |
| **Time tracking** (timer, billable flags, unbilled→invoice import) | 10 time-to-invoice | **Moderate-strong** | Yes, but gaps in competitors | Confirmed: billable entries import into invoices. Dubsado lacks time tracking, Wave lacks it, 17hats charges extra. "Included and connected to invoices" is now a verified claim |
| **Services library** (priced services, default tasks, feeds proposals) | 5 scope creep (supporting) | **Moderate** (missed in v1) | Partially | Quietly useful: reusable priced services make proposals fast and consistent. Supporting cast for the proposals story, not a lead angle |
| **CRM / Kanban** (+ lead source, next action, estimated value) | 6 tool sprawl | **Moderate** | Yes | Richer than v1 assumed (follow-up dates, pipeline value). Still supports the one-place story rather than leading |
| **Projects + tasks** (Kanban, custom columns, deadline notifications) | 6 tool sprawl | **Moderate** | Yes | Deadline notifications confirmed. Same read as v1: necessary, not a lead angle vs free Trello |
| **Dashboard analytics** (hours, unbilled, pending payment, approvals counts) | 4, 6 (visibility) | **Moderate** (missed in v1) | Yes | "Pending payment" and "unbilled hours" tiles surface the money-admin pains at a glance. Good demo material for the video/screenshots (careful: dollar figures in ad screenshots stay a Meta risk) |
| **Notes → tasks** (rich text, folders) | — | **Weak** | No | Unchanged from v1: maps to no researched pain. Delighter, not an acquisition angle |
| **Global search / notifications** | — (glue) | **Weak** alone | Yes | Product glue. Not marketing material |

## Which features address the loudest pains

Unchanged conclusion, stronger evidence: approvals owns the loudest cluster (scattered feedback/versions/sign-off), invoicing+time owns the money cluster — and now **proposals bridges the two** (scope agreed before work, approvals during work, invoice after). "From kickoff to paid" on the landing page is exactly this story.

## Is the differentiator still the differentiator?

Yes — approvals, framed in-category (see market scan). The proposals module strengthens the surrounding story but proposals themselves are table stakes among paid all-in-ones.

## Real gaps (corrected)

- **Contracts/e-signatures: still absent per product docs.** Bonsai/HoneyBook/Dubsado all have them. The landing page currently claims them — reconcile (LP audit action 2)
- **No client payment processing.** No fees is a real angle; "clients pay by card" isn't available. Don't imply online payment collection in copy
