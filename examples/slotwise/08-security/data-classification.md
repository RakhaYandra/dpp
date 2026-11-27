---
id: SLOTWISE-08-data-classification
title: Data Classification
domain: 08-security
tier: recommended
status: draft
version: 0.1.0
owner: security-lead
contributors: [product-manager, engineering-lead, legal]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [architecture-overview, data-model]
feeds: [security-requirements, privacy-requirements, threat-model, access-control-matrix, backup-and-recovery, test-data-management]
applies_to: [all]
---

# Data Classification: SlotWise

## 1. Classification Scheme

| Level | Definition | Example (SlotWise) | Harm if exposed |
|---|---|---|---|
| **Public** | Intended for anyone | Service names, prices and open slots on the booking page | None |
| **Internal** | Not secret, but not for outsiders | Aggregate booking counts, internal planning documents | Low |
| **Confidential** | Disclosure causes harm to individuals or the business | Customer names and phone numbers, booking history joined to a customer | Significant |
| **Restricted** | Disclosure causes severe harm or breaks obligations | Owner credentials, booking-link tokens, secrets, provider API keys | Severe |

## 2. Handling Rules by Level

| Rule | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Storage encryption | Not required | Recommended | Required | Required, with managed keys |
| Transport encryption | Required | Required | Required | Required |
| Who may access | Anyone | Team | Need-to-know, role-based | Named individuals or services, audited |
| Allowed in logs and error messages | Yes | Yes | No, mask or omit | Never |
| Allowed in non-production environments | Yes | Yes | Only masked or synthetic | Never |
| Sharing with third parties | Free | Approval | Contract and approval | Prohibited unless explicitly approved |
| Backup protection | Standard | Standard | Encrypted, access controlled | Encrypted, separate access |
| Retention and deletion | Per policy | Per policy | 90 days after appointment, or on request within 30 days | Minimal, secure deletion |
| Labelling | Not needed | Document header | Document and dataset label | Document and dataset label |

These cells become the SR- requirements in [Security Requirements](security-requirements.md), mainly SR-003, SR-004 and SR-007.

## 3. Data Inventory and Classification

| Data set | Entity / field (see Data Model) | Level | Personal data? | Owner | Stored in | Shared with | Retention | Notes |
|---|---|---|---|---|---|---|---|---|
| Customer contact details | Customer.phone, Customer.name | Confidential | Yes | Product | Primary data store and backups | DEP-01 messaging provider | 90 days after appointment, deletion on request within 30 days per NFR-004 | Consent basis in [Privacy Requirements](privacy-requirements.md) |
| Booking records | Booking.id, Booking.status, Booking.start_time | Internal | Indirectly | Product | Primary data store | Not shared | 13 months | Becomes Confidential when joined with customer details |
| Owner credentials and booking-link tokens | Credential fields and booking link tokens | Restricted | No | Engineering | Identity store and booking service | Not shared | Life of account or booking | Rotation under SR-004 |
| Application and audit logs | Structured log events | Internal | Must not contain personal data | Engineering | Log store | Not shared | 30 days | Masking rules in [Observability Strategy](../09-release-ops/observability-strategy.md) |
| Analytics events | EVT-001, EVT-002 and EVT-003 properties | Internal | Pseudonymous identifiers only | Product | Analytics store | Reporting dashboards | 12 months | No phone numbers or free text |

## 4. Special Cases

| Case | Rule |
|---|---|
| Derived or combined data, for example a booking joined to a customer | Takes the highest level of its components, so Confidential |
| Aggregated or anonymised data | Counts as anonymous only after review for re-identification; salon-level counts with at least 3 salons are Internal |
| Data from third parties | Classified on receipt; DEP-01 contract terms apply |
| Test and training data | Synthetic only; never copied from production without PM and security approval |

## 5. Ownership and Review

| Item | Rule |
|---|---|
| Data owner responsibilities | Approve classification, access and sharing for their data set |
| Review cadence | Every 12 months and whenever a new data type is added |
| Reclassification process | Security lead requests a change, data owner approves, inventory and related tests are updated |

## Completion Criteria

- [x] The scheme has few levels, each defined by harm, with an example.
- [x] Handling rules exist for storage, transit, access, logging, non-production use, sharing, backup and deletion.
- [x] Every data entity in the data model appears in the inventory with a level and an owner; personal data is flagged.
- [x] Derived and aggregated data rules are defined.
- [x] Rules are reflected in `SR-` requirements and test-data rules.
