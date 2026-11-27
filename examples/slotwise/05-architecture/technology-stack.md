---
id: SLOTWISE-05-technology-stack
title: Technology Stack Selection
domain: 05-architecture
tier: recommended
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [developers, operations-lead, security-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [architecture-overview, non-functional-requirements]
feeds: [adr, infrastructure-and-scalability, test-strategy, deployment-plan, resource-plan]
applies_to: [all]
---

# Technology Stack Selection: SlotWise

## 1. Selection Criteria

| Criterion | Weight | Why it matters here |
|---|---|---|
| Fit with requirements (NFRs, constraints) | High | NFR-001 lookup speed and NFR-003 no double bookings drive the data store and write path (ADR-0001) |
| Team skills and learning time | High | Two engineers and 14 weeks (CON-01) leave little room for a new platform |
| Ecosystem, maturity and community | Medium | Common tooling shortens debugging time |
| Operability (monitoring, upgrades, managed options) | Medium | One small team owns the service after launch |
| Security posture and update cadence | High | Customer contact data is personal (NFR-004, SR-008) |
| Licence and total cost | Medium | Pilot budget is not yet set, see Infrastructure and Scalability Strategy |
| Lock-in and exit cost | Medium | Data must be exportable if the pilot ends |

## 2. Stack Summary

| Layer | Choice | Version / edition | Status | Decision (ADR) | Alternatives rejected | Verified by |
|---|---|---|---|---|---|---|
| Client (web) | Server-rendered HTML with vanilla JavaScript, matching `ui-prototype.html` | No framework | Selected | ADR-0003 | Single page framework, rejected for learning time | TS-007 |
| Client (mobile) | None in R1, the booking page is responsive | Not applicable | Out of scope | None | Native app, rejected for CON-01 | TS-007 |
| Application runtime / language | Node.js LTS with TypeScript | 22 LTS, proposed | Selected, team confirmation [OPEN: engineering-lead, 2026-12-15] | ADR-0001 | Separate services per domain, rejected for operations cost | TS-002 |
| Primary data store | Managed PostgreSQL | 16 | Selected | ADR-0001 | Document store, rejected because the uniqueness rule needs a transaction | TS-002 |
| Messaging / queue | Managed queue with retries and a worker | Provider [OPEN: engineering-lead, 2026-12-15] | Selected pattern | ADR-0002 | Inline send, rejected because provider outage would fail bookings | TS-003 |
| Authentication service | Built-in owner identity plus signed manage tokens | Not applicable | Selected | ADR-0003, ADR-0005 | External identity provider, deferred with owner [OPEN: security-lead, 2026-12-15] | TS-004 |
| Hosting / platform | Managed container platform | Provider [OPEN: engineering-lead, 2026-12-15] | Selected pattern | None | Self-managed virtual machines, rejected for operations cost | TS-010 |
| Observability tooling | Metrics, logs and alerts from the hosting platform | [OPEN: engineering-lead, 2026-12-15] | Open | None | Self-hosted stack, rejected for CON-01 | TS-010 |
| CI/CD and source hosting | Managed source control and pipeline | [OPEN: engineering-lead, 2026-12-15] | Open | None | Self-hosted runner, rejected for CON-01 | None |
| Testing tools | HTTP contract tests plus a browser test runner | [OPEN: qa-lead, 2026-12-15] | Open | None | Manual-only testing, rejected because NFR-002 and NFR-003 need repeatable checks | TS-002, TS-007 |
| Third-party services | Email and SMS delivery provider (DEP-01) | Vendor [OPEN: engineering-lead, 2026-12-15] | Open | ADR-0002 | In-house delivery, rejected for CON-01 | TS-003 |

## 3. Evaluation for Contested Choices

| Option | Fit with requirements | Team skills and learning time | Operability | Notes |
|---|---|---|---|---|
| Managed PostgreSQL | High, transactions and uniqueness rule for ADR-0001 | High, standard SQL | High, managed backups | Selected |
| Embedded database file | Low, no safe concurrent write guard | High | Low, backup and restore are manual | Rejected under NFR-003 |
| Document store | Medium, flexible schema | Medium | High when managed | Rejected because the atomic slot guard is harder to prove |

A short proof of concept for the concurrent slot guard is recorded with TS-002; results are [OPEN: engineering-lead, 2026-12-15].

## 4. Dependencies and Licences

| Component | Licence | Obligation | Support / end-of-life date | Owner |
|---|---|---|---|---|
| Node.js LTS | MIT | Keep notices in distributions | [OPEN: engineering-lead, 2026-12-15] | Engineering lead |
| PostgreSQL | PostgreSQL Licence | Keep notices in distributions | [OPEN: engineering-lead, 2026-12-15] | Engineering lead |
| Email and SMS provider | [OPEN: engineering-lead, 2026-12-15] | Contract and data processing terms to be reviewed | [OPEN: owner, 2026-12-15] | Engineering lead |

## 5. Upgrade and Deprecation Policy

Dependencies are reviewed monthly. Security patches for Critical findings are applied within 7 days under SR-008. Major upgrades are decided by the engineering lead with a rollback rehearsal from the Deployment Plan. A deprecated library is removed within one release after its replacement passes TS-002 and TS-007.

## 6. Risks

| ID | Risk | Mitigation |
|---|---|---|
| RISK-02 | Provider outage delays reminders (ADR-0002) | Queue retries and backlog alert |
| RISK-04 | Two engineers cannot deliver R1 in 14 weeks (CON-01) | Keep waiting list for R2 and avoid new platforms |
| TECH-01 | Team has no confirmed Node.js LTS experience | Confirm skills before selection, owner [OPEN: engineering-lead, 2026-12-15] |

TECH-01 is a tracking label local to this document and has a named owner.

## Completion Criteria

- [x] Each layer has a choice, version and a link to the supporting ADR (or is marked open with a decision date).
- [x] Criteria and rejected alternatives are documented.
- [ ] Licences, support status and costs are verified and dated.
- [ ] Team capability and operations burden are assessed.
- [x] Lock-in and exit paths are considered: data exports come from the managed data store.
