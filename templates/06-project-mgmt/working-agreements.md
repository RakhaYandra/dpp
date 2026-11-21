---
id: DPP-06-working-agreements
title: Working Agreements (Definition of Ready and Definition of Done)
domain: 06-project-mgmt
tier: recommended
status: draft
version: 0.1.0
owner: project-manager
contributors: [product-manager, engineering-lead, qa-lead, designer]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [test-strategy, project-charter]
feeds: [user-stories, sprint-planning, test-plan, release-plan]
applies_to: [all]
---

# Working Agreements: [Team / Project Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Records how the team agrees to work: the **Definition of Ready** (when work may start), the **Definition of Done** (when work counts as finished) and the practices around them. One short document replaces separate DoR and DoD files. |
| **When to use** | Before the first iteration; revisit in retrospectives. Valuable for solo developers too, as a self-discipline checklist. |
| **Owner** | The team, facilitated by the Project Manager. |
| **Required inputs** | [Test Strategy](../07-quality/test-strategy.md) quality gates; [Non-Functional Requirements](../03-requirements/non-functional-requirements.md); team experience. |
| **Related documents** | [User Stories](../03-requirements/user-stories.md) · [Sprint Planning](sprint-planning.md) · [Release Plan](../09-release-ops/release-plan.md) |

</details>

> **Guidance:** Keep each list to **what is true for every item** (6–10 points). Make every point **checkable**. Agreements are owned by the team and change by team decision, not by decree. A Definition of Done that nobody applies is worse than none: remove points you do not enforce.

## 1. Definition of Ready (a story may enter an iteration when…)

- [ ] It has an ID, a linked requirement (FR-) and a persona.
- [ ] Acceptance criteria are written, testable and agreed with the PM.
- [ ] Applicable business rules (BR-) and NFRs are referenced.
- [ ] Design or flow reference exists where the story has UI.
- [ ] Dependencies are identified and not blocking.
- [ ] The team has estimated it and it fits in one iteration.
- [ ] Open questions that affect the story are answered.

## 2. Definition of Done (a story is done when…)

**Story level**
- [ ] All acceptance criteria are met and demonstrated.
- [ ] Code (or content/design) is reviewed by another person (solo: self-review against a checklist after a pause).
- [ ] Automated tests required by the [Test Strategy](../07-quality/test-strategy.md) are written and passing.
- [ ] No open Critical or High defects attached to the story.
- [ ] Applicable NFR checks are done (performance, accessibility, security).
- [ ] Analytics events in the [Event Tracking Plan](../10-analytics/event-tracking-plan.md) are implemented and verified.
- [ ] Documentation affected by the change is updated (API spec, data model, help content).
- [ ] The change is deployable to a test environment.

**Release level**
- [ ] Release Plan go/no-go criteria met; rollback verified.
- [ ] Release notes written; support informed.

## 3. Working Practices

| Topic | Agreement |
|---|---|
| Iteration length and rhythm | [e.g. 2 weeks; planning, review, retrospective] |
| Daily communication | [Stand-up format / async update] |
| Branching and review rules | [Principles; tool-neutral] |
| Handling urgent work | [Rules for interrupting the iteration] |
| Definition of a blocker and escalation | [After N hours → whom] |
| Decision-making | [Who decides what; how disagreements resolve] |
| Working hours, availability, time zones | |

## 4. Review and Change

| Date | Change | Reason | Agreed by |
|---|---|---|---|

## Completion Criteria

- [ ] Ready and Done lists are short, checkable and match the Test Strategy.
- [ ] Both lists are agreed by everyone who uses them.
- [ ] Practices cover communication, escalation and urgent work.
- [ ] A review moment (retrospective) is scheduled.
