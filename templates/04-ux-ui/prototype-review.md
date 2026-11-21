---
id: DPP-04-prototype-review
title: Prototype Review
domain: 04-ux-ui
tier: optional
status: draft
version: 0.1.0
owner: designer
contributors: [product-manager, engineering-lead, qa-lead, ux-researcher]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [wireframe-spec, user-flow]
feeds: [user-stories, wireframe-spec, design-system, test-scenarios]
applies_to: [all]
---

# Prototype Review: [Prototype / Version]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Records a structured review of a prototype by stakeholders and users: what was reviewed, how, what was found, and what will change. Use one copy per review round. |
| **When to use** | Before development of a flow or feature, whenever a clickable or realistic prototype exists. Skip for trivial screens. |
| **Owner** | UX Designer. |
| **Required inputs** | A prototype link; [Wireframe Spec](wireframe-spec.md); [User Flow](user-flow.md); target tasks from [User Stories](../03-requirements/user-stories.md). |
| **Related documents** | [User Research](../01-discovery/user-research.md) (usability study method) · [Design System](design-system.md) · [Accessibility & Responsive](accessibility-and-responsive.md) |

</details>

> **Guidance:** Review with **tasks**, not opinions: "Book a Saturday haircut" tells you more than "What do you think?". Separate **stakeholder review** (alignment) from **user testing** (usability). Record severity and a decision for each finding so feedback does not disappear.

## 1. Review Details

| | |
|---|---|
| **Prototype / version / link** | |
| **Fidelity and scope** | [Low/high; flows covered: UF-01] |
| **Review type** | ☐ Stakeholder ☐ Moderated user test ☐ Unmoderated test ☐ Heuristic / expert review ☐ Accessibility review |
| **Date, participants** | [Roles/IDs; number] |
| **Questions to answer** | [Hypotheses: e.g. users find the slot picker without help] |

## 2. Tasks and Success Criteria

| Task | Success criterion | Result (success / difficulty / fail) | Time | Notes |
|---|---|---|---|---|
| Book a Saturday appointment | Completes unaided in ≤ 90 s | 7/8 succeeded | 62 s median | One missed the date picker |

## 3. Findings

| ID | Finding | Evidence | Severity (Critical / Major / Minor / Idea) | Screen / flow | Decision | Owner |
|---|---|---|---|---|---|---|
| PR-01 | Date picker not noticed on small screens | 3/8 hesitated | Major | S-02 | Change: move above services | Designer |

Severity guide: **Critical** blocks task completion · **Major** causes significant difficulty · **Minor** causes slight friction · **Idea** is an improvement suggestion.

## 4. Heuristic / Accessibility Checks (optional)

| Check | Pass? | Notes |
|---|---|---|
| Visibility of system status | | |
| Error prevention and recovery | | |
| Consistency with design system | | |
| Keyboard and screen-reader path for key flow | | |

## 5. Outcome and Follow-Up

**Decision:** ☐ Proceed to build ☐ Proceed with changes ☐ Re-test after changes ☐ Rework flow

| Follow-up action | Updates (documents / stories) | Owner | Due |
|---|---|---|---|

## Completion Criteria

- [ ] Scope, participants and questions are stated.
- [ ] Tasks have measurable success criteria and recorded results.
- [ ] Every finding has severity, a decision and an owner.
- [ ] Critical and Major findings lead to updates in the wireframe spec, flows or stories.
- [ ] A go / rework decision is recorded.
