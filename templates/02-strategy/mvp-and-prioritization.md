---
id: DPP-02-mvp-and-prioritization
title: MVP Definition and Feature Prioritization
domain: 02-strategy
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, designer]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [goals-and-metrics, assumption-map]
feeds: [prd, user-stories, roadmap, milestone-plan, release-plan]
applies_to: [all]
---

# MVP Definition and Prioritization: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines the **smallest release that can test the core hypothesis** and ranks candidate features transparently. One document covers both MVP definition and feature prioritization, since the first depends on the second. |
| **When to use** | After goals and key assumptions are known; before the PRD fixes scope. Revisit before each release. |
| **Owner** | Product Manager, with Engineering for cost estimates. |
| **Required inputs** | [Goals & Metrics](goals-and-metrics.md); [Assumption Map](../01-discovery/assumption-map.md); candidate feature ideas from research. |
| **Related documents** | [PRD](../03-requirements/prd.md) (priority per FR) · [Roadmap](roadmap.md) · [Release Plan](../09-release-ops/release-plan.md) |

</details>

> **Guidance:** An MVP is not a half-built product; it is an **experiment designed to learn**. If you cannot state what you will learn from it, it is a first release, not an MVP. Be explicit about what you are *not* building.

## 1. MVP Hypothesis

| | |
|---|---|
| **Hypothesis** | We believe that [target user] will [behaviour] if we provide [capability], and we will know this when [metric: MET-xx] reaches [target]. |
| **Riskiest assumptions tested** | ASM-01, ASM-04 |
| **Learning goal** | [What we will know after launch that we do not know now] |
| **Success / failure thresholds** | [Persevere if…, pivot if…] |
| **Audience and size** | [First users, number] |

## 2. Candidate Features

| ID | Candidate feature | Persona | Goal / metric | Supports hypothesis? |
|---|---|---|---|---|
| C-01 | Customer self-booking page | PER-01 | GOAL-02 / MET-02 | Yes |
| C-02 | Automated reminders | PER-01 | MET-01 | Yes |
| C-03 | Online payments | PER-01 | GOAL-01 | No (later) |

## 3. Prioritization

Choose **one** scoring method and state why. Common options: **MoSCoW** (simple), **RICE** (Reach × Impact × Confidence ÷ Effort), **Value vs. Effort**, **Kano** (must-be / performance / delighter).

| Candidate | Reach | Impact | Confidence | Effort | RICE score | MoSCoW | Decision |
|---|---|---|---|---|---|---|---|
| C-01 | 500 | 3 | 80% | 3 | 400 | Must | R1 |
| C-02 | 500 | 2 | 70% | 2 | 350 | Must | R1 |
| C-03 | 300 | 2 | 50% | 5 | 60 | Won't (now) | R3 |

*RICE units: Reach = users per period; Impact = 0.25–3; Confidence = %; Effort = person-weeks.* Record the formula you use so scores can be reproduced.

## 4. MVP Scope

| In MVP (Must) | Deliberately out of MVP | Manual or "concierge" substitutes |
|---|---|---|
| C-01, C-02 | C-03 payments: collect deposits offline | Owner enters special cases by hand |

**Check:** if you remove any Must item, does the hypothesis still get tested? If yes, it is not a Must.

## 5. Dependencies and Sequencing

[Technical or business dependencies that affect order; link to [Architecture Overview](../05-architecture/architecture-overview.md).]

## 6. Review Triggers

[Events that cause re-prioritization: failed experiment, new competitor, capacity change.]

## Completion Criteria

- [ ] The MVP is framed as a testable hypothesis with success thresholds.
- [ ] Every Must feature supports the hypothesis and traces to a goal.
- [ ] Prioritization method and inputs are transparent and reproducible.
- [ ] Out-of-scope items and manual workarounds are explicit.
- [ ] Priorities match the PRD requirement catalog.
