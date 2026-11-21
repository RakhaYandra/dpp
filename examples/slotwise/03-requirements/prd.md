---
id: SLOTWISE-prd
title: Product Requirements Document: SlotWise
domain: 03-requirements
tier: mandatory
status: approved
version: 1.0.0
owner: product-manager
contributors: []
created: 2026-09-01
last_updated: 2026-11-10
depends_on: [product-brief, goals-and-metrics]
feeds: [user-stories, non-functional-requirements, architecture-overview, test-scenarios]
applies_to: [saas]
---

# Product Requirements Document: SlotWise

## 1. Summary

SlotWise lets small salons take bookings online, confirm and remind automatically, and manage a staff calendar. Problem and evidence: [Product Brief](../01-discovery/product-brief.md). Goals: [Goals & Metrics](../02-strategy/goals-and-metrics.md).

## 2. Users

| ID | Persona | Description |
|---|---|---|
| PER-01 | Maya, salon owner | Runs a 3-chair salon; books by phone; manages everything from her phone between clients |
| PER-02 | Dani, customer | Books services on a phone; wants confirmation and a simple way to reschedule |

## 3. Assumptions, constraints, dependencies

| ID | Type | Statement | Owner | Status |
|---|---|---|---|---|
| ASM-01 | Assumption | Customers will accept a booking link instead of calling | Product | Testing in pilot |
| CON-01 | Constraint | Launch capacity: 2 engineers, 1 designer, 14 weeks | Eng lead | Fixed |
| DEP-01 | Dependency | An email/SMS delivery provider (chosen in ADR-0002) | Eng lead | Open |

## 4. Requirements

Priority uses MoSCoW. Release R1 is the pilot launch.

| ID | Requirement | Priority | Goal | Release |
|---|---|---|---|---|
| FR-001 | A customer can see open time slots for a service and book one without creating an account | Must | GOAL-02 | R1 |
| FR-002 | The system sends a booking confirmation and a reminder before the appointment | Must | GOAL-01 | R1 |
| FR-003 | A customer can cancel or reschedule from a link in the message, up to a cutoff set by the salon | Must | GOAL-01 | R1 |
| FR-004 | The owner can set services, staff, working hours and time off | Must | GOAL-02 | R1 |
| FR-005 | The owner can mark an appointment as completed or no-show | Should | GOAL-01 | R1 |
| FR-006 | Waiting list that offers freed slots | Could | GOAL-01 | R2 |

## 5. Non-goals

Payments, marketplace listing, multi-location management.

## 6. Open questions

| ID | Question | Owner | Due |
|---|---|---|---|
| Q-001 | Which reminder timings (24 h, 2 h) reduce no-shows most? | Product | Pilot week 6 |

Quality targets are in [Non-Functional Requirements](non-functional-requirements.md); stories and acceptance criteria in [User Stories](user-stories.md).

## Completion Criteria

- [x] Every requirement has an ID, priority and goal
- [x] Every Must requirement has stories and tests (checked by `check-traceability`)
