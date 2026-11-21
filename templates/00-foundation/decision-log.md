---
id: DPP-00-decision-log
title: Decision Log
domain: 00-foundation
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [project-manager, engineering-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: []
feeds: [prd, roadmap, post-launch-review, risk-register, planning-readiness-review]
applies_to: [all]
---

# Decision Log: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | A chronological register of product and project decisions: what was decided, when, by whom, why and what was rejected. It is the memory of the project and the audit trail for scope and priority changes. Canonical home for `DEC-` IDs. **Architecture decisions** are recorded separately as [ADRs](../05-architecture/adr.md). |
| **When to use** | Whenever a decision changes scope, priorities, budget, schedule, policy or direction, or resolves an open question. Add the entry at the time. |
| **Owner** | Product Manager (project decisions: Project Manager). |
| **Required inputs** | The decision, its drivers and the people involved. |
| **Related documents** | [PRD](../03-requirements/prd.md) (Key Decisions summary) · [ADR](../05-architecture/adr.md) · [Project Charter](../06-project-mgmt/project-charter.md) (change control) |

</details>

> **Guidance:** Log **decisions**, not discussions. Keep entries short (a few lines). Record **why** and **alternatives rejected**; those are what people forget. A decision can be reversed, but never silently: add a new entry that supersedes the old.

| ID | Date | Decision | Type | Decided by | Rationale | Alternatives rejected | Impact (documents / IDs affected) | Status |
|---|---|---|---|---|---|---|---|---|
| DEC-01 | YYYY-MM-DD | Guest booking without accounts in R1; accounts deferred to R2 | Scope | PM, Sponsor | Lowers friction; tests ASM-01 quickly | Mandatory accounts (higher drop-off risk) | FR-001, US-002, R1 | Active |
| DEC-02 | YYYY-MM-DD | Use RICE for prioritization | Process | PM | Transparent and reproducible | MoSCoW only | MVP & Prioritization | Active |

Type values: **Scope · Priority · Schedule · Budget · Policy · Process · Technical (non-architectural) · Resolved question**. Status: **Active · Superseded by DEC-xx · Reversed**.

## Open Questions Register (optional)

| ID | Question | Raised by | Owner | Needed by | Status | Resolved in |
|---|---|---|---|---|---|---|
| Q-01 | | | | | Open | DEC-xx |

## Completion Criteria

- [ ] Every scope, priority, policy or budget change in the PRD or charter has an entry.
- [ ] Each entry has a date, decision maker, rationale, rejected alternatives and impact.
- [ ] Reversals are recorded as new entries that reference the old one.
- [ ] Resolved open questions point to the decision that closed them.
