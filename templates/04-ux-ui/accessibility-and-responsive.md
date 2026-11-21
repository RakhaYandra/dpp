---
id: DPP-04-accessibility-and-responsive
title: Accessibility and Responsive Design Guidelines
domain: 04-ux-ui
tier: recommended
status: draft
version: 0.1.0
owner: designer
contributors: [engineering-lead, qa-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [non-functional-requirements]
feeds: [design-system, wireframe-spec, test-strategy, prototype-review]
applies_to: [all]
---

# Accessibility and Responsive Design Guidelines: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Turns the accessibility and compatibility targets in the NFRs into concrete design and build rules, and defines how the product adapts across screen sizes and input methods. One document covers both, because small screens and assistive technology share many constraints. |
| **When to use** | Before wireframes and the design system, so rules are built in rather than retrofitted. Required for any user-facing product; scope the depth to the audience and legal context. |
| **Owner** | UX Designer, with Engineering and QA. |
| **Required inputs** | Accessibility and compatibility NFRs ([NFR](../03-requirements/non-functional-requirements.md)); [Persona](../01-discovery/persona.md) accessibility needs; supported device and browser list. |
| **Related documents** | [Design System](design-system.md) · [Wireframe Spec](wireframe-spec.md) · [Test Strategy](../07-quality/test-strategy.md) |

</details>

> **Guidance:** Name a **specific, published standard and conformance level** as your target (for example the W3C Web Content Accessibility Guidelines, WCAG, at level AA for web content; platform accessibility guidelines for native apps). Check the current version of the standard and any legal obligations that apply to you; this template does not substitute for legal advice. Do not claim conformance you have not tested.

## 1. Targets

| Item | Target | Source |
|---|---|---|
| Accessibility standard and level | [e.g. WCAG 2.2 Level AA] | NFR-011 |
| Scope | [Which products, flows, platforms] | |
| Out of scope and why | | |
| Legal / contractual obligations | [Verify with qualified advice] | |

## 2. Accessibility Rules

| Area | Rule | Applies to | Verified by |
|---|---|---|---|
| Perceivable: text alternatives | Meaningful images have text alternatives; decorative images are hidden from assistive tech | All | Review, automated + manual test |
| Perceivable: contrast and colour | Text and key UI meet the contrast ratios of the target level; colour is never the only signal | All | Design review |
| Perceivable: text resize and reflow | Content usable at 200% zoom and on narrow screens without loss | Web | Manual test |
| Operable: keyboard | Every function reachable by keyboard; logical focus order; visible focus | All | Manual test |
| Operable: targets and timing | Adequate touch target size; no time limits without extension | Mobile, forms | Review |
| Understandable: forms | Visible labels, clear instructions, errors identified in text with suggestions | Forms | Manual test |
| Understandable: language | Language declared; plain wording | All | Review |
| Robust: semantics | Native elements and roles; names, states announced by screen readers | All | Screen-reader test |
| Motion and media | Reduced-motion preference respected; captions/transcripts for media | Media | Review |

## 3. Responsive Design Rules

| Item | Decision |
|---|---|
| Approach | [Mobile-first / desktop-first; content priority at small sizes] |
| Breakpoints | [Name, minimum width, layout change. Example: *compact* < 600, *medium* 600–1024, *expanded* > 1024] |
| Layout behaviour | [Grid, stacking order, navigation changes] |
| Touch vs pointer vs keyboard | [Input method adaptations; hover must not be the only way to reveal content] |
| Orientation and zoom | [Supported orientations; no zoom blocking] |
| Content adaptation | [Truncation, table handling, images] |
| Performance on small devices | [Link to NFR-001; image and font budgets] |
| Supported devices and browsers | [List with version policy; see NFR-013] |

## 4. Testing Approach

| Method | When | Owner |
|---|---|---|
| Automated checks in build | Every change | Engineering |
| Manual keyboard and screen-reader pass on key flows | Each release | QA |
| Usability session with people who use assistive technology | Before launch | UX |
| Device and breakpoint matrix | Each release | QA |

## 5. Known Gaps and Plan

| Issue | Severity | Planned fix | Date |
|---|---|---|---|

## Completion Criteria

- [ ] A specific standard, version and level are named and match the NFR.
- [ ] Each rule is concrete enough to be tested, with an owner and method.
- [ ] Breakpoints, layout behaviour and input methods are defined.
- [ ] Supported devices and browsers are listed.
- [ ] Known gaps are recorded; no unverified conformance claims are made.
