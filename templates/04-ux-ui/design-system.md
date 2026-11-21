---
id: DPP-04-design-system
title: Design System and UI Guidelines
domain: 04-ux-ui
tier: recommended
status: draft
version: 0.1.0
owner: designer
contributors: [engineering-lead, product-manager]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [information-architecture, accessibility-and-responsive]
feeds: [wireframe-spec, prototype-review, test-scenarios]
applies_to: [all]
---

# Design System and UI Guidelines: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines the shared visual language and reusable components (tokens, patterns, usage rules) so the product looks and behaves consistently and teams build faster. Includes the UI guidelines; there is no separate guidelines file. |
| **When to use** | Before high-fidelity design for any product with more than a few screens or more than one designer or developer. For a tiny product, a one-page style sheet in this format is enough. |
| **Owner** | Designer, with a front-end engineer. |
| **Required inputs** | Brand assets; [Information Architecture](information-architecture.md); [Accessibility & Responsive Guidelines](accessibility-and-responsive.md); platform constraints from the [Architecture Overview](../05-architecture/architecture-overview.md). |
| **Related documents** | [Wireframe Spec](wireframe-spec.md) · [Prototype Review](prototype-review.md) |

</details>

> **Guidance:** Describe **tokens and rules**, not implementations. Keep it technology-agnostic: record values (e.g. a colour hex or size) in a neutral token table that any platform can consume. Every component entry must say *when to use it* and *when not to*. Adopt an existing public system where possible and record deviations only.

## 1. Principles

[3–5 design principles with a "so we…" consequence each. Example: *Clear over clever → we use plain labels and never icon-only buttons.*]

## 2. Foundations (Design Tokens)

| Category | Token | Value | Usage | Contrast / constraint |
|---|---|---|---|---|
| Colour | `color.primary` | #… | Primary actions | ≥ 4.5:1 on background |
| Colour | `color.danger` | #… | Errors, destructive | Never colour alone |
| Typography | `type.body` | [family, size, line height] | Body text | ≥ 16 px equivalent on mobile |
| Spacing | `space.2` | 8 | Standard gap | |
| Radius / elevation | | | | |
| Motion | `motion.fast` | [duration, easing] | Feedback | Respects reduced-motion setting |
| Iconography | | | | Always with accessible label |

## 3. Components

| Component | Purpose | Variants | States | Accessibility notes | Do / Don't |
|---|---|---|---|---|---|
| Button | Trigger an action | Primary, secondary, destructive | Default, hover, focus, pressed, disabled, loading | Visible focus; ≥ 44×44 px target | One primary per view |
| Form field | Capture input | Text, phone, select | Default, focus, error, disabled | Label always visible; error linked to field | |
| Modal / dialog | Focused decision | | | Focus trapped; Esc closes | Do not use for long forms |

## 4. Patterns

| Pattern | Guidance |
|---|---|
| Forms and validation | When to validate, how to word errors, required-field marking |
| Empty states | Explain, offer next action |
| Loading and progress | Skeletons vs spinners; thresholds |
| Errors and recovery | Plain language; what happened, what to do |
| Notifications and feedback | Toast vs inline vs email |
| Navigation | See [Information Architecture](information-architecture.md) |
| Data display | Tables, lists, pagination, sorting |

## 5. Content and Voice

[Tone, terminology (link to [Glossary](../00-foundation/glossary.md)), capitalization, date/number/currency formats, localization rules (text expansion, right-to-left).]

## 6. Governance

| Item | Rule |
|---|---|
| Where the source of truth lives | [Design file link / code library link] |
| How to propose a new component | [Process] |
| Versioning and deprecation | [Rule] |
| Ownership | [Role] |

## Completion Criteria

- [ ] Tokens cover colour, type, spacing and states, with accessible contrast values.
- [ ] Each component states usage, variants, states and accessibility behaviour.
- [ ] Error, empty and loading patterns are defined.
- [ ] Voice, terminology and formats are documented and consistent with the glossary.
- [ ] A single source of truth and a change process are named.
