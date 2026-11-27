---
id: SLOTWISE-08-security-requirements
title: Security Requirements
domain: 08-security
tier: recommended
status: draft
version: 0.1.0
owner: security-lead
contributors: [engineering-lead, product-manager, qa-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [non-functional-requirements, architecture-overview]
feeds: [authentication-authorization, threat-model, security-test-plan, test-strategy, access-control-matrix, compliance-assessment]
applies_to: [all]
---

# Security Requirements: SlotWise

## 1. Security Objectives

Protect PD-01 and PD-02 from disclosure to another salon or to the public. Keep booking state trustworthy so no booking can be altered by an unauthorised party under NFR-003. Keep the booking page available during salon hours under NFR-002. Make staff and support access to personal data attributable and reviewable. All items are pilot targets for the fictional R1, not claims about a live system.

## 2. Requirement Catalog

**Priority:** Must / Should / May. **Verification:** Test (T), Inspection (I), Analysis (A), Monitoring (M).

| ID | Area | Requirement | Source | Priority | Verification | Status |
|---|---|---|---|---|---|---|
| SR-001 | Identity and access | Every non-public API operation authenticates the caller and checks authorisation before returning data | US-004, TH-002 | Must | T | Proposed |
| SR-002 | Identity and access | Access to another salon's records is denied even with a valid session (tenant boundary) | BR-005, TH-003, multi-tenancy package | Must | T | Proposed |
| SR-003 | Data protection | PD-02 is encrypted in transit on all connections and at rest in the data store and backups | NFR-004, TH-001 | Must | I, T | Proposed |
| SR-004 | Data protection | Secrets and link tokens are not stored in source control or documents; they live in a managed secret store and rotate every 90 days | TH-007 | Must | I | Proposed |
| SR-005 | Input handling | All external input is validated on the server and output is encoded for its context | TH-004 | Must | T | Proposed |
| SR-006 | Abuse protection | Public booking endpoints are rate-limited per client to limit scripted abuse | TH-005 | Should | T, M | Proposed |
| SR-007 | Logging and audit | Authentication events, permission changes and staff access to personal data are logged, time-stamped and protected from alteration | TH-006, NFR-004 | Must | I, T | Proposed |
| SR-008 | Vulnerability management | Dependencies are scanned on every build; Critical findings are fixed or formally accepted within 7 days | CON-01 | Must | M | Proposed |

## 3. Area Checklist

| Area | Prompts | Written / N/A |
|---|---|---|
| Identity and access | Authentication strength, session handling, least privilege, default deny. Detail in the [Authentication & Authorization design](../05-architecture/authentication-authorization.md) and [Access Control Matrix](access-control-matrix.md) | SR-001, SR-002 |
| Data protection | Classification-based handling in [Data Classification](data-classification.md), encryption, key management, masking, data minimisation | SR-003, SR-004 |
| Input and output handling | Validation, encoding, injection classes; no file uploads in R1 | SR-005 |
| Secure development | Code review, branch protection, secrets scanning, secure defaults | SR-004, SR-008 |
| Third parties | DEP-01 vendor terms and package provenance; agreement details open with the engineering lead | SR-003, section 5 of the [Privacy Requirements](privacy-requirements.md) |
| Logging, monitoring and audit | Log content, access, alerting in [Observability Strategy](../09-release-ops/observability-strategy.md) | SR-007 |
| Vulnerability and patch management | Scanning every build, Critical response in 7 days, end-of-life tracked by Eng Lead | SR-008 |
| Infrastructure and configuration | Environment separation, production access, network boundaries in [Environment Strategy](../09-release-ops/environment-strategy.md) | SR-001, SR-002 |
| Resilience and abuse | Rate limiting and backup protection | SR-006, [Backup & Recovery](../09-release-ops/backup-and-recovery.md) |
| Incident response | Detection, roles, communication in [Incident Management](../09-release-ops/incident-management.md) | SR-007 |
| Privacy | Personal-data handling specified in [Privacy Requirements](privacy-requirements.md) | SR-003, SR-007 |

## 4. Exceptions and Accepted Risk

| ID | Requirement affected | Reason | Compensating control | Approved by / expiry | Risk ID |
|---|---|---|---|---|---|
| EX-01 | SR-006 | Full per-tenant quota enforcement is deferred by CON-01 and DEC-001 | Basic public-endpoint rate limiting in R1, DEP-01 quota alert MON-005, manual review of spikes | PM, 2027-03-05 | RISK-04 |

Every exception needs an expiry date and a Risk Register entry.

## 5. Traceability

| SR | Threat (TH-) | NFR | Design (ADR / component) | Test scenario (TS-) |
|---|---|---|---|---|
| SR-001 | TH-002 | NFR-002 | ADR-0005 | TS-001, TS-008 |
| SR-002 | TH-003 | NFR-003 | ADR-0005, multi-tenancy package | TS-001, TS-008 |
| SR-003 | TH-001 | NFR-004 | Data store and DEP-01 contract | TS-006 |
| SR-004 | TH-007 | NFR-004 | Managed secret store | TS-003 |
| SR-005 | TH-004 | NFR-001 | Booking service validation | TS-001 |
| SR-006 | TH-005 | NFR-002 | Edge rate limiting | TS-005 |
| SR-007 | TH-006 | NFR-004 | Audit log | TS-009 |
| SR-008 | Not threat-derived | NFR-002 | CI pipeline | TS-010 |

## Completion Criteria

- [x] Every area in the checklist has at least one requirement or a recorded reason it does not apply.
- [x] Each `SR-` requirement is verifiable, with a priority and verification method.
- [x] Requirements derived from threats cite the `TH-` ID; each *Must* threat mitigation has at least one `SR-`.
- [x] Exceptions have compensating controls, expiry dates and linked risks.
- [x] Referenced external catalogues are cited by name and version; no unassessed conformance is claimed.
- [x] The NFR summary row points to this document and the two are consistent.
