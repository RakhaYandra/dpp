---
id: SLOTWISE-09-deployment-plan
title: Deployment Plan
domain: 09-release-ops
tier: recommended
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [operations-lead, qa-lead, security-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [release-plan, environment-strategy, infrastructure-and-scalability]
feeds: [operational-readiness, incident-management, observability-strategy]
applies_to: [all]
---

# Deployment Plan: SlotWise R1 Procedure

## 1. Deployment Approach

| Topic | Decision |
|---|---|
| Strategy | Rolling deployment with a feature flag on the public booking link; owners keep their calendar if the link is disabled |
| Automation | CI builds once, runs unit and API tests, deploys to test automatically, then to staging and production with manual approval at the go/no-go |
| Downtime expected | None expected for the pilot; the link flag is the fallback if health checks fail |
| Roles during deployment | Engineering lead executes, QA lead verifies smoke tests, PM communicates and makes the go/no-go decision |

## 2. Prerequisites Checklist

- [ ] Release candidate R1-RC-2027-02-26 built once, tested and signed off per the Test Strategy gates.
- [ ] Staging environment healthy; capacity checked against 50 concurrent users (NFR-001).
- [ ] Database migration reviewed, backward-compatible with the previous version, no destructive change.
- [ ] Configuration and secrets in the managed store; no pending changes in the repository.
- [ ] Backup and restore point confirmed, rehearsal recorded on 2027-02-12 per [Backup & Recovery](backup-and-recovery.md).
- [ ] MON-001 to MON-005 active with dashboards visible to on-call.
- [ ] Rollback steps reviewed with the second engineer available as backup.
- [ ] Communication sent to the three pilot salons per the [Release Plan](release-plan.md).

## 3. Deployment Steps

| # | Step | Owner | Command / action reference | Expected result | Time | If it fails |
|---|---|---|---|---|---|---|
| 1 | Announce start at 09:00 UTC and freeze other changes | PM | Team channel and salon notice | All roles acknowledged | 10 min | Postpone |
| 2 | Verify latest backup and record its id | Eng Lead | Backup dashboard | Backup id recorded | 10 min | Stop |
| 3 | Apply backward-compatible migration | Eng Lead | Migration job in the pipeline | Migration log clean | 15 min | Roll back per §5 |
| 4 | Deploy new version to the first instance group | Eng Lead | Pipeline deploy stage | Health checks pass | 15 min | Stop, roll back |
| 5 | Run smoke tests TC-001 and TC-003 | QA lead | Test suite | Key journeys pass | 15 min | Stop, roll back |
| 6 | Shift remaining traffic and enable the booking-link flag for pilot salons | Eng Lead | Feature flag control | Error rate and latency within NFR-002 targets | 20 min | Disable flag |
| 7 | Post-deploy checks and announcement | PM | Dashboards and salon notice | MON-001 to MON-005 green | 20 min | Open incident |

## 4. Verification

| Check | Method | Pass criteria |
|---|---|---|
| Health and version | Status endpoint and build label | R1-RC-2027-02-26 running on all instances |
| Smoke tests | TC-001 and TC-003 | All pass |
| Metrics | Service health dashboard | Error rate below 2% and slot lookup p95 under 800 ms (NFR-001, NFR-002) |
| Integrations | Test transaction to DEP-01 sandbox | Confirmation delivered within 1 minute (AC-002.1) |

## 5. Technical Rollback Procedure

The decision criteria are in the [Release Plan](release-plan.md); this is the *how*.

| Step | Action | Verification |
|---|---|---|
| 1 | Stop rollout, route traffic to the previous version or disable the public booking-link flag | Owners still see their calendar |
| 2 | Revert the application version to the previous build | Status endpoint reports previous version |
| 3 | Data: keep the backward-compatible schema, no schema revert needed | Migration log unchanged and booking reads succeed |
| 4 | Re-run TC-001 and TC-002 | Both pass |
| 5 | Communicate to pilot salons and open an incident record | Salon acknowledgement and incident id recorded |

## 6. Post-Deployment

Hypercare runs for 2 weeks from 2027-03-05 to 2027-03-19. The engineering lead owns on-call during that period, with MON-001 to MON-005 reviewed twice daily. Cleanup tasks are removal of the temporary feature flag guard and archiving of the release build record. The version, deploy time and deployer are recorded in the readiness review and linked from the Release Plan.

## Completion Criteria

- [x] A person unfamiliar with the system could follow the steps.
- [x] Prerequisites, verification and rollback are all explicit and have owners.
- [x] Data migration and backup handling are addressed.
- [ ] Procedure has been rehearsed in a production-like environment.
- [x] No secrets or personal data appear in the document.
