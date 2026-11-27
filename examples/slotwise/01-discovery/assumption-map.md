---
id: SLOTWISE-assumption-map
title: Assumption Map: SlotWise
domain: 01-discovery
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, designer]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [product-brief]
feeds: [user-research, prd, risk-register, mvp-and-prioritization, roadmap]
applies_to: [saas]
---

# Assumption Map: SlotWise

## 1. Assumption Register

| ID | Category | Assumption (testable statement) | Impact if wrong (1–5) | Evidence today (1 none – 5 strong) | Risk rank | Status |
|---|---|---|---|---|---|---|
| ASM-01 | Desirability | At least 6 of 10 pilot salon owners will let customers self-book without approving each booking | 5 | 2 | High | Testing |
| ASM-02 | Viability | Owners will pay at least 29 USD per month for a salon subscription with reminders | 5 | 2 | High | Unvalidated |
| ASM-03 | Feasibility | Email and SMS delivery cost stays below 15% of subscription revenue (DEP-01) | 3 | 2 | Medium | Unvalidated |
| ASM-04 | Usability | A new owner can publish a booking page in under 30 minutes unaided | 4 | 1 | High | Unvalidated |

**Risk rank:** High when impact ≥ 4 and evidence ≤ 2; Medium when one is borderline; Low otherwise. Status: *Unvalidated · Testing · Validated · Invalidated · Retired*. Evidence for ASM-01 comes from the 24 owner survey; note the survey measured time spent, not willingness to delegate booking.

## 2. Priority Grid

|  | **Little evidence** | **Strong evidence** |
|---|---|---|
| **High impact** | **Test first**: ASM-02, ASM-04; ASM-01 already testing | Monitor during pilot |
| **Low impact** | Test if cheap: ASM-03 via provider quote | Ignore |

## 3. Test Plan (for High-risk assumptions)

| ID | Experiment | Success criterion (set *before* testing) | Cost / effort | Owner | Due | Result |
|---|---|---|---|---|---|---|
| ASM-01 | Concierge pilot with 3 salons for 2 weeks; owners watch a booking link handle real customers | 6 of 10 owners keep self-booking enabled at week 2 | 2 days setup, 2 weeks observation | product-manager | 2026-12-15 | Pending |
| ASM-02 | Price page offering 29 USD per month; count paid sign-ups from local salon outreach | 20 paid sign-ups by 2026-12-15 | 3 days | product-manager | 2026-12-15 | Pending |
| ASM-04 | Usability test with 5 new owners and a draft booking page | 4 of 5 publish a page in under 30 minutes unaided | 2 days | designer | 2026-12-15 | Pending |

Cheap test options: interviews, prototypes, landing page tests, concierge/manual service, data analysis, technical spike. ASM-03 is checked with a DEP-01 quote rather than a user experiment.

## 4. Outcomes and Decisions

| ASM | Result | Decision (persevere / pivot / stop / re-test) | Documents updated |
|---|---|---|---|
| Pending pilot results | No experiment has completed | Re-test at the due dates above | None yet |

Link invalidated assumptions to decisions in the [Decision Log](../00-foundation/decision-log.md) and remaining high-risk ones to the [Risk Register](../06-project-mgmt/risk-register.md). ASM-01 relates to RISK-01 and ASM-03 to RISK-02; ASM-02 is tracked with the business model pricing test.

## Completion Criteria

- [x] Assumptions span desirability, viability, feasibility and usability.
- [x] Each is a testable statement with impact and evidence ratings.
- [x] Every High-risk assumption has an experiment with a success criterion set in advance.
- [ ] Results update status and trigger documented decisions.
- [x] Unresolved High-risk assumptions appear in the Risk Register.
