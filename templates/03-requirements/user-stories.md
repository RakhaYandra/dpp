---
id: DPP-03-user-stories
title: User Stories and Acceptance Criteria
domain: 03-requirements
tier: mandatory
status: draft
version: 0.1.0
owner: product-manager
contributors: []
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [prd, persona]
feeds: [test-scenarios, requirements-traceability-matrix, sprint-planning, uat-plan]
applies_to: [all]
---

# User Stories and Acceptance Criteria: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Breaks each PRD requirement into stories small enough to design, build and test, each with acceptance criteria that define "done" in observable terms. Acceptance criteria live here; there is no separate acceptance-criteria document. |
| **When to use** | After the PRD requirements are drafted; refine continuously as stories are planned into iterations. Only *Must* requirements need stories before development starts. |
| **Owner** | Product Manager, with Engineering and QA review. |
| **Required inputs** | [PRD](prd.md) requirement catalog; [Persona](../01-discovery/persona.md); [Business Rules](business-rules.md) if any. |
| **Related documents** | [Test Scenarios](../07-quality/test-scenarios.md) · [Non-Functional Requirements](non-functional-requirements.md) · [RTM](requirements-traceability-matrix.md) · [Working Agreements](../06-project-mgmt/working-agreements.md) (Definition of Ready) |

</details>

> **Guidance:** This file can hold the stories directly, or serve as an index that points to your issue tracker (one row per story with the tracker link). If the tracker is the source of truth, keep the IDs identical in both places.

## 1. Story Format

> **Story:** As a **[persona]**, I want **[capability]** so that **[benefit]**.
> **Acceptance criteria:** testable statements, preferably in *Given / When / Then* form.

**Good story checklist (INVEST):** Independent · Negotiable · Valuable · Estimable · Small · Testable.
Split a story if it cannot be completed within one iteration, or if its criteria cover more than one behaviour.

## 2. Story Index

| ID | Requirement | Persona | Story (short) | Priority | Release | Status |
|---|---|---|---|---|---|---|
| US-001 | FR-001 | PER-01 | Customer views available slots for a service | Must | R1 | Ready |
| US-002 | FR-001 | PER-01 | Customer books a slot without registering | Must | R1 | Ready |
| US-005 | FR-002 | PER-01 | Customer receives a booking confirmation | Must | R1 | Draft |

Status values: *Draft · Ready (meets Definition of Ready) · In progress · Done · Dropped*.

## 3. Story Details

### US-002 — Customer books a slot without registering

- **Requirement:** FR-001 · **Persona:** PER-01 · **Priority:** Must · **Release:** R1
- **Story:** As a *customer of a salon*, I want to *book an available slot using only my name and phone number* so that *I can book in under a minute without creating an account*.
- **Business rules:** BR-002 (a slot cannot be double-booked)
- **Related NFRs:** NFR-001 (booking page performance)
- **Acceptance criteria:**

| ID | Given | When | Then |
|---|---|---|---|
| AC-002.1 | A service has an open slot | The customer submits name, phone and the slot | A booking is created and a confirmation screen shows date, time, service |
| AC-002.2 | Two customers select the same last slot | Both submit within the same second | Exactly one booking succeeds; the other sees a "slot no longer available" message with alternatives |
| AC-002.3 | The phone number is invalid | The customer submits | The form shows a field-level error; no booking is created |

- **Out of scope for this story:** payment, rescheduling (see US-010)
- **Design reference:** [link to flow or wireframe]
- **Notes / open points:** [e.g. Q-03: is a phone number or e-mail required?]

*(Repeat for each story. Delete the example above.)*

## 4. Writing Acceptance Criteria

> **Guidance:**
> - Each criterion is **observable and binary**: a tester can say pass or fail without interpretation.
> - Cover the **happy path, at least one failure path, and boundary conditions** (empty, maximum, duplicate, concurrent, unauthorized).
> - State **what**, not **how**; keep implementation choices out.
> - Do not hide quality targets here: reference an NFR ID instead ("meets NFR-001").
> - Avoid vague terms: *quickly, user-friendly, appropriate, properly*.

## 5. Coverage Check

| Requirement | Priority | Stories | All stories have ≥ 1 AC? |
|---|---|---|---|
| FR-001 | Must | US-001, US-002 | Yes |
| FR-002 | Must | US-005 | **No** (US-005) |

## Completion Criteria

- [ ] Every *Must* FR has at least one story; every story references an FR and a persona.
- [ ] Every story has at least one acceptance criterion; each criterion is binary and testable.
- [ ] Failure and boundary cases are covered for stories with data entry, permissions or concurrency.
- [ ] Stories planned for the next iteration meet the Definition of Ready.
- [ ] Applicable business rules and NFRs are referenced by ID.
- [ ] No story is larger than one iteration of work.
