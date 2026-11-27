---
id: SLOTWISE-vision-and-value-proposition
title: Product Vision and Value Proposition: SlotWise
domain: 02-strategy
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [founder, designer]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [product-brief]
feeds: [goals-and-metrics, roadmap, mvp-and-prioritization, prd]
applies_to: [saas]
---

# Product Vision and Value Proposition: SlotWise

## 1. Vision

**Vision statement** (one sentence, a state of the world you want to create):

> Every small salon runs on a calendar customers can book themselves, so owners spend their time with clients instead of on the phone.

| Element | Answer |
|---|---|
| Who benefits | Owners and customers of salons with 1 to 5 staff, starting with PER-01 Maya and PER-02 Dani |
| What changes for them | Booking becomes online by default, confirmations and reminders are automatic, and no-shows fall |
| Time horizon | 3 years |
| How it connects to the organization's strategy | A low-cost SaaS subscription that reaches 40 paying salons by day 90 (MET-03) and grows from there |

## 2. Mission and Principles (optional)

- **What we do each day to move toward the vision:** Ship the smallest booking loop that removes one phone call, then measure whether the slot was kept.
- **Product principles:** A customer never needs an account to book (DEC-002). Simple for the owner beats configurable under CON-01. Message delivery never blocks a booking (ADR-0002). One transaction guards each slot (ADR-0001).

## 3. Value Proposition

| Element | Statement |
|---|---|
| **Target customer** | Maya, owner of a 3-chair salon, who books between clients from her phone (PER-01) |
| **Problem / job to be done** | Keep chairs full without spending about 6 hours a week on scheduling messages and losing 18% of appointments to no-shows |
| **Our solution** | A shareable web booking page with live availability, confirmation, a 24 hour reminder and a cancel or reschedule link up to the salon cutoff |
| **Primary benefit** | Fewer no-shows and less time spent scheduling, measured by MET-01 and MET-02 |
| **Unlike** (alternatives) | Phone and manual messages, or account-based tools that cost 39 USD or more and take over an hour to set up |
| **Proof points** | 24 owner survey and 1,140 appointment logs in the Product Brief; F-02 shows 6 of 12 customers abandon account sign-up; TS-002 verifies the slot guard |

**One-sentence form:** *For owners of small salons who book between clients, SlotWise is a booking page that lets customers reserve, confirm and reschedule without an account. Unlike phone booking and account-based tools, it cuts scheduling time and no-shows.*

## 4. Customer Value Map

| Customer pain | Gain they want | Feature or capability that delivers it | Requirement |
|---|---|---|---|
| Missed appointments | A predictable day | Reminder and cancel link | FR-002, FR-003 |
| Phone interruptions between clients | Time to work with clients | Guest booking page | FR-001 |
| Unclear availability | Trust that a booked slot is real | Owner sets services, staff, hours and time off | FR-004 |
| No visibility of no-shows | A number to improve | Owner marks completed or no-show | FR-005 |

## 5. Positioning and Messaging Guardrails

- **Terms we use / avoid** (add to the project [Glossary](../00-foundation/glossary.md)): use booking, slot, cutoff and no-show. Avoid appointment request, order and tenant in customer-facing copy.
- **Claims we must be able to prove:** "booking confirmed in under 1 minute" (AC-002.1 and TS-003); "no double bookings" (NFR-003 and TS-002). The claim "setup under 30 minutes" is only used after ASM-04 passes.
- **Tone:** Plain and practical, no jargon, written for someone reading on a phone between clients.

## 6. Validation

| Claim | How tested | Result |
|---|---|---|
| Customers prefer booking without an account | Customer interviews, F-02 | Supported by 6 of 12 customers, 2026-09-08 |
| Owners will pay 29 USD per month | Price page test for ASM-02 | Pending, due 2026-12-15 |
| A new owner can publish a page in 30 minutes | Usability test for ASM-04 | Pending, due 2026-12-15 |
| Reminders reduce no-shows | Pilot measurement of MET-01 | Pending, day 90 review |

## Completion Criteria

- [x] The vision states a direction and beneficiary, not a feature list.
- [x] The value proposition names a specific customer, problem, benefit and alternative.
- [x] Each claim is supported by a proof point or a planned validation.
- [x] A new team member can restate vision and value proposition in their own words.
- [x] Terms to use or avoid are recorded for consistency.
