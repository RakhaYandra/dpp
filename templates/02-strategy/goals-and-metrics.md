---
id: DPP-02-goals-and-metrics
title: Goals and Success Metrics
domain: 02-strategy
tier: mandatory
status: draft
version: 0.1.0
owner: product-manager
contributors: []
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [product-brief]
feeds: [prd, analytics-plan, roadmap, mvp-and-prioritization, post-launch-review]
applies_to: [all]
---

# Goals and Success Metrics: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines what "success" means before building: the outcomes the product must achieve and the measurable evidence that will show whether it did. It is the canonical home for `GOAL-` and `MET-` IDs and replaces separate "Product Goals" and "Success Metrics" documents. |
| **When to use** | After the Product Brief; before the PRD. Revisit at each roadmap review. |
| **Owner** | Product Manager (with business sponsor for business goals). |
| **Required inputs** | [Product Brief](../01-discovery/product-brief.md); company or personal objectives; any baseline data. |
| **Related documents** | [PRD](../03-requirements/prd.md) · [Analytics Plan](../10-analytics/analytics-plan.md) (how metrics are computed and instrumented) · [Roadmap](roadmap.md) · [Post-Launch Review](../10-analytics/post-launch-review.md) |

</details>

> **Guidance:** *Goals* say what must become true; *metrics* say how you will know. This document holds the **targets**. The [Analytics Plan](../10-analytics/analytics-plan.md) holds the **measurement method** (formula, data source, event). Do not define the same metric in both places.

## 1. Strategic Context

[One paragraph: the vision or company objective this product serves, and the time horizon these goals cover.]

## 2. Goals

> **Guidance:** Write goals as outcomes, not features ("reduce missed appointments", not "build reminders"). Aim for 1–3 business goals and 1–3 user goals. Each goal must be testable by at least one metric below.

| ID | Type | Goal | Rationale | Time horizon |
|---|---|---|---|---|
| GOAL-01 | Business | [e.g. Reach a sustainable base of paying small businesses] | [Why it matters] | [e.g. 12 months] |
| GOAL-02 | User | [e.g. Owners stop losing sessions to no-shows] | [Link to problem in Brief] | [e.g. 3 months after launch] |

## 3. Success Metrics

> **Guidance:** For each goal pick one primary metric and, if needed, up to two supporting metrics. Mix *outcome* metrics (results the user or business gets) with *adoption/behaviour* metrics (leading indicators). Avoid vanity metrics (totals that only go up). If no baseline exists, state how and when you will establish one.

| ID | Goal | Metric | Type | Baseline | Target | By when | Owner |
|---|---|---|---|---|---|---|---|
| MET-01 | GOAL-02 | Customer no-show rate | Outcome | 18% (survey, n=40) *establish in-product by [date]* | ≤ 10% | Launch + 3 months | PM |
| MET-02 | GOAL-02 | Share of bookings made online | Adoption | 0% | ≥ 60% | Launch + 2 months | PM |
| MET-03 | GOAL-01 | Paying accounts | Outcome | 0 | 50 | Launch + 6 months | Founder |

## 4. Guardrail Metrics

> **Guidance:** What must *not* get worse while you pursue the goals (e.g. error rate, support load, page performance, churn). Guardrails stop success on one metric from hiding damage elsewhere.

| ID | Guardrail | Threshold | Action if breached |
|---|---|---|---|
| MET-G1 | Booking error rate | < 1% of attempts | Pause rollout, investigate |

## 5. Qualitative Objectives

[Outcomes that numbers capture poorly (e.g. "Owners describe the tool as something they no longer think about") and how you will gather evidence: interviews, feedback prompts, support themes.]

## 6. Review Cadence and Decision Rules

| When | Question | Decision it supports |
|---|---|---|
| [Week 1 / 4 / 12 after launch] | [Are targets on track?] | [Continue / adjust / stop] |

**Decision rule example:** if MET-01 is not below 14% after 8 weeks, run a root-cause review of reminder timing and message content before building new features.

## 7. Risks to Measurement

[Small sample sizes, seasonality, no baseline, privacy limits on data collection. For each, note the mitigation.]

## Completion Criteria

- [ ] Every goal has an ID and at least one metric; every metric traces to a goal.
- [ ] Every metric has baseline (or plan to get one), target, time frame and owner.
- [ ] At least one metric is an outcome, not only activity.
- [ ] Guardrails exist for quality, performance or cost where relevant.
- [ ] Targets are realistic for the stated time frame and audience size.
- [ ] Measurement methods are defined in the Analytics Plan, not here.
