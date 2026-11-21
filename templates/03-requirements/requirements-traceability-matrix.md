---
id: DPP-03-requirements-traceability-matrix
title: Requirements Traceability Matrix (RTM)
domain: 03-requirements
tier: recommended
status: draft
version: 0.1.0
owner: business-analyst
contributors: [product-manager, qa-lead, engineering-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [prd, user-stories, non-functional-requirements]
feeds: [test-plan, release-plan, uat-plan, planning-readiness-review]
applies_to: [all]
---

# Requirements Traceability Matrix: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Joins the chain from goals to requirements, stories, design, architecture and tests in a single view, so you can prove every requirement is justified, designed, built and tested, and see the impact of a change. It contains **links only** and defines no new IDs. |
| **When to use** | When the PRD and first stories exist; maintained through delivery. Optional for solo projects if `scripts/check-traceability` passes; recommended for teams, mandatory in regulated or contractual contexts. |
| **Owner** | Business Analyst or QA Lead. |
| **Required inputs** | [PRD](prd.md) FR catalog; [User Stories](user-stories.md); [NFRs](non-functional-requirements.md); [Test Scenarios](../07-quality/test-scenarios.md); [ADRs](../05-architecture/adr.md). |
| **Related documents** | [Traceability guide](../../guides/traceability.md) · [Test Plan](../07-quality/test-plan.md) · [Release Plan](../09-release-ops/release-plan.md) |

</details>

> **Guidance:** The RTM is only useful if it is **kept small and current**. Prefer generating it from the source documents (or from your tracker) over hand-editing. One row per FR or NFR. Do not copy requirement text; use IDs and short titles.

## 1. Functional Traceability

| Goal | FR | Title | Pri | Release | Stories | Acceptance criteria | Design ref | Architecture ref | Test scenarios | Coverage |
|---|---|---|---|---|---|---|---|---|---|---|
| GOAL-02 | FR-001 | Customer self-booking | Must | R1 | US-001–004 | AC-001.1 … AC-004.2 | Flow F-01 | ADR-0003 | TS-001–TS-006 | ● Covered |
| GOAL-02 | FR-002 | Confirmations and reminders | Must | R1 | US-005–006 | AC-005.1 … | Flow F-02 | ADR-0002 | TS-007–TS-009 | ◐ Partial |
| GOAL-01 | FR-003 | Online deposits | Should | R2 | — | — | — | — | — | ○ Not started |

**Coverage key:** ● every story has ≥ 1 AC and every AC has ≥ 1 scenario · ◐ gaps exist (list below) · ○ no downstream items yet.

## 2. Non-Functional Traceability

| NFR | Title | Pri | Addressed by (design / ADR) | Verified by (scenario / monitoring) | Coverage |
|---|---|---|---|---|---|
| NFR-001 | Booking page speed | Must | ADR-0001 | TS-030 (performance), MON-01 | ● |
| NFR-008 | Personal data protection | Must | ADR-0005 | TS-040 (security) | ◐ |

## 3. Metrics Traceability

| Goal | Metric | Events / data source | Dashboard or report |
|---|---|---|---|
| GOAL-02 | MET-01 | EVT-004, EVT-005 | [Link] |

## 4. Business Rules Coverage

| BR | Enforced in (FR / story) | Verified by (TS) |
|---|---|---|
| BR-002 | FR-001 / US-002 | TS-003 |

## 5. Gaps and Actions

| Gap | Impact | Action | Owner | Due |
|---|---|---|---|---|
| FR-002: AC-006.2 has no test scenario | Reminder failure path untested | Add TS | QA | [Date] |

## 6. Change Impact Log

| Date | Changed item | Items reviewed | Outcome |
|---|---|---|---|

## Completion Criteria

- [ ] Every FR and every *Must* NFR appears with its goal and release.
- [ ] Every *Must* FR links to stories, acceptance criteria and test scenarios; gaps are listed with owners.
- [ ] Every metric links to a data source.
- [ ] The matrix defines no new IDs; every ID resolves in its canonical document.
- [ ] Updated whenever scope or tests change; last-updated date is current.
