---
id: DPP-PKG-saas-multi-tenancy-and-isolation
title: Multi-Tenancy and Tenant Isolation
domain: package-saas
tier: package
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [security-lead, operations-lead, product-manager]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [architecture-overview, data-model, security-requirements]
feeds: [infrastructure-and-scalability, test-strategy, threat-model, usage-metering, subscription-and-billing]
applies_to: [saas]
---

# Multi-Tenancy and Tenant Isolation: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines what a *tenant* is in your product, how many tenants share the system, and how tenants are kept apart (data, performance, configuration, security). Combines "multi-tenancy architecture" and "tenant isolation" because the isolation level *is* the architecture choice. |
| **When to use** | For any product serving several customer organisations from one deployment. Decide before the data model and authorization design are fixed: retrofitting tenancy is very expensive. |
| **Owner** | Engineering Lead with Security Lead. |
| **Required inputs** | [Architecture Overview](../../templates/05-architecture/architecture-overview.md); [Data Model](../../templates/05-architecture/data-model.md); [Security Requirements](../../templates/08-security/security-requirements.md); customer expectations (contracts, regulated customers, noisy-neighbour sensitivity). |
| **Related documents** | [Authentication & Authorization](../../templates/05-architecture/authentication-authorization.md) · [Access Control Matrix](../../templates/08-security/access-control-matrix.md) · [Usage Metering](usage-metering.md) · [Threat Model](../../templates/08-security/threat-model.md) |

</details>

> **Guidance:** The core question: *how strongly must tenant A be unable to see, affect or slow down tenant B?* More isolation costs more and adds operational load. Choose the **lowest isolation level that satisfies your customers' and regulators' requirements**, record it as an ADR, and keep a path to higher isolation for specific tenants if needed.

## 1. Tenant Definition

| Question | Answer |
|---|---|
| What is a tenant? | [Customer organisation / workspace / account] |
| Tenant hierarchy | [Tenant → groups/locations → users] |
| Can a user belong to several tenants? | [Yes/No; how switching works] |
| Expected tenant count and size distribution | [Launch / 12 months; largest tenant relative to the median] |
| Customer-specific needs | [Regulated, data residency, dedicated hosting requests] |

## 2. Isolation Dimensions and Requirements

| Dimension | Requirement | Source |
|---|---|---|
| Data | No tenant can read or modify another tenant's data under any code path | SR-xxx |
| Performance | One tenant's load must not degrade others beyond [x%] | NFR-xxx |
| Configuration | Settings and customisations are tenant-scoped | |
| Security | Credentials, keys and tokens are tenant-scoped; compromise of one tenant does not expose others | |
| Operations | Backup/restore, deletion and export possible per tenant | |
| Cost attribution | Resource use attributable per tenant ([Usage Metering](usage-metering.md)) | |

## 3. Isolation Model Options

| Model | Description | Isolation | Cost / ops load | Fit |
|---|---|---|---|---|
| Shared everything, tenant key on each record | One database/schema, rows tagged by tenant | Logical; relies on correct enforcement | Lowest | Many small tenants |
| Separate schema/namespace per tenant | Shared database server, separate structures | Stronger logical separation | Medium | Medium tenants |
| Separate database / storage per tenant | Dedicated data store, shared application | Strong data isolation | Higher | Regulated or large tenants |
| Dedicated deployment per tenant | Separate stack | Strongest | Highest | Strict contractual needs |
| **Chosen model** | [ ] | | | ADR-xxxx |

**Hybrid path:** [Default model with an upgrade path for selected tenants.]

## 4. Enforcement Design

| Layer | Mechanism |
|---|---|
| Request identification | How the tenant is determined (token claim, hostname, path) and **never from untrusted input alone** |
| Application | Tenant context carried through every call; shared helper for data access |
| Data store | Tenant key mandatory on tenant-owned data; database-level guards where available |
| Background work | Jobs and events carry tenant context |
| Caches, search indexes, files | Tenant-scoped keys/paths |
| Logs and analytics | Tenant id recorded; no cross-tenant data in shared views |
| Admin / support access | Time-limited, audited, tenant-approved where required |

## 5. Noisy Neighbour Controls

[Per-tenant rate limits, quotas, fair queueing, resource limits, capacity monitoring per tenant; see [Rate Limiting & Quotas](../api-platform/rate-limiting-and-quotas.md).]

## 6. Tenant Lifecycle

| Event | Handling |
|---|---|
| Onboarding / provisioning | [Automation, defaults, seed data] |
| Configuration changes and feature flags | |
| Migration between isolation tiers | |
| Suspension (non-payment, abuse) | |
| Export and offboarding | |
| Deletion (including backups) | [Aligned with [Privacy Requirements](../../templates/08-security/privacy-requirements.md)] |

## 7. Verification

| Test | Method | Frequency |
|---|---|---|
| Cross-tenant access attempts on every API and background path | Automated negative tests | Every change |
| Tenant-isolation review in design and code review | Checklist | Each feature |
| Penetration test with tenant-isolation scope | Manual | Before launch and yearly |
| Noisy neighbour load test | Performance test | Before launch |

## Completion Criteria

- [ ] Tenant, hierarchy and membership rules are defined.
- [ ] The isolation model is chosen against explicit requirements and recorded as an ADR.
- [ ] Enforcement is described at every layer, including jobs, caches and admin access.
- [ ] Noisy-neighbour controls and tenant lifecycle (including deletion) are defined.
- [ ] Cross-tenant tests are part of the Test Strategy.
