---
id: DPP-PKG-enterprise-change-management-and-training
title: Change Management and Training
domain: package-enterprise
tier: package
status: draft
version: 0.1.0
owner: product-manager
contributors: [business-owner, hr-or-training-lead, support-lead, project-manager]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [persona, release-plan, communication-plan]
feeds: [launch-and-support-plan, uat-plan, operational-readiness, post-launch-review]
applies_to: [enterprise]
---

# Change Management and Training: [Product Name]

<details>
<summary><strong>About this template</strong> (delivered once per rollout)</summary>

| | |
|---|---|
| **Purpose** | Plans the **people side** of introducing an internal or enterprise system: who is affected, how their work changes, how they are prepared, and how adoption will be measured and supported. A system that works but is not adopted has failed. |
| **When to use** | For internal business systems and enterprise rollouts that replace or change how people work. Not needed for products people choose voluntarily as consumers. |
| **Owner** | Product Manager with the business owner. |
| **Required inputs** | [Persona](../../templates/01-discovery/persona.md) (roles); [Release Plan](../../templates/09-release-ops/release-plan.md); [Communication Plan](../../templates/06-project-mgmt/communication-plan.md); process maps of current ways of working. |
| **Related documents** | [Launch & Support Plan](../../templates/09-release-ops/launch-and-support-plan.md) · [UAT Plan](../../templates/07-quality/uat-plan.md) · [Post-Launch Review](../../templates/10-analytics/post-launch-review.md) |

</details>

> **Guidance:** Start with **what changes for whom**, then ask what each group needs in order to change (awareness, reason, skill, tools, permission, time). Involve a few **champions** early: they test the product, teach peers and surface resistance honestly. Do not assume training equals adoption; measure behaviour.

## 1. Impact Assessment

| Stakeholder group | Current way of working | What changes | Degree of impact (H/M/L) | Likely concerns | Benefit to them |
|---|---|---|---|---|---|
| Front-desk staff | Paper diary and phone | Enter and manage bookings in the system | High | Slower at first; fear of errors | Fewer calls |
| Managers | Weekly manual report | Real-time view | Medium | | |

## 2. Change Strategy

| Topic | Decision |
|---|---|
| Case for change (the "why") | [Plain-language, in terms of each group's benefits] |
| Sponsor and visible leadership | [Who communicates; what they say and do] |
| Change champions | [Names, roles, time allocation] |
| Rollout approach | [Pilot group → phased waves / big bang; criteria for moving on; link to [Release Plan](../../templates/09-release-ops/release-plan.md)] |
| Parallel running and cut-over | [Duration of old and new processes in parallel; end-date; fallback] |
| Process and policy changes needed | [Updated procedures, responsibilities, approvals] |

## 3. Training Plan

| Audience | Learning objective | Method (workshop, self-paced, floor-walker, job aid) | Duration | Timing | Trainer | Materials | Success check |
|---|---|---|---|---|---|---|---|
| Front desk | Create, move and cancel a booking unaided | Hands-on workshop + quick guide | 90 min | 2 weeks before go-live | | | Practical exercise |

**Materials and environment:** [Sandbox with realistic synthetic data; quick-reference guides; short videos; FAQ.] Update with each release.

## 4. Communication Timeline

| When | Message | Audience | Channel | Owner |
|---|---|---|---|---|
| T–8 weeks | What is changing and why | All affected | | |
| T–2 weeks | What to expect, training schedule | | | |
| T+0 | Go-live and where to get help | | | |
| T+2 weeks | Early results and fixes | | | |

## 5. Support During Transition

| Item | Plan |
|---|---|
| Floor-walkers / hypercare | [Coverage in first weeks] |
| Help channel and response times | |
| Known issues and workaround list | |
| Feedback loop | [Weekly check-in with champions; route to [User Feedback Plan](../../templates/10-analytics/user-feedback-plan.md)] |

## 6. Adoption Measurement

| Measure | Target | Source | Review |
|---|---|---|---|
| Share of eligible users active weekly | | Usage data | |
| Share of bookings made in the system vs old method | | | |
| Training completion | | | |
| Support contacts per user (declining) | | | |
| User confidence/satisfaction | | Survey | |

## 7. Resistance and Risks

| Risk | Early signal | Response |
|---|---|---|
| Users keep using the old method | Low usage after wave 1 | Leader reinforcement; remove old path on a date |

## Completion Criteria

- [ ] Each affected group has a defined impact, concerns and benefits.
- [ ] A rollout approach with cut-over and fallback is agreed with the business owner.
- [ ] Training objectives, methods, timing and success checks exist for every audience.
- [ ] Communication and hypercare support plans are scheduled.
- [ ] Adoption is measured with targets and fed into the post-launch review.
