---
id: SLOTWISE-non-functional-requirements
title: Non-Functional Requirements: SlotWise
domain: 03-requirements
tier: mandatory
status: approved
version: 1.0.0
owner: engineering-lead
contributors: []
created: 2026-09-01
last_updated: 2026-11-10
depends_on: [prd]
feeds: [architecture-overview, test-scenarios]
applies_to: [saas]
---

# Non-Functional Requirements: SlotWise

| ID | Category | Requirement | Measure | Verified by |
|---|---|---|---|---|
| NFR-001 | Performance | The booking page shows slots quickly | 95% of slot lookups under 800 ms at 50 concurrent users | [TS-005](../07-quality/test-scenarios.md) |
| NFR-002 | Availability | The booking page is available during salon hours | 99.5% monthly uptime | Monitoring (see [Architecture](../05-architecture/architecture-overview.md)) |
| NFR-003 | Data integrity | A slot is never booked twice | 0 double bookings in 1,000 concurrent attempts | TS-002 |
| NFR-004 | Privacy | Customer contact data is used only for booking messages and deletable on request | Deletion completes within 30 days | TS-006 |
| NFR-005 | Accessibility | Booking flow is usable by keyboard and screen reader | Passes the team's agreed accessibility checklist for the booking flow | TS-007 |

Note: the targets are planning assumptions for a pilot, to be revisited with real load data.

## Completion Criteria

- [x] Each requirement is measurable and has a verification method
