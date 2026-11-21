---
id: DPP-07-test-plan
title: Test Plan
domain: 07-quality
tier: recommended
status: draft
version: 0.1.0
owner: qa-lead
contributors: [engineering-lead, product-manager]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [test-strategy, prd, user-stories]
feeds: [test-scenarios, uat-plan, release-plan, planning-readiness-review]
applies_to: [all]
---

# Test Plan: [Product Name] — [Release ID, e.g. R1]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Turns the long-lived [Test Strategy](test-strategy.md) into a concrete plan for **one release**: what will be tested, when, by whom, in which environment, and what must be true to start and finish testing. |
| **When to use** | When scope for a release is agreed (see the PRD release table); update as scope or dates change. One copy per release. |
| **Owner** | QA Lead (solo projects: the developer). |
| **Required inputs** | [Test Strategy](test-strategy.md); [PRD](../03-requirements/prd.md) release scoping; [User Stories](../03-requirements/user-stories.md); [Milestone Plan](../06-project-mgmt/milestone-plan.md); [Risk Register](../06-project-mgmt/risk-register.md). |
| **Related documents** | [Test Scenarios](test-scenarios.md) · [UAT Plan](uat-plan.md) · [Environment Strategy](../09-release-ops/environment-strategy.md) · [Release Plan](../09-release-ops/release-plan.md) |

</details>

> **Guidance:** The strategy says *how we approach quality*; the plan says *what, when, who, where* for this release. Do not repeat strategy content: link to it and record only release-specific decisions and deviations.

## 1. Release Context

| | |
|---|---|
| **Release** | R1 — MVP |
| **Target release date** | [Date] |
| **Test window** | [Start – end; code-freeze date] |
| **Strategy version followed** | [Test Strategy v0.x; deviations listed in §10] |

## 2. Scope

### 2.1 In scope

| Requirement | Stories | Priority | Test focus | Scenarios |
|---|---|---|---|---|
| FR-001 Customer self-booking | US-001–US-004 | Must | Functional, concurrency, accessibility | TS-001–TS-006 |
| FR-002 Confirmations and reminders | US-005–US-006 | Must | Functional, provider failure | TS-007–TS-009 |
| NFR-001, NFR-002 Performance | — | Must | Load | TS-030, TS-031 |

### 2.2 Out of scope for this release

| Item | Reason | Risk accepted by |
|---|---|---|
| FR-003 Online deposits | Deferred to R2 | PM |

## 3. Test Approach for This Release

| Test type | Applies? | Coverage target | Owner | Notes |
|---|---|---|---|---|
| Unit / integration | Yes | Per strategy | Developers | |
| API / contract | Yes | All API-001–API-003 | Dev + QA | |
| End-to-end | Yes | UF-01, UF-02 | QA | |
| Performance | Yes | NFR-001/002 | QA / Eng | See [Performance Test Plan](performance-test-plan.md) |
| Security | Yes | [Scope] | Security / QA | See [Security Test Plan](security-test-plan.md) |
| Accessibility | Yes | Booking flow | QA / Design | |
| Exploratory | Yes | 2 sessions per Must FR | QA | |
| Regression | Yes | Smoke + critical set | QA | |
| UAT | Yes | See [UAT Plan](uat-plan.md) | Business | |

## 4. Schedule

| Date | Activity | Owner | Depends on |
|---|---|---|---|
| [Date] | Test environment ready; smoke tests pass | Eng | Deployment pipeline |
| [Date] | Scenario execution cycle 1 | QA | Feature complete (Must) |
| [Date] | Defect fix window | Dev | Cycle 1 results |
| [Date] | Cycle 2 + regression | QA | |
| [Date] | UAT | Business | Exit criteria cycle 2 |
| [Date] | Go/no-go (see Release Plan) | PM | |

## 5. Environments and Data

| Environment | Purpose | Build / config | Data | Availability | Owner |
|---|---|---|---|---|---|
| Test | Functional, integration | Latest merged build | Synthetic (see [Test Data Management](test-data-management.md)) | [Hours] | Eng |
| Staging | Pre-release, performance, UAT | Release candidate | Synthetic, production-like volume | | Eng |

Third-party services: [sandbox or simulator for each; limits].

## 6. Roles and Responsibilities

| Role | Person | Responsibilities |
|---|---|---|
| Test lead | | Plan, reporting, quality gate input |
| Testers | | Execute scenarios, log defects |
| Developers | | Fix defects, maintain automated tests |
| Product owner | | Triage priority, accept risks |

## 7. Entry and Exit Criteria

| Gate | Criteria (this release) |
|---|---|
| Entry: start cycle 1 | Build deployed; smoke tests pass; scenarios reviewed; test data loaded |
| Exit: cycle complete | All planned scenarios run; no open Critical defects; High defects triaged |
| Exit: ready for UAT | All Must scenarios pass; Critical = 0, High accepted or fixed |
| Exit: ready to release | Meets [Test Strategy §8](test-strategy.md) and the [Release Plan](../09-release-ops/release-plan.md) go/no-go criteria |

## 8. Defect Handling for This Release

| Item | Decision |
|---|---|
| Tracker and workflow | [Tool-agnostic: link] |
| Triage cadence | [Daily during test window] |
| Fix and retest turnaround | [Critical: same day; High: 2 days] |

## 9. Risks and Contingencies

| ID | Test risk | Mitigation | Owner |
|---|---|---|---|
| RISK-xx | Messaging sandbox differs from production behaviour | Contract tests plus a monitored pilot | QA |

## 10. Deviations from the Test Strategy

[List any approved departures and the reason; leave empty if none.]

## 11. Reporting

| Report | Content | Audience | Frequency |
|---|---|---|---|
| Progress | Scenarios run/passed/failed, open defects by severity | Team | Daily |
| Quality summary | Coverage by requirement, NFR results, residual risk | PM, sponsor | At each gate |

## Completion Criteria

- [ ] In-scope and out-of-scope items reference requirement and story IDs.
- [ ] Every Must requirement has scenarios assigned and an owner.
- [ ] Schedule, environments and test data are available for every planned activity.
- [ ] Entry and exit criteria are measurable and consistent with the Test Strategy and Release Plan.
- [ ] Test risks are recorded with mitigations.
- [ ] Deviations from the strategy are documented and approved.
