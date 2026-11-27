---
id: SLOTWISE-requirements-traceability-matrix
title: Requirements Traceability Matrix: SlotWise
domain: 03-requirements
tier: recommended
status: draft
version: 0.1.0
owner: business-analyst
contributors: [product-manager, qa-lead, engineering-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [prd, user-stories, non-functional-requirements]
feeds: [test-plan, release-plan, uat-plan, planning-readiness-review]
applies_to: [saas]
---

# Requirements Traceability Matrix: SlotWise

## 1. Functional Traceability

| Goal | FR | Title | Pri | Release | Stories | Acceptance criteria | Design ref | Architecture ref | Test scenarios | Coverage |
|---|---|---|---|---|---|---|---|---|---|---|
| GOAL-02 | FR-001 | Guest slot view and booking | Must | R1 | US-001 | AC-001.1, AC-001.2, AC-001.3 | UF-01, S-01 | ADR-0001, ADR-0003 | TS-001, TS-002 | ● Covered |
| GOAL-01 | FR-002 | Confirmation and reminder | Must | R1 | US-002 | AC-002.1, AC-002.2, AC-002.3 | UF-02, S-04 | ADR-0002 | TS-003 | ● Covered |
| GOAL-01 | FR-003 | Cancel or reschedule up to cutoff | Must | R1 | US-003 | AC-003.1, AC-003.2 | UF-03, S-04 | ADR-0001 | TS-004 | ● Covered |
| GOAL-02 | FR-004 | Owner sets services, staff, hours and time off | Must | R1 | US-004 | AC-004.1, AC-004.2 | S-02 | Architecture Overview building blocks | TS-008 | ● Covered |
| GOAL-01 | FR-005 | Mark completed or no-show | Should | R1 | US-005 | AC-005.1 | S-03 | Architecture Overview building blocks | TS-009 | ● Covered |
| GOAL-01 | FR-006 | Waiting list offers freed slots | Could | R2 | Not started | Not started | Not started | Not started | Not started | ○ Not started |

**Coverage key:** ● every story has ≥ 1 AC and every AC has ≥ 1 scenario · ◐ gaps exist (list below) · ○ no downstream items yet. FR-006 is deferred by DEC-003 and is not a Must item for R1.

## 2. Non-Functional Traceability

| NFR | Title | Pri | Addressed by (design / ADR) | Verified by (scenario / monitoring) | Coverage |
|---|---|---|---|---|---|
| NFR-001 | Booking page speed | Must | Booking service design, ADR-0003 | TS-005 | ● |
| NFR-002 | Availability during salon hours | Must | Queue and retry design in ADR-0002, monitoring design in observability-strategy | TS-010 | ● |
| NFR-003 | No double bookings | Must | ADR-0001 | TS-002 | ● |
| NFR-004 | Customer data privacy and deletion | Must | ADR-0005, privacy-requirements | TS-006 | ● |
| NFR-005 | Accessibility of the booking flow | Must | Accessibility and Responsive Design Guidelines | TS-007 | ● |

## 3. Metrics Traceability

| Goal | Metric | Events / data source | Dashboard or report |
|---|---|---|---|
| GOAL-01 | MET-01 | Appointment status field, EVT-003 | [Analytics Plan](../10-analytics/analytics-plan.md) |
| GOAL-02 | MET-02 | Booking source field, EVT-002 | [Analytics Plan](../10-analytics/analytics-plan.md) |
| GOAL-02 | MET-03 | Billing records, [Subscription and Billing](../packages/saas/subscription-and-billing.md) | [Goals and Metrics](../02-strategy/goals-and-metrics.md) |

## 4. Business Rules Coverage

| BR | Enforced in (FR / story) | Verified by (TS) |
|---|---|---|
| BR-001 | FR-001 / US-001 | TS-001 |
| BR-002 | FR-001 / US-001 | TS-002 |
| BR-003 | FR-001 / US-004 | TS-008 |
| BR-004 | FR-003 / US-003 | TS-004 |
| BR-005 | FR-004 / US-004 | TS-008 |
| BR-006 | FR-002 / US-002 | TS-003 |

## 5. Gaps and Actions

| Gap | Impact | Action | Owner | Due |
|---|---|---|---|---|
| FR-006 has no stories or scenarios in R1 | Waiting list is untested until R2 | Re-open this row at R2 planning per DEC-003 | product-manager | 2027-01-04 |
| Q-001 reminder timing is open | MET-01 may not reach 10% | Test 24 h and 2 h timings in the pilot | product | Pilot week 6 |
| DEP-01 provider not selected | Reminder delivery risk RISK-02 remains open | Complete selection per ADR-0002 | engineering-lead | 2026-12-15 |
| Event fields for MET-01 and MET-02 are draft | Metric dashboards may not be ready at day 90 | Confirm fields in [Event Tracking Plan](../10-analytics/event-tracking-plan.md) | product-manager | 2026-12-15 |

## 6. Change Impact Log

| Date | Changed item | Items reviewed | Outcome |
|---|---|---|---|
| 2026-11-27 | FR-006 deferred to R2 by DEC-003 | PRD, user-stories, test-scenarios, release-plan | R1 matrix updated; FR-006 marked as not started |
| 2026-11-27 | BR-004 revised after DEC-001 | business-rules, user-stories, test-scenarios | Deposit logic removed, cutoff rule kept |

## Completion Criteria

- [x] Every FR and every *Must* NFR appears with its goal and release.
- [x] Every *Must* FR links to stories, acceptance criteria and test scenarios; gaps are listed with owners.
- [x] Every metric links to a data source.
- [x] The matrix defines no new IDs; every ID resolves in its canonical document.
- [x] Updated whenever scope or tests change; last-updated date is current.
