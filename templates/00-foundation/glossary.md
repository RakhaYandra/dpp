---
id: DPP-00-glossary
title: Project Glossary
domain: 00-foundation
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [all]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: []
feeds: [prd, user-stories, design-system, data-model, wireframe-spec]
applies_to: [all]
---

# Project Glossary: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | One agreed meaning for every term the project uses (domain words, product concepts, abbreviations), so that requirements, code, UI copy and data names are consistent. The repository's own [GLOSSARY.md](../../GLOSSARY.md) defines *framework* terms; this file defines *your product's* terms. |
| **When to use** | Start in discovery; add a term whenever two people use it differently or a new concept appears. Keep it alive. |
| **Owner** | Product Manager (everyone may propose entries). |
| **Required inputs** | Interviews, existing documents, domain vocabulary. |
| **Related documents** | [PRD](../03-requirements/prd.md) · [Data Model](../05-architecture/data-model.md) · [Design System](../04-ux-ui/design-system.md) |

</details>

> **Guidance:** Define each term **once**, in plain language, and say what it is **not** if confusion is likely. Prefer the words **users** use. Record the **one** term to use and list synonyms to avoid. Use the same term in UI copy, requirements and data names.

| Term | Definition | Use in UI / docs | Avoid (synonyms) | Related terms | Source / owner |
|---|---|---|---|---|---|
| Booking | A customer's confirmed reservation of one slot for a service | "Booking" | appointment request, order | Slot, Service | PM |
| Slot | A bookable time period offered for a service | "Time" in UI | window, opening | Booking | PM |
| Business | The customer organisation that offers services on the product | "Your business" | tenant (technical term only), client | Owner | PM |
| Customer | A person who books with a business | "Customer" | user (ambiguous) | | PM |
| No-show | A confirmed booking where the customer did not attend and did not cancel | "No-show" | missed | Booking | PM |

## Abbreviations

| Abbreviation | Meaning |
|---|---|
| | |

## Change Log

| Date | Term | Change | Reason |
|---|---|---|---|

## Completion Criteria

- [ ] Every domain term used in the PRD, stories, data model and UI appears once with one definition.
- [ ] Synonyms to avoid are listed for terms with competing wordings.
- [ ] Terms match those used in UI copy and data names.
- [ ] New terms are added when introduced; owner is named.
