---
id: SLOTWISE-04-prototype-review
title: Prototype Review: SlotWise Booking v0.1
domain: 04-ux-ui
tier: optional
status: draft
version: 0.1.0
owner: designer
contributors: [product-manager, engineering-lead, qa-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [ui-design, wireframe-spec, user-flow]
feeds: [user-stories, wireframe-spec, design-system, test-scenarios]
applies_to: [saas]
---

# Prototype Review: SlotWise Booking v0.1

## 1. Review Details

| | |
|---|---|
| **Prototype / version / link** | `ui-prototype.html`, v0.1, clickable starter |
| **UI design reference** | S-01 to S-03 in [UI Design](ui-design.md), section 2 |
| **Fidelity and scope** | Low to medium fidelity, flow UF-01 |
| **Review type** | ☑ Stakeholder ☐ Moderated user test ☐ Unmoderated test ☑ Heuristic / expert review ☑ Accessibility review |
| **Date, participants** | 2026-11-27, PER-01 salon owner, PER-02 customer, designer, engineering lead. Internal review, not a user study |
| **Questions to answer** | Can a customer find an open slot and submit the form without an account? Do the empty, slot-taken and error states say what to do next? Is the manage link explained clearly? |

## 2. Tasks and Success Criteria

| Task | Success criterion | Result (success / difficulty / fail) | Time | Notes |
|---|---|---|---|---|
| Pick a service and open the slot list | Reaches S-01 without help | Success | Not timed | Internal walkthrough, not a timed study |
| Choose a slot and open S-02 | Selected slot and duration are visible | Success | Not timed | Slot-taken state also checked |
| Submit the form on S-03 | Empty name shows validation, filled name shows success | Success | Not timed | Both paths checked |
| Try the empty and error states | Message names the cause and the next action | Difficulty | Not timed | Empty copy was too generic on first run |

## 3. Findings

| ID | Finding | Evidence | Severity (Critical / Major / Minor / Idea) | Screen / flow | Decision | Owner |
|---|---|---|---|---|---|---|
| PR-01 | Empty state did not say what to do next | Reviewer paused on the first run | Major | S-01, UF-01 | Change: "Belum ada slot tersedia. Pilih tanggal lain." | Designer |
| PR-02 | Slot-taken path needed an explicit alternative | Reviewer asked where to go after the failure | Major | S-02, UF-01 | Change: keep the nearest alternatives in the error copy | Designer |
| PR-03 | Confirmation copy did not explain the manage link | Two reviewers asked how long the link stays valid | Minor | S-04, UF-02 | Change: state that the link is private and time limited | Product manager |
| PR-04 | Focus ring was hard to see in the light theme | Heuristic check on the state buttons | Minor | S-01 | Change: raise the border contrast token | Designer |

Severity guide: **Critical** blocks task completion · **Major** causes significant difficulty · **Minor** causes slight friction · **Idea** is an improvement suggestion.

## 4. Heuristic / Accessibility Checks

| Check | Pass? | Notes |
|---|---|---|
| Visibility of system status | Pass | State switches are announced with `role="status"` |
| Error prevention and recovery | Pass after PR-01 and PR-02 | Errors name the cause and the next action |
| Consistency with design system | Pass | One accent, native controls, system type stack |
| Keyboard and screen-reader path for key flow | Partial | Keyboard and focus passes done. Full screen reader pass is scheduled in UAT |

## 5. Outcome and Follow-Up

**Decision:** ☐ Proceed to build ☑ Proceed with changes ☐ Re-test after changes ☐ Rework flow

| Follow-up action | Updates (documents / stories) | Owner | Due |
|---|---|---|---|
| Rewrite empty and slot-taken copy | `ui-design.md` section 3, `wireframe-spec.md` M-20 and M-21 | Designer | 2026-12-01 |
| Explain the manage link | `ui-design.md` S-04 | Product manager | 2026-12-01 |
| Run the screen reader pass | `uat-plan.md` | QA lead | 2026-12-08 |
| Recheck the focus token | `design-system.md` | Designer | 2026-12-01 |

## Completion Criteria

- [x] Scope, participants and questions are stated.
- [x] Tasks have measurable success criteria and recorded results.
- [x] Every finding has severity, a decision and an owner.
- [x] Critical and Major findings lead to updates in the UI design, wireframe spec, flows or stories.
- [x] A go / rework decision is recorded.
