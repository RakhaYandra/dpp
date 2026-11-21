---
id: DPP-06-sprint-planning
title: Sprint / Iteration Planning
domain: 06-project-mgmt
tier: optional
status: draft
version: 0.1.0
owner: project-manager
contributors: [product-manager, engineering-lead, qa-lead, designer]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [user-stories, working-agreements, milestone-plan]
feeds: [test-plan, release-plan]
applies_to: [all]
---

# Sprint / Iteration Plan: [Iteration N]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Captures the goal, scope, capacity and risks of one iteration so the team commits to a realistic amount of work and can review the outcome. Use one copy per iteration, or keep it in your tracker and use this only as the structure. |
| **When to use** | At the start of each iteration (sprint) in iterative delivery. Not needed for strictly sequential projects, or if your tracker already holds all this information. |
| **Owner** | Team, facilitated by the Project Manager or Scrum Master role. |
| **Required inputs** | Prioritized [User Stories](../03-requirements/user-stories.md) meeting the Definition of Ready; [Working Agreements](working-agreements.md); team capacity; [Milestone Plan](milestone-plan.md). |
| **Related documents** | [Test Plan](../07-quality/test-plan.md) · [Release Plan](../09-release-ops/release-plan.md) |

</details>

> **Guidance:** Plan around a **goal**, not a list of tickets. Commit based on historical throughput, not hope. Leave slack for defects and surprises. The plan is a working tool; do not spend longer writing it than the time it saves.

## 1. Iteration Overview

| | |
|---|---|
| **Iteration / dates** | [N] · [start] – [end] |
| **Goal (one sentence)** | [e.g. A customer can book a slot end to end on a phone (US-001–US-004)] |
| **Linked milestone / release** | M4 / R1 |

## 2. Capacity

| Person / role | Available days | Planned focus | Notes |
|---|---|---|---|
| | | | Leave, holidays, meetings |
| **Total capacity** | | **Historic velocity or throughput:** | |

## 3. Committed Scope

| Story | Title | Estimate | Owner | Ready? | Dependencies | NFR / test notes |
|---|---|---|---|---|---|---|
| US-001 | View available slots | 3 | | ✔ | | NFR-001 |
| US-002 | Book a slot | 5 | | ✔ | API-002 | Concurrency test TS-0xx |

**Stretch items (only if capacity remains):** [ ]
**Buffer reserved for defects and unplanned work:** [x%]

## 4. Risks and Blockers

| Item | Mitigation | Owner |
|---|---|---|

## 5. Review and Retrospective (complete at the end)

| Area | Result |
|---|---|
| Goal achieved? | Yes / Partly / No |
| Committed vs completed | |
| Defects found / escaped | |
| What went well | |
| What to improve (one or two concrete actions, with owner) | |
| Changes to backlog, plan or agreements | |

## Completion Criteria

- [ ] The iteration has a single, understandable goal.
- [ ] Every committed story meets the Definition of Ready.
- [ ] Commitment is consistent with capacity and historical throughput.
- [ ] Risks and dependencies are visible.
- [ ] Outcome and improvement actions are recorded at the end.
