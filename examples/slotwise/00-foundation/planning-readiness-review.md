---
id: SLOTWISE-planning-readiness-review
title: Planning Readiness Review (Gate to Implementation): SlotWise
domain: 00-foundation
tier: mandatory
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, qa-lead, designer, project-manager, security-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [prd, architecture-overview, test-strategy, release-plan, risk-register]
feeds: []
applies_to: [saas]
---

# Planning Readiness Review: SlotWise

## 1. Scope of the Review

| | |
|---|---|
| **Product / release** | SlotWise R1, the pilot release with FR-001 to FR-005 |
| **Profile** | ☐ Solo ☑ Team ☐ Enterprise |
| **Product types / packages** | SaaS, packages [saas] |
| **Review date and participants** | 2026-11-27, product manager, engineering lead, QA lead, designer, project manager, security lead |

## 2. Document Status (from the manifest)

| Tier | Document | Status | Comment |
|---|---|---|---|
| Mandatory | Product Brief | approved | Problem and evidence from 24 owner interviews |
| Mandatory | Goals & Metrics | approved | GOAL-01 and GOAL-02 with MET-01 to MET-03 |
| Mandatory | PRD | approved | FR-001 to FR-006, Q-001 open with owner |
| Mandatory | User Stories (all Must FRs) | approved | US-001 to US-005, AC-001.1 to AC-005.1 |
| Mandatory | Non-Functional Requirements | approved | NFR-001 to NFR-005 |
| Mandatory | Architecture Overview | approved | ADR-0001 and ADR-0002 accepted |
| Mandatory | Risk Register | approved | RISK-01 to RISK-04, each with owner and mitigation |
| Mandatory | Test Strategy | draft | Approval needed from QA lead, see carried-forward gap on quality |
| Mandatory | Release Plan | approved | Rollout and rollback defined for R1 |
| Recommended / optional / package | Discovery and strategy set: assumption-map, competitor-analysis, persona, user-research, business-model, mvp-and-prioritization, roadmap, vision-and-value-proposition | draft | Drafted 2026-11-27, approval pending |
| Recommended / optional / package | Requirements and design set: business-rules, requirements-traceability-matrix, glossary, accessibility-and-responsive, design-system, information-architecture, ui-design, user-flow, wireframe-spec | draft | Drafted 2026-11-27, approval pending |
| Recommended / optional / package | Architecture, security, delivery, quality, ops and analytics sets, plus adr and the [SaaS package](../packages/saas/subscription-and-billing.md) | draft | Drafted 2026-11-27, approval pending |

## 3. Readiness Checklist

| # | Area | Check | ★ | Result | Evidence / gap |
|---|---|---|---|---|---|
| 1 | Problem and goals | Problem has evidence; every goal has a measurable metric | ★ | Pass | Product Brief survey of 24 owners; MET-01 to MET-03 in Goals and Metrics |
| 2 | Scope | In/out scope explicit; MVP boundary agreed | ★ | Pass | PRD non-goals; DEC-001 and DEC-003; MVP document draft |
| 3 | Requirements | Every Must FR has stories and acceptance criteria | ★ | Pass | FR-001 to FR-004 trace to US-001 to US-004 and AC-001.1 to AC-004.2 in the RTM |
| 4 | Quality | Measurable NFRs exist for performance, availability, security/privacy, accessibility | ★ | Gap, accepted | NFR-001 to NFR-005 measurable; NFR-004 covers privacy; security detail is draft in security-requirements, see carried-forward gap on quality |
| 5 | Traceability | No undefined or duplicate IDs; Must FRs trace to goals and forward to tests | | Pass | RTM covers FR-001 to FR-006, NFR-001 to NFR-005 and MET-01 to MET-03 |
| 6 | Design | Key flows and screens for Must stories exist and are reviewed | | Gap | Flows UF-01 to UF-03 and screens S-01 to S-04 are draft, see carried-forward gap on design |
| 7 | Architecture | Drivers traced; key ADRs accepted; external dependencies identified | ★ | Pass | ADR-0001 and ADR-0002 accepted in Architecture Overview; DEP-01 open with engineering lead |
| 8 | Data and API | Data model and API contract consistent with architecture and rules | | Gap | Data model and API specification are draft, see carried-forward gap on data |
| 9 | Security and privacy | Threat model reviewed; data classified; privacy requirements identified | | Gap | Threat model, data classification and privacy requirements are draft, see carried-forward gap on quality |
| 10 | Test approach | Test strategy agreed; scenarios exist for Must criteria | ★ | Gap, accepted | TS-001 to TS-010 cover every Must AC and NFR; test strategy approval is part of the quality gap |
| 11 | Delivery plan | Milestones, resources, Definition of Ready/Done agreed | | Pass | CON-01 fixes 2 engineers, 1 designer and 14 weeks; Release Plan rollout; working agreements draft |
| 12 | Risks | Top risks have owners and mitigations; open questions have owners and dates | ★ | Pass | RISK-01 to RISK-04 owned; Q-001 owned by product with pilot week 6 due date |
| 13 | Release and operations | Release approach, rollback idea, monitoring approach outlined | ★ | Pass | Release Plan rollback triggers at 1% failed messages or double bookings; monitoring design draft |
| 14 | Consistency | Terminology matches glossary; no conflicting requirements across documents | | Pass | Glossary terms booking, slot, cutoff, no-show match PRD and stories |
| 15 | Approvals | Required stakeholders have approved scope | ★ | Gap | 10 scaffold documents plus README are approved; new documents are draft, see carried-forward gap on approvals |

## 4. Known Gaps Carried Forward

| Gap | Risk if ignored | Owner | Due | Accepted by |
|---|---|---|---|---|
| UX flows and screens remain draft | Owner onboarding may exceed the 30 minute target (ASM-04) | designer | 2026-12-15 | product-manager, conditionally |
| Data model and API contract remain draft | Rules BR-001 to BR-006 may be implemented inconsistently | engineering-lead | 2026-12-15 | product-manager, conditionally |
| Test strategy, security and privacy documents remain draft | Privacy and security checks for NFR-004 may be missed | security-lead and qa-lead | 2026-12-15 | product-manager, conditionally |
| New documents are not yet approved | Scope could drift during implementation | product-manager | 2026-12-15 | product-manager, conditionally |
| DEP-01 provider not selected | Reminder delivery risk RISK-02 stays open | engineering-lead | 2026-12-15 | product-manager, conditionally |
| Q-001 reminder timing unresolved | MET-01 may not reach 10% | product | Pilot week 6 | product-manager, conditionally |

Validation run on 2026-11-27: `validate-metadata` reported 0 errors and 0 warnings; `check-links` reported no broken links; `check-traceability` warnings are the open IDs tracked above and are owned by the agents completing those documents.

## 5. Decision

☑ **Proceed with conditions** · ☐ **Proceed** · ☐ **Not ready**

Conditions: the carried-forward gaps are closed by 2026-12-15, and the ★ items marked Gap, accepted stay within their recorded owner and due date.

Decision maker: product-manager · Date: 2026-11-27 · Notes: R1 scope stays at FR-001 to FR-005 under CON-01; FR-006 remains in R2 per DEC-003.

Record the decision in the [Decision Log](decision-log.md).

## Completion Criteria

- [ ] Every mandatory document is approved or has a reasoned exception.
- [x] All ★ items pass or have a recorded, accepted gap.
- [x] Validation scripts have been run and results attached or summarized.
- [x] Carried-forward gaps have owners and dates.
- [ ] A decision is recorded and communicated.
