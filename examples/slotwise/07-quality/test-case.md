---
id: SLOTWISE-07-test-case
title: Test Case
domain: 07-quality
tier: recommended
status: draft
version: 0.1.0
owner: qa-lead
contributors: [developers, business-analyst]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [test-scenarios, test-strategy]
feeds: [test-plan, uat-plan, requirements-traceability-matrix]
applies_to: [all]
---

# Test Case: TC-002 Concurrent booking of the last slot

## 0. Case Catalog

| ID | Title | Scenario | Covers | Type / priority | Automation |
|---|---|---|---|---|---|
| TC-001 | Customer books an open slot without an account | TS-001 | AC-001.1, AC-001.3, FR-001, US-001 | Functional / Must | Automated |
| TC-002 | Concurrent booking of the last slot | TS-002 | AC-001.2, NFR-003, BR-002 | Concurrency / Must | Automated |
| TC-003 | Confirmation and reminder timing | TS-003 | AC-002.1, AC-002.2, AC-002.3, US-002 | Functional / Must | Automated |
| TC-004 | Cancel and reschedule before and after cutoff | TS-004 | AC-003.1, AC-003.2, US-003 | Functional / Must | Automated |
| TC-005 | Slot lookup under 50 concurrent users | TS-005 | NFR-001 | Performance / Must | Automated |
| TC-006 | Customer data deletion request | TS-006 | NFR-004, US-001 | Privacy / Must | Manual |
| TC-007 | Keyboard and screen-reader booking walkthrough | TS-007 | NFR-005 | Accessibility / Must | Manual |
| TC-008 | Owner edits hours, time off and staff | TS-008 | AC-004.1, AC-004.2, US-004 | Functional / Must | Automated |
| TC-009 | Owner marks no-show | TS-009 | AC-005.1, US-005, MET-01 | Functional / Should | Automated |
| TC-010 | Uptime check during salon hours | TS-010 | NFR-002, MON-001 | Monitoring / Must | Automated |

## 1. Header

| Field | Value |
|---|---|
| **Test case ID** | TC-002 |
| **Title** | Concurrent booking of the last slot |
| **Scenario** | TS-002 |
| **Covers** | AC-001.2 · BR-002 · NFR-003 |
| **Requirement / story** | FR-001 / US-001 |
| **Type / priority** | Concurrency / Must |
| **Automation** | Automated, concurrency test in CI plus a pre-release run on staging |
| **Author / reviewer / date** | QA lead / Engineering lead / 2026-11-27 |
| **Estimated time** | 15 minutes per run |

## 2. Preconditions and Data

| Item | Detail |
|---|---|
| Environment / build | Test environment, release candidate build R1-RC-2027-02-26 |
| Required state | One service with exactly one open slot at 2027-02-26 10:00 UTC, staff member assigned |
| Accounts and roles | Two synthetic guest customers, no accounts created |
| Data set | Synthetic booking fixture with one salon, one service and one slot; no real personal data |
| Dependencies | DEP-01 messaging simulator active, so no real messages are sent |

## 3. Steps and Expected Results

| # | Action | Test data | Expected result |
|---|---|---|---|
| 1 | Customer A and Customer B open the booking page for the same service | Service fixture with one slot | Both see the open slot |
| 2 | Both select the slot and submit their details at the same moment | A and B use different synthetic names and phone numbers | Exactly one confirmation is shown; the other request gets a conflict response |
| 3 | Check the other customer's screen | Conflict response | Message offers the nearest alternative slots; no booking exists for this customer |
| 4 | Check the owner calendar | Same service and slot | One booking for the slot and no duplicate rows |

## 4. Postconditions and Clean-up

One confirmed booking remains for the fixture slot and the losing customer has no booking. After the run, the QA lead deletes the synthetic bookings and resets the fixture to one open slot. No personal data is retained.

## 5. Result Record (per execution)

| Date | Build | Tester | Result (Pass / Fail / Blocked) | Defect ID | Evidence | Notes |
|---|---|---|---|---|---|---|

## Completion Criteria

- [x] The case links to a scenario and to the acceptance criteria or rules it covers.
- [x] Preconditions and data are specified and use no real personal data.
- [x] Each step has an expected, observable result.
- [x] A person unfamiliar with the feature can execute it unaided.
- [x] Result records and defect links are kept for each run.
