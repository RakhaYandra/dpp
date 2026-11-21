---
id: DPP-01-product-brief
title: Product Brief
domain: 01-discovery
tier: mandatory
status: draft
version: 0.1.0
owner: product-manager
contributors: []
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: []
feeds: [goals-and-metrics, prd, persona, vision-and-value-proposition, project-charter]
applies_to: [all]
---

# Product Brief: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | A one- to two-page statement of the problem, the people who have it, the proposed direction and why it is worth pursuing. It is the starting point for everything else and the document to show someone who asks "what is this?". It also contains the problem statement; there is no separate file. |
| **When to use** | First. Before requirements, design or architecture. Revisit when research invalidates an assumption. |
| **Owner** | Product Manager or founder. |
| **Required inputs** | An idea, a first conversation with a few potential users, and whatever evidence already exists (support requests, observed workarounds, internal data). Not required: a finished market study. |
| **Related documents** | [Goals & Metrics](../02-strategy/goals-and-metrics.md) · [PRD](../03-requirements/prd.md) · [Persona](persona.md) · [Assumption Map](assumption-map.md) · [Opportunity Assessment](opportunity-assessment.md) |

</details>

> **Guidance:** Be specific and brief. A brief that could describe any product has said nothing. If you cannot fill a section with evidence, write "Unknown" and list how you will find out. Unknowns feed the Assumption Map.

## 1. Summary

[Three sentences: who the product is for, what problem it solves, and the approach.]

> *Example:* SlotWise is booking software for solo and small service businesses (salons, tutors, studios) who currently take appointments by phone and chat. It lets their customers self-book and automatically confirms and reminds them, so owners spend less time scheduling and lose fewer sessions to no-shows.

## 2. Problem Statement

> **Guidance:** Describe the problem, not the solution. Use the pattern: *[Who] struggles to [do what] because [cause], which results in [consequence].* Include at least one piece of evidence.

| | |
|---|---|
| **Who has the problem** | [Specific group, not "everyone"] |
| **The problem** | [What they cannot do, or do badly] |
| **Root cause** | [Why it happens, if known] |
| **Consequence** | [Cost in time, money, risk or frustration] |
| **Current workaround** | [What they do today and what is wrong with it] |
| **Evidence** | [Interviews, data, observation; with counts and dates. Mark "Unverified" if none yet] |
| **Frequency and severity** | [How often and how painful] |

## 3. Target Users

| Segment | Description | Size or reach (if known) | Priority |
|---|---|---|---|
| [Primary] | [Role, context, key trait] | [Estimate and source] | Primary |
| [Secondary] | | | Secondary |

Detailed personas belong in [Persona](persona.md).

## 4. Proposed Direction

- **Approach:** [How you intend to solve it, in a few sentences, without feature lists]
- **Why this approach:** [Alternatives considered and why they were set aside]
- **Differentiation:** [What is meaningfully different from current alternatives; detail in [Competitor Analysis](competitor-analysis.md)]
- **Product type:** [web app / mobile / SaaS / API platform / enterprise / internal system / developer tool / other] — determines the optional packages you will need.

## 5. Value and Feasibility Snapshot

| Dimension | Assessment | Confidence (H/M/L) | Basis |
|---|---|---|---|
| User value | [Why users would switch or adopt] | | |
| Business value | [Revenue, savings, strategic benefit] | | |
| Feasibility | [Can we build and run it with the available skills and time?] | | |
| Viability | [Can it be sustained legally, financially, operationally?] | | |

## 6. Key Assumptions and Unknowns

> **Guidance:** List the beliefs that, if wrong, would sink the idea. Keep the top 3–5 here; maintain the full list in the [Assumption Map](assumption-map.md).

| ID | Assumption | If wrong… | How to test |
|---|---|---|---|
| ASM-01 | [e.g. Owners will let customers self-book rather than insisting on confirming each request] | [Core flow fails] | [Interview 10 owners; pilot with 5] |

## 7. Constraints and Boundaries

- **Time / budget / team:** [Known limits]
- **Non-negotiables:** [Legal, platform, brand, integration constraints]
- **Explicitly not this product:** [Boundary statements]

## 8. Recommendation and Next Steps

- **Recommendation:** ☐ Proceed to define · ☐ Validate further first · ☐ Stop
- **Next steps:** [Specific actions, owners, dates; e.g. "Complete 10 interviews by [date] → update Persona and Assumption Map"]

## Completion Criteria

- [ ] The problem is stated without describing a solution, with at least one piece of evidence or a plan to obtain it.
- [ ] A specific primary user group is named.
- [ ] The approach and its rationale fit in a few sentences.
- [ ] Product type is stated, so product-specific packages can be selected.
- [ ] Top assumptions are listed with a way to test each.
- [ ] A clear recommendation and next step exist.
- [ ] A newcomer can explain the product after reading it for two minutes.
