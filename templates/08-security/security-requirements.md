---
id: DPP-08-security-requirements
title: Security Requirements
domain: 08-security
tier: recommended
status: draft
version: 0.1.0
owner: security-lead
contributors: [engineering-lead, product-manager, qa-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [non-functional-requirements, architecture-overview]
feeds: [authentication-authorization, threat-model, security-test-plan, test-strategy, access-control-matrix, compliance-assessment]
applies_to: [all]
---

# Security Requirements: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | The detailed catalog of security requirements the product must meet. The [NFR](../03-requirements/non-functional-requirements.md) document holds one summary row per security topic (for example NFR-008); this document expands it into testable `SR-` requirements. Canonical home for `SR-` IDs. |
| **When to use** | After NFRs and the architecture overview; before design of authentication, the threat model and security testing. Revisit after each threat-model review. |
| **Owner** | Security Lead (solo projects: the developer, using a recognised checklist as a prompt). |
| **Required inputs** | [NFRs](../03-requirements/non-functional-requirements.md); [Architecture Overview](../05-architecture/architecture-overview.md); [Data Classification](data-classification.md); obligations identified in [Compliance Assessment](compliance-assessment.md). |
| **Related documents** | [Authentication & Authorization](../05-architecture/authentication-authorization.md) · [Threat Model](threat-model.md) · [Security Test Plan](../07-quality/security-test-plan.md) · [Incident Management](../09-release-ops/incident-management.md) |

</details>

> **Guidance:** Write requirements as **verifiable statements** ("must", with a condition and a way to verify), not aspirations ("be secure"). Reference a recognised catalogue (for example OWASP ASVS or an equivalent for your platform) as a source of ideas and cite its exact version; do not claim conformance you have not assessed. Requirements that come from a threat (see [Threat Model](threat-model.md)) should cite the `TH-` ID.

## 1. Security Objectives

[Three to five outcomes: what must be protected (confidentiality, integrity, availability, accountability) and from whom. Example: *Protect customers' contact details from disclosure to other businesses; ensure bookings cannot be altered by unauthorised parties.*]

## 2. Requirement Catalog

**Priority:** Must / Should / May. **Verification:** Test (T), Inspection (I), Analysis (A), Monitoring (M).

| ID | Area | Requirement | Source | Priority | Verification | Status |
|---|---|---|---|---|---|---|
| SR-001 | Identity and access | Every non-public API operation must authenticate the caller and check authorisation before returning data | NFR-008; TH-02 | Must | T | Proposed |
| SR-002 | Identity and access | Access to another business's records must be denied even with a valid session (tenant boundary) | BR-005; TH-03 | Must | T | Proposed |
| SR-003 | Data protection | Personal data must be encrypted in transit on all connections, and at rest in all data stores and backups | NFR-008 | Must | I, T | Proposed |
| SR-004 | Data protection | Secrets must not be stored in source control or documents; they are held in a managed secret store and rotated on a defined schedule | TH-07 | Must | I | Proposed |
| SR-005 | Input handling | All external input must be validated on the server; output must be encoded for its context | TH-04 | Must | T | Proposed |
| SR-006 | Abuse protection | Public booking endpoints must be rate-limited per client to limit scripted abuse | TH-05 | Should | T, M | Proposed |
| SR-007 | Logging and audit | Authentication events, permission changes and access to personal data by staff must be logged, time-stamped and protected from alteration | NFR-008 | Must | I, T | Proposed |
| SR-008 | Vulnerability management | Dependencies must be scanned on every build; Critical findings must be fixed or formally accepted within [N] days | CON-xx | Must | M | Proposed |

*(Delete the example rows and add your own.)*

## 3. Area Checklist

> **Guidance:** For each area, write at least one `SR-` requirement or mark it *Not applicable* with a reason. Use the questions as prompts, not as a complete standard.

| Area | Prompts | Written / N/A |
|---|---|---|
| Identity and access | Authentication strength, session handling, least privilege, default deny. Detail in [Authentication & Authorization](../05-architecture/authentication-authorization.md) and [Access Control Matrix](access-control-matrix.md) | |
| Data protection | Classification-based handling ([Data Classification](data-classification.md)), encryption, key management, masking, data minimisation | |
| Input and output handling | Validation, encoding, file uploads, deserialisation, injection classes | |
| Secure development | Code review, branch protection, secrets scanning, dependency policy, secure defaults, training | |
| Third parties | Vendor assessment, data-sharing terms, SDK and package provenance; see [Integration Specification](../05-architecture/integration-specification.md) | |
| Logging, monitoring and audit | What is logged, protection of logs, alerting; see [Observability Strategy](../09-release-ops/observability-strategy.md) | |
| Vulnerability and patch management | Scanning cadence, severity response times, end-of-life tracking | |
| Infrastructure and configuration | Hardening, network segmentation, admin access, environment separation | |
| Resilience and abuse | Rate limiting, denial-of-service posture, backup protection | |
| Incident response | Detection, roles, communication, evidence; see [Incident Management](../09-release-ops/incident-management.md) | |
| Privacy | Personal-data handling is specified in [Privacy Requirements](privacy-requirements.md) | |

## 4. Exceptions and Accepted Risk

| ID | Requirement affected | Reason | Compensating control | Approved by / expiry | Risk ID |
|---|---|---|---|---|---|
| EX-01 | SR-xxx | [Why it cannot be met now] | [What reduces exposure] | [Name / date] | RISK-xx |

Every exception needs an expiry date and a Risk Register entry.

## 5. Traceability

| SR | Threat (TH-) | NFR | Design (ADR / component) | Test scenario (TS-) |
|---|---|---|---|---|
| SR-002 | TH-03 | NFR-008 | ADR-0005 | TS-040 |

## Completion Criteria

- [ ] Every area in the checklist has at least one requirement or a recorded reason it does not apply.
- [ ] Each `SR-` requirement is verifiable, with a priority and verification method.
- [ ] Requirements derived from threats cite the `TH-` ID; each *Must* threat mitigation has at least one `SR-`.
- [ ] Exceptions have compensating controls, expiry dates and linked risks.
- [ ] Referenced external catalogues are cited by name and version; no unassessed conformance is claimed.
- [ ] The NFR summary row points to this document and the two are consistent.
