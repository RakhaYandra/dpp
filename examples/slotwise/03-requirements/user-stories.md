---
id: SLOTWISE-user-stories
title: User Stories and Acceptance Criteria: SlotWise
domain: 03-requirements
tier: mandatory
status: approved
version: 1.0.0
owner: product-manager
contributors: []
created: 2026-09-01
last_updated: 2026-11-10
depends_on: [prd]
feeds: [test-scenarios]
applies_to: [saas]
---

# User Stories and Acceptance Criteria: SlotWise

## Stories

| ID | Story | Requirement | Persona | Priority |
|---|---|---|---|---|
| US-001 | As a customer, I want to pick a service and an open slot so that I can book without calling | FR-001 | PER-02 | Must |
| US-002 | As a customer, I want a confirmation and a reminder so that I do not forget my appointment | FR-002 | PER-02 | Must |
| US-003 | As a customer, I want to cancel or reschedule from my message so that the salon can offer my slot to someone else | FR-003 | PER-02 | Must |
| US-004 | As an owner, I want to set services, staff and hours so that customers see only real availability | FR-004 | PER-01 | Must |
| US-005 | As an owner, I want to mark no-shows so that I can see my no-show rate | FR-005 | PER-01 | Should |

## Acceptance criteria

| ID | Given / When / Then |
|---|---|
| AC-001.1 | Given a service with free slots, when the customer opens the booking page, then only slots inside working hours and not already booked are shown |
| AC-001.2 | Given two customers choose the same slot, when both confirm, then exactly one booking succeeds and the other is offered the nearest alternatives |
| AC-001.3 | Given a valid slot, when the customer enters name and phone or email, then a booking is created without an account |
| AC-002.1 | Given a new booking, when it is created, then a confirmation is sent within 1 minute |
| AC-002.2 | Given a booking, when 24 hours remain, then a reminder is sent once |
| AC-002.3 | Given a cancelled booking, when the reminder time passes, then no reminder is sent |
| AC-003.1 | Given a booking before the cancellation cutoff, when the customer uses the link to cancel, then the slot is freed immediately |
| AC-003.2 | Given a booking after the cutoff, when the customer opens the link, then cancellation is refused and the salon's phone number is shown |
| AC-004.1 | Given an owner marks time off, when customers view availability, then those hours are not offered |
| AC-004.2 | Given a booked slot, when the owner shortens working hours over it, then the owner is warned and the booking stays |
| AC-005.1 | Given a past appointment, when the owner marks no-show, then it counts in MET-01 |

## Completion Criteria

- [x] Each story links to a requirement
- [x] Each story has at least one observable acceptance criterion
