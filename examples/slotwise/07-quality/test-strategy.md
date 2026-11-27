---
id: SLOTWISE-07-test-strategy
title: Test Strategy
domain: 07-quality
tier: mandatory
status: draft
version: 0.1.0
owner: qa-lead
contributors: [engineering-lead, product-manager]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [prd, non-functional-requirements, architecture-overview]
feeds: [test-plan, test-scenarios, test-data-management, performance-test-plan, security-test-plan, uat-plan, release-plan]
applies_to: [all]
---

# Test Strategy: SlotWise

## 1. Objectives and Quality Goals

Testing must give enough confidence to release FR-001 to FR-004 as Must items and FR-005 as a Should item, protect the booking and reminder flows that drive GOAL-01 and GOAL-02, and produce evidence for NFR-001 to NFR-005. MET-01 and MET-02 are pilot targets in [Goals & Metrics](../02-strategy/goals-and-metrics.md), so tests verify the data behind them, not the target values. Because the team is small under CON-01, automation focuses on the flows that would block a release if they failed.

## 2. Scope

| In scope | Out of scope (and why) |
|---|---|
| FR-001 to FR-005, AC-001.1 to AC-005.1, BR-001 to BR-006, NFR-001 to NFR-005, DEP-01 message contract, booking data deletion, accessibility of the booking flow | DEP-01 internals, verified by sandbox contract checks only; payments and checkout, excluded by DEC-001; FR-006, deferred by DEC-003; salon-owned devices and networks |

## 3. Risk-Based Focus

| Area | Risk / criticality | Test emphasis |
|---|---|---|
| Booking reservation | High, double bookings per RISK-03 and NFR-003 | TC-002 concurrency, boundary and negative cases, exploratory sessions |
| Reminder delivery | Medium, missed messages weaken MET-01 via RISK-01 and RISK-02 | TC-003 timing, DEP-01 failure simulation, MON-003 backlog alert |
| Tenant boundary | High, one salon must never see another salon's customers | Negative access checks built into TC-001 and TC-008 |
| Capacity | Medium, 14 weeks with 2 engineers per RISK-04 | Weekly scope check; FR-006 held for R2 |

## 4. Test Levels and Types

| Level / type | Purpose | Owner | Automated? | When it runs | Entry / exit |
|---|---|---|---|---|---|
| Unit | Verify booking and cancellation rules in isolation | Developers | Yes | Every change | Pass required to merge |
| Integration / component | Verify booking service, data store and queue together | Developers | Yes | Every change and nightly | Pass before staging deployment |
| API / contract | Verify API-001 to API-003 behaviour and errors | Dev + QA | Yes | Every change | Conforms to the API Specification |
| End-to-end | Verify customer booking and owner setup journeys | QA | Selected journeys TC-001 and TC-003 | Per build and pre-release | Pass before UAT |
| Non-functional: performance | Verify NFR-001 with TS-005 | QA / Eng | Yes | Pre-release | p95 under 800 ms at 50 users |
| Non-functional: security | Verify SR-001 to SR-008 and TH-001 to TH-007 | Security / QA | Partially | Pre-release | No open Critical finding |
| Accessibility | Verify NFR-005 with TS-007 | QA / Designer | Partly | Per release | Agreed checklist passes |
| Exploratory | Find what scripted tests miss | QA | No | Per feature | Findings triaged same day |
| Regression | Protect existing behaviour | QA | Yes | Pre-release | Smoke plus TC-001 to TC-003 pass |
| User acceptance | Confirm business fit with pilot owners | Business | No | Pre-release | Sign-off in the [UAT Plan](uat-plan.md) |

## 5. Approach by Concern

| Concern | Approach |
|---|---|
| **Test design** | Scenarios derived from AC-001.1 to AC-005.1 and BR-001 to BR-006; boundary and negative cases required for cancellation cutoff and slot conflicts |
| **Traceability** | Every Must AC maps to at least one of TS-001 to TS-010 and to a TC case; coverage is checked in the [RTM](../03-requirements/requirements-traceability-matrix.md) |
| **Defect management** | Severity scale in §9, triage daily during the test window, release blocked by Critical defects |
| **Test data** | Synthetic fixture only, no real personal data; deletion test TC-006 uses a synthetic customer record |
| **Environments** | See [Environment Strategy](../09-release-ops/environment-strategy.md); unit and integration in test, performance and UAT in staging |
| **Configuration and compatibility** | Current Chrome, Firefox and Safari on desktop, plus Safari on iOS and Chrome on Android; keyboard and screen reader for the booking flow |

