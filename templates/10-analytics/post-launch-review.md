---
id: DPP-10-post-launch-review
title: Post-Launch Review
domain: 10-analytics
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, qa-lead, support-lead, designer]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [goals-and-metrics, analytics-plan, release-plan]
feeds: [roadmap, mvp-and-prioritization, risk-register, assumption-map, decision-log]
applies_to: [all]
---

# Post-Launch Review: [Product Name] — [Release / Period]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Compares what actually happened after launch with what was planned (goals, metrics, expected results, assumptions, delivery) and decides what to do next. It closes the planning loop and turns experience into better future plans. |
| **When to use** | At the review points scheduled in the PRD (for example week 1, week 4, week 12 after launch), and after major releases. Keep the earlier reviews short. |
| **Owner** | Product Manager. |
| **Required inputs** | Metric data ([Analytics Plan](analytics-plan.md)); [Goals & Metrics](../02-strategy/goals-and-metrics.md) targets and the PRD's *Expected Results*; release and incident records; [User Feedback Plan](user-feedback-plan.md) output. |
| **Related documents** | [Roadmap](../02-strategy/roadmap.md) · [Assumption Map](../01-discovery/assumption-map.md) · [Risk Register](../06-project-mgmt/risk-register.md) · [Decision Log](../00-foundation/decision-log.md) |

</details>

> **Guidance:** Be **honest and blameless**. Separate *what happened* from *why* and from *what we will do*. Compare against the targets set **before** launch; do not move the goalposts. Include what worked, not only what failed.

## 1. Review Context

| | |
|---|---|
| **Release / period** | R1; launch date [ ]; review at [week N] |
| **Participants** | |
| **Data sources and cut-off date** | |

## 2. Goals and Metrics: Plan vs Actual

| ID | Metric | Target | Actual | Variance | Status | Confidence in data |
|---|---|---|---|---|---|---|
| MET-01 | No-show rate | ≤ 10% | [ ] | | On track / Behind / Missed / Exceeded | |
| MET-G1 | Booking error rate (guardrail) | < 1% | | | | |

**Expected results from the PRD vs reality:** [e.g. expected 30 of 50 pilot businesses to activate; actual 22.]

## 3. Delivery and Operations

| Area | Planned | Actual | Notes |
|---|---|---|---|
| Scope delivered (FR/US) | | | |
| Schedule | | | |
| Quality (defect escapes, incidents) | | | |
| Operations (SLO attainment, support load) | | | |

## 4. Users and Feedback

[Top themes from feedback and support; evidence of whether personas and use cases matched real use; surprises.]

## 5. Assumptions and Risks

| ID | Assumption / risk | Prior status | Evidence now | New status |
|---|---|---|---|---|

## 6. Learnings

| What went well | What did not | What surprised us |
|---|---|---|

## 7. Decisions and Actions

| Decision / action | Type (persevere / iterate / pivot / stop / fix) | Owner | Due | Updates (Roadmap, PRD, risks) |
|---|---|---|---|---|

Record significant decisions in the [Decision Log](../00-foundation/decision-log.md).

## 8. Process Improvements for Future Planning

[Which framework documents or estimates proved wrong or missing, so the planning process itself improves.]

## Completion Criteria

- [ ] Actuals are compared with pre-launch targets and expected results, including guardrails.
- [ ] Delivery, operational and user perspectives are covered.
- [ ] Assumptions and risks are updated in their registers.
- [ ] Concrete decisions and owned actions exist and are reflected in the roadmap.
- [ ] Learnings are shared with the team.
