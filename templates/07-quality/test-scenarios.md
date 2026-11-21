---
id: DPP-07-test-scenarios
title: Test Scenarios
domain: 07-quality
tier: recommended
status: draft
version: 0.1.0
owner: qa-lead
contributors: [business-analyst, developers, product-manager]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [user-stories, test-strategy, business-rules, non-functional-requirements]
feeds: [test-case, test-plan, requirements-traceability-matrix, uat-plan]
applies_to: [all]
---

# Test Scenarios: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | The catalog of **what must be verified**, written at scenario level and linked to acceptance criteria, business rules and NFRs. It is the bridge between requirements and detailed test cases. Canonical home for `TS-` IDs. |
| **When to use** | As soon as stories have acceptance criteria; refine each iteration. Required to claim traceability from requirement to test. |
| **Owner** | QA Lead, with Business Analyst and developers reviewing. |
| **Required inputs** | [User Stories](../03-requirements/user-stories.md) with acceptance criteria; [Business Rules](../03-requirements/business-rules.md); [NFRs](../03-requirements/non-functional-requirements.md); [Test Strategy](test-strategy.md). |
| **Related documents** | [Test Case](test-case.md) (detailed steps, `TC-` IDs) · [Test Plan](test-plan.md) · [RTM](../03-requirements/requirements-traceability-matrix.md) · [UAT Plan](uat-plan.md) |

</details>

> **Guidance:** A scenario answers **"what situation do we need to check, and what should happen?"** in one or two lines. Detailed steps and data go into a [Test Case](test-case.md) only where they add value (complex, manual, regulated or high-risk checks). Include **negative, boundary, concurrency and permission** scenarios, not just happy paths. Every acceptance criterion must be covered by at least one scenario.

## 1. Scenario Catalog

**Type:** F functional · N negative · B boundary · C concurrency · P permission · I integration · NF non-functional · A accessibility · R regression
**Priority:** Must / Should / Could · **Automation:** Auto / Manual / Planned

| ID | Scenario | Covers (AC / BR / NFR) | Requirement / Story | Preconditions | Expected result | Type | Pri | Automation | Status |
|---|---|---|---|---|---|---|---|---|---|
| TS-001 | Customer books an open slot with valid details | AC-002.1 | FR-001 / US-002 | Service has an open slot | Booking created; confirmation shown with date, time, service | F | Must | Auto | Ready |
| TS-002 | Two customers book the last slot at the same moment | AC-002.2, BR-002 | FR-001 / US-002 | One open slot | Exactly one booking succeeds; the other is told the slot is unavailable and offered alternatives | C | Must | Auto | Ready |
| TS-003 | Booking with invalid phone number | AC-002.3, BR-006 | FR-001 / US-002 | — | Field error; no booking created | N | Must | Auto | Ready |
| TS-004 | Owner without edit rights tries to change availability | BR-005 | FR-005 / US-011 | Staff user without permission | Action denied; event audited | P | Must | Auto | Draft |
| TS-030 | Booking page loads within target on mid-range phone profile | NFR-001 | — | Production-like data | p95 interactive ≤ 2 s | NF | Must | Auto | Planned |

## 2. Writing Good Scenarios

> **Guidance:**
> - **State the condition and the observable result**, not the steps ("Booking fails when slot is taken", not "Click button X").
> - **One idea per scenario.** If the expected result has "and" repeated, split it.
> - **Boundaries:** minimum/maximum lengths, first/last slot of day, time-zone and daylight-saving changes, empty lists, maximum page size.
> - **Permissions:** each role × each protected operation (see [Access Control Matrix](../08-security/access-control-matrix.md)).
> - **Failure of dependencies:** provider timeout, partial failure, retries, duplicates.
> - Link NFR scenarios to the monitoring rule that will verify them in production (`MON-`).

## 3. Coverage Check

| Requirement | Priority | Stories | ACs | ACs with ≥ 1 scenario | NFRs / BRs covered | Gap |
|---|---|---|---|---|---|---|
| FR-001 | Must | US-001–US-004 | 12 | 11 | BR-001, BR-002 | AC-004.2 uncovered |
| FR-002 | Must | US-005–US-006 | 5 | 5 | NFR-004 | — |

Rule: **100% of Must acceptance criteria and Must NFRs are covered** before the release gate. Gaps become tasks in the [Test Plan](test-plan.md).

## 4. Execution Status Summary (per release)

| Release | Planned | Passed | Failed | Blocked | Not run | Notes |
|---|---|---|---|---|---|---|
| R1 | | | | | | |

## 5. Retired and Changed Scenarios

| ID | Change | Reason | Date |
|---|---|---|---|

Never reuse an ID; mark retired scenarios and keep the row.

## Completion Criteria

- [ ] Every Must acceptance criterion, business rule and Must NFR is linked to at least one scenario.
- [ ] Negative, boundary, permission and concurrency cases exist for stories with data entry, roles or shared resources.
- [ ] Scenarios state conditions and observable results, one idea each.
- [ ] Priority, type and automation status are set.
- [ ] Coverage gaps are listed with owners.
- [ ] IDs are unique and consistent with the RTM.