## 6. API Testing Approach

The [API Specification](../05-architecture/api-specification.md) is the source of truth for API-001 to API-003. Tests verify response shapes, conflict responses, error codes and idempotency against it. Negative cases cover invalid input, missing or expired booking-link tokens, over-limit requests and injection strings. DEP-01 is verified with its sandbox and a contract check; live delivery is watched during the pilot with MON-005.

## 7. Test Automation Approach

| Question | Answer |
|---|---|
| What is automated first? | TC-001 booking, TC-002 concurrency, TC-003 message timing, and API contract checks |
| What stays manual? | Exploratory sessions, TC-007 screen-reader walkthrough, UAT with salon owners |
| Automation principles | Deterministic synthetic data, independent cases, maintained like product code |
| Where does it run? | Local and in CI on every change; performance on staging before each release candidate |
| How are flaky tests handled? | Quarantine within 1 working day, fix within 2 working days, QA lead owns the quarantine list |
| Maintenance ownership | QA lead owns the suite, both engineers maintain cases for their components |

Tooling is chosen in the [Technology Stack](../05-architecture/technology-stack.md) or recorded as an ADR; this strategy stays tool-agnostic.

## 8. Entry, Exit and Release Quality Criteria

| Gate | Criteria |
|---|---|
| Ready to test a build | Build deploys to the test environment; smoke tests pass; DEP-01 sandbox reachable |
| Ready for UAT | US-001 to US-005 implemented; no open Critical or High defects in them |
| **Ready to release** | All Must scenarios pass; no open Critical defects; High defects accepted by PM with mitigation; NFR-001 to NFR-005 targets met or exceptions approved; regression pass complete; known issues documented |

Final release criteria are confirmed in the [Release Plan](../09-release-ops/release-plan.md).

## 9. Defect Severity and Handling

| Severity | Definition | Response |
|---|---|---|
| Critical | Data loss, double booking, security breach, core flow unusable, no workaround | Block release; fix immediately |
| High | Major function broken, workaround is poor | Fix before release unless PM accepts in writing |
| Medium | Function impaired, reasonable workaround | Schedule in the iteration |
| Low | Cosmetic or minor | Backlog |

## 10. Roles, Metrics and Reporting

- **Roles:** QA lead designs and reports tests, both engineers execute unit and integration tests, QA executes TS cases, PM triages priority and accepts residual risk, Eng Lead approves release quality with QA.
- **Metrics:** scenario pass rate across TS-001 to TS-010, Must AC coverage, defect escape rate from UAT, flaky test rate, defect aging. A pass rate below 100% on Must scenarios blocks release; a flaky rate above 5% triggers quarantine review.
- **Reporting:** daily progress to the team during the test window, quality summary to PM and sponsor at each gate.

## 11. Risks and Assumptions

RISK-02 may make the DEP-01 sandbox unlike live delivery, so contract tests and a monitored pilot are planned. RISK-03 drives TC-002. RISK-04 limits test depth, so FR-006 stays out of R1. ASM-01 is still being tested in the pilot; if customers reject the booking link, MET-02 is at risk and the team revisits onboarding rather than adding scope.

## Completion Criteria

- [x] Scope and exclusions are explicit, with reasons.
- [x] Test levels and types cover functional behaviour *and* each *Must* NFR category.
- [x] High-risk areas receive explicit emphasis, traced to the Risk Register.
- [x] Traceability from acceptance criteria to scenarios is defined.
- [x] Automation approach states what is automated, where it runs and who maintains it.
- [x] Defect severity scale and release quality gates are defined and agreed with the PM.
- [x] Environments and test data approach exist and avoid real personal data.
- [x] Roles and reporting are assigned.
