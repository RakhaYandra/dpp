---
id: SLOTWISE-06-working-agreements
title: Working Agreements (Definition of Ready and Definition of Done)
domain: 06-project-mgmt
tier: recommended
status: draft
version: 0.1.0
owner: project-manager
contributors: [product-manager, engineering-lead, qa-lead, designer]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [test-strategy, project-charter]
feeds: [user-stories, sprint-planning, test-plan, release-plan]
applies_to: [all]
---

# Working Agreements: SlotWise Team

## 1. Definition of Ready (a story may enter an iteration when…)

- [ ] It has an ID from US-001 to US-005, a linked requirement from FR-001 to FR-005 and a persona, PER-01 or PER-02.
- [ ] Acceptance criteria from AC-001.1 to AC-005.1 are written, testable and agreed with the PM.
- [ ] Applicable business rules BR-001 to BR-006 and NFR-001 to NFR-005 are referenced where they affect the story.
- [ ] A flow or screen reference exists where the story has UI, from the agreed user flow and information architecture.
- [ ] Dependencies are identified: ASM-01 for customer acceptance of the link, DEP-01 for messages; none block the iteration.
- [ ] The team has estimated it and it fits in a 2-week iteration under CON-01.
- [ ] Open questions that affect the story are answered, including Q-001 for reminder timing.

## 2. Definition of Done (a story is done when…)

**Story level**
- [ ] All acceptance criteria are met and demonstrated against TS-001 to TS-010 as applicable.
- [ ] Code, design or content is reviewed by the other engineer or the designer; with a team this small, self-review against the checklist after a half-day pause is allowed when the author is the only reviewer available.
- [ ] Automated tests required by the [Test Strategy](../07-quality/test-strategy.md) are written and passing, including TC-001 to TC-010 where applicable.
- [ ] No open Critical or High defects attached to the story.
- [ ] Applicable NFR checks are done: NFR-001 and NFR-003 for booking, NFR-004 for deletion, NFR-005 for accessibility.
- [ ] Analytics events EVT-001 to EVT-003 in the [Event Tracking Plan](../10-analytics/event-tracking-plan.md) are implemented and verified where the story touches the funnel.
- [ ] Documentation affected by the change is updated: API spec, data model, security requirements or help text.
- [ ] The change is deployable to the test environment.

**Release level**
- [ ] Release Plan go/no-go criteria met; rollback rehearsed per the [Deployment Plan](../09-release-ops/deployment-plan.md).
- [ ] Release notes written; the three pilot salons informed.

## 3. Working Practices

| Topic | Agreement |
|---|---|
| Iteration length and rhythm | 2 weeks, starting 2026-11-30; planning on Mondays, review and retrospective every second Friday, first on 2026-12-11 |
| Daily communication | Async stand-up by 10:00 UTC with blockers in the team channel; 15-minute call only for a SEV1 or SEV2 incident |
| Branching and review rules | Short-lived branches from the main line, one pull request per story, at least one reviewer, no direct commits to the release branch |
| Handling urgent work | Only SEV1 and SEV2 from the [Incident Management Plan](../09-release-ops/incident-management.md) may interrupt an iteration; PM records the scope trade-off |
| Definition of a blocker and escalation | No progress for 4 working hours is a blocker: engineer to Eng Lead, Eng Lead to PM the same day |
| Decision-making | PM owns scope and priority, Eng Lead owns technical approach, designer owns interaction detail; unresolved disputes go to the sponsor within 2 working days |
| Working hours, availability, time zones | Core hours 09:00 to 15:00 UTC, two engineers and one designer under CON-01; on-call follows the incident plan |

## 4. Review and Change

| Date | Change | Reason | Agreed by |
|---|---|---|---|
| 2026-11-27 | Initial agreements recorded | Project kickoff for the 14-week R1 plan | PM, Eng Lead, designer, QA lead |

A retrospective every second Friday reviews these agreements; the first review is 2026-12-11 and any change is recorded in this table.

## Completion Criteria

- [x] Ready and Done lists are short, checkable and match the Test Strategy.
- [x] Both lists are agreed by everyone who uses them.
- [x] Practices cover communication, escalation and urgent work.
- [x] A review moment (retrospective) is scheduled.
