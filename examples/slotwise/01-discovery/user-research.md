---
id: SLOTWISE-user-research
title: User Research Plan and Findings: SlotWise Pilot Discovery
domain: 01-discovery
tier: recommended
status: draft
version: 0.1.0
owner: ux-researcher
contributors: [product-manager, designer]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [product-brief]
feeds: [persona, assumption-map, prd, information-architecture, user-flow]
applies_to: [saas]
---

# User Research: SlotWise Pilot Discovery

## 1. Research Goals and Decisions

| Research question | Decision it informs | Related ASM-/Q- |
|---|---|---|
| How do owners handle no-shows today? | Whether reminders or deposits come first in R1 | ASM-02, Q-001 |
| Will customers use a shared booking link instead of calling? | Whether guest booking is the default flow | ASM-01 |
| Can a new owner publish a booking page unaided? | How much owner onboarding R1 needs | ASM-04 |
| What reminder timing is worth testing in the pilot? | The reminder schedule for FR-002 | Q-001 |

## 2. Method

| Item | Plan |
|---|---|
| Method(s) | ☑ Interviews ☑ Survey ☐ Observation / contextual inquiry ☐ Diary study ☑ Usability test ☑ Analytics review ☐ Support-ticket analysis |
| Why this method | Interviews explain why owners reconfirm manually; the survey and 1,140 booking logs quantify no-shows and online share; usability tests answer the setup question |
| Participants | 24 salon owners interviewed or surveyed in August 2026, 12 customers interviewed in August to September 2026, booking logs from 3 pilot salons |
| Incentives and consent | Written consent for interviews, recordings transcribed and anonymized, no names or phone numbers in the repository, contact data deleted within 30 days per NFR-004 |
| Materials | Discussion guide, owner survey, paper booking page prototype, anonymized booking log extract |
| Schedule and owner | August to September 2026; ux-researcher ran sessions, product-manager took notes |

**Discussion guide outline** (interviews): context → recent real example → current workflow → pain and workarounds → what they tried → wrap-up. Ask about **past behaviour**, not hypothetical preferences; avoid leading questions.

## 3. Participants

| ID | Segment | Relevant traits | Date | Notes link |
|---|---|---|---|---|
| P01 | Solo salon owner | 5 years in business, phone bookings, 2 chairs | 2026-08-04 | Anonymized notes, not stored in repo |
| P02 | Salon owner | 3 chairs, first to try an online booking tool | 2026-08-06 | Anonymized notes, not stored in repo |
| P03 | Salon owner | 4 staff, high no-show rate | 2026-08-11 | Anonymized notes, not stored in repo |
| P04 | Customer | Books haircuts monthly, prefers phone | 2026-09-03 | Anonymized notes, not stored in repo |
| P05 | Customer | Reschedules often, uses reminders | 2026-09-08 | Anonymized notes, not stored in repo |

## 4. Findings

| ID | Observation | Evidence (participants) | Severity / frequency | Interpretation |
|---|---|---|---|---|
| F-01 | Owners re-confirm every booking by message the day before | 7 of 9 owners interviewed | Frequent, about 1 hour per day | Automating reminders addresses a daily chore |
| F-02 | Customers abandon booking when asked to create an account | 6 of 12 customers interviewed | Frequent, high severity for online share | Guest booking removes the main drop-off |
| F-03 | No-shows are filled by phone calls after the fact | 5 of 9 owners; 18% of 1,140 logged appointments | Frequent, largest revenue loss named | Reminders plus a cancel link target MET-01 |

**Representative quotes:** "I call them the day before, every time" (owner P01). "I will not make a password for one haircut" (customer P04). Both are anonymized and invented for this worked example.

## 5. Insights and Implications

| Insight | Implication for product | Action | Owner |
|---|---|---|---|
| Manual reconfirmation is a daily chore (F-01) | Reminder messaging is an MVP must | Keep FR-002 in R1; test timings under Q-001 | product-manager |
| Account creation causes drop-off (F-02) | Guest booking is the default flow | Keep DEC-002 and FR-001; update PER-02 | product-manager |
| No-shows hurt revenue and are handled reactively (F-03) | Measure and reduce no-shows in R1 | Keep FR-005, target MET-01 at 10% or less | product-manager |

## 6. Assumptions Updated

| Assumption | Previous status | New status | Basis |
|---|---|---|---|
| ASM-01 | Unvalidated | Testing | F-02 plus the planned concierge pilot |
| ASM-02 | Unvalidated | Inconclusive | F-01 shows the need but not willingness to pay 29 USD |
| ASM-04 | Unvalidated | Unvalidated | No usability test had run at the time of this study |

## 7. Limitations and Next Steps

The owner sample comes from one pilot region and may overrepresent owners already open to technology. No-show rates combine self-reports with booking logs, but the logs do not record the reason for each absence. Customers were not asked about price. Follow-up work is the ASM-02 price page test and the ASM-04 usability test, both due 2026-12-15. No identifiable personal data is stored in the repository.

## Completion Criteria

- [x] Every study states the decision it informs.
- [x] Method and sample fit the question; consent and data handling are recorded.
- [x] Findings separate observation from interpretation and state counts.
- [x] Insights lead to concrete actions or document updates (Persona, Assumption Map, PRD).
- [x] Limitations are stated honestly.
- [x] No identifiable personal data is stored in the repository.
