---
id: SLOTWISE-07-uat-plan
title: User Acceptance Testing (UAT) Plan
domain: 07-quality
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [qa-lead, business-analyst, business-stakeholders]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [user-stories, test-plan, use-cases]
feeds: [release-plan, operational-readiness, post-launch-review]
applies_to: [all]
---

# UAT Plan: SlotWise R1

## 1. Objectives and Scope

| | |
|---|---|
| **Objective** | Confirm that PER-01 Maya and PER-02 Dani can complete their key tasks to the pilot business's satisfaction |
| **Release / build** | R1, release candidate R1-RC-2027-02-26 |
| **In scope** | FR-001, FR-002, FR-003, FR-004 and FR-005 with US-001 to US-005 |
| **Out of scope** | Performance and security testing, covered by TS-005 and SR-001 to SR-008; FR-006, deferred to R2 by DEC-003; payments, excluded by DEC-001 |
| **Environment** | Staging with synthetic data modelled on three pilot salons; see [Environment Strategy](../09-release-ops/environment-strategy.md) |

## 2. Participants

| Role / persona | Participant(s) | Responsibilities | Availability |
|---|---|---|---|
| Business owner (PER-01) | 3 pilot salon owners | Run owner scenarios on their own phones, log feedback | 2027-02-22 to 2027-02-26, 10:00 to 16:00 UTC |
| Customer (PER-02) | 5 customer volunteers | Book and cancel as a customer | 2027-02-22 to 2027-02-26 |
| Business sponsor | Maya, pilot salon owner | Decide acceptance | 2027-02-26 |
| UAT coordinator | QA lead | Briefing, support, triage | All test days |

## 3. UAT Scenarios

| ID | Business scenario | Role | Source (story / use case) | Acceptance criteria | Result | Comments |
|---|---|---|---|---|---|---|
| UAT-01 | A new owner sets up services, staff and opening hours and shares the booking link | Owner (PER-01) | US-004 | AC-004.1, AC-004.2; setup within 30 minutes is a pilot target, not a gate | Not yet run | None |
| UAT-02 | A customer books a slot on a phone and receives a confirmation | Customer (PER-02) | US-001, US-002 | AC-001.1, AC-001.3, AC-002.1; TS-001 and TC-003 results available | Not yet run | None |
| UAT-03 | A customer cancels from the message link before the cutoff | Customer (PER-02) | US-003 | AC-003.1; TS-004 result available | Not yet run | None |
| UAT-04 | An owner marks a no-show and sees it counted in MET-01 | Owner (PER-01) | US-005 | AC-005.1; TS-009 result available | Not yet run | None |

Use `UAT-` IDs only within this document; each links to its source story and, where relevant, to system scenarios TS-001 to TS-009.

## 3a. Conduct

| Item | Plan |
|---|---|
| Briefing | Remote session on 2027-02-19 covering the four scenarios, what is being tested, and that DEP-01 sandbox messages are used |
| Test period | 2027-02-22 to 2027-02-26, support available 10:00 to 16:00 UTC |
| How to record results | Tool-agnostic tracker with UAT ID, severity, screenshots and owner comment |
| Support during UAT | QA lead answers questions within 1 working hour; PM handles scope questions |

## 4. Entry and Exit Criteria

| Gate | Criteria |
|---|---|
| Entry | [Test Plan](test-plan.md) exit criteria met; no open Critical defects; staging stable; four scenarios and briefing material ready; all participants confirmed |
| Exit | All Must UAT scenarios executed; no open Critical or unaccepted High defects; outstanding issues have an agreed decision; sponsor signs off |

## 5. Defect and Feedback Triage

| Category | Definition | Handling |
|---|---|---|
| Defect | Behaviour contradicts an acceptance criterion or business rule | Log with a TC ID, severity per [Test Strategy](test-strategy.md), fix and retest |
| Change request | A new or different need | Log for the PM and record a DEC- ID in the [Decision Log](../00-foundation/decision-log.md); not a UAT blocker unless agreed |
| Usability issue | Task possible but difficult | Record with the designer and prioritise for R2 |
| Training or documentation gap | Users confused by missing help | Add to the operations handover in [Operational Readiness](../09-release-ops/operational-readiness.md) |

Triage meeting: daily at 16:00 UTC during UAT, attended by PM, QA lead and Eng Lead. Decision authority on severity and acceptance: PM with sponsor sign-off.

## 6. Results Summary

| Scenarios | Planned | Passed | Failed | Blocked | Accepted with conditions |
|---|---|---|---|---|---|
| Must, UAT-01 to UAT-03 | 3 | 0 | 0 | 0 | 0 |
| Should, UAT-04 | 1 | 0 | 0 | 0 | 0 |

| Open issue | Severity | Decision (fix before release / accept / defer) | Owner |
|---|---|---|---|

## 7. Sign-off

| Role | Name | Decision | Conditions | Date |
|---|---|---|---|---|
| Business sponsor | Maya (PER-01) | Pending | No open Critical defects and UAT-01 to UAT-03 passed | 2027-02-26 |
| Product | PM | Pending | Matches sponsor decision | 2027-02-26 |
| QA | QA lead | Pending | Test Plan exit criteria met | 2027-02-26 |

Sign-off feeds the go/no-go decision in the [Release Plan](../09-release-ops/release-plan.md).

## Completion Criteria

- [x] Scope, participants and environment are defined; participants represent real roles.
- [x] Every *Must* story with a business-facing outcome has a UAT scenario.
- [x] Scenarios use business language and have explicit acceptance criteria.
- [x] Entry and exit criteria and decision authority are agreed in advance.
- [x] Defects, change requests and usability issues are separated and triaged.
- [x] Results and sign-off are recorded and feed the release decision.
