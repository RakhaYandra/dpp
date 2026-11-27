---
id: SLOTWISE-09-observability-strategy
title: Observability Strategy (Monitoring and Logging)
domain: 09-release-ops
tier: recommended
status: draft
version: 0.1.0
owner: operations-lead
contributors: [engineering-lead, security-lead, product-manager]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [architecture-overview, non-functional-requirements]
feeds: [operational-readiness, incident-management, deployment-plan, test-strategy, analytics-plan]
applies_to: [all]
---

# Observability Strategy: SlotWise

## 1. Objectives and Service Levels

| Service level indicator (SLI) | Target (SLO) | Source requirement | Measured by |
|---|---|---|---|
| Booking request success rate | 99.5% monthly | NFR-002 | Request outcome metric, alert MON-001 |
| Slot lookup latency | p95 under 800 ms at 50 concurrent users | NFR-001 | Latency metric, alert MON-002 |
| Confirmation delivery within 1 minute | 99% of confirmations in R1 pilot | AC-002.1, FR-002 | Delivery events from DEP-01, alert MON-005 |
| Availability of the booking page during salon hours | 99.5% monthly | NFR-002 | Synthetic booking check TS-010 |

Targets are pilot goals set on 2026-11-27, not measured production results.

## 2. Telemetry Plan

| Signal | What we collect | Where | Retention | Owner |
|---|---|---|---|---|
| Metrics | Request rate, errors, latency, queue age, message delivery outcomes | Metrics store | 13 months | Engineering lead |
| Logs | Structured application, access and audit logs | Log store | 30 days | Engineering lead |
| Traces | Request path across booking service, queue and worker, sampled at 10% | Trace store | 14 days | Engineering lead |
| Synthetic checks | Scripted booking journey equivalent to TC-001, every 10 minutes | External check service | 13 months | QA lead |
| Real-user monitoring | Client-side errors and page timing for the booking flow, pseudonymous only | Analytics store | 13 months | Product manager |

## 3. Logging Standards

| Topic | Standard |
|---|---|
| Format | Structured JSON with UTC timestamp, severity, component and correlation id |
| Levels | Error for failed requests, warning for retryable failures, info for lifecycle events, debug disabled in production by default |
| Content rules | No secrets, tokens or full phone numbers; PD-02 is masked and names are omitted from logs under SR-004 and the data classification |
| Audit events | Sign-in success and failure, role changes, personal-data export or deletion, support access, logged under SR-007 |
| Retention and access | Logs kept 30 days; readable by engineering lead and security lead only; audit events protected from alteration |
| Time and clocks | All hosts synchronised to a common UTC time source |

## 4. Alerting

| ID | Alert | Condition | Severity | Notify | Response / runbook | SLO |
|---|---|---|---|---|---|---|
| MON-001 | Booking failure rate high | Above 2% for 10 minutes | SEV2 page during salon hours | On-call engineer | Booking errors runbook in [Incident Management](incident-management.md) | SLI row 1 |
| MON-002 | Slot lookup slow | p95 above 800 ms for 10 minutes | SEV3 ticket | Engineering lead | Performance runbook, compare with TS-005 | SLI row 2 |
| MON-003 | Queue age high | Oldest job older than 5 minutes | SEV2 ticket | Engineering lead | Queue runbook, check ADR-0002 worker | Confirmation delivery |
| MON-004 | Backup job failed | Any scheduled backup failure | SEV3 ticket | Engineering lead | Restore runbook in [Backup & Recovery](backup-and-recovery.md) | Recovery target |
| MON-005 | Message delivery anomalies | DEP-01 failures above 1% per day or event volume drop above 50% | SEV2 ticket on-call | Engineering lead | Provider runbook, contact DEP-01 support | SLI row 3 |

**Alert quality rule:** review alerts monthly; delete, tune or automate any alert that is routinely ignored. The first review is 2027-04-05.

## 5. Dashboards and Reports

| Dashboard | Audience | Content |
|---|---|---|
| Service health | On-call engineer | MON-001 to MON-005, SLIs, queue age, DEP-01 status |
| Release | Team | Error rate and latency before and after each release |
| Capacity and cost | Engineering lead and PM | Instance utilisation, DEP-01 quota usage, monthly spend |

## 6. On-Call and Response

The engineering lead is primary on-call with the second engineer as backup from 2027-03-05 to 2027-03-19, then a weekly rotation. Escalation goes to the PM after 30 minutes on SEV1. Handover happens every Monday at 10:00 UTC and records open alerts and incidents. The process and severity levels are in [Incident Management](incident-management.md).

## 7. Privacy, Security and Cost of Telemetry

Telemetry uses pseudonymous identifiers only and excludes PD-01 and PD-02 from messages and metric labels. Access to dashboards is limited to named roles under SR-007. Traces are sampled at 10% and old logs age out after 30 days to control cost. Analytics events EVT-001 to EVT-003 are reported separately in the [Analytics Plan](../10-analytics/analytics-plan.md) and never contain free text from customers.

## Completion Criteria

- [x] Each service level is tied to a requirement and has an SLI and measurement.
- [x] Telemetry covers metrics, logs and at least one external check of the main user journey.
- [x] Logging rules prevent secrets and unnecessary personal data.
- [x] Every alert is actionable and links to a response.
- [x] Retention, access and on-call ownership are defined.
