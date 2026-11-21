---
id: DPP-PKG-enterprise-enterprise-integration
title: Enterprise Integration
domain: package-enterprise
tier: package
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [enterprise-architect, security-lead, it-operations, product-manager]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [integration-specification, authentication-authorization, architecture-overview]
feeds: [test-strategy, risk-register, change-management-and-training, operational-readiness, data-governance]
applies_to: [enterprise]
---

# Enterprise Integration: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Covers the integration needs specific to enterprise and internal systems: identity and directory services, single sign-on, user provisioning, connections to line-of-business systems, data exchange standards, network and environment constraints, and organisational approvals. It *extends* the general [Integration Specification](../../templates/05-architecture/integration-specification.md); it does not replace it. |
| **When to use** | When the product must live inside a customer's or company's IT landscape. |
| **Owner** | Engineering Lead with the enterprise architect and IT operations. |
| **Required inputs** | [Integration Specification](../../templates/05-architecture/integration-specification.md); [Authentication & Authorization](../../templates/05-architecture/authentication-authorization.md); the organisation's IT standards, security policies and architecture principles. |
| **Related documents** | [Audit Logging](audit-logging.md) · [Data Governance](data-governance.md) · [Change Management & Training](change-management-and-training.md) · [Operational Readiness](../../templates/09-release-ops/operational-readiness.md) |

</details>

> **Guidance:** Enterprise integration is as much about **approvals, owners and lead times** as about interfaces. Identify the people who control each connected system early; their calendars often set your schedule. Use **open, widely adopted standards** where the organisation supports them, and name them with versions in ADRs.

## 1. Landscape and Constraints

| Item | Detail |
|---|---|
| Hosting and network model required by the organisation | [Cloud / on-premises / hybrid; network zones; outbound/inbound restrictions] |
| IT policies that apply | [Security baseline, change management, data residency, approved technologies] |
| Architecture review board / approvals | [Process, lead time, owner] |
| Environments available for integration testing | [Dev/test/UAT of connected systems; availability windows] |

## 2. Identity, Access and Provisioning

| Topic | Requirement |
|---|---|
| Single sign-on | [Supported protocols and identity providers] |
| Multi-factor authentication | [Delegated to the identity provider or enforced by the product] |
| User and group provisioning/deprovisioning | [Automated lifecycle from directory; timing of removal on departure] |
| Role mapping | [Directory groups → product roles; see [Access Control Matrix](../../templates/08-security/access-control-matrix.md)] |
| Service accounts | [Naming, ownership, rotation] |
| Access reviews | [Periodic certification; reports] |

## 3. Connected Systems

| ID | System | Owner | Purpose | Data / direction | Method | Frequency | SLA | Test environment | Lead time |
|---|---|---|---|---|---|---|---|---|---|
| INT-10 | [HR / ERP / CRM / ticketing / data warehouse] | | | | | | | | |

Each integration is specified in detail in the [Integration Specification](../../templates/05-architecture/integration-specification.md) using the same ID.

## 4. Data Exchange Rules

| Topic | Decision |
|---|---|
| Source of truth per data element | [Master data ownership] |
| Formats and standards | |
| Mapping and transformation | [Owner; change process] |
| Reconciliation and error queues | [How failed records are resolved and by whom] |
| Initial data migration | [Scope, cut-over, validation, rollback] |
| Batch windows and load limits | |

## 5. Operations and Support Model

| Topic | Decision |
|---|---|
| Monitoring of integrations | [Visibility for the customer's IT team] |
| Incident routing across organisations | [Contacts, escalation; see [Incident Management](../../templates/09-release-ops/incident-management.md)] |
| Change coordination | [Notice of changes to connected systems; test before production] |
| Release and maintenance windows | |
| Documentation for IT operations | [Runbooks, architecture diagrams, data-flow diagrams] |

## 6. Security and Compliance Alignment

[Evidence the organisation's security team requires (questionnaires, architecture documentation, test reports); data-flow review; vendor assessment; link to [Compliance Assessment](../../templates/08-security/compliance-assessment.md).]

## 7. Risks

| ID | Risk | Mitigation |
|---|---|---|
| RISK-xx | [e.g. Directory team cannot provide test accounts until week 6] | |

## Completion Criteria

- [ ] Organisational constraints, approvals and lead times are identified with owners.
- [ ] Identity, provisioning, role mapping and access review are specified.
- [ ] Every connected system has an owner, method, data rule, environment and SLA.
- [ ] Data ownership, reconciliation and migration are defined.
- [ ] Operations, support and security-alignment responsibilities are agreed with the organisation's IT.
