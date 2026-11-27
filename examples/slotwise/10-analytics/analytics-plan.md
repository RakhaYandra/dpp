---
id: SLOTWISE-10-analytics-plan
title: Analytics Plan (KPIs and Product Health Metrics)
domain: 10-analytics
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [data-analyst, engineering-lead, privacy-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [goals-and-metrics, prd]
feeds: [event-tracking-plan, post-launch-review, observability-strategy]
applies_to: [all]
---

# Analytics Plan: SlotWise

## 1. Questions and Decisions

| Question | Decision it informs | Metrics |
|---|---|---|
| Are owners making online booking the default? | Whether to invest in onboarding or keep phone booking support | MET-02, activation target |
| Are reminders reducing no-shows? | Whether to build deposits in R2, and how to answer Q-001 | MET-01, reminder delivery from MON-005 |
| Are salons paying after the pilot? | Whether the subscription plan in the SaaS package is viable | MET-03 |

## 2. Metric Dictionary

| ID | Name | Definition (plain language) | Formula | Numerator / denominator source | Event(s) | Segments | Frequency | Owner | Caveats |
|---|---|---|---|---|---|---|---|---|---|
| MET-01 | No-show rate | Share of confirmed appointments the owner marks as no-show | no_show divided by (completed plus no_show) | Booking status from US-005 and AC-005.1 | EVT-003 | Salon size, service | Monthly | PM | Depends on owners marking status; target is 10% or less by 2027-06-03 |
| MET-02 | Online booking share | Share of bookings created by customers through the public link | customer_source divided by all bookings | Booking source field from API-002 | EVT-002 | Salon, week | Monthly | PM | Target is at least 50% by 2027-06-03 |
| MET-03 | Paying salons after 90 days | Count of salons with a paid subscription at day 90 | count of active paying salon accounts | Billing records in [Subscription & Billing](../packages/saas/subscription-and-billing.md) | Not event-based | Plan | Monthly | PM | Target is 40 salons by 2027-06-03; payments are manual in R1 per DEC-001 |

All values are pilot targets from [Goals & Metrics](../02-strategy/goals-and-metrics.md), not observed results.

## 3. Product Health Metrics

| Dimension | Metric | Definition | Healthy range / alert | Owner |
|---|---|---|---|---|
| Acquisition | New salon sign-ups | Salon accounts created in the period | Target set for the pilot and reviewed on 2027-06-03 | PM |
| Activation | Salons with a published booking link | First successful link shared by owner | 30 minutes median target for first setup | PM |
| Engagement | Salons with at least one booking per week | Active salon count | Reviewed at the monthly product review | PM |
| Retention | Month-1 retained salons | Salons still active 30 days after sign-up | Reviewed at the 90-day review | PM |
| Quality | Booking error rate | Failed booking requests over all requests | Below 1% target, measured by MON-001 | Engineering lead |
| Support | Contacts per 100 active salons | Support messages divided by active salons, scaled | Reviewed weekly during hypercare | PM |
| Satisfaction | Owner feedback theme count | Themes from pilot feedback, not a score claim | Reviewed at the 90-day review | PM |
| Revenue | Paying salons | Same as MET-03 | 40 by 2027-06-03 target | PM |

## 4. Instrumentation Approach

| Topic | Decision |
|---|---|
| Tooling and data store | Recorded in the [Technology Stack](../05-architecture/technology-stack.md); the analytics store is separate from the booking store |
| Identity (users, accounts, devices) | Pseudonymous salon account id and session id; no name, phone or email in event payloads |
| Consent and opt-out | Booking-message consent from NFR-004; analytics events use only pseudonymous ids and are suppressed for sessions that opt out |
| Data quality checks | Monthly reconciliation of EVT-002 count against booking records, and EVT-003 status counts against the owner calendar |
| Retention of analytics data | 12 months, then aggregated counts retained |
| Access | PM and data analyst see dashboards; support sees no individual-level analytics |

## 5. Reporting and Review

| Report / dashboard | Audience | Cadence | Metrics | Owner |
|---|---|---|---|---|
| Launch dashboard | Team | Daily for 2 weeks from 2027-03-05 | MET-01, MET-02, guardrail from MON-001 | PM |
| Monthly product review | Sponsor and team | Monthly from 2027-04-05 | MET-01, MET-02, MET-03, health metrics | PM |
| 90-day review | Sponsor and team | 2027-06-03 | All goals and actions | PM |

## 6. Experimentation (optional)

No A/B test is planned for R1 because three pilot salons are too few for a reliable split. Q-001 on reminder timing is answered by comparing no-show rates before and after the change during pilot weeks, with MET-01 as the outcome and owner feedback as context. The PM decides whether to change the default reminder time and records the outcome in the Decision Log.

## Completion Criteria

- [x] Every goal metric has an unambiguous definition, formula, source and owner.
- [x] Metrics are linked to the decisions they inform; vanity metrics are avoided.
- [x] Health metrics cover acquisition, activation, engagement, retention, quality and support.
- [x] Identity, consent, retention and access follow the privacy requirements.
- [x] Reports and review cadence exist.
