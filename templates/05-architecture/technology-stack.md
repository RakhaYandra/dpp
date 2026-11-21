---
id: DPP-05-technology-stack
title: Technology Stack Selection
domain: 05-architecture
tier: recommended
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [developers, operations-lead, security-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [architecture-overview, non-functional-requirements]
feeds: [adr, infrastructure-and-scalability, test-strategy, deployment-plan, resource-plan]
applies_to: [all]
---

# Technology Stack Selection: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Records which technologies the product will use, **why**, and what was rejected. This is the only place in the framework where specific technologies are named; every other document stays technology-agnostic. |
| **When to use** | After architecture drivers are clear, and before implementation planning. Only select what you need to decide now; leave the rest "open". |
| **Owner** | Engineering Lead. |
| **Required inputs** | [Architecture Overview](architecture-overview.md) drivers; [NFRs](../03-requirements/non-functional-requirements.md); team skills; budget and licensing constraints; hiring market. |
| **Related documents** | [ADR](adr.md) (one ADR per significant choice) · [Infrastructure & Scalability](infrastructure-and-scalability.md) · [Resource Plan](../06-project-mgmt/resource-plan.md) |

</details>

> **Guidance:** Choose **boring, well-supported technology** unless a requirement justifies otherwise. Evaluate against your **criteria**, not popularity. Verify versions, licences, support status and pricing at the time of decision and record the date. Consider total cost: learning curve, operations burden, vendor lock-in and exit.

## 1. Selection Criteria

| Criterion | Weight | Why it matters here |
|---|---|---|
| Fit with requirements (NFRs, constraints) | High | |
| Team skills and learning time | High | |
| Ecosystem, maturity and community | Medium | |
| Operability (monitoring, upgrades, managed options) | Medium | |
| Security posture and update cadence | High | |
| Licence and total cost | Medium | |
| Lock-in and exit cost | Medium | |

## 2. Stack Summary

| Layer | Choice | Version / edition | Status | Decision (ADR) | Alternatives rejected |
|---|---|---|---|---|---|
| Client (web) | [ ] | | Selected | ADR-00xx | |
| Client (mobile) | [ ] | | Open | | |
| Application runtime / language | [ ] | | Selected | | |
| Primary data store | [ ] | | Selected | | |
| Messaging / queue | [ ] | | | | |
| Authentication service | [ ] | | | | |
| Hosting / platform | [ ] | | | | |
| Observability tooling | [ ] | | | | |
| CI/CD and source hosting | [ ] | | | | |
| Testing tools | [ ] | | | | |
| Third-party services | [See Integration Specification] | | | | |

## 3. Evaluation for Contested Choices

| Option | Criterion 1 | Criterion 2 | Criterion 3 | Total | Notes |
|---|---|---|---|---|---|
| Option A | | | | | |
| Option B | | | | | |

Use a short **proof of concept** where the risk is high; record results and the date.

## 4. Dependencies and Licences

| Component | Licence | Obligation | Support / end-of-life date | Owner |
|---|---|---|---|---|

## 5. Upgrade and Deprecation Policy

[How frequently dependencies are updated, how security patches are handled, who decides on major upgrades.]

## 6. Risks

| ID | Risk | Mitigation |
|---|---|---|

## Completion Criteria

- [ ] Each layer has a choice, version and a link to the supporting ADR (or is marked open with a decision date).
- [ ] Criteria and rejected alternatives are documented.
- [ ] Licences, support status and costs are verified and dated.
- [ ] Team capability and operations burden are assessed.
- [ ] Lock-in and exit paths are considered for key components.
