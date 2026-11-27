---
id: SLOTWISE-06-project-charter
title: Project Charter
domain: 06-project-mgmt
tier: recommended
status: draft
version: 0.1.0
owner: project-manager
contributors: [product-manager, sponsor, engineering-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [product-brief, goals-and-metrics]
feeds: [milestone-plan, wbs, resource-plan, communication-plan, risk-register, working-agreements]
applies_to: [all]
---

# Project Charter: SlotWise

## 1. Purpose and Objectives

| | |
|---|---|
| **Project purpose** | Deliver a pilot booking service for small salons so owners spend less time on phone bookings and customers receive reminders. Evidence is in the [Product Brief](../01-discovery/product-brief.md) |
| **Objectives** | Release R1 by 2027-03-05 with FR-001 to FR-005 complete; verify MET-01 and MET-02 with three pilot salons; hand over operations with rehearsed rollback and recovery; stay within CON-01 |
| **Linked product goals** | GOAL-01, GOAL-02 |

## 2. Project Scope

| In scope (deliverables) | Out of scope | Interfaces with other projects |
|---|---|---|
| R1 build, test, release to three pilot salons, support handover | Payments and in-app checkout (DEC-001), marketplace listing, multi-location management, FR-006 waiting list (DEC-003), marketing site | DEP-01 messaging provider onboarding; pilot salon scheduling; [Decision Log](../00-foundation/decision-log.md) |

**Deliverables and acceptance:** FR-001 to FR-005 with US-001 to US-005 and AC-001.1 to AC-005.1 demonstrated, TS-001 to TS-010 executed, UAT signed off by the pilot salon owner, and operational readiness review recorded in [Operational Readiness](../09-release-ops/operational-readiness.md).

## 3. Constraints and Assumptions

| ID | Type | Statement |
|---|---|---|
| CON-01 | Constraint | 2 engineers, 1 designer and 14 weeks from 2026-11-30; budget ceiling to be confirmed by the sponsor |
| ASM-01 | Assumption | Customers will accept a booking link instead of calling; tested in the pilot |
| DEP-01 | Dependency | Email and SMS delivery provider chosen in ADR-0002; account and sandbox needed by 2026-12-18 |

## 4. Stakeholders and Governance

| Role | Name | Responsibility | Decision rights |
|---|---|---|---|
| Sponsor | Maya, pilot salon owner (PER-01) | Funds the pilot, accepts the final scope | Approve scope, schedule or budget changes |
| Product Manager | Product manager | Scope, priorities, Q-001 and UAT acceptance | Decide scope within this charter |
| Engineering Lead | Engineering lead | Technical delivery, ADR-0001 and ADR-0002 | Decide technical approach |
| Designer | Designer | Booking and owner-calendar experience | Decide usability details |
| QA Lead | QA lead | Test Strategy gates and release quality evidence | Recommend go or no-go |
| Other stakeholders | Three pilot salons and their customers | Pilot feedback | Consult and inform |

**Decision and escalation rules:** the team decides implementation details, test technique and design variants. Scope changes beyond FR-001 to FR-005, schedule changes beyond the 5-day buffer and any new spend go to the sponsor. Disputes escalate from PM to sponsor within 2 working days. Significant choices are logged in the [Decision Log](../00-foundation/decision-log.md).
**Change control:** request to the PM with impact on FR, US, TS, RISK and the milestone dates; Eng Lead assesses feasibility; sponsor approves changes to scope, schedule or budget; outcome is recorded with a DEC- ID in the Decision Log.

## 5. Summary Plan

| Item | Summary | Detail |
|---|---|---|
| Timeline | Start 2026-11-30, target release 2027-03-05, 90-day review 2027-06-03 | [Milestone Plan](milestone-plan.md) |
| Budget | Ceiling to be confirmed by sponsor, main categories are engineering time, DEP-01 messages and hosting | [OPEN: sponsor, 2026-12-15] |
| Team | 2 engineers, 1 designer, PM and QA lead, under CON-01 | [OPEN: project-manager, 2026-12-15] |
| Top risks | RISK-01, RISK-02 and RISK-04 | [Risk Register](risk-register.md) |

## 6. Success and Closure Criteria

The pilot is complete when R1 is deployed to three salons, UAT is signed off, TS-001 to TS-010 have results recorded, operations handover is accepted, and the 90-day review is scheduled for 2027-06-03. After handover the team moves to R2 planning, which starts with FR-006 per DEC-003. MET-01, MET-02 and MET-03 are pilot targets, not achieved production figures, and are judged at the 90-day review.

## 7. Approval

| Role | Name | Date | Decision |
|---|---|---|---|
| Sponsor | Maya (PER-01) | 2026-12-04 | Pending sign-off on scope and budget |
| Project Manager | Project manager | 2026-11-27 | Draft submitted for approval |

## Completion Criteria

- [x] Purpose and measurable objectives link to product goals.
- [x] Scope boundaries and deliverables are explicit; exclusions are listed.
- [x] Constraints, assumptions, decision rights and change control are defined.
- [x] Time, budget and team are summarized and consistent with the detailed plans.
- [ ] Closure criteria exist and the sponsor has approved.
