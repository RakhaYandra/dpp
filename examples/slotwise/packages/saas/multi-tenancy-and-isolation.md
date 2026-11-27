---
id: SLOTWISE-PKG-saas-multi-tenancy-and-isolation
title: Multi-Tenancy and Tenant Isolation
domain: package-saas
tier: package
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [security-lead, operations-lead, product-manager]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [architecture-overview, data-model, security-requirements]
feeds: [infrastructure-and-scalability, test-strategy, threat-model, usage-metering, subscription-and-billing]
applies_to: [saas]
---

# Multi-Tenancy and Tenant Isolation: SlotWise

## 1. Tenant Definition

| Question | Answer |
|---|---|
| What is a tenant? | One salon business account owned by PER-01 |
| Tenant hierarchy | Tenant, then staff members and services; guest customers are not tenant users |
| Can a user belong to several tenants? | No in R1; each owner account belongs to one salon and switching is not offered |
| Expected tenant count and size distribution | 3 pilot salons at launch, 40 paying salons target by 2027-06-03 per MET-03; largest tenant expected below twice the median, a planning assumption |
| Customer-specific needs | None in R1; data residency requests are open with the engineering lead by 2026-12-15 |

## 2. Isolation Dimensions and Requirements

| Dimension | Requirement | Source |
|---|---|---|
| Data | No salon can read or modify another salon's data on any code path | SR-002, TH-003 |
| Performance | One salon's load must not push slot lookup beyond NFR-001 at 50 concurrent users | NFR-001, TS-005 |
| Configuration | Services, staff, working hours and time off are tenant-scoped | FR-004, US-004 |
| Security | Tokens and credentials are tenant-scoped; compromise of one salon does not expose another | SR-001, SR-004 |
| Operations | Backup, restore and deletion can be performed per salon | NFR-004, backup and recovery plan |
| Cost attribution | Message and storage use is attributable per salon in [Usage Metering](usage-metering.md) | DEP-01 cost tracking |

## 3. Isolation Model Options

| Model | Description | Isolation | Cost / ops load | Fit |
|---|---|---|---|---|
| Shared everything, tenant key on each record | One database, rows tagged with salon id | Logical, relies on correct enforcement | Lowest | Many small salons, chosen for R1 |
| Separate schema per tenant | Shared database server, separate structures | Stronger logical separation | Medium | Future larger salons |
| Separate database per tenant | Dedicated data store, shared application | Strong data isolation | Higher | Regulated tenants, not in R1 |
| Dedicated deployment per tenant | Separate stack | Strongest | Highest | Strict contracts, not in R1 |
| **Chosen model** | Shared everything with a mandatory salon id on tenant-owned records, recorded in ADR-0005 | Logical with mandatory guards | Lowest | Fits CON-01 and the pilot scale |

**Hybrid path:** none in R1. Revisit separate schemas if a salon exceeds 10 times the median load or signs a contract needing stronger separation, with a decision recorded in the ADR document.

## 4. Enforcement Design

| Layer | Mechanism |
|---|---|
| Request identification | Tenant comes from the authenticated owner session or the booking link token, never from a client-supplied salon id |
| Application | Tenant context is carried through every call; one shared data-access helper applies the salon filter |
| Data store | Salon id is mandatory on tenant-owned tables and enforced with a database constraint alongside ADR-0001 slot uniqueness |
| Background work | Queue jobs and notification events carry the salon id from ADR-0002 |
| Caches, search indexes, files | Keys and paths are prefixed with the salon id; no file uploads in R1 |
| Logs and analytics | Tenant id is recorded in audit events and EVT-001 to EVT-003; no cross-salon data in shared views |
| Admin / support access | Time-limited, approved and audited under SR-007 and the [Access Control Matrix](../../08-security/access-control-matrix.md) |

## 5. Noisy Neighbour Controls

Public booking endpoints are rate-limited per client under SR-006. Message jobs are processed through a single fair queue with a backlog alert MON-003. Capacity is watched per salon through request rates and DEP-01 quota alerts MON-005. A salon that repeatedly exceeds its fair share is reviewed by the PM and engineering lead; no hard per-salon quota is enforced in R1 under EX-01.

## 6. Tenant Lifecycle

| Event | Handling |
|---|---|
| Onboarding / provisioning | Owner signs up, creates the salon and publishes a booking link as part of US-004 |
| Configuration changes and feature flags | Owner edits services, staff and hours; the public booking-link flag is controlled by operations |
| Migration between isolation tiers | Not offered in R1; a future change needs an ADR |
| Suspension | Manual, following non-payment or abuse, with the booking link disabled and the owner calendar preserved |
| Export and offboarding | Booking data exported to the owner on request under NFR-004 |
| Deletion | Salon data removed from live store and backups per [Privacy Requirements](../../08-security/privacy-requirements.md) and the backup deletion log |

## 7. Verification

| Test | Method | Frequency |
|---|---|---|
| Cross-salon access attempts on booking and owner paths | Negative tests in TC-001 and TC-008 | Every change and before release |
| Tenant-isolation review in design and code review | Checklist referencing SR-002 | Each feature |
| Manual isolation review with tenant scope | Planned before launch and yearly, not yet performed | Before 2027-03-05 |
| Noisy neighbour load test | TS-005 with a second synthetic salon | Before release |

## Completion Criteria

- [x] Tenant, hierarchy and membership rules are defined.
- [x] The isolation model is chosen against explicit requirements and recorded as an ADR.
- [x] Enforcement is described at every layer, including jobs, caches and admin access.
- [x] Noisy-neighbour controls and tenant lifecycle (including deletion) are defined.
- [x] Cross-tenant tests are part of the Test Strategy.
