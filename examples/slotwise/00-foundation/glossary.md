---
id: SLOTWISE-glossary
title: Project Glossary: SlotWise
domain: 00-foundation
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [designer, engineering-lead, qa-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: []
feeds: [prd, user-stories, design-system, data-model, wireframe-spec]
applies_to: [saas]
---

# Project Glossary: SlotWise

| Term | Definition | Use in UI / docs | Avoid (synonyms) | Related terms | Source / owner |
|---|---|---|---|---|---|
| Booking | A customer's confirmed reservation of one slot for a service | "Booking" | appointment request, order | Slot, Service, Customer | PM |
| Slot | A bookable time period offered for a service | "Time" in UI | window, opening | Booking, Availability | PM |
| Salon | The customer organisation that offers services on SlotWise | "Your salon" | tenant (technical term only), client, business | Owner, Staff | PM |
| Owner | The salon account holder who configures services, staff and hours | "Owner" | admin, tenant admin | Salon, Staff | PM |
| Staff | A person who delivers a service and occupies a slot | "Team member" in UI | resource, employee | Availability, Slot | PM |
| Service | A bookable offering with a duration, for example a haircut | "Service" | product, item | Slot, Staff | PM |
| Availability | The published working hours, staff assignments and time off that define bookable slots | "Availability" | schedule (use for the owner calendar view) | Slot, Time off | PM |
| Time off | Hours an owner removes from availability | "Time off" | holiday, block | Availability | PM |
| Cutoff | The hours before a slot start when a customer can no longer cancel or reschedule from the link | "Cancellation cutoff" | deadline, lock time | Booking, Slot | PM |
| Customer | A person who books with a salon, without an account in R1 | "Customer" | user (ambiguous), guest in customer-facing copy | Booking, No-show | PM |
| Confirmation | The message sent within 1 minute of a booking being created | "Confirmation" | receipt | Reminder, Booking | PM |
| Reminder | The single message sent 24 hours before an appointment | "Reminder" | notification (too broad) | Confirmation, No-show | PM |
| Booking link | The URL in a message that lets a customer cancel or reschedule up to the cutoff | "Manage booking" | magic link, token | Cutoff, Booking | PM |
| Completed | Appointment status set when the customer attended | "Completed" | done, served | No-show, MET-01 | PM |
| No-show | A confirmed booking where the customer did not attend and did not cancel | "No-show" | missed | Booking, MET-01 | PM |
| Waiting list | The R2 list that offers a slot freed by a cancellation | "Waiting list" | queue (technical term only) | Slot, FR-006 | PM |
| R1 | The pilot release with FR-001 to FR-005 | "Pilot release" | MVP (use in strategy docs only) | R2 | PM |
| R2 | The follow-up release that includes FR-006 | "Next release" | phase 2 | R1 | PM |

## Abbreviations

| Abbreviation | Meaning |
|---|---|
| AC | Acceptance Criterion, defined in [User Stories](../03-requirements/user-stories.md) |
| ADR | Architecture Decision Record |
| ASM | Assumption ID in the [Assumption Map](../01-discovery/assumption-map.md) |
| FR | Functional Requirement in the [PRD](../03-requirements/prd.md) |
| MET | Success metric in [Goals and Metrics](../02-strategy/goals-and-metrics.md) |
| NFR | Non-Functional Requirement |
| PER | Persona ID in [Personas](../01-discovery/persona.md) |
| TS | Test Scenario in [Test Scenarios](../07-quality/test-scenarios.md) |

## Change Log

| Date | Term | Change | Reason |
|---|---|---|---|
| 2026-11-27 | Initial set | Added salon-specific terms and abbreviations from the PRD and stories | Draft baseline for the team profile |

## Completion Criteria

- [x] Every domain term used in the PRD, stories, data model and UI appears once with one definition.
- [x] Synonyms to avoid are listed for terms with competing wordings.
- [x] Terms match those used in UI copy and data names.
- [ ] New terms are added when introduced; owner is named.
