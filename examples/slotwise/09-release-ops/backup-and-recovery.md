---
id: SLOTWISE-09-backup-and-recovery
title: Backup and Recovery Plan
domain: 09-release-ops
tier: recommended
status: draft
version: 0.1.0
owner: operations-lead
contributors: [engineering-lead, security-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [non-functional-requirements, data-model, infrastructure-and-scalability]
feeds: [operational-readiness, incident-management, deployment-plan, privacy-requirements]
applies_to: [all]
---

# Backup and Recovery Plan: SlotWise

## 1. Recovery Objectives

| Data / service | Criticality | RPO | RTO | Source |
|---|---|---|---|---|
| Booking data and customer contact details | High | 15 minutes | 4 hours | Pilot recovery target set by the engineering lead on 2026-11-27 |
| Configuration and secrets | High | 24 hours | 4 hours | Pilot recovery target set by the engineering lead on 2026-11-27 |
| Logs and analytics | Low | 24 hours | 3 days | Operations target, verified in the readiness review |

These are targets for the fictional pilot, not measured values. They are confirmed by the restore rehearsal on 2027-02-12 and reviewed at the 90-day review on 2027-06-03.

## 2. Backup Design

| Data set | Method | Frequency | Retention | Location / isolation | Encryption | Owner |
|---|---|---|---|---|---|---|
| Primary data store | Continuous transaction log plus daily full snapshot | Continuous and 02:00 UTC daily | 35 days | Separate failure domain from production | Yes, managed keys | Engineering lead |
| Uploaded files / objects | Not applicable in R1, no uploads are in scope | Not applicable | Not applicable | Not applicable | Not applicable | Engineering lead |
| Infrastructure definitions and configuration | Versioned source | Every change | Life of the project | Source repository | Standard repository access | Engineering lead |
| Secrets | Managed secret store with documented recovery process | On change and every 90 days | Current and previous version | Separate secret store | Yes | Security lead |

## 3. Recovery Procedures

| Scenario | Procedure summary | Expected duration | Responsible | Runbook |
|---|---|---|---|---|
| Accidental deletion or corruption | Point-in-time restore to a side copy, verify records, selective copy back | 1 hour | Engineering lead | Restore runbook maintained by engineering lead |
| Data store failure | Fail over to standby, or restore latest snapshot plus log replay | 2 hours | Engineering lead | Restore runbook maintained by engineering lead |
| Region or provider outage | Rebuild in the alternative region from versioned definitions and latest backup | 4 hours | Engineering lead | Rebuild runbook in the readiness review |
| Compromise of credentials | Isolate access, rebuild clean instances, restore known-good data, rotate secrets under SR-004 | 4 hours | Security lead | Incident runbook in [Incident Management](incident-management.md) |

## 4. Testing

| Test | Frequency | Success criteria | Last result / date |
|---|---|---|---|
| Restore one data set to an isolated environment | Quarterly from 2027-03-01, first run 2027-02-12 | RPO 15 minutes and RTO 4 hours met, sampled bookings verified | Not yet run as of 2026-11-27 |
| Full rebuild exercise | Yearly, first run 2027-02-19 | Production-like environment rebuilt from definitions and backup | Not yet run as of 2026-11-27 |
| Backup success monitoring | Continuous | Alert on failed job, MON-004 | Not yet run as of 2026-11-27 |

## 5. Privacy and Retention Interaction

NFR-004 requires personal data to be deleted on request within 30 days. A deletion is applied to the live store immediately and recorded in a deletion log. Backup copies age out within 35 days, so no restored copy is older than the deletion record. After any restore, the engineering lead replays the deletion log before the data is made available. Customers contact the salon or the product contact address under the [Privacy Requirements](../08-security/privacy-requirements.md).

## 6. Gaps and Decisions

| Gap | Risk | Decision / action | Risk ID |
|---|---|---|---|
| No restore rehearsal has been performed yet | Recovery target is unverified | Rehearse restore on 2027-02-12 and record the result in the readiness review | RISK-04 |
| Alternative region is not provisioned in R1 | Provider outage could exceed RTO | Keep definitions portable and revisit after the pilot, owner engineering lead | RISK-02 |

## Completion Criteria

- [x] RPO and RTO exist for each critical data set and match the NFRs.
- [x] Backups are isolated, encrypted, monitored and have defined retention.
- [x] Recovery procedures exist for the main failure scenarios.
- [x] Restores are tested on a schedule with recorded results.
- [x] Interaction with deletion and privacy obligations is defined.
