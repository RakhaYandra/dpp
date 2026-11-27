---
id: SLOTWISE-09-environment-strategy
title: Environment Strategy
domain: 09-release-ops
tier: recommended
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [operations-lead, qa-lead, security-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [architecture-overview, infrastructure-and-scalability]
feeds: [deployment-plan, test-plan, test-data-management, release-plan, operational-readiness]
applies_to: [all]
---

# Environment Strategy: SlotWise

## 1. Environment Catalog

| Environment | Purpose | Used by | Production parity | Data | Access | Deployed from | Lifetime |
|---|---|---|---|---|---|---|---|
| Local / development | Build and debug | Both engineers | Low | Synthetic booking fixture | Developer account | Working copy | Per developer |
| Integration / test | Automated and manual testing, TC-001 to TC-010 | QA lead, engineers | Medium | Synthetic, resettable, no real personal data | Team | Main branch builds | Persistent |
| Staging / pre-production | Release rehearsal, UAT, performance checks | QA lead, pilot owners | High for configuration and topology, smaller scale | Synthetic, 1,000 booking fixture | Restricted, named accounts | Release candidate R1-RC-2027-02-26 | Persistent |
| Production | Real pilot salons | Customers and owners | Not applicable | Real booking data, protected under SR-003 | Least privilege, audited SR-007 | Approved releases only | Persistent |
| Preview | Review of a single change | Reviewers | Low | Synthetic | Reviewers | Pull requests | Shut down after 48 hours |

## 2. Parity and Differences

| Aspect | Staging vs production | Accepted difference and risk |
|---|---|---|
| Topology, scale | Same component topology, 1 instance group in staging and 2 in production | Performance results use a 50-user load profile instead of full production load, accepted by QA lead |
| Versions and configuration | Same release candidate build and configuration shape, different secrets | Config values differ per environment, no code difference |
| Third-party integrations | DEP-01 sandbox in staging, live account in production | Live delivery may differ from sandbox; mitigated by contract checks and a monitored pilot, RISK-02 |
| Data volume | 1,000 synthetic bookings in staging | Pilot volume is smaller, so growth paths are reviewed at the 90-day review |

## 3. Promotion and Configuration

| Topic | Decision |
|---|---|
| Promotion path | One build artifact moves test to staging to production; no rebuild between environments |
| Configuration and secrets | Per-environment configuration lives outside the code; secrets stay in the managed secret store and never in the repository under SR-004 |
| Environment creation | Reproducible from versioned infrastructure definitions reviewed by the engineering lead |
| Database changes | Forward-only and backward-compatible migrations applied in environment order, verified by TC-001 and TC-002 |
| Feature flags | Public booking-link flag used for rollout and rollback in the [Deployment Plan](deployment-plan.md) |

## 4. Access and Security

| Environment | Who may access | How (approval, audit) | Data restrictions |
|---|---|---|---|
| Local and preview | Engineers and designers | Team account | Synthetic data only |
| Test | Team, QA lead controls resets | Team account, change log | Synthetic data only |
| Staging | QA lead, engineers, pilot owners during UAT | Named accounts, approval by PM | Synthetic or masked data only |
| Production | On-call engineers, support agent with case approval | Least privilege, audited under SR-007, break-glass reviewed within 4 hours | Real personal data, no copies to lower environments |

## 5. Cost and Housekeeping

Monthly spend is reviewed by the engineering lead against the sponsor budget ceiling, confirmed by 2026-12-15. Preview environments are shut down automatically after 48 hours. Test and staging are reset weekly on Mondays. Production backups follow [Backup & Recovery](backup-and-recovery.md). The engineering lead owns cleanup and flags unused resources at the monthly review.

## Completion Criteria

- [x] Each environment has a purpose, owner, access rule and data rule.
- [x] Production-parity gaps are listed with their risk.
- [x] Promotion path uses the same build artifact across environments.
- [x] No real personal data in lower environments without approval and equal protection.
- [x] Configuration and secrets handling is defined.
