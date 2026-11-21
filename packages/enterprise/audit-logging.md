---
id: DPP-PKG-enterprise-audit-logging
title: Audit Logging Requirements
domain: package-enterprise
tier: package
status: draft
version: 0.1.0
owner: security-lead
contributors: [engineering-lead, compliance-lead, product-manager, operations-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [security-requirements, access-control-matrix, observability-strategy]
feeds: [data-model, test-strategy, compliance-assessment, user-stories, incident-management]
applies_to: [enterprise, saas]
---

# Audit Logging Requirements: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Specifies the **audit trail**: a tamper-evident, queryable record of who did what, to which data, when and from where, kept to support accountability, investigations, customer audits and regulatory evidence. It differs from operational logs ([Observability Strategy](../../templates/09-release-ops/observability-strategy.md)), which exist to run the system. |
| **When to use** | When the product handles sensitive data, financial or regulated processes, multiple privileged roles, or customers who require audit evidence. |
| **Owner** | Security Lead with Compliance. |
| **Required inputs** | [Security Requirements](../../templates/08-security/security-requirements.md); [Access Control Matrix](../../templates/08-security/access-control-matrix.md); [Compliance Assessment](../../templates/08-security/compliance-assessment.md) obligations (which specify retention and content); [Privacy Requirements](../../templates/08-security/privacy-requirements.md). |
| **Related documents** | [Data Model](../../templates/05-architecture/data-model.md) · [Incident Management](../../templates/09-release-ops/incident-management.md) · [Data Governance](data-governance.md) |

</details>

> **Guidance:** Decide **what must be provable** before deciding what to log. Record **facts**, not sensitive content: capture identifiers and what changed, minimising personal data. Retention requirements come from your obligations (verified with qualified advice), balanced against privacy deletion duties.

## 1. Audit Objectives

| Objective | Question the log must answer | Source requirement |
|---|---|---|
| Accountability | Who changed a business's availability or billing settings? | SR-xxx |
| Investigation | What did a compromised account access? | |
| Customer assurance | Which support staff accessed our data and why? | |
| Compliance evidence | Evidence that access reviews and approvals happened | CMP-xx |

## 2. Auditable Events

| Category | Events | Actor types | Details captured |
|---|---|---|---|
| Authentication | Sign-in success/failure, MFA changes, password/credential reset, session revocation | All | |
| Authorisation and roles | Role or permission change, privilege elevation, access grants/revocations | Admin, owner | Before/after |
| Data access | Read of sensitive records, bulk export, report generation | User, support | Record ids, purpose |
| Data change | Create/update/delete of controlled records | User, system | Before/after values (minimised) |
| Configuration | Security and business settings, integrations, API credentials | Admin | |
| Support and privileged access | Impersonation, break-glass use, production access | Staff | Ticket/approval reference |
| Lifecycle | Tenant creation, suspension, deletion, export | System, admin | |
| Audit system itself | Access to audit data, changes to retention, failures | Admin | |

## 3. Record Format

| Field | Description |
|---|---|
| `event_id`, `timestamp` (UTC, synchronised clock) | Unique, ordered |
| `actor` | Identity (user id/service), role, tenant, authentication method |
| `action` | Standard action name |
| `target` | Resource type and id |
| `outcome` | Success / failure / denied, with reason code |
| `source` | Client address / device / session id (retention and privacy considered) |
| `request_id` | Correlation id |
| `changes` | Field-level before/after where required, with sensitive values masked |
| `reason / reference` | Ticket, approval or justification |

## 4. Integrity, Storage and Access

| Topic | Requirement |
|---|---|
| Tamper resistance | Append-only; integrity protection (hash chaining or write-once storage); separate from application admin rights |
| Completeness | Failure to write an audit record for a controlled action is handled deliberately (block or alert) |
| Retention | [Per obligation; period and basis recorded here] |
| Access | Restricted roles; access to the audit trail is itself audited |
| Tenant access | [Customers can view/export their own audit log] |
| Time and clock | Reliable time source |
| Privacy | Personal data minimised; deletion/anonymisation rules for retained records |

## 5. Reporting and Review

| Item | Requirement |
|---|---|
| Search and filtering | By actor, target, time, action |
| Export formats | |
| Alerts on suspicious patterns | [Rules; MON-xx] |
| Periodic reviews | [Privileged access review cadence; owner] |

## 6. Testing

[Every auditable event produces a correct record; tamper attempts detected; retention and access controls verified; performance impact within NFR; completeness under failure.]

## Completion Criteria

- [ ] Audit objectives trace to security, customer or compliance requirements.
- [ ] Auditable events cover authentication, roles, data access/change, configuration, privileged support access and the audit system itself.
- [ ] Record format identifies who, what, when, where, outcome and reason, with minimal personal data.
- [ ] Integrity, retention (with stated basis), access and tenant visibility are defined.
- [ ] Review process and tests exist.
