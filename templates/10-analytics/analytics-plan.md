---
id: DPP-10-analytics-plan
title: Analytics Plan (KPIs and Product Health Metrics)
domain: 10-analytics
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [data-analyst, engineering-lead, privacy-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [goals-and-metrics, prd]
feeds: [event-tracking-plan, user-feedback-plan, post-launch-review, observability-strategy]
applies_to: [all]
---

# Analytics Plan: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines **how** the product's goals and health are measured: the precise definition of each metric (formula, source, owner), the questions analytics must answer, reporting and decisions. [Goals & Metrics](../02-strategy/goals-and-metrics.md) sets the *targets*; this document is the *measurement method*, and also holds KPI definitions and product health metrics (no separate files). |
| **When to use** | After goals are set and before tracking is implemented. Update when metrics or tooling change. |
| **Owner** | Product Manager with a data analyst where available. |
| **Required inputs** | [Goals & Metrics](../02-strategy/goals-and-metrics.md); [PRD](../03-requirements/prd.md); [Privacy Requirements](../08-security/privacy-requirements.md) constraints on data collection. |
| **Related documents** | [Event Tracking Plan](event-tracking-plan.md) · [User Feedback Plan](user-feedback-plan.md) · [Post-Launch Review](post-launch-review.md) · [Observability Strategy](../09-release-ops/observability-strategy.md) (operational telemetry) |

</details>

> **Guidance:** Start from **decisions**: "What will we do differently depending on this number?" Collect only the data you need (**data minimization**). Define every metric so two people computing it get the same answer. Distinguish **product analytics** (user behaviour, here) from **operational telemetry** (system health, Observability Strategy).

## 1. Questions and Decisions

| Question | Decision it informs | Metrics |
|---|---|---|
| Are owners activating self-booking? | Whether to invest in onboarding | MET-02, activation rate |
| Are reminders reducing no-shows? | Whether to build deposits | MET-01 |

## 2. Metric Dictionary

> **Guidance:** One row per metric. The IDs `MET-` are defined in Goals & Metrics; add supporting metrics here with `MET-` IDs continuing the sequence, and update Goals & Metrics if they are targets.

| ID | Name | Definition (plain language) | Formula | Numerator / denominator source | Event(s) | Segments | Frequency | Owner | Caveats |
|---|---|---|---|---|---|---|---|---|---|
| MET-01 | No-show rate | Share of confirmed bookings marked no-show | no_show ÷ (completed + no_show) | Booking status | EVT-004, EVT-005 | Business size, service | Weekly | PM | Depends on owners marking status |
| MET-02 | Online booking share | Share of bookings created by customers | online ÷ all bookings | Booking source field | EVT-002 | | Weekly | PM | |

## 3. Product Health Metrics

| Dimension | Metric | Definition | Healthy range / alert | Owner |
|---|---|---|---|---|
| Acquisition | New sign-ups | | | |
| Activation | Time to first published booking page | | ≤ 30 min median (ASM-04) | |
| Engagement | Active businesses per week | | | |
| Retention | Month-n retention | | | |
| Quality | Error rate on key flows | | MET-G1 | |
| Support | Contacts per 100 active accounts | | | |
| Satisfaction | [Survey score] | | | |
| Revenue (if applicable) | Paying accounts, churn | | | |

## 4. Instrumentation Approach

| Topic | Decision |
|---|---|
| Tooling and data store | [Referenced in Technology Stack] |
| Identity (users, accounts, devices) | [Pseudonymous ids; no direct identifiers in events] |
| Consent and opt-out | [How consent is collected and respected] |
| Data quality checks | [Validation, anomaly alerts, reconciliation with source-of-truth systems] |
| Retention of analytics data | |
| Access | [Who can see what] |

## 5. Reporting and Review

| Report / dashboard | Audience | Cadence | Metrics | Owner |
|---|---|---|---|---|
| Launch dashboard | Team | Daily for 2 weeks | MET-01/02, guardrails | |
| Monthly product review | Leadership | Monthly | | |

## 6. Experimentation (optional)

[Whether you will A/B test; minimum sample sizes, guardrails, who decides.]

## Completion Criteria

- [ ] Every goal metric has an unambiguous definition, formula, source and owner.
- [ ] Metrics are linked to the decisions they inform; vanity metrics are avoided.
- [ ] Health metrics cover acquisition, activation, engagement, retention, quality and support.
- [ ] Identity, consent, retention and access follow the privacy requirements.
- [ ] Reports and review cadence exist.
