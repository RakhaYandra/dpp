---
id: SLOTWISE-competitor-analysis
title: Competitor Analysis: SlotWise
domain: 01-discovery
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [business-analyst, designer]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [product-brief]
feeds: [vision-and-value-proposition, mvp-and-prioritization, prd, business-model, roadmap]
applies_to: [saas]
---

# Competitor Analysis: SlotWise

> *Worked example. Competitor names, prices and trial notes below are fictional and invented for illustration.*

## 1. Alternatives Landscape

| Type | Alternative | Why users use it | Where it falls short for our users |
|---|---|---|---|
| Direct | SalonDesk | Established booking pages for salons, simple owner calendar | Requires a customer account, setup took over an hour in trial, 39 USD per month |
| Direct | SlotBook | Reminders and a customer app | Customer app is required, 59 USD per month, no cancel link in messages |
| Indirect | Shared calendar plus manual messages | Free or already owned, familiar | No slot guard against double booking, owner still confirms every appointment |
| Indirect | Social media direct messages | Customers already use the apps | No availability, no reminder, messages get buried |
| Non-consumption | Paper diary and phone calls | Free, familiar | Manual effort, about 6 hours a week, no reminders, 18% no-show rate |

## 2. Evaluation Criteria

Criteria come from the 24 owner survey and 12 customer interviews in [User Research](user-research.md): setup time for a solo owner, customer booking without an account, automatic reminders with a cancel link, monthly price for a 3-chair salon, owner calendar on a phone, and data export.

## 3. Comparison Matrix

Rating scale: ● strong · ◐ partial · ○ absent · ? unknown. Add the evidence column for any non-obvious rating.

| Criterion | Weight | Us (planned) | SalonDesk | SlotBook | Manual process | Evidence |
|---|---|---|---|---|---|---|
| Setup time under 30 min | High | ● | ◐ | ○ | ● | Trial notes 2026-11-12 and 2026-11-14; SalonDesk needed 65 min, SlotBook needed a sales call |
| Customer self-booking without account | High | ● | ○ | ◐ | ○ | Sign-up flow checked 2026-11-12; SlotBook asks for an app install |
| Reminders with cancel link | High | ● | ◐ | ● | ○ | Trial notes 2026-11-14; SalonDesk reminders have no link |
| Price fit for 3-chair salon | High | ● | ○ | ◐ | ● | Public pricing checked 2026-11-12: 39 and 59 USD per month, planned price 29 USD |
| Owner calendar on phone | Medium | ● | ◐ | ● | ◐ | Trial notes 2026-11-14 |
| Data export | Low | ○ | ◐ | ● | ○ | Trial notes 2026-11-14; export is not in R1 per PRD non-goals |

## 4. Competitor Profiles (key competitors only)

### SalonDesk

| | |
|---|---|
| **Positioning** | Booking software for hair and beauty salons of any size |
| **Target customer** | Salons with 3 to 20 staff |
| **Pricing and packaging** | 39 USD per month per location, public pricing checked 2026-11-12 |
| **Strengths** | Simple editor for services and staff, established brand in the pilot region |
| **Weaknesses / gaps** | Customer account required, reminders have no cancel link, setup over an hour |
| **Recent moves** | Added a calendar widget in October 2026, fictional example note |
| **How they might respond to us** | Remove the account requirement for customers or discount to match 29 USD |

### SlotBook

| | |
|---|---|
| **Positioning** | Mobile-first booking and loyalty app for beauty appointments |
| **Target customer** | Customers of mid-size salons and chains |
| **Pricing and packaging** | 59 USD per month per salon, public pricing checked 2026-11-12 |
| **Strengths** | Polished customer app, reminders already include a manage link |
| **Weaknesses / gaps** | App install required, price too high for a 3-chair salon, sales call for setup |
| **Recent moves** | Bundled loyalty points in September 2026, fictional example note |
| **How they might respond to us** | Offer a low-cost web-only tier for small salons |

## 5. Positioning and Differentiation

| Question | Answer |
|---|---|
| Where is the unserved or underserved need? | Small salons with 1 to 5 staff need a booking page customers use without an account, at a price under 30 USD per month |
| Our differentiator, in one sentence | A 3-chair salon can publish a booking page in 30 minutes and customers book, confirm and reschedule without an account |
| Is it defensible? Why? | Not by technology alone. It holds if we keep setup under 30 minutes, keep the guest flow, and stay at 29 USD while larger tools carry account and app overhead |
| What do we deliberately *not* compete on? | Payments (DEC-001), marketplace discovery, multi-location management, loyalty programs |

## 6. Implications

| Finding | Implication | Feeds |
|---|---|---|
| Both direct competitors require a customer account or app | Guest booking is a differentiator | FR-001, Vision and Value Proposition |
| Reminders with a cancel link are rare or absent | Confirmation, reminder and cutoff-based cancel are R1 musts | FR-002, FR-003, MVP document |
| Cheapest direct alternative is 39 USD per month | A 29 USD salon price undercuts without a transaction fee | Business Model, MET-03 |
| Competitor setup takes over an hour | The 30 minute owner setup target needs a usability test (ASM-04) | Assumption Map, MVP document |

## 7. Sources and Refresh

| Source | Date checked | Next refresh |
|---|---|---|
| SalonDesk public pricing and trial notes, fictional example | 2026-11-12 | 2027-02-12 |
| SlotBook public pricing and trial notes, fictional example | 2026-11-14 | 2027-02-14 |
| Owner and customer interviews in [User Research](user-research.md) | 2026-09-10 | 2027-01-10 |

## Completion Criteria

- [x] Direct, indirect and non-consumption alternatives are listed.
- [x] Criteria reflect user needs from research, not an arbitrary feature checklist.
- [x] Every rating that is not obvious has evidence and a date; unknowns are marked.
- [x] A differentiation statement and its defensibility are stated.
- [x] Implications feed the value proposition, MVP and PRD.
- [x] Review date set.
