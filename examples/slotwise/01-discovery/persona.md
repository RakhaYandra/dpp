---
id: SLOTWISE-persona
title: User Personas: SlotWise
domain: 01-discovery
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [ux-researcher, designer]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [product-brief]
feeds: [prd, user-stories, user-flow, wireframe-spec]
applies_to: [saas]
---

# User Personas: SlotWise

## 1. Persona Summary

| ID | Persona | Type | Evidence base | Confidence |
|---|---|---|---|---|
| PER-01 | Maya, owner of a 3-chair salon | Primary | 24 owner interviews and survey, August 2026; booking logs from 3 pilot salons | High |
| PER-02 | Dani, salon customer | Secondary | 12 customer interviews, August to September 2026 | Medium |

## 2. Persona Detail (repeat per persona)

### PER-01, Maya, salon owner

> *"I book between clients. By the time I call back, the slot is gone or they have forgotten."* Interview O07, August 2026.

| | |
|---|---|
| **Who they are** | Owns a 3-chair salon, takes bookings by phone and messaging apps, works a full chair schedule herself |
| **Goals** | Keep the chair calendar full, stop repeating the same scheduling messages, see who did not show up |
| **Tasks they perform** | Answer booking requests, match a service to a staff member and slot, send confirmations, fill cancelled slots, mark attendance |
| **Pain points today** | About 6 hours a week on scheduling messages; median no-show rate 18% of appointments; double bookings when two requests arrive together |
| **Current tools and workarounds** | Phone, messaging apps and a paper or shared calendar. Manual reconfirmation the day before, reported by 7 of 9 interviewees (F-01) |
| **Motivations and decision criteria** | Saves time per week, fewer empty chairs, price under 30 USD per month, setup without a sales call |
| **Technical comfort** | Intermediate, runs the salon from a phone, little patience for configuration screens |
| **Usage context** | Short sessions between clients, often one-handed on a phone, frequent interruptions |
| **Accessibility needs** | Large tap targets and readable text on a small screen; no known assistive technology use in the sample |
| **Success looks like** | Customers book online without a call, reminders go out automatically, and no-show rate drops toward 10% (MET-01) |

### PER-02, Dani, salon customer

> *"I do not want to make an account just to book a haircut, but I do want a reminder."* Interviewee C04, September 2026.

| | |
|---|---|
| **Who they are** | Regular salon customer who books and reschedules from a phone |
| **Goals** | Find a real open time, get a confirmation, change or cancel plans without calling during salon hours |
| **Tasks they perform** | Pick a service, choose a time, provide name and phone or email, reschedule or cancel before the cutoff |
| **Pain points today** | Calls go unanswered while the owner is with a client; no reminder means forgotten appointments; account sign-up is abandoned by 6 of 12 interviewees (F-02) |
| **Current tools and workarounds** | Phone calls and direct messages, then a personal phone reminder |
| **Motivations and decision criteria** | Speed, no account, a clear confirmation, a link that works later if plans change |
| **Technical comfort** | Comfortable with phone browsing and message links |
| **Usage context** | Evening or commute, low patience for long forms, may return to the booking link days later |
| **Accessibility needs** | Keyboard-operable flow and readable labels; NFR-005 sets the verification target |
| **Success looks like** | A booking confirmed in under a minute and a single reminder 24 hours before the appointment |

## 3. Role Cards (non-primary roles)

| Role | Interacts with product to… | Needs | Permissions summary |
|---|---|---|---|
| Support agent | Answer owner questions about bookings and messages | Read-only view of a salon's bookings and message log | Limited, audited |

## 4. Anti-Personas (optional)

Multi-location chains and marketplaces are deliberately not served in R1. Owners who require deposits or customer accounts are outside the current scope per DEC-001 and the PRD non-goals.

## 5. Validation Log

| Date | What was learned | Persona changed |
|---|---|---|
| 2026-09-10 | Owners book between clients and need phone-first screens | PER-01: added usage context and tap target need |
| 2026-11-10 | Customers abandon account-based booking | PER-02: added no-account decision criterion |

## Completion Criteria

- [x] Each persona is traceable to research evidence; unvalidated traits are labelled.
- [x] Goals, pain points and context are specific enough to drive design decisions.
- [x] Primary persona is distinguished from secondary.
- [x] Non-user roles (admin, support) are identified where relevant.
- [x] PRD requirements reference persona IDs.
