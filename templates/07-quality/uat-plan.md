---
id: DPP-07-uat-plan
title: User Acceptance Testing (UAT) Plan
domain: 07-quality
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [qa-lead, business-analyst, business-stakeholders]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [user-stories, test-plan, use-cases]
feeds: [release-plan, operational-readiness, post-launch-review]
applies_to: [all]
---

# UAT Plan: [Product Name] — [Release ID]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Plans how the people who will use and own the product confirm that it meets business needs in realistic conditions, and how their acceptance is recorded. UAT answers "is this the right product?" where earlier testing answered "is it built correctly?". |
| **When to use** | After system testing meets the Test Plan exit criteria and before release. Recommended for any product with business owners or paying customers; for internal tools it is often the main acceptance mechanism. |
| **Owner** | Product Manager, supported by QA. |
| **Required inputs** | [User Stories](../03-requirements/user-stories.md) and acceptance criteria; [Use Cases](../03-requirements/use-cases.md) (if any); [Test Plan](test-plan.md) exit status; representative users. |
| **Related documents** | [Test Scenarios](test-scenarios.md) · [Release Plan](../09-release-ops/release-plan.md) · [Operational Readiness](../09-release-ops/operational-readiness.md) |

</details>

> **Guidance:** UAT is **not a second round of system testing**. Testers use real-world tasks, real roles and business language. Keep scripts short, provide support, and define in advance what counts as acceptance so the outcome is a decision, not a debate.

## 1. Objectives and Scope

| | |
|---|---|
| **Objective** | Confirm that [PER-01 and PER-02] can complete their key tasks to the business's satisfaction |
| **Release / build** | R1, release candidate [id] |
| **In scope** | FR-001, FR-002, FR-005 (Must items) |
| **Out of scope** | Performance and security testing (covered elsewhere); deferred items FR-003 |
| **Environment** | Staging with synthetic data modelled on real business scenarios; see [Test Data Management](test-data-management.md) |

## 2. Participants

| Role / persona | Participant(s) | Responsibilities | Availability |
|---|---|---|---|
| Business owner (PER-02) | [Pilot owners, 3–5] | Run scenarios on their own devices; log feedback | [Dates] |
| Customer (PER-01) | [5 volunteers] | Book as a customer | |
| Business sponsor | [Name] | Decide acceptance | |
| UAT coordinator | [QA / PM] | Briefing, support, triage | |

## 3. UAT Scenarios

> **Guidance:** Derive from user stories, use cases and real working days, not from system test cases. Pass/fail is judged against acceptance criteria and business expectations.

| ID | Business scenario | Role | Source (story / use case) | Acceptance criteria | Result | Comments |
|---|---|---|---|---|---|---|
| UAT-01 | A new owner sets up services and opening hours and shares the booking link | Owner | US-010, UC-003 | AC-010.1–AC-010.3; first-time setup done within 30 min unaided (ASM-04) | | |
| UAT-02 | A customer books and receives a confirmation on a phone | Customer | US-002, UC-001 | AC-002.1; confirmation arrives | | |
| UAT-03 | An owner reschedules a customer's booking | Owner | US-009 | AC-009.1 | | |

Use `UAT-` IDs only within this document; link each to its source story and, where relevant, to system scenarios (`TS-`).

## 3a. Conduct

| Item | Plan |
|---|---|
| Briefing | [Format, date; what is and is not being tested] |
| Test period | [Dates; daily support hours] |
| How to record results | [Form/tracker; screenshots; severity] |
| Support during UAT | [Contact, response time] |

## 4. Entry and Exit Criteria

| Gate | Criteria |
|---|---|
| Entry | Test Plan exit criteria met; no open Critical defects; UAT environment stable; scenarios and training ready; participants confirmed |
| Exit | All *Must* UAT scenarios executed; no open Critical or unaccepted High defects; outstanding issues have an agreed decision; sponsor has signed |

## 5. Defect and Feedback Triage

| Category | Definition | Handling |
|---|---|---|
| Defect | Behaviour contradicts an acceptance criterion or rule | Log, severity per [Test Strategy](test-strategy.md), fix and retest |
| Change request | A new or different need | Log as candidate (`C-`) or decision (`DEC-`); decide with PM; not a UAT blocker unless agreed |
| Usability issue | Task possible but difficult | Record; prioritise with design |
| Training/documentation gap | Users confused by missing help | Add to [Launch & Support Plan](../09-release-ops/launch-and-support-plan.md) |

Triage meeting: [cadence, attendees]. Decision authority on severity and acceptance: [Name].

## 6. Results Summary

| Scenarios | Planned | Passed | Failed | Blocked | Accepted with conditions |
|---|---|---|---|---|---|
| Must | | | | | |
| Should | | | | | |

| Open issue | Severity | Decision (fix before release / accept / defer) | Owner |
|---|---|---|---|

## 7. Sign-off

| Role | Name | Decision | Conditions | Date |
|---|---|---|---|---|
| Business sponsor | | ☐ Accept ☐ Accept with conditions ☐ Reject | | |
| Product | | | | |
| QA | | | | |

Sign-off feeds the go/no-go decision in the [Release Plan](../09-release-ops/release-plan.md).

## Completion Criteria

- [ ] Scope, participants and environment are defined; participants represent real roles.
- [ ] Every *Must* story with a business-facing outcome has a UAT scenario.
- [ ] Scenarios use business language and have explicit acceptance criteria.
- [ ] Entry and exit criteria and decision authority are agreed in advance.
- [ ] Defects, change requests and usability issues are separated and triaged.
- [ ] Results and sign-off are recorded and feed the release decision.
