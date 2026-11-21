---
id: SLOTWISE-test-scenarios
title: Test Scenarios: SlotWise
domain: 07-quality
tier: recommended
status: approved
version: 1.0.0
owner: qa-lead
contributors: []
created: 2026-09-01
last_updated: 2026-11-10
depends_on: [user-stories, non-functional-requirements]
feeds: [release-plan]
applies_to: [saas]
---

# Test Scenarios: SlotWise

| ID | Scenario | Covers | Type | Expected result |
|---|---|---|---|---|
| TS-001 | Customer books an open slot without an account | AC-001.1 – AC-001.3 | Functional | Booking created; only valid slots shown |
| TS-002 | 1,000 concurrent attempts on one slot | AC-001.2, NFR-003 | Concurrency | Exactly one booking succeeds; 0 double bookings |
| TS-003 | Confirmation and reminder timing | AC-002.1 – AC-002.3 | Functional | Confirmation < 1 min; one reminder; none if cancelled |
| TS-004 | Cancel and reschedule before and after cutoff | AC-003.1, AC-003.2 | Functional | Slot freed before cutoff; refused after |
| TS-005 | Slot lookup under 50 concurrent users | NFR-001 | Performance | 95% under 800 ms |
| TS-006 | Customer data deletion request | NFR-004 | Privacy | Data removed within 30 days |
| TS-007 | Keyboard and screen-reader walkthrough of booking | NFR-005 | Accessibility | Checklist passes |
| TS-008 | Owner edits hours, time off and staff | AC-004.1, AC-004.2 | Functional | Availability reflects changes; warning on conflicts |
| TS-009 | Owner marks no-show | AC-005.1 | Functional | Counted in MET-01 |
| TS-010 | Uptime check during salon hours | NFR-002 | Monitoring | Meets 99.5% monthly |

## Completion Criteria

- [x] Every Must acceptance criterion and every NFR has at least one scenario
