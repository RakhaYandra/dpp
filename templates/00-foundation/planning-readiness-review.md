---
id: DPP-00-planning-readiness-review
title: Planning Readiness Review (Gate to Implementation)
domain: 00-foundation
tier: mandatory
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, qa-lead, designer, project-manager, security-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [prd, architecture-overview, test-strategy, release-plan, risk-register]
feeds: []
applies_to: [all]
---

# Planning Readiness Review: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | The checkpoint that answers: *Is the planning good enough to start building, and what are we knowingly carrying forward?* It checks completeness, consistency and traceability of the planning documents for the chosen profile, and records the decision to proceed. |
| **When to use** | When the team believes planning is complete, before the first implementation iteration. Repeat a light version before each major release (R2, R3…). |
| **Owner** | Product Manager, with the whole core team reviewing. |
| **Required inputs** | The [Project Manifest](project-manifest.yaml); all documents marked approved or in review for your profile; output of `scripts/check-traceability` and `scripts/validate-metadata`. |
| **Related documents** | [Requirements Traceability Matrix](../03-requirements/requirements-traceability-matrix.md) · [Decision Log](decision-log.md) · [Operational Readiness](../09-release-ops/operational-readiness.md) (the later, release-time gate) |

</details>

> **Guidance:** The goal is **informed commitment, not perfection**. Not-applicable is a valid answer when justified. Unresolved gaps are recorded with an owner and a date, and accepted explicitly by the decision maker. Use the profile you chose in the manifest: *solo* teams complete only the mandatory section and items marked ★.

## 1. Scope of the Review

| | |
|---|---|
| **Product / release** | |
| **Profile** | ☐ Solo ☐ Team ☐ Enterprise |
| **Product types / packages** | |
| **Review date and participants** | |

## 2. Document Status (from the manifest)

| Tier | Document | Status | Comment |
|---|---|---|---|
| Mandatory | Product Brief | | |
| Mandatory | Goals & Metrics | | |
| Mandatory | PRD | | |
| Mandatory | User Stories (all Must FRs) | | |
| Mandatory | Non-Functional Requirements | | |
| Mandatory | Architecture Overview | | |
| Mandatory | Risk Register | | |
| Mandatory | Test Strategy | | |
| Mandatory | Release Plan | | |
| Recommended / optional / package | [as selected in the manifest] | | |

## 3. Readiness Checklist

| # | Area | Check | ★ | Result | Evidence / gap |
|---|---|---|---|---|---|
| 1 | Problem and goals | Problem has evidence; every goal has a measurable metric | ★ | | |
| 2 | Scope | In/out scope explicit; MVP boundary agreed | ★ | | |
| 3 | Requirements | Every Must FR has stories and acceptance criteria | ★ | | |
| 4 | Quality | Measurable NFRs exist for performance, availability, security/privacy, accessibility | ★ | | |
| 5 | Traceability | No undefined or duplicate IDs; Must FRs trace to goals and forward to tests | | | |
| 6 | Design | Key flows and screens for Must stories exist and are reviewed | | | |
| 7 | Architecture | Drivers traced; key ADRs accepted; external dependencies identified | ★ | | |
| 8 | Data and API | Data model and API contract consistent with architecture and rules | | | |
| 9 | Security and privacy | Threat model reviewed; data classified; privacy requirements identified | | | |
| 10 | Test approach | Test strategy agreed; scenarios exist for Must criteria | ★ | | |
| 11 | Delivery plan | Milestones, resources, Definition of Ready/Done agreed | | | |
| 12 | Risks | Top risks have owners and mitigations; open questions have owners and dates | ★ | | |
| 13 | Release and operations | Release approach, rollback idea, monitoring approach outlined | ★ | | |
| 14 | Consistency | Terminology matches glossary; no conflicting requirements across documents | | | |
| 15 | Approvals | Required stakeholders have approved scope | ★ | | |

## 4. Known Gaps Carried Forward

| Gap | Risk if ignored | Owner | Due | Accepted by |
|---|---|---|---|---|

## 5. Decision

☐ **Proceed** · ☐ **Proceed with conditions** (list) · ☐ **Not ready** (list blockers and re-review date)

Decision maker: [Name] · Date: [ ] · Notes: [ ]

Record the decision in the [Decision Log](decision-log.md).

## Completion Criteria

- [ ] Every mandatory document is approved or has a reasoned exception.
- [ ] All ★ items pass or have a recorded, accepted gap.
- [ ] Validation scripts have been run and results attached or summarized.
- [ ] Carried-forward gaps have owners and dates.
- [ ] A decision is recorded and communicated.
