---
id: DPP-06-risk-register
title: Risk Register
domain: 06-project-mgmt
tier: mandatory
status: draft
version: 0.1.0
owner: project-manager
contributors: [product-manager, engineering-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [prd]
feeds: [milestone-plan, release-plan, test-strategy, project-charter]
applies_to: [all]
---

# Risk Register: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | The single list of things that might go wrong (or unexpectedly go right), how likely and severe they are, what is being done about them, and who is responsible. It is the canonical home for `RISK-` IDs; the PRD only shows the top few. |
| **When to use** | Start during discovery; review at every milestone and before every release. A register nobody revisits is worse than none. |
| **Owner** | Project Manager (solo projects: the developer or founder). |
| **Required inputs** | [PRD](../03-requirements/prd.md) scope and assumptions; [Assumption Map](../01-discovery/assumption-map.md); [Architecture Overview](../05-architecture/architecture-overview.md); input from engineering, design, QA, security and business. |
| **Related documents** | [Threat Model](../08-security/threat-model.md) (security threats feed in here) · [Release Plan](../09-release-ops/release-plan.md) · [Milestone Plan](milestone-plan.md) |

</details>

> **Guidance:** A risk is an **uncertain future event with a consequence**, written as *"If [cause/condition], then [event], resulting in [impact]."* A fact that is already happening is an **issue**; track it separately or flip its status. Distinguish a risk from a task ("write tests") and from a wish ("don't be late").

## 1. Scoring Method

**Probability:** 1 Rare (< 10%) · 2 Unlikely (10–30%) · 3 Possible (30–60%) · 4 Likely (60–85%) · 5 Almost certain (> 85%)
**Impact:** 1 Negligible · 2 Minor (absorbed in the schedule) · 3 Moderate (milestone slips or scope trims) · 4 Major (release at risk, significant cost) · 5 Severe (product viability, legal or safety harm)

**Score = Probability × Impact.** Suggested bands: **1–5 Low**, **6–12 Medium**, **13–25 High**. Adjust bands to your context and record the change here.

**Response options:** *Avoid* (change the plan) · *Mitigate* (reduce likelihood or impact) · *Transfer* (insurance, contract, vendor) · *Accept* (consciously, with a trigger) · *Exploit* (for positive risks).

## 2. Register

| ID | Category | Risk (If… then… resulting in…) | P | I | Score | Response | Mitigation / contingency | Trigger | Owner | Status | Next review |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RISK-01 | Product | If owners do not trust self-booking, then adoption stalls, so MET-02 is missed | 3 | 4 | 12 | Mitigate | Pilot with 5 owners before build; add owner approval mode | Pilot adoption < 50% | PM | Open | [Date] |
| RISK-02 | Technical | If double-booking occurs under concurrency, then customers are turned away at the door | 2 | 5 | 10 | Mitigate | Atomic reservation (ADR-0003); concurrency tests TS-0xx | Any production double-booking | Eng Lead | Open | [Date] |
| RISK-03 | Delivery | If one developer is unavailable for 2+ weeks, then R1 slips | 3 | 3 | 9 | Accept | Keep docs current; defer R2 scope | Absence announced | PM | Open | [Date] |

**Categories to consider:** Product/market · Scope · Schedule · Resources · Technical · Integration/third-party · Security · Privacy/legal · Quality · Operational · Financial · Organizational.

## 3. Heat Map Summary

|  | Impact 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **P5** | | | | | |
| **P4** | | | | | |
| **P3** | | | RISK-03 | RISK-01 | |
| **P2** | | | | | RISK-02 |
| **P1** | | | | | |

## 4. Top Risks Reported in the PRD

[List the 3–5 highest-scoring open risks by ID. Keep the PRD's Top Risks table in sync.]

## 5. Issues and Closed Risks

| ID | Outcome | Date | Lesson |
|---|---|---|---|
| RISK-xx | Occurred → became an issue / Retired / Avoided | [Date] | [What we learned] |

## 6. Review Cadence

| When | Who | Focus |
|---|---|---|
| Every [two weeks / milestone] | Core team | Re-score open risks, check triggers, add new ones |
| Before each release | PM + Eng + QA | Release-blocking risks accepted or mitigated |

## Completion Criteria

- [ ] Risks are written in cause → event → impact form, not as vague worries.
- [ ] Every risk has an owner, a score, a response and a trigger or review date.
- [ ] Every High risk has a concrete mitigation or contingency, not just "monitor".
- [ ] Risks cover product, delivery, technical, security/privacy, and third-party categories (or note why not).
- [ ] The PRD's top risks match this register's highest-scoring items.
- [ ] Review dates exist and the last review is recent.
