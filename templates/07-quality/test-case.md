---
id: DPP-07-test-case
title: Test Case
domain: 07-quality
tier: recommended
status: draft
version: 0.1.0
owner: qa-lead
contributors: [developers, business-analyst]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [test-scenarios, test-strategy]
feeds: [test-plan, uat-plan, requirements-traceability-matrix]
applies_to: [all]
---

# Test Case: TC-000 — [Short title]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | A detailed, repeatable test record (steps, data, expected results) for a [Test Scenario](test-scenarios.md). Canonical home for `TC-` IDs. Use it where steps matter: manual tests, complex set-up, regulated products, handover to external testers, or high-risk flows. Automated tests may reference the TC ID in the test name instead of keeping a full document. |
| **When to use** | After the scenario catalog exists, for scenarios that need step-level detail. Not every scenario needs a case. |
| **Owner** | QA Lead or tester. |
| **Required inputs** | The linked [Test Scenario](test-scenarios.md); [User Stories](../03-requirements/user-stories.md) acceptance criteria; [Test Data Management](test-data-management.md) data sets. |
| **Related documents** | [Test Plan](test-plan.md) · [UAT Plan](uat-plan.md) · [RTM](../03-requirements/requirements-traceability-matrix.md) |

</details>

> **Guidance:** One test case per file, or a table of cases in one file (for small projects). Write steps so that someone who has **not** seen the product can run them, and make expected results **observable and specific**. Keep a case independent of others where possible; state dependencies explicitly. Do not include real personal data.

## 1. Header

| Field | Value |
|---|---|
| **Test case ID** | TC-101 |
| **Title** | Concurrent booking of the last slot |
| **Scenario** | TS-002 |
| **Covers** | AC-002.2 · BR-002 |
| **Requirement / story** | FR-001 / US-002 |
| **Type / priority** | Concurrency / Must |
| **Automation** | ☐ Manual ☐ Automated (reference: [test name or path]) |
| **Author / reviewer / date** | |
| **Estimated time** | |

## 2. Preconditions and Data

| Item | Detail |
|---|---|
| Environment / build | [Test; build id] |
| Required state | One service with exactly one open slot at [date/time] |
| Accounts and roles | Two guest customers (synthetic) |
| Data set | DS-booking-01 (see [Test Data Management](test-data-management.md)) |
| Dependencies | Messaging simulator active |

## 3. Steps and Expected Results

| # | Action | Test data | Expected result |
|---|---|---|---|
| 1 | Customer A and Customer B open the booking page for the same service | — | Both see the open slot |
| 2 | Both select the slot and submit details simultaneously | A: synthetic name/phone; B: synthetic name/phone | Exactly one confirmation is shown |
| 3 | Check the other customer's screen | — | "Slot no longer available" message with alternative slots; no booking exists for this customer |
| 4 | Check the owner calendar | — | One booking for the slot; no duplicates |

## 4. Postconditions and Clean-up

[State after the test; how to reset data.]

## 5. Result Record (per execution)

| Date | Build | Tester | Result (Pass / Fail / Blocked) | Defect ID | Evidence | Notes |
|---|---|---|---|---|---|---|

## Completion Criteria

- [ ] The case links to a scenario and to the acceptance criteria or rules it covers.
- [ ] Preconditions and data are specified and use no real personal data.
- [ ] Each step has an expected, observable result.
- [ ] A person unfamiliar with the feature can execute it unaided.
- [ ] Result records and defect links are kept for each run.
