---
id: DPP-01-persona
title: User Persona
domain: 01-discovery
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [ux-researcher, designer]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [product-brief]
feeds: [prd, user-stories, use-cases, user-flow, wireframe-spec]
applies_to: [all]
---

# User Personas: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Gives the team a shared, evidence-based picture of the people the product serves, so decisions are made for specific users rather than "everyone". Canonical home for `PER-` IDs. |
| **When to use** | After first user conversations; refine as research accumulates. Skip personas for internal tools with a handful of known users; list the roles in the PRD instead. |
| **Owner** | Product Manager or UX Researcher. |
| **Required inputs** | [Product Brief](product-brief.md); interview notes, survey data or observations from [User Research](user-research.md). |
| **Related documents** | [PRD](../03-requirements/prd.md) · [User Stories](../03-requirements/user-stories.md) · [User Flow](../04-ux-ui/user-flow.md) |

</details>

> **Guidance:** A persona is a **research-based archetype**, not a fictional character invented in a meeting. Every claim should trace to something you saw or heard. Mark unvalidated traits as *Hypothesis*. Use 1–3 personas; more dilutes focus. Include **non-primary roles** that touch the product (admin, approver, support) as short role cards.

## 1. Persona Summary

| ID | Persona | Type | Evidence base | Confidence |
|---|---|---|---|---|
| PER-01 | [Name, role] | Primary | [e.g. 8 interviews, 1 survey] | High / Med / Low |
| PER-02 | [Name, role] | Secondary | | |

## 2. Persona Detail (repeat per persona)

### PER-01 — [Name], [Role]

> *"[A representative quote from research]"* — [source: interview #]

| | |
|---|---|
| **Who they are** | [Role, context, experience; avoid demographics that do not affect behaviour] |
| **Goals** | [What they are trying to achieve, in their words] |
| **Tasks they perform** | [Key jobs the product must support] |
| **Pain points today** | [Specific frustrations, with frequency and severity] |
| **Current tools and workarounds** | [What they use now and why it falls short] |
| **Motivations and decision criteria** | [What makes them adopt, pay, or switch] |
| **Technical comfort** | [Beginner / Intermediate / Advanced; devices and connectivity] |
| **Usage context** | [Where, when, how often, interruptions] |
| **Accessibility needs** | [Known needs or constraints] |
| **Success looks like** | [Observable outcome for them] |

> *Example:* **PER-01 — Maya, solo salon owner.** Takes appointments through chat and phone while working with a client; loses ~3 sessions a month to no-shows; uses a paper diary plus a messaging app; comfortable with a phone, not with "software"; wants "to stop answering the phone during appointments."

## 3. Role Cards (non-primary roles)

| Role | Interacts with product to… | Needs | Permissions summary |
|---|---|---|---|
| Support agent | Resolve customer issues | Read-only view of a business's bookings | Limited, audited |

## 4. Anti-Personas (optional)

[Who the product is deliberately *not* for, and why. Prevents scope creep.]

## 5. Validation Log

| Date | What was learned | Persona changed |
|---|---|---|
| [Date] | [Insight] | PER-01: removed "wants calendar sync" |

## Completion Criteria

- [ ] Each persona is traceable to research evidence; unvalidated traits are labelled.
- [ ] Goals, pain points and context are specific enough to drive design decisions.
- [ ] Primary persona is distinguished from secondary.
- [ ] Non-user roles (admin, support) are identified where relevant.
- [ ] PRD requirements reference persona IDs.
