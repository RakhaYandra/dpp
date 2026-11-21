---
id: DPP-01-assumption-map
title: Assumption Map
domain: 01-discovery
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, designer]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [product-brief]
feeds: [user-research, prd, risk-register, mvp-and-prioritization, roadmap]
applies_to: [all]
---

# Assumption Map: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Makes the beliefs your plan depends on explicit, ranks them by risk, and defines the cheapest way to test the riskiest ones before heavy investment. Canonical home for `ASM-` IDs. |
| **When to use** | After the Product Brief; update after each research cycle and before committing to the MVP. |
| **Owner** | Product Manager, with Engineering and Design contributing technical and usability assumptions. |
| **Required inputs** | [Product Brief](product-brief.md) (its top assumptions); any early research. |
| **Related documents** | [User Research](user-research.md) · [Risk Register](../06-project-mgmt/risk-register.md) · [MVP & Prioritization](../02-strategy/mvp-and-prioritization.md) |

</details>

> **Guidance:** An assumption is something you believe but have not verified. Sweep four categories: **Desirability** (do people want this?), **Viability** (can it work as a business?), **Feasibility** (can we build and operate it?), **Usability** (can they use it?). Write each as a **testable statement**, not a hope.

## 1. Assumption Register

| ID | Category | Assumption (testable statement) | Impact if wrong (1–5) | Evidence today (1 none – 5 strong) | Risk rank | Status |
|---|---|---|---|---|---|---|
| ASM-01 | Desirability | At least 6 of 10 solo owners will let customers self-book without approving each booking | 5 | 1 | High | Unvalidated |
| ASM-02 | Viability | Owners will pay at least [amount]/month for reminders | 5 | 2 | High | Unvalidated |
| ASM-03 | Feasibility | Messaging delivery costs stay below [x]% of subscription price | 3 | 2 | Medium | Unvalidated |
| ASM-04 | Usability | A new owner can publish a booking page in under 30 minutes unaided | 4 | 1 | High | Unvalidated |

**Risk rank:** High when impact ≥ 4 and evidence ≤ 2; Medium when one is borderline; Low otherwise. Status: *Unvalidated · Testing · Validated · Invalidated · Retired*.

## 2. Priority Grid

|  | **Little evidence** | **Strong evidence** |
|---|---|---|
| **High impact** | **Test first**: ASM-01, ASM-02, ASM-04 | Monitor |
| **Low impact** | Test if cheap | Ignore |

## 3. Test Plan (for High-risk assumptions)

| ID | Experiment | Success criterion (set *before* testing) | Cost / effort | Owner | Due | Result |
|---|---|---|---|---|---|---|
| ASM-01 | Interview 10 owners with a paper prototype of the booking page | ≥ 6 accept self-booking | 2 days | PM | [Date] | |
| ASM-02 | Pre-launch page with price; count sign-ups | ≥ 20 sign-ups at stated price | 3 days | Founder | [Date] | |

Cheap test options: interviews, prototypes, landing page tests, concierge/manual service, data analysis, technical spike.

## 4. Outcomes and Decisions

| ASM | Result | Decision (persevere / pivot / stop / re-test) | Documents updated |
|---|---|---|---|

Link invalidated assumptions to decisions in the [Decision Log](../00-foundation/decision-log.md) and remaining high-risk ones to the [Risk Register](../06-project-mgmt/risk-register.md).

## Completion Criteria

- [ ] Assumptions span desirability, viability, feasibility and usability.
- [ ] Each is a testable statement with impact and evidence ratings.
- [ ] Every High-risk assumption has an experiment with a success criterion set in advance.
- [ ] Results update status and trigger documented decisions.
- [ ] Unresolved High-risk assumptions appear in the Risk Register.
