---
id: SLOTWISE-09-operational-readiness
title: Operational Readiness Review
domain: 09-release-ops
tier: recommended
status: draft
version: 0.1.0
owner: operations-lead
contributors: [engineering-lead, qa-lead, product-manager, security-lead, support-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [deployment-plan, observability-strategy, incident-management, backup-and-recovery]
feeds: [release-plan, launch-and-support-plan, planning-readiness-review]
applies_to: [all]
---

# Operational Readiness Review: SlotWise R1

## 1. Readiness Checklist

| # | Area | Check | Critical? | Status | Evidence / owner / date |
|---|---|---|---|---|---|
| 1 | Deployment | Deployment and rollback rehearsed in production-like environment | Yes | Planned | Rehearsal 2027-02-12, Engineering lead |
| 2 | Deployment | Configuration, secrets and migrations verified | Yes | Planned | [Deployment Plan](deployment-plan.md) checklist, Engineering lead, 2027-02-19 |
| 3 | Monitoring | Dashboards and alerts live for all SLIs; alerts tested | Yes | Planned | MON-001 to MON-005 in [Observability Strategy](observability-strategy.md), Operations lead, 2027-02-19 |
| 4 | Monitoring | Synthetic check covers main user journey | Yes | Planned | TC-001 scripted as synthetic check, QA lead, 2027-02-19 |
| 5 | Incidents | On-call schedule, escalation and runbooks in place | Yes | Planned | [Incident Management](incident-management.md), PM, 2027-02-19 |
| 6 | Incidents | Communication templates and status channel ready | No | Ready | Email and chat templates in the incident plan, PM, 2026-11-27 |
| 7 | Recovery | Backups running; restore tested within target | Yes | Planned | Restore rehearsal 2027-02-12, Engineering lead |
| 8 | Security | Security tests complete; no open Critical findings | Yes | Planned | SR-001 to SR-008 and TH-001 to TH-007, Security lead, 2027-02-19 |
| 9 | Security | Access to production limited and audited | Yes | Planned | [Access Control Matrix](../08-security/access-control-matrix.md), Security lead, 2027-02-19 |
| 10 | Privacy | Privacy notices, consent and deletion process ready | Yes | Planned | [Privacy Requirements](../08-security/privacy-requirements.md), PM, 2027-02-19 |
| 11 | Performance | Load targets met for NFR-001 and NFR-002 | Yes | Planned | TS-005 and TS-010, QA lead, 2027-02-19 |
| 12 | Capacity | Capacity, quotas and vendor limits verified | No | Planned | DEP-01 quota check, Engineering lead, 2026-12-18 |
| 13 | Dependencies | Third-party agreement, limits, support contact confirmed | No | Planned | DEP-01 provider account, Engineering lead, 2026-12-18 |
| 14 | Support | Support team trained; known issues list ready | Yes | Planned | Three pilot salons briefed 2027-02-22, PM |
| 15 | Business | Manual invoicing and pricing live and tested | No | Planned | [Subscription & Billing](../packages/saas/subscription-and-billing.md), PM, 2027-02-19 |
| 16 | Analytics | Events and dashboards verified for launch metrics | No | Planned | EVT-001 to EVT-003, PM, 2027-02-19 |
| 17 | Documentation | Runbooks, architecture and operations docs current | No | Planned | Document review, Engineering lead, 2027-02-19 |
| 18 | People | Launch roles and availability confirmed, including out of hours | Yes | Planned | Launch roster, PM, 2027-02-26 |

## 2. Gaps and Risk Acceptance

| # | Gap | Risk | Mitigation | Accepted by / date | Risk ID |
|---|---|---|---|---|---|
| 1 | Restore rehearsal not yet run | Recovery target unverified | Rehearse on 2027-02-12 and record result in [Backup & Recovery](backup-and-recovery.md) | PM, target 2027-02-19 | RISK-04 |
| 2 | DEP-01 agreement and location still open | Personal-data sharing terms unverified | Confirm by 2026-12-18 before any real message is sent | PM, target 2026-12-18 | RISK-02 |

## 3. Conclusion

Not ready as of 2026-11-27. Formal review is scheduled for 2027-02-26 with the operations lead as reviewer. The conclusion will be Ready, Ready with accepted gaps, or Not ready, and will be linked from the Release Plan.

## Completion Criteria

- [x] Every checklist item is marked with evidence, a gap plan or a reasoned "not applicable".
- [ ] All critical gaps are fixed or explicitly accepted by the decision maker.
- [ ] Recovery and rollback have actually been rehearsed, not only documented.
- [x] The conclusion is recorded and linked from the Release Plan.
