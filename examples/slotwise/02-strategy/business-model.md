---
id: SLOTWISE-business-model
title: Business Model: SlotWise
domain: 02-strategy
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [founder, finance, sales]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [vision-and-value-proposition]
feeds: [goals-and-metrics, roadmap, prd, subscription-and-billing]
applies_to: [saas]
---

# Business Model: SlotWise

## 1. Model Overview

| Block | Description |
|---|---|
| **Customer segments** | Independent salons and studios with 1 to 5 staff, starting with 3 pilot salons and a target of 40 paying salons (MET-03) |
| **Value proposition** | A guest booking page with confirmations and reminders, described in [Vision and Value Proposition](vision-and-value-proposition.md) |
| **Channels** (reach, sell, deliver) | Reach through local salon associations and word of mouth; self-serve sign-up; delivery through the booking web app |
| **Customer relationships** | Self-serve with assisted onboarding for the pilot salons, then lightweight email support |
| **Revenue streams** | Monthly salon subscription of 29 USD. No payments or transaction fee in R1 (DEC-001) |
| **Key resources** | Booking service, notification worker, salon calendar, small team under CON-01 |
| **Key activities** | Keep published availability correct, deliver messages with retries, support owners during the pilot |
| **Key partners / suppliers** | Email and SMS delivery provider DEP-01, selected per ADR-0002 |
| **Cost structure** | Hosting, per-message fees, 2 engineers and 1 designer for 14 weeks, part-time support |

## 2. Pricing and Packaging

| Plan / tier | Target segment | Price and unit | Included | Limits | Rationale |
|---|---|---|---|---|---|
| Trial | Pilot owners | 14 days free, then no free tier | FR-001 to FR-005, guest booking, reminders | 1 salon, up to 5 staff | Acquisition, matches the 2 week pilot rollout |
| Standard | Salons with 1 to 5 staff | 29 USD per salon per month | Guest booking page, owner calendar, confirmations, reminders, cancel link | 1 location, up to 5 staff, unlimited bookings | Undercuts the 39 USD and 59 USD alternatives in [Competitor Analysis](../01-discovery/competitor-analysis.md) |

- **Price metric** (what the customer pays for: seats, usage, locations): one salon location per month, not per booking and not per staff member.
- **How price relates to value delivered:** one recovered no-show or about 10 minutes saved per day covers the monthly fee at typical salon prices.
- **Alternatives' prices:** SalonDesk 39 USD and SlotBook 59 USD per month, public pricing checked 2026-11-12 in Competitor Analysis.

## 3. Unit Economics

| Item | Estimate | Assumption ID |
|---|---|---|
| Average revenue per account (monthly) | 29 USD | ASM-02 |
| Cost to serve per account (hosting, messaging, support) | 3 USD (about 1 USD hosting, 2 USD messages) | ASM-03 |
| Gross margin | About 90% | Derived from the two rows above |
| Customer acquisition cost | 45 USD, pilot outreach estimate | Planning estimate, owner product-manager |
| Expected lifetime (months) | 12, planning estimate | Planning estimate, owner product-manager |
| Payback period | About 2 months at 29 USD and 90% margin | Derived from the rows above |

## 4. Scenarios

| Scenario | Key assumptions | Month-12 accounts | Month-12 revenue | Break-even |
|---|---|---|---|---|
| Conservative | ASM-02 inconclusive, MET-02 at 30% | 20 | 580 USD monthly | Month 18 |
| Expected | ASM-02 validated, MET-02 at 50%, MET-03 at 40 salons | 40 | 1,160 USD monthly | Month 12 |
| Optimistic | ASM-02 validated, word of mouth, MET-02 above 60% | 80 | 2,320 USD monthly | Month 8 |

## 5. Funding and Cost-Benefit (non-commercial or internal products)

Not applicable. SlotWise is a commercial SaaS, so the subscription model and unit economics above are the relevant case.

## 6. Risks and Open Questions

| ID | Risk / question | Mitigation | Owner |
|---|---|---|---|
| Q-001 | Which reminder timings reduce no-shows most? | Test 24 h and 2 h in the pilot before fixing the schedule | product-manager |
| ASM-02 | Owners may not pay 29 USD per month | Price page test by 2026-12-15 | product-manager |
| ASM-03 | Message costs may exceed 15% of revenue | Quote from DEP-01 and monthly cost alert | engineering-lead |
| RISK-01 | Customers ignore reminders, so MET-01 does not improve | Include cancel link in every message (FR-003) | product-manager |

Billing, subscription state and usage limits are flagged for the [Subscription and Billing Requirements](../packages/saas/subscription-and-billing.md) document in the SaaS package.

## Completion Criteria

- [x] Who pays, for what and how much is explicit.
- [x] Pricing is justified relative to value and alternatives.
- [x] Unit economics use labelled assumptions and show their sources.
- [x] Scenarios show what must be true for viability.
- [x] Billing, metering or cost-tracking needs are flagged for requirements and (if SaaS) the SaaS package.
