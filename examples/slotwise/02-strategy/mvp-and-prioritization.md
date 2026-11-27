---
id: SLOTWISE-mvp-and-prioritization
title: MVP Definition and Feature Prioritization: SlotWise
domain: 02-strategy
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, designer]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [goals-and-metrics, assumption-map]
feeds: [prd, user-stories, roadmap, milestone-plan, release-plan]
applies_to: [saas]
---

# MVP Definition and Prioritization: SlotWise

## 1. MVP Hypothesis

| | |
|---|---|
| **Hypothesis** | We believe that owners of 1 to 5 staff salons will move bookings online if we provide a shareable booking page with confirmations, reminders and a cancel link, and we will know this when MET-02 reaches at least 50% and MET-01 falls to 10% or less within 90 days of R1 |
| **Riskiest assumptions tested** | ASM-01, ASM-04 |
| **Learning goal** | Whether owners let customers self-book and customers actually use the link instead of calling |
| **Success / failure thresholds** | Persevere if MET-02 ≥ 50% and MET-01 ≤ 10% at day 90. Pivot if online share stays below 25% at pilot week 6. Stop if owners switch self-booking off in the pilot |
| **Audience and size** | 3 pilot salons for 2 weeks, then 10 salons for 4 weeks, then 40 paying salons at day 90 per the [Release Plan](../09-release-ops/release-plan.md) and MET-03 |

## 2. Candidate Features

| ID | Candidate feature | Persona | Goal / metric | Supports hypothesis? |
|---|---|---|---|---|
| C-01 | Customer self-booking page with live availability | PER-01 | GOAL-02 / MET-02 | Yes |
| C-02 | Automated confirmations, reminders and cancel link | PER-02 | GOAL-01 / MET-01 | Yes |
| C-03 | Online payments and deposits | PER-01 | GOAL-01 | No, deferred by DEC-001 |

## 3. Prioritization

Method: **RICE**, so the trade-off between a small team and a 14 week window (CON-01) is visible and reproducible. Reach counts distinct customers in the first 90 days. Effort is person-weeks for the 2 engineers. MoSCoW is recorded as a cross-check against the PRD.

| Candidate | Reach | Impact | Confidence | Effort | RICE score | MoSCoW | Decision |
|---|---|---|---|---|---|---|---|
| C-01 | 400 | 3 | 80% | 4 | 240 | Must | R1 |
| C-02 | 400 | 2 | 70% | 3 | 187 | Must | R1 |
| C-03 | 400 | 2 | 50% | 6 | 67 | Won't (now) | Out of R1, revisit in R2 |

*RICE formula: Reach × Impact × Confidence ÷ Effort. Impact uses 0.25 to 3. C-03 effort includes payment provider integration, which DEC-001 estimates at about 3 weeks of saving.*

## 4. MVP Scope

| In MVP (Must) | Deliberately out of MVP | Manual or "concierge" substitutes |
|---|---|---|
| C-01 and C-02, plus owner setup FR-004 and no-show marking FR-005 | C-03 payments (DEC-001), FR-006 waiting list (DEC-003), marketplace discovery, multi-location | Deposits collected in person; owner fills freed slots by phone; owner sends a manual reminder if DEP-01 is unavailable |

**Check:** removing C-01 or C-02 breaks the hypothesis because neither MET-02 nor MET-01 could move. Removing FR-005 would leave MET-01 unmeasurable, so it stays as Should in R1.

## 5. Dependencies and Sequencing

DEP-01 must be selected per ADR-0002 before notification work starts. Owner availability (FR-004) precedes the public page (FR-001), because customers must see real slots. The slot guard in ADR-0001 is a precondition for concurrent booking (NFR-003). CON-01 caps the team at 2 engineers and 1 designer for 14 weeks, so FR-006 is held for R2 (RISK-04). See [Architecture Overview](../05-architecture/architecture-overview.md).

## 6. Review Triggers

Re-prioritize when ASM-01 or ASM-04 fails its experiment, when MET-01 has not moved by pilot week 6 (RISK-01), when message cost exceeds 15% of revenue (ASM-03), when a competitor changes pricing as tracked in [Competitor Analysis](../01-discovery/competitor-analysis.md), or when CON-01 capacity changes.

## Completion Criteria

- [x] The MVP is framed as a testable hypothesis with success thresholds.
- [x] Every Must feature supports the hypothesis and traces to a goal.
- [x] Prioritization method and inputs are transparent and reproducible.
- [x] Out-of-scope items and manual workarounds are explicit.
- [x] Priorities match the PRD requirement catalog.
