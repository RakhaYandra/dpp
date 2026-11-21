---
id: DPP-PKG-enterprise-data-governance
title: Data Governance
domain: package-enterprise
tier: package
status: draft
version: 0.1.0
owner: data-owner
contributors: [compliance-lead, security-lead, engineering-lead, legal]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [data-classification, privacy-requirements, data-model]
feeds: [audit-logging, compliance-assessment, enterprise-integration, backup-and-recovery, test-data-management]
applies_to: [enterprise, saas]
---

# Data Governance: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Establishes who is accountable for the product's data, the policies that apply to it across its lifecycle (quality, access, retention, sharing, deletion), and the processes that keep those policies working. It builds on [Data Classification](../../templates/08-security/data-classification.md) and [Privacy Requirements](../../templates/08-security/privacy-requirements.md) rather than repeating them. |
| **When to use** | When data is a shared organisational asset, subject to retention rules, used for reporting or analytics across teams, or feeds regulated decisions. Skip for simple products whose data rules are fully covered by classification and privacy documents. |
| **Owner** | Data Owner (a business role) with the data steward. |
| **Required inputs** | [Data Classification](../../templates/08-security/data-classification.md); [Privacy Requirements](../../templates/08-security/privacy-requirements.md); [Data Model](../../templates/05-architecture/data-model.md); organisational data policies. |
| **Related documents** | [Audit Logging](audit-logging.md) · [Compliance Assessment](../../templates/08-security/compliance-assessment.md) · [Backup & Recovery](../../templates/09-release-ops/backup-and-recovery.md) |

</details>

> **Guidance:** Governance is **accountability plus lightweight process**, not a committee for its own sake. Every data domain needs a **named owner who can say yes or no**. Do not restate legal duties from memory: reference the organisation's policies and verified obligations.

## 1. Roles and Accountability

| Role | Responsibility | Person / team |
|---|---|---|
| Data owner (per domain) | Decides purpose, access, retention and sharing | |
| Data steward | Maintains definitions and quality | |
| Data custodian (technical) | Implements controls, storage, backup | |
| Privacy / compliance contact | Advises on obligations | |
| Data consumers | Follow rules; report issues | |

## 2. Data Domains and Ownership

| Domain | Key entities | Owner | Source of truth | Classification | Consumers | Shared externally? |
|---|---|---|---|---|---|---|
| Customers | Customer, contact | | | Confidential | | |
| Bookings | Booking, slot | | | Internal | | |

## 3. Policies

| Policy area | Rule | Basis (policy or verified obligation) | Enforcement |
|---|---|---|---|
| Access | Need-to-know; approvals by data owner; periodic review | | Access Control Matrix |
| Retention and deletion | [By data set; deletion in all copies including backups and analytics] | | |
| Quality | [Definitions, validation, accuracy targets, correction process] | | |
| Sharing and transfer | [Internal, third-party, cross-border; agreements required] | | |
| Use for analytics / secondary purposes | [Approval and de-identification rules] | | |
| Test and non-production use | [Masking/synthetic data; see [Test Data Management](../../templates/07-quality/test-data-management.md)] | | |
| Lineage and catalogue | [Where data is documented; how lineage is tracked] | | |

## 4. Processes

| Process | Trigger | Owner | SLA | Record |
|---|---|---|---|---|
| Data access request / approval | | | | |
| Data quality issue handling | | | | |
| Data subject request handling | See [Privacy Requirements](../../templates/08-security/privacy-requirements.md) | | | |
| Retention review and disposal | Periodic | | | |
| New data collection approval | Any new personal or sensitive field | | | |
| Incident involving data | See [Incident Management](../../templates/09-release-ops/incident-management.md) | | | |

## 5. Controls and Monitoring

| Control | Evidence | Frequency | Owner |
|---|---|---|---|
| Access recertification | Signed review | Quarterly | |
| Retention job execution | Job reports | Monthly | |
| Data quality metrics | Dashboard | | |
| Policy exceptions | Register | | |

## 6. Exceptions and Escalation

[How exceptions are requested, approved, time-limited and recorded; escalation path for disputes between data owners.]

## Completion Criteria

- [ ] Every data domain has a named owner, source of truth and classification.
- [ ] Policies for access, retention/deletion, quality, sharing and non-production use are defined with their basis.
- [ ] Processes have owners, triggers and records.
- [ ] Controls produce reviewable evidence on a schedule.
- [ ] No legal obligation is asserted without a verified reference.
