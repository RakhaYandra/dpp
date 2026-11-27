---
id: SLOTWISE-04-design-system
title: Design System and UI Guidelines
domain: 04-ux-ui
tier: recommended
status: draft
version: 0.1.0
owner: designer
contributors: [engineering-lead, product-manager]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [information-architecture, accessibility-and-responsive]
feeds: [wireframe-spec, prototype-review, test-scenarios]
applies_to: [all]
---

# Design System and UI Guidelines: SlotWise

## 1. Principles

| Principle | Consequence |
|---|---|
| Clear over clever | We use plain labels and native controls, so a customer books without learning an interface. |
| One primary action per screen | The next step is obvious even on a phone held between clients. |
| State is written in words | Empty, loading and error states name the cause and the next action, so colour is never the only signal. |
| Small footprint | No external assets or framework in the prototype, so the page opens offline and loads fast under NFR-001. |
| Draft without direction | With no DESIGN.md, one neutral accent is used sparingly and the prototype stays a working draft. |

## 2. Foundations (Design Tokens)

| Category | Token | Value | Usage | Contrast / constraint |
|---|---|---|---|---|
| Colour | `color.primary` | #1f4e3d | Primary action and focus outline | 9.48:1 with white text; 8.77:1 on light surface |
| Colour | `color.primary-hover` | #17392d | Hover on primary action | Same hue, darker only on hover |
| Colour | `color.surface` | #f7f6f2 | Page background | Base neutral |
| Colour | `color.raised` | #ffffff | Panels and inputs | 17.43:1 with body text |
| Colour | `color.sunken` | #ecebe5 | Hover on secondary button | Neutral, no new hue |
| Colour | `color.border` | #d5d3ca | Panel borders | Non-text boundary |
| Colour | `color.border-strong` | #8b887d | Input and button borders | 3.55:1 on white, meets 3:1 for controls |
| Colour | `color.text` | #1a1a18 | Body text | 17.43:1 on white |
| Colour | `color.text-muted` | #55534c | Supporting text | 7.12:1 on light surface |
| Colour dark theme | `color.dark.accent` | #9ad9bb | Primary action, focus outline | 11.66:1 with #101210 text |
| Colour dark theme | `color.dark.text` | #f2f1ec | Body text on #171917 | 15.63:1 |
| Typography | `type.body` | system-ui, 16 px, line height 1.5 | Body and labels | No external font; readable at 200% zoom |
| Typography | `type.heading` | system-ui, 24 px, line height 1.3 | Screen heading | Bold weight, no icon |
| Spacing | `space.2` | 8 px | Standard gap and padding step | Used for all control gaps |
| Radius / elevation | `radius.control` | 4 px | Buttons, inputs, panels | No pill shapes and no shadows in the draft |
| Motion | `motion.fast` | No transition; hover or focus background change only | Feedback on controls | MOTION 1, no animation or loop |
| Iconography | `icon.none` | No icons in the prototype | All actions are text labels | If added later, each needs an accessible label |

## 3. Components

| Component | Purpose | Variants | States | Accessibility notes | Do / Don't |
|---|---|---|---|---|---|
| Button | Trigger a named action | Primary, secondary, state toggle, theme toggle | Default, hover, focus, pressed, disabled | Native button, visible 3 px focus outline, minimum 44 px target | One primary per screen; do not use an icon-only button |
| Select and date input | Choose service and date | Single select, date input | Default, focus, error | Visible label, native keyboard behavior | Do not hide the label or rely on placeholder text |
| Text field | Capture name and contact detail | Text, phone or email | Default, focus, error, disabled | Label above the field; error linked with aria-describedby | Do not validate only by colour |
| Slot row | Offer one bookable time | Open, taken | Default, hover, focus on action | Each row action is a button with a unique accessible name | Do not show fake times as real data; label placeholders |
| Feedback message | Report state or result | Status, error, success | Default, announced | role status or role alert, plain text with a next action | Do not clear the message before the user reads it |
| State switch | Let reviewers inspect states | Default, loading, empty, error | Pressed or not pressed | aria-pressed on each toggle | Prototype only, not a production control |

## 4. Patterns

| Pattern | Guidance |
|---|---|
| Forms and validation | Visible labels, validation on submit, inline error with a suggested fix, focus on the first error, entered data kept on failure. |
| Empty states | Say why the list is empty and offer one next action, for example "Belum ada slot tersedia untuk tanggal ini. Pilih tanggal lain." |
| Loading and progress | Text with role status instead of a spinner, because MOTION 1 excludes animation; show it only while data is pending. |
| Errors and recovery | Name what failed, keep user input, offer retry or alternatives; see M-20 and M-14 in the [Wireframe Spec](wireframe-spec.md). |
| Notifications and feedback | Inline feedback for form results; confirmations and reminders arrive by message, not as a toast in the booking page. |
| Navigation | See the [Information Architecture](information-architecture.md); guests have no account menu, and the owner area is signed in. |
| Data display | Slot rows show only the fields needed to choose a time; values in the prototype are labelled placeholders. |

## 5. Content and Voice

Customer copy is in Bahasa Indonesia and uses short, plain sentences. Planning documents are in English and follow the terms in the [Glossary](../00-foundation/glossary.md): Booking, Slot, Business, Customer, No-show. In customer copy, Slot is shown as "waktu". Dates and phone formats are [OPEN: owner, 2026-12-15]. Currency is not displayed because payments are out of scope (DEC-001). Localization and right-to-left behavior are [OPEN: owner, 2026-12-15].

## 6. Governance

| Item | Rule |
|---|---|
| Where the source of truth lives | This document for decisions, and the CSS custom properties in `ui-prototype.html` for the draft token values |
| How to propose a new component | Designer writes the component row with states and accessibility notes, then engineering lead reviews the change |
| Versioning and deprecation | Semantic version in frontmatter; a removed token is kept as deprecated for one release |
| Ownership | Designer owns tokens and copy; engineering lead owns implementation constraints |

## Completion Criteria

- [x] Tokens cover colour, type, spacing and states, with accessible contrast values.
- [x] Each component states usage, variants, states and accessibility behaviour.
- [x] Error, empty and loading patterns are defined.
- [x] Voice, terminology and formats are documented and consistent with the glossary.
- [x] A single source of truth and a change process are named.
- [ ] Locale formats and localization scope are confirmed by the owner.
