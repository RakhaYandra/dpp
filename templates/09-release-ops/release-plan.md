---
id: DPP-09-release-plan
title: Release Plan
domain: 09-release-ops
tier: mandatory
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, qa-lead, operations-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [prd, test-strategy, risk-register]
feeds: [deployment-plan, operational-readiness, launch-and-support-plan, post-launch-review]
applies_to: [all]
---

# Release Plan: [Product Name] — [Release ID, e.g. R1]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines *what* is released, *when*, *to whom*, *under what conditions*, and *how to back out*. It contains the go/no-go criteria and the **rollback plan** (there is no separate rollback file). The technical steps live in the [Deployment Plan](deployment-plan.md). |
| **When to use** | Draft when the PRD's release scoping is agreed; finalize before the release candidate. Use one copy per release. |
| **Owner** | Product Manager (with Engineering as release manager). |
| **Required inputs** | [PRD](../03-requirements/prd.md) release table; [Test Strategy](../07-quality/test-strategy.md) quality gates; [Risk Register](../06-project-mgmt/risk-register.md); [Milestone Plan](../06-project-mgmt/milestone-plan.md). |
| **Related documents** | [Deployment Plan](deployment-plan.md) · [Environment Strategy](environment-strategy.md) · [Operational Readiness](operational-readiness.md) · [Launch & Support Plan](launch-and-support-plan.md) · [Post-Launch Review](../10-analytics/post-launch-review.md) |

</details>

> **Guidance:** A release plan is a decision tool. Someone reading it the day before release should know exactly what is shipping, what must be true to proceed, and what happens if it goes wrong.

## 1. Release Summary

| | |
|---|---|
| **Release ID / name** | R1 — [name] |
| **Type** | ☐ MVP / initial · ☐ Feature · ☐ Maintenance · ☐ Hotfix |
| **Target date / window** | [Date, time window, time zone] |
| **Audience** | [Internal / beta cohort / % of users / everyone] |
| **Release manager** | [Name] · **Decision maker (go/no-go):** [Name] |

## 2. Scope

> **Guidance:** Reference IDs from the PRD and user stories. Anything not listed is not in the release.

| Item | ID | Status | Notes |
|---|---|---|---|
| Customer self-booking | FR-001 (US-001–004) | Complete | |
| Confirmations and reminders | FR-002 (US-005–006) | In progress | |
| **Known gaps / deferred** | FR-003 | Moved to R2 | See DEC-0x |

**Breaking or visible changes:** [Migrations, changed behaviour, deprecated features, user action required.]

## 3. Release Strategy

| Question | Decision |
|---|---|
| Rollout approach | ☐ Big bang · ☐ Phased by % · ☐ Canary · ☐ Beta cohort · ☐ Feature flag |
| Phases | [e.g. Internal (day 0) → 5 pilot businesses (day 3) → all (day 10)] |
| Advance criteria between phases | [Error rate < X, no Critical defects, MET-G1 within threshold] |
| Data migration needed? | [Yes/No, link to plan] |
| Compatibility / client updates | [Old clients supported until…; app store review lead time] |

### 3.1 Release Candidate Checklist

- [ ] All in-scope stories meet their acceptance criteria.
- [ ] Test Strategy "ready to release" criteria met (§4).
- [ ] Deployment and rollback rehearsed in a production-like environment.
- [ ] Monitoring and alerts for new behaviour are in place ([Observability Strategy](observability-strategy.md)).
- [ ] [Operational Readiness](operational-readiness.md) checklist is complete.
- [ ] Support and documentation are ready ([Launch & Support Plan](launch-and-support-plan.md)).
- [ ] Release notes and customer communications are approved.

## 4. Go / No-Go Criteria

| Criterion | Threshold | Evidence | Status |
|---|---|---|---|
| Must scenarios pass | 100% | Test report | |
| Open Critical defects | 0 | Defect list | |
| Open High defects | 0, or approved exception | Defect list + approval | |
| NFR targets (performance, availability, security) | Met or exception approved | Test results | |
| Security review of changes | Completed; no open Critical findings | Security Test Plan | |
| Rollback tested | Yes | Rehearsal log | |
| Support ready | Yes | Support checklist | |
| Open High risks | Accepted with mitigation | Risk Register | |

**Decision:** ☐ Go · ☐ Conditional go · ☐ No-go — by [Name], [Date]. Rationale: [ ]

## 5. Schedule

| Time | Activity | Owner |
|---|---|---|
| T–5 days | Code freeze; release candidate built | Engineering |
| T–3 days | Final regression; go/no-go meeting | QA / PM |
| T–0 | Deploy per [Deployment Plan](deployment-plan.md) | Release manager |
| T+1 h | Post-deploy verification and smoke tests | QA |
| T+1 day | First metrics check | PM |

Avoid release windows that coincide with peak usage, holidays, or when key people are unavailable.

## 6. Communication

| Audience | Message | Channel | When | Owner |
|---|---|---|---|---|
| Internal team | Release status | [Chat/e-mail] | T–1 day, T–0 | PM |
| Customers | Release notes / downtime notice | [In-app, e-mail] | [When] | PM |
| Support | Known issues, FAQ | [Doc] | T–2 days | PM |

## 7. Rollback Plan

> **Guidance:** Decide the rollback approach *before* releasing. The best rollback is rehearsed. Consider data changes: they are the usual reason rollback is hard.

| Item | Plan |
|---|---|
| **Rollback triggers** | [e.g. Error rate > 2% for 10 min; Critical defect confirmed; data integrity issue; guardrail MET-G1 breached] |
| **Decision authority** | [Who may call rollback, including out of hours] |
| **Method** | ☐ Redeploy previous version · ☐ Disable feature flag · ☐ Restore from backup · ☐ Forward-fix |
| **Data changes** | [Are migrations reversible? If not, how is compatibility preserved?] |
| **Estimated rollback time** | [Target] |
| **Verification after rollback** | [Checks that prove the previous state is healthy] |
| **Communication on rollback** | [Who informs customers and how] |
| **Point of no return** | [Step after which rollback is no longer possible and what that implies] |

## 8. Post-Release Monitoring

| Period | Watch | Owner | Escalation |
|---|---|---|---|
| First 24 h | Error rate, latency, booking completion, support contacts | [Name] | [On-call route] |
| First week | MET-01/02 leading indicators, defect reports | PM | |

Follow-up: [Post-Launch Review](../10-analytics/post-launch-review.md) scheduled for [date].

## 9. Risks

| ID | Release risk | Mitigation | Owner |
|---|---|---|---|
| RISK-xx | [e.g. App-store review delay] | [Submit 7 days early] | |

## 10. Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Product | | ☐ Approve | |
| Engineering | | ☐ Approve | |
| QA | | ☐ Approve | |
| Operations / support | | ☐ Approve | |

## Completion Criteria

- [ ] Scope lists requirement and story IDs and states what is deferred.
- [ ] Rollout strategy and criteria for advancing each phase are defined.
- [ ] Go/no-go criteria are measurable, evidenced and owned by a named decision maker.
- [ ] Rollback triggers, method, authority and data handling are defined and rehearsed.
- [ ] Communication to customers, support and the team is planned.
- [ ] Post-release monitoring and a review date exist.
- [ ] Quality gates match the Test Strategy; NFR targets and open risks are reconciled.
