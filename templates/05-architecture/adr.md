---
id: DPP-05-adr
title: Architecture Decision Record (ADR)
domain: 05-architecture
tier: recommended
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [architect, product-manager, security-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [architecture-overview, non-functional-requirements]
feeds: [architecture-overview, component-design, technology-stack, infrastructure-and-scalability, test-strategy, threat-model]
applies_to: [all]
---

# ADR-0000: [Short title of the decision]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Records one significant architectural decision: the context, the options considered, the choice and its consequences. ADRs preserve the *why* so the team does not re-argue settled questions or lose rationale when people leave. Canonical home for `ADR-` IDs. |
| **When to use** | Whenever a decision is hard to reverse, affects several components, trades off quality attributes, or was debated. Write it when the decision is made, not afterwards. Do not write ADRs for trivial or easily reversed choices. |
| **Owner** | The decision owner (usually the Engineering Lead or architect). |
| **Required inputs** | The driving requirement(s) ([NFR](../03-requirements/non-functional-requirements.md), [PRD](../03-requirements/prd.md)); constraints; candidate options and their evidence. |
| **Related documents** | [Architecture Overview](architecture-overview.md) · [Technology Stack](technology-stack.md) · [Decision Log](../00-foundation/decision-log.md) (product/project decisions, not architecture) |

</details>

> **Guidance:** **One decision per file**, saved as `adr-NNNN-short-title.md` in `docs/05-architecture/adr/`, numbered sequentially and never deleted. To change a decision, write a new ADR that supersedes the old one and mark the old one *Superseded*. Be honest about trade-offs: an ADR with no downsides has not been thought through. Keep it under two pages. Keep an index (below) in the architecture folder.

## Metadata

| | |
|---|---|
| **Status** | ☐ Proposed · ☐ Accepted · ☐ Rejected · ☐ Deprecated · ☐ Superseded by ADR-xxxx |
| **Date** | YYYY-MM-DD |
| **Decision makers / consulted** | [Names or roles] |
| **Related requirements** | [NFR-002, BR-002, FR-001] |
| **Related ADRs** | [ADR-xxxx] |

## 1. Context

[The situation and forces at play: what needs deciding and why now; relevant requirements, constraints, assumptions. Neutral and factual.]

## 2. Decision Drivers

- [e.g. Strong consistency for slot reservation (BR-002)]
- [e.g. Small team; limited operations capacity (CON-01)]
- [e.g. p95 latency ≤ 400 ms (NFR-002)]

## 3. Options Considered

| Option | Description | Pros | Cons | Fit with drivers |
|---|---|---|---|---|
| A | | | | |
| B | | | | |
| C: do nothing / defer | | | | |

## 4. Decision

**We will [choose option X]** because [reasons mapped to the drivers].

## 5. Consequences

| Type | Consequence |
|---|---|
| Positive | |
| Negative / costs | |
| Risks introduced | [Add to Risk Register: RISK-xx] |
| Required follow-up | [Actions, owners] |
| What would make us revisit | [Trigger or review date] |

## 6. Validation

[How we will know the decision works: spike result, benchmark, test scenario ID, monitoring metric.]

## ADR Index (keep in `docs/05-architecture/adr/README.md`)

| ADR | Title | Status | Date | Supersedes |
|---|---|---|---|---|
| ADR-0001 | | Accepted | | |

## Completion Criteria

- [ ] The decision is stated in one clear sentence.
- [ ] Context and drivers reference requirement IDs.
- [ ] At least two real options (including a non-action) were compared fairly.
- [ ] Negative consequences and follow-up actions are recorded.
- [ ] Status and date are set; superseded decisions are linked both ways.
- [ ] The architecture overview and index reflect the decision.
