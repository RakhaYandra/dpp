---
id: DPP-09-operational-readiness
title: Operational Readiness Review
domain: 09-release-ops
tier: recommended
status: draft
version: 0.1.0
owner: operations-lead
contributors: [engineering-lead, qa-lead, product-manager, security-lead, support-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [deployment-plan, observability-strategy, incident-management, backup-and-recovery]
feeds: [release-plan, launch-and-support-plan, planning-readiness-review]
applies_to: [all]
---

# Operational Readiness Review: [Product Name] — [Release]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | A checklist-based review that confirms the product can be **run**, not just built: monitored, supported, recoverable, secure and documented. Its result feeds the release go/no-go. |
| **When to use** | Before the first production release and before significant changes; complete one to two weeks before launch so gaps can be fixed. |
| **Owner** | Operations Lead (solo: the developer, using the checklist as a final self-audit). |
| **Required inputs** | Completed operations documents listed under *Related*, test results, and release candidate status. |
| **Related documents** | [Deployment Plan](deployment-plan.md) · [Observability Strategy](observability-strategy.md) · [Incident Management](incident-management.md) · [Backup & Recovery](backup-and-recovery.md) · [Release Plan](release-plan.md) |

</details>

> **Guidance:** Mark each item **Ready / Gap (with owner and date) / Not applicable (with reason)**. Evidence beats assertion: link to the proof. An unchecked critical item is a release risk, to be accepted explicitly by the decision maker.

## 1. Readiness Checklist

| # | Area | Check | Critical? | Status | Evidence / owner / date |
|---|---|---|---|---|---|
| 1 | Deployment | Deployment and rollback rehearsed in production-like environment | Yes | | |
| 2 | Deployment | Configuration, secrets and migrations verified | Yes | | |
| 3 | Monitoring | Dashboards and alerts live for all SLIs; alerts tested | Yes | | |
| 4 | Monitoring | Synthetic check covers main user journey | Yes | | |
| 5 | Incidents | On-call schedule, escalation and runbooks in place | Yes | | |
| 6 | Incidents | Communication templates and status channel ready | | | |
| 7 | Recovery | Backups running; restore tested within RPO/RTO | Yes | | |
| 8 | Security | Security tests complete; no open Critical findings | Yes | | |
| 9 | Security | Access to production limited and audited | Yes | | |
| 10 | Privacy | Privacy notices, consent and data-subject processes ready | Yes | | |
| 11 | Performance | Load targets met (NFR-001/002/006) | Yes | | |
| 12 | Capacity | Capacity, quotas and vendor limits verified | | | |
| 13 | Dependencies | Third-party contracts, limits, support contacts confirmed | | | |
| 14 | Support | Support team trained; documentation and known issues ready | Yes | | |
| 15 | Business | Billing, legal terms, and pricing are live and tested (if applicable) | | | |
| 16 | Analytics | Events and dashboards verified for launch metrics | | | |
| 17 | Documentation | Runbooks, architecture and operations docs current | | | |
| 18 | People | Launch roles and availability confirmed, including out of hours | | | |

## 2. Gaps and Risk Acceptance

| # | Gap | Risk | Mitigation | Accepted by / date | RISK- |
|---|---|---|---|---|---|

## 3. Conclusion

☐ Ready ☐ Ready with accepted gaps ☐ Not ready — **Reviewer:** [Name], [Date]. Summary: [ ]

## Completion Criteria

- [ ] Every checklist item is marked with evidence, a gap plan or a reasoned "not applicable".
- [ ] All critical gaps are fixed or explicitly accepted by the decision maker.
- [ ] Recovery and rollback have actually been rehearsed, not only documented.
- [ ] The conclusion is recorded and linked from the Release Plan.
