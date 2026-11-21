---
id: DPP-08-data-classification
title: Data Classification
domain: 08-security
tier: recommended
status: draft
version: 0.1.0
owner: security-lead
contributors: [product-manager, engineering-lead, legal]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [architecture-overview, data-model]
feeds: [security-requirements, privacy-requirements, threat-model, access-control-matrix, backup-and-recovery, test-data-management]
applies_to: [all]
---

# Data Classification: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines how sensitive each kind of data is and the handling rules that follow from its level, so protection effort is proportionate and consistent across storage, access, sharing, logging, testing and backup. |
| **When to use** | After the data model is drafted; before security requirements and test-data planning. Keep it short: a classification nobody remembers is worthless. |
| **Owner** | Security Lead, with data owners from the business. |
| **Required inputs** | [Data Model](../05-architecture/data-model.md) entities and fields; [Architecture Overview](../05-architecture/architecture-overview.md) data overview; contractual and legal obligations ([Compliance Assessment](compliance-assessment.md)). |
| **Related documents** | [Security Requirements](security-requirements.md) · [Privacy Requirements](privacy-requirements.md) · [Backup & Recovery](../09-release-ops/backup-and-recovery.md) · [Test Data Management](../07-quality/test-data-management.md) |

</details>

> **Guidance:** Use **three or four levels at most**; the names below are a common pattern, not a standard. Classify by **harm if the data is disclosed, altered or lost**, then attach rules. Personal data is covered in more detail in [Privacy Requirements](privacy-requirements.md); a field can be both *Confidential* and *personal data*. When in doubt, classify higher and review.

## 1. Classification Scheme

| Level | Definition | Example (SlotWise) | Harm if exposed |
|---|---|---|---|
| **Public** | Intended for anyone | Service names and prices on the booking page | None |
| **Internal** | Not secret, but not for outsiders | Aggregate usage statistics, internal documentation | Low |
| **Confidential** | Disclosure causes harm to individuals or the business | Customer names and phone numbers, booking history | Significant |
| **Restricted** | Disclosure causes severe harm or breaks obligations | Credentials, tokens, secrets, payment-related data held in the system | Severe |

## 2. Handling Rules by Level

| Rule | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Storage encryption | Not required | Recommended | Required | Required, with managed keys |
| Transport encryption | Required | Required | Required | Required |
| Who may access | Anyone | Staff | Need-to-know, role-based | Named individuals / services, audited |
| Allowed in logs and error messages | Yes | Yes | **No** (mask or omit) | **Never** |
| Allowed in non-production environments | Yes | Yes | Only masked or synthetic | Never |
| Sharing with third parties | Free | Approval | Contract and approval | Prohibited unless explicitly approved |
| Backup protection | Standard | Standard | Encrypted; access controlled | Encrypted; separate access |
| Retention and deletion | Per policy | Per policy | Defined limit, secure deletion | Minimal, secure deletion |
| Labelling | Not needed | Document header | Document and dataset label | Document and dataset label |

*Adjust the table to your context; each cell becomes one or more `SR-` requirements.*

## 3. Data Inventory and Classification

| Data set | Entity / field (see Data Model) | Level | Personal data? | Owner | Stored in | Shared with | Retention | Notes |
|---|---|---|---|---|---|---|---|---|
| Customer contact details | Customer.phone, Customer.name | Confidential | Yes | Product | Primary data store; backups | Messaging provider | [Period] | Consent basis in Privacy Requirements |
| Booking records | Booking.* | Internal | Indirectly | Product | Primary data store | — | [Period] | Linked to customer, so treat as Confidential when joined |
| Authentication secrets | Credential.* | Restricted | No | Engineering | Identity service | — | Life of account | |
| Application logs | — | Internal | Must not contain personal data | Engineering | Log store | — | [Period] | See SR-007 |

## 4. Special Cases

| Case | Rule |
|---|---|
| Derived or combined data (e.g. joined data sets) | Takes the highest level of its components unless de-identified and reviewed |
| Aggregated or anonymised data | Define the test for "anonymous"; review for re-identification risk |
| Data from third parties | Classified on receipt; contract terms apply |
| Test and training data | Synthetic or masked; never copied from production without approval |

## 5. Ownership and Review

| Item | Rule |
|---|---|
| Data owner responsibilities | Approve classification, access and sharing |
| Review cadence | [Annually and on each new data type] |
| Reclassification process | [Request → owner approval → update inventory and tests] |

## Completion Criteria

- [ ] The scheme has few levels, each defined by harm, with an example.
- [ ] Handling rules exist for storage, transit, access, logging, non-production use, sharing, backup and deletion.
- [ ] Every data entity in the data model appears in the inventory with a level and an owner; personal data is flagged.
- [ ] Derived and aggregated data rules are defined.
- [ ] Rules are reflected in `SR-` requirements and test-data rules.
