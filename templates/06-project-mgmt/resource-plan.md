---
id: DPP-06-resource-plan
title: Resource Plan
domain: 06-project-mgmt
tier: optional
status: draft
version: 0.1.0
owner: project-manager
contributors: [product-manager, engineering-lead, finance]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [project-charter, wbs]
feeds: [milestone-plan, risk-register, communication-plan]
applies_to: [all]
---

# Resource Plan: [Project Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Plans the people, skills, tools and money the project needs, when it needs them, and what happens if they are not available. |
| **When to use** | When the project involves more than one person, external vendors, or a budget that must be approved. Solo projects can capture this in the Charter. |
| **Owner** | Project Manager. |
| **Required inputs** | [Project Charter](project-charter.md) constraints; [WBS](wbs.md) estimates; [Technology Stack](../05-architecture/technology-stack.md) (tools, licences); [Infrastructure & Scalability](../05-architecture/infrastructure-and-scalability.md) (running costs). |
| **Related documents** | [Milestone Plan](milestone-plan.md) · [Risk Register](risk-register.md) · [Communication Plan](communication-plan.md) |

</details>

> **Guidance:** Plan **skills over names**. Highlight the **single points of failure** (skills held by one person). Budget **running costs** (hosting, messaging, licences, support) as well as build costs. Never include personal data such as salaries in a shared repository; use roles and cost bands.

## 1. Roles and Skills Needed

| Role / skill | Needed for | Level of effort (FTE or days) | When | Source (internal / contractor / vendor) | Named person |
|---|---|---|---|---|---|
| Product management | Scope, priorities | 0.5 FTE | Whole project | Internal | |
| Front-end development | M2–M4 | 1.0 | | | |
| QA | M4–M5 | 0.5 | | | |

## 2. Skill Gaps and Single Points of Failure

| Skill | Held by | Gap / risk | Plan (train, hire, document, contract) |
|---|---|---|---|

## 3. Tools, Environments and Licences

| Item | Purpose | Cost model | Owner | Needed by |
|---|---|---|---|---|

## 4. Budget

| Category | Build phase | Run (monthly) | Basis | Contingency |
|---|---|---|---|---|
| People (bands) | | | | |
| Infrastructure | | | | |
| Third-party services | | | | |
| Tools and licences | | | | |
| Other (legal, accessibility audit, security testing, marketing) | | | | |
| **Total** | | | | |

## 5. Availability and Allocation

[Calendar constraints, shared resources, onboarding time, holiday periods; link to [Milestone Plan](milestone-plan.md).]

## 6. Risks and Contingency

| Risk | Mitigation | RISK- ID |
|---|---|---|

## Completion Criteria

- [ ] Roles, skills, effort and timing are consistent with the WBS and Milestone Plan.
- [ ] Skill gaps and single points of failure have a plan.
- [ ] Budget covers build and running costs, with stated basis and contingency.
- [ ] Tools and licences are identified with owners and dates.
- [ ] No personal or sensitive financial data is stored in the repository.
