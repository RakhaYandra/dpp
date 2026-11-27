---
id: DPP-04-ui-design
title: UI Design and Interactive Prototype
domain: 04-ux-ui
tier: recommended
status: draft
version: 0.1.0
owner: designer
contributors: [product-manager, engineering-lead, qa-lead, ux-researcher]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [prd, persona, information-architecture, user-flow, design-system, accessibility-and-responsive]
feeds: [wireframe-spec, prototype-review, test-scenarios, event-tracking-plan]
applies_to: [all]
---

# UI Design and Interactive Prototype: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Turns agreed flows and design rules into screens the team can click through. It records what each screen is for, how it behaves in every state, and where the prototype lives. |
| **When to use** | After information architecture and user flows, before designs are locked and before build. Skip with a recorded reason for API-only products or a single trivial screen. |
| **Owner** | Designer, with a front-end engineer for feasibility. |
| **Required inputs** | Requirements, persona, information architecture, flows, design tokens and accessibility targets. See `prd`, `persona`, `information-architecture`, `user-flow`, `design-system`, `accessibility-and-responsive`. |
| **Related documents** | `wireframe-spec`, `prototype-review`, `test-scenarios`, `event-tracking-plan`. |

</details>

> **Guidance:** The prototype is a decision tool, not decoration. Replace every placeholder with real content, keep the same screen IDs as the wireframe spec, and give every control a real action. If no visual direction exists yet, label the prototype as a draft without direction and keep motion to hover and focus states.

## 1. Direction and Inputs

| Item | Source | Decision for this product |
|---|---|---|
| Product and audience | `product-brief`, `persona` | |
| Visual direction | DESIGN.md or brand guidance | |
| Flows in scope | `user-flow` | |
| Tokens and components | `design-system` | |
| Accessibility target | `accessibility-and-responsive` | |

Direction status: [ ] Direction exists [ ] Draft without direction. If there is no direction, say so here and treat the prototype as a working draft, not a finished design.

## 2. Screen Inventory

| Prototype route | Wireframe screen | Screen name | Flow | Requirement | States covered | Status |
|---|---|---|---|---|---|---|
| list | S-01 | [Screen name] | UF-01 | FR-001 | default, loading, empty, error | draft |
| detail | S-02 | [Screen name] | UF-01 | FR-001 | default, confirmation | draft |

Routes are the button labels in the prototype file. Keep them stable so review notes point to the same screen.

## 3. Screen Design

Repeat this block for every screen in the inventory.

### [Screen name]

| Item | Detail |
|---|---|
| Decision the user makes here | |
| Wireframe and flow | S-01, UF-01 |
| Layout regions | |
| Components and tokens | |
| Content and copy | |
| Interaction and feedback | |
| Responsive behaviour | |
| Keyboard and screen-reader path | |

### States

| State | What the user sees | Cause | Next action |
|---|---|---|---|
| Default | | Normal use | |
| Loading | | Data is being fetched | |
| Empty | | No items match | |
| Error | | The request failed | |
| Confirmation | | The action succeeded | |

## 4. Prototype Artefact

| | |
|---|---|
| File | `ui-prototype.html` |
| Format | One HTML file with inline CSS and vanilla JavaScript, no build step and no external assets |
| Status | Starter, not production code. Every value in brackets is a placeholder. |
| Open it | Open the file in a browser. No server is required. |

Starter choices and reasons:

| Choice | Reason |
|---|---|
| Neutral surface with one accent | The starter must fit any product. The accent marks the primary action only. |
| System UI type stack | No external font dependency, and text stays readable at 200% zoom. |
| List, detail and form screens | These shapes expose states and feedback without assuming a product-specific shell. |
| Motion limited to hover and focus | Review should focus on decisions, not animation. |

Before review:

- [ ] Replace `[PRODUCT NAME]` and every screen label with real product language.
- [ ] Rename the prototype routes to match the wireframe screen IDs in section 2.
- [ ] Replace the CSS token values with the tokens from `design-system`.
- [ ] Fill the state copy with real causes and real next actions.
- [ ] Check that each control does what its label says, including keyboard use.
- [ ] Check the layout at a narrow width and at 200% zoom.

## 5. Handoff to Prototype Review

Create a copy of the framework template `prototype-review` when the prototype is ready. Use the review to answer the questions in section 1, not to collect opinions about colours. Record every finding against a screen ID from section 2 and move Critical or Major findings back into this document and into `wireframe-spec`.

## Completion Criteria

- [ ] Direction is stated, or the prototype is explicitly marked as a draft without direction.
- [ ] Every screen in the inventory has a design block and a state table.
- [ ] Screen IDs match the wireframe spec and flows.
- [ ] The prototype file opens in a browser with no external dependencies.
- [ ] No placeholder is presented as final content.
- [ ] Every control has a real action, and each state names its cause and next action.
- [ ] Keyboard path, narrow width and 200% zoom were checked.
- [ ] Findings from prototype review have a screen ID and an owner.
