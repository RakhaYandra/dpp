---
id: SLOTWISE-04-accessibility-and-responsive
title: Accessibility and Responsive Design Guidelines
domain: 04-ux-ui
tier: recommended
status: draft
version: 0.1.0
owner: designer
contributors: [engineering-lead, qa-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [non-functional-requirements]
feeds: [design-system, wireframe-spec, test-strategy, prototype-review]
applies_to: [all]
---

# Accessibility and Responsive Design Guidelines: SlotWise

## 1. Targets

| Item | Target | Source |
|---|---|---|
| Accessibility standard and level | WCAG 2.2 Level AA, used as the team checklist | NFR-005 |
| Scope | Booking web app, screens S-01 to S-04, and the owner area | FR-001, FR-002, FR-003, FR-004, FR-005 |
| Out of scope and why | Native mobile apps and third-party message clients, neither is in R1 | PRD non-goals |
| Legal / contractual obligations | [OPEN: owner, 2026-12-15] after review by qualified advice | [OPEN: owner, 2026-12-15] |

## 2. Accessibility Rules

| Area | Rule | Applies to | Verified by |
|---|---|---|---|
| Perceivable: text alternatives | Decorative shapes carry no text; every control has a text label, so no image alternative is needed in R1 | All screens | Design review and TS-007 |
| Perceivable: contrast and colour | Body text at least 4.5:1, large text at least 3:1, control borders at least 3:1; colour never carries status alone | All screens | Design review with the contrast values in the Design System |
| Perceivable: text resize and reflow | Usable at 200% zoom with no horizontal page scroll; slot table scrolls inside its own panel | Booking web app | Manual test at 200% zoom, TS-007 |
| Operable: keyboard | Skip link, native controls, visual order matches focus order, 3 px visible focus outline | All screens | Keyboard-only walkthrough, TS-007 |
| Operable: targets and timing | Buttons at least 44 px high; no session time limit on the guest booking flow | Forms and slot list | Review and TS-007 |
| Understandable: forms | Visible labels, inline errors with a suggested fix, first error focused, data kept after failure | S-03 confirmation form | Manual test, TS-007 |
| Understandable: language | Prototype declares lang="id" because customer copy is in Bahasa Indonesia; planning documents are in English | Prototype and docs | Review |
| Robust: semantics | Native buttons, selects, inputs and tables with scope on headers; feedback uses role status or role alert | All screens | Screen-reader pass, TS-007 |
| Motion and media | Hover and focus background changes only, no animation or loop; no media in R1 | All screens | Code review of `ui-prototype.html` |

## 3. Responsive Design Rules

| Item | Decision |
|---|---|
| Approach | Mobile first, because PER-02 books on a phone and PER-01 works between clients |
| Breakpoints | compact: below 640 px; expanded: 640 px and above |
| Layout behaviour | Single column in compact, wider panel with the same region order in expanded; slot table scrolling inside its panel at both widths |
| Touch vs pointer vs keyboard | All actions are native buttons and links, reachable by touch, pointer and keyboard; hover is never the only way to reveal content |
| Orientation and zoom | Portrait and landscape supported; zoom is not blocked; 200% zoom keeps controls reachable |
| Content adaptation | Long service or staff labels wrap and do not truncate; slot table scrolls horizontally inside its panel rather than off screen |
| Performance on small devices | No external fonts, images or scripts; slot lookup target under 800 ms at 50 concurrent users (NFR-001, TS-005) |
| Supported devices and browsers | Current versions of Chrome, Firefox and Safari on Android and iOS; exact version policy is [OPEN: designer, 2026-12-15] |

## 4. Testing Approach

| Method | When | Owner |
|---|---|---|
| Automated checks in build | Every change to the booking web app | Engineering |
| Manual keyboard and screen-reader pass on the booking flow | Each release, recorded against TS-007 | QA |
| Usability session with a person who uses assistive technology | Before pilot launch; date is [OPEN: designer, 2026-12-15] | Designer |
| Device and breakpoint matrix at 360 px, 640 px and 200% zoom | Each release | QA |

## 5. Known Gaps and Plan

| Issue | Severity | Planned fix | Date |
|---|---|---|---|
| Legal or contractual accessibility obligations are unconfirmed | Medium | Ask owner and review with qualified advice | [OPEN: owner, 2026-12-15] |
| Screen-reader session with an assistive-technology user is not booked | Medium | Schedule before pilot launch | [OPEN: designer, 2026-12-15] |
| Owner area has had no 200% zoom pass | Low | Run the same checklist used for S-01 to S-04 | [OPEN: qa-lead, 2026-12-15] |

## Completion Criteria

- [x] A specific standard, version and level are named and match NFR-005.
- [x] Each rule is concrete enough to be tested, with an owner and method.
- [x] Breakpoints, layout behaviour and input methods are defined.
- [x] Supported devices and browsers are listed, with the exact version policy left open.
- [x] Known gaps are recorded; no unverified conformance claims are made.
