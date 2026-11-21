---
id: DPP-07-test-strategy
title: Test Strategy
domain: 07-quality
tier: mandatory
status: draft
version: 0.1.0
owner: qa-lead
contributors: [engineering-lead, product-manager]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [prd, non-functional-requirements, architecture-overview]
feeds: [test-plan, test-scenarios, test-data-management, performance-test-plan, security-test-plan, uat-plan, release-plan]
applies_to: [all]
---

# Test Strategy: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines **how quality will be assured** across the product: what is tested, at which levels, with what approach, by whom, with what environments and data, and what quality bar must be met to release. It also holds the API-testing and automation approach as sections; separate files exist only for deep dives (performance, security, UAT). |
| **When to use** | After PRD, NFRs and architecture overview are stable; before test scenarios and sprint planning. Revisit when scope or architecture changes materially. |
| **Owner** | QA Lead (solo projects: the developer, acting as QA). |
| **Required inputs** | [PRD](../03-requirements/prd.md) scope and priorities; [NFRs](../03-requirements/non-functional-requirements.md); [Architecture Overview](../05-architecture/architecture-overview.md); [Risk Register](../06-project-mgmt/risk-register.md). |
| **Related documents** | [Test Plan](test-plan.md) (the *when/who* for a given release) · [Test Scenarios](test-scenarios.md) · [Test Data Management](test-data-management.md) · [Performance Test Plan](performance-test-plan.md) · [Security Test Plan](security-test-plan.md) · [UAT Plan](uat-plan.md) |

</details>

> **Guidance:** The *strategy* is long-lived and answers "what is our approach to quality?". The [*plan*](test-plan.md) is per release and answers "what exactly will we test, when, who does it?". Do not repeat plan content here.

## 1. Objectives and Quality Goals

[What testing must achieve: confidence in *Must* requirements, protection of critical flows, evidence for NFR targets. Link to the quality-related goals and guardrails in [Goals & Metrics](../02-strategy/goals-and-metrics.md).]

## 2. Scope

| In scope | Out of scope (and why) |
|---|---|
| [Functional behaviour of FR-001–FR-0xx, NFRs, integrations, data migration, accessibility] | [e.g. Third-party provider internals; verified by contract tests only] |

## 3. Risk-Based Focus

> **Guidance:** Spend effort where failure hurts most. Pull from the [Risk Register](../06-project-mgmt/risk-register.md) and critical flows.

| Area | Risk / criticality | Test emphasis |
|---|---|---|
| Booking reservation | High: double-booking (RISK-02) | Concurrency tests, boundary tests, exploratory sessions |
| Reminder delivery | Medium: missed messages hurt MET-01 | Provider failure simulation, retry verification |

## 4. Test Levels and Types

| Level / type | Purpose | Owner | Automated? | When it runs | Entry / exit |
|---|---|---|---|---|---|
| Unit | Verify logic in isolation | Developers | Yes | Every change | Pass required to merge |
| Integration / component | Verify modules and data stores together | Developers | Yes | Every change / nightly | |
| API / contract | Verify interface behaviour, errors, versioning, consumer expectations | Dev + QA | Yes | Every change | See §6 |
| End-to-end | Verify critical user journeys | QA | Selected journeys | Per build / pre-release | |
| Non-functional: performance | Verify NFR performance and scale targets | QA / Eng | Yes | Pre-release | [Performance Test Plan](performance-test-plan.md) |
| Non-functional: security | Verify security requirements | Security / QA | Partially | Pre-release | [Security Test Plan](security-test-plan.md) |
| Accessibility | Verify NFR accessibility target | QA / Design | Partly | Per release | |
| Exploratory | Find what scripted tests miss | QA | No | Per feature | |
| Regression | Protect existing behaviour | QA | Yes | Pre-release | |
| User acceptance | Confirm the product meets business needs | Business | No | Pre-release | [UAT Plan](uat-plan.md) |

