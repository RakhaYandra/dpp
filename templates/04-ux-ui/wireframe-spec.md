---
id: DPP-04-wireframe-spec
title: Wireframe Specification
domain: 04-ux-ui
tier: recommended
status: draft
version: 0.1.0
owner: designer
contributors: [product-manager, engineering-lead, qa-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [user-flow, information-architecture]
feeds: [prototype-review, user-stories, test-scenarios, design-system]
applies_to: [all]
---

# Wireframe Specification: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Documents, screen by screen, what each screen contains, how it behaves in every state, and which requirements it satisfies. The wireframes themselves live in your design tool; this document links them and records what a picture cannot: behaviour, rules, states and content. |
| **When to use** | After flows are agreed; before high-fidelity design and development. Required for any screen with non-obvious behaviour. |
| **Owner** | UX Designer. |
| **Required inputs** | [User Flow](user-flow.md); [Information Architecture](information-architecture.md); [Business Rules](../03-requirements/business-rules.md); [Accessibility & Responsive Guidelines](accessibility-and-responsive.md). |
| **Related documents** | [Design System](design-system.md) · [Prototype Review](prototype-review.md) · [User Stories](../03-requirements/user-stories.md) |

</details>

> **Guidance:** Use a link to the design file as the source of the visual, and keep this document in sync only for **behaviour and content**. Do not describe pixel-level styling here; that belongs in the design system. Provide one spec block per screen, and reuse component names exactly as they appear in the design system.

## 1. Screen Inventory

| Screen ID | Name | Flow | Requirements | Design link | Fidelity | Status |
|---|---|---|---|---|---|---|
| S-01 | Booking home | UF-01 | FR-001 | [Link] | Low | Reviewed |
| S-03 | Enter details | UF-01 | FR-001 | [Link] | Low | Draft |

## 2. Screen Specification (repeat per screen)

### S-03 — Enter details

| | |
|---|---|
| **Purpose** | Collect minimal details to confirm the booking |
| **Who sees it / access** | Public customer; no sign-in |
| **Entry from / exit to** | S-02 slot picker → S-04 confirmation |
| **Requirements / stories** | FR-001; US-002; AC-002.1–AC-002.3 |

**Content and components**

| Element | Type | Content / data source | Required | Validation / rule | Notes |
|---|---|---|---|---|---|
| Name | Text field | Customer input | Yes | 1–80 chars | |
| Phone | Phone field | Customer input | Yes | Valid format; BR-006 | Inline error message M-12 |
| Booking summary | Read-only | Service, date, time | — | — | |
| Confirm | Primary button | — | — | Disabled until valid | |

**States**

| State | Behaviour |
|---|---|
| Default | Fields empty; focus on Name |
| Loading / submitting | Button shows progress; fields disabled; prevents double submit |
| Validation error | Inline message beside field; focus first error; summary announced to assistive tech |
| Slot taken | Message M-14; return to S-02 with alternatives |
| Offline / error | Message M-20; retry option; entered data preserved |
| Success | Navigate to S-04 |

**Interactions and behaviour:** [Keyboard order, shortcuts, gestures, autosave, back behaviour, timeouts.]
**Responsive behaviour:** [What changes at each breakpoint; see [Accessibility & Responsive](accessibility-and-responsive.md).]
**Content and copy:** [Text keys and message catalog entries; tone; localization notes.]
**Analytics events:** EVT-002 on submit; EVT-003 on validation error.
**Open questions:** [Q-xx]

## 3. Message Catalog (shared copy)

| ID | Context | Text | Notes |
|---|---|---|---|
| M-12 | Invalid phone | [Short message that says what to fix] | |

## 4. Review and Traceability

| Requirement | Screens | Complete? |
|---|---|---|
| FR-001 | S-01–S-04 | Yes |

## Completion Criteria

- [ ] Every screen maps to at least one requirement; every UI-facing FR maps to screens.
- [ ] Each screen documents content, validation, access and all relevant states (empty, loading, error, success).
- [ ] Responsive and accessibility behaviour is specified or referenced.
- [ ] Copy is catalogued and consistent with the glossary.
- [ ] Design links resolve and match the described version.
