---
id: SLOTWISE-07-test-plan
title: Test Plan
domain: 07-quality
tier: recommended
status: draft
version: 0.1.0
owner: qa-lead
contributors: [engineering-lead, product-manager]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [test-strategy, prd, user-stories]
feeds: [test-scenarios, uat-plan, release-plan, planning-readiness-review]
applies_to: [all]
---

# Test Plan: SlotWise R1 Pilot

## 1. Release Context

| | |
|---|---|
| **Release** | R1 pilot, FR-001 to FR-005; FR-006 deferred to R2 per DEC-003 |
| **Target release date** | 2027-03-05 |
| **Test window** | 2027-02-08 to 2027-02-26; code freeze 2027-02-05 |
| **Strategy version followed** | Test Strategy v0.1.0, dated 2026-11-27; no deviations approved yet |

## 2. Scope

### 2.1 In scope

| Requirement | Stories | Priority | Test focus | Scenarios |
|---|---|---|---|---|
| FR-001 Customer self-booking | US-001 | Must | Functional, concurrency, accessibility | TS-001, TS-002, TS-007 |
| FR-002 Confirmations and reminders | US-002 | Must | Functional, timing, provider failure | TS-003 |
| FR-003 Cancel and reschedule | US-003 | Must | Cutoff boundary, token access | TS-004 |
| FR-004 Owner setup | US-004 | Must | Availability changes, conflicts | TS-008 |
| FR-005 No-show marking | US-005 | Should | MET-01 calculation | TS-009 |
| NFR-001 to NFR-005 | Not story-specific | Must | Performance, monitoring, integrity, privacy, accessibility | TS-002, TS-005, TS-006, TS-007, TS-010 |

### 2.2 Out of scope for this release

| Item | Reason | Risk accepted by |
|---|---|---|
| FR-006 waiting list | Deferred to R2 by DEC-003 | PM |
| Payments and checkout | Non-goal, DEC-001 | PM |
| DEP-01 internal behaviour | Verified by sandbox contract checks only | Eng Lead |

## 3. Test Approach for This Release

| Test type | Applies? | Coverage target | Owner | Notes |
|---|---|---|---|---|
| Unit / integration | Yes | Booking rules BR-001 to BR-005 | Developers | Runs on every change |
| API / contract | Yes | API-001 to API-003 | Dev + QA | Against the API Specification |
| End-to-end | Yes | UF-01 to UF-03 | QA | Book, confirm, cancel |
| Performance | Yes | NFR-001, TS-005 | QA / Eng | 50 concurrent slot lookups |
| Security | Yes | SR-001 to SR-008, TH-001 to TH-007 | Security / QA | Scope from the [Threat Model](../08-security/threat-model.md) |
| Accessibility | Yes | Booking flow, NFR-005 | QA / Designer | TS-007 |
| Exploratory | Yes | 2 sessions per Must FR | QA | 2027-02-12 and 2027-02-19 |
| Regression | Yes | Smoke plus TC-001, TC-002, TC-003 | QA | Before each release candidate |
| UAT | Yes | See [UAT Plan](uat-plan.md) | Pilot owners | 2027-02-22 to 2027-02-26 |

## 4. Schedule

| Date | Activity | Owner | Depends on |
|---|---|---|---|
| 2027-02-08 | Test environment ready; smoke tests pass | Eng Lead | Deployment pipeline |
| 2027-02-08 to 2027-02-12 | Scenario execution cycle 1, TS-001 to TS-010 | QA | Feature complete, M4 |
| 2027-02-15 to 2027-02-19 | Defect fix window and cycle 2 regression | Dev | Cycle 1 results |
| 2027-02-22 to 2027-02-26 | UAT with pilot salons | PM | Exit criteria for cycle 2 |
| 2027-02-26 | Go/no-go input to the [Release Plan](../09-release-ops/release-plan.md) | PM | UAT sign-off |

## 5. Environments and Data

| Environment | Purpose | Build / config | Data | Availability | Owner |
|---|---|---|---|---|---|
| Test | Functional, integration, API | Latest merged build | Synthetic booking fixture, no real personal data | Weekdays 09:00 to 18:00 UTC | Eng Lead |
| Staging | Release rehearsal, performance, UAT | Release candidate R1-RC-2027-02-26 | Synthetic, production-like volume of 1,000 bookings | Weekdays 09:00 to 18:00 UTC | Eng Lead |

Third-party services: DEP-01 sandbox for confirmation and reminder delivery, with no real customer numbers. The provider account and sandbox are due by 2026-12-18.

## 6. Roles and Responsibilities

| Role | Person | Responsibilities |
|---|---|---|
| Test lead | QA lead | Plan, reporting, quality gate input |
| Testers | QA lead and designated developer | Execute TS-001 to TS-010, log defects |
| Developers | Both engineers | Fix defects, maintain automated TC cases |
| Product owner | PM | Triage priority, accept residual risk |
| Pilot owners | PER-01 salons | UAT and feedback |

## 7. Entry and Exit Criteria

| Gate | Criteria (this release) |
|---|---|
| Entry: start cycle 1 | Build deployed; smoke tests pass; TS-001 to TS-010 reviewed; synthetic data loaded; DEP-01 sandbox reachable |
| Exit: cycle complete | All planned scenarios run; no open Critical defects; High defects triaged |
| Exit: ready for UAT | All Must scenarios pass; Critical = 0; High accepted by PM or fixed |
| Exit: ready to release | Meets [Test Strategy §8](test-strategy.md) and the [Release Plan](../09-release-ops/release-plan.md) go/no-go criteria |

## 8. Defect Handling for This Release

| Item | Decision |
|---|---|
| Tracker and workflow | Tool-agnostic tracker; every defect links to a TC ID and a severity from the Test Strategy |
| Triage cadence | Daily at 10:00 UTC during the test window |
| Fix and retest turnaround | Critical same day; High within 2 working days; Medium scheduled by PM |

## 9. Risks and Contingencies

| ID | Test risk | Mitigation | Owner |
|---|---|---|---|
| RISK-02 | DEP-01 sandbox differs from live delivery behaviour | Sandbox contract checks plus a monitored pilot | QA lead |
| RISK-03 | Double booking under load | TC-002 before every release candidate | Eng Lead |
| RISK-04 | Test window compressed by 14-week capacity | Hold FR-006 for R2 and use the 5-day milestone buffer | PM |

## 10. Deviations from the Test Strategy

None approved as of 2026-11-27. Any deviation needs PM agreement and a record in this section before it takes effect.

## 11. Reporting

| Report | Content | Audience | Frequency |
|---|---|---|---|
| Progress | Scenarios run, passed and failed, open defects by severity | Team | Daily during the test window |
| Quality summary | Coverage by FR and NFR, residual risk | PM and sponsor | At each release gate |

## Completion Criteria

- [x] In-scope and out-of-scope items reference requirement and story IDs.
- [x] Every Must requirement has scenarios assigned and an owner.
- [x] Schedule, environments and test data are available for every planned activity.
- [x] Entry and exit criteria are measurable and consistent with the Test Strategy and Release Plan.
- [x] Test risks are recorded with mitigations.
- [x] Deviations from the strategy are documented and approved.