Add or remove rows to match the product (e.g. device matrix for mobile, upgrade/migration tests for enterprise).

## 5. Approach by Concern

| Concern | Approach |
|---|---|
| **Test design** | Scenarios derived from acceptance criteria (`AC-`) and business rules (`BR-`); boundary and negative cases required |
| **Traceability** | Every *Must* AC maps to ≥ 1 test scenario (`TS-`); coverage checked in the [RTM](../03-requirements/requirements-traceability-matrix.md) |
| **Defect management** | Severity scale, triage cadence, fix-priority rules, defect lifecycle (see §9) |
| **Test data** | See [Test Data Management](test-data-management.md); no real personal data in non-production environments |
| **Environments** | See [Environment Strategy](../09-release-ops/environment-strategy.md); which tests run where |
| **Configuration and compatibility** | [Supported browsers, devices, OS versions; test matrix] |

## 6. API Testing Approach

[Applies if the product exposes or consumes APIs.]

- **Contract:** the [API Specification](../05-architecture/api-specification.md) is the source of truth; tests verify responses, error shapes, pagination, versioning and idempotency against it.
- **Negative and security cases:** invalid input, missing/expired credentials, over-limit requests, injection attempts.
- **Consumers and providers:** [how third-party or partner integrations are verified: contract tests, sandbox, mocks].

## 7. Test Automation Approach

| Question | Answer |
|---|---|
| What is automated first? | [Critical journeys, regression-prone areas, API contract] |
| What stays manual? | [Exploratory, visual, one-off, usability] |
| Automation principles | [Deterministic, independent, fast, maintained like product code] |
| Where does it run? | [Local, CI on every change, scheduled] |
| How are flaky tests handled? | [Quarantine, fix within N days, owner] |
| Maintenance ownership | [Role] |

Tooling is chosen in the [Technology Stack](../05-architecture/technology-stack.md) or recorded as an ADR; this strategy stays tool-agnostic.

## 8. Entry, Exit and Release Quality Criteria

| Gate | Criteria |
|---|---|
| Ready to test a build | Build deploys to the test environment; smoke tests pass |
| Ready for UAT | All *Must* stories implemented; no open Critical/High defects in them |
| **Ready to release** | All *Must* scenarios pass; no open Critical defects; High defects accepted by PM with mitigation; NFR targets met or exceptions approved; regression pass complete; known issues documented |

Final release criteria are confirmed in the [Release Plan](../09-release-ops/release-plan.md).

## 9. Defect Severity and Handling

| Severity | Definition | Response |
|---|---|---|
| Critical | Data loss, security breach, core flow unusable, no workaround | Block release; fix immediately |
| High | Major function broken, workaround is poor | Fix before release unless approved |
| Medium | Function impaired, reasonable workaround | Schedule |
| Low | Cosmetic or minor | Backlog |

## 10. Roles, Metrics and Reporting

- **Roles:** [Who designs tests, who executes, who triages, who approves release quality]
- **Metrics:** [Scenario pass rate, requirement coverage, defect escape rate, flaky test rate, defect aging; what you will do with them]
- **Reporting:** [What is reported, to whom, how often]

## 11. Risks and Assumptions

[Test-specific risks (environment availability, data realism, tooling) and assumptions; link to RISK- IDs.]

## Completion Criteria

- [ ] Scope and exclusions are explicit, with reasons.
- [ ] Test levels and types cover functional behaviour *and* each *Must* NFR category.
- [ ] High-risk areas receive explicit emphasis, traced to the Risk Register.
- [ ] Traceability from acceptance criteria to scenarios is defined.
- [ ] Automation approach states what is automated, where it runs and who maintains it.
- [ ] Defect severity scale and release quality gates are defined and agreed with the PM.
- [ ] Environments and test data approach exist and avoid real personal data.
- [ ] Roles and reporting are assigned.
