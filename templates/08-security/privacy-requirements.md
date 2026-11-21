---
id: DPP-08-privacy-requirements
title: Privacy Requirements
domain: 08-security
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [legal, security-lead, engineering-lead, designer]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [data-classification, data-model]
feeds: [security-requirements, compliance-assessment, user-stories, event-tracking-plan, backup-and-recovery, data-governance]
applies_to: [all]
---

# Privacy Requirements: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Specifies how the product collects, uses, shares, retains and deletes **personal data**, and how individuals can exercise their rights, so privacy is designed in and traceable to requirements rather than added at launch. |
| **When to use** | Whenever the product processes data about identifiable people (customers, staff, end users, analytics identifiers). Skip only if you can demonstrate there is no personal data. |
| **Owner** | Product Manager, with Legal or a privacy advisor. |
| **Required inputs** | [Data Classification](data-classification.md) inventory; [Data Model](../05-architecture/data-model.md); [Integration Specification](../05-architecture/integration-specification.md) (processors, vendors); analytics needs from the [Event Tracking Plan](../10-analytics/event-tracking-plan.md). |
| **Related documents** | [Security Requirements](security-requirements.md) · [Compliance Assessment](compliance-assessment.md) · [Backup & Recovery](../09-release-ops/backup-and-recovery.md) · [Data Governance](../../packages/enterprise/data-governance.md) (enterprise package) |

</details>

> **Guidance:** **This template is not legal advice.** Privacy obligations depend on where your users and your organisation are, and on what you do with the data. Identify the laws and regulations that apply (the list in section 2 is a prompt, not a determination) and have a qualified person confirm the interpretation. Record the **authoritative source and the date checked** for every legal or contractual obligation; never paraphrase a law from memory as a requirement. Design for **data minimisation**: if you do not need it, do not collect it.

## 1. Personal Data Inventory

| ID | Data element | Whose data | Purpose of use | Necessary? (why) | Source | Sensitivity | Shared with | Retention |
|---|---|---|---|---|---|---|---|---|
| PD-01 | Customer name | End customer | Identify the booking | Yes | Customer | Confidential | Business owner | [Period] |
| PD-02 | Customer phone | End customer | Send confirmations and reminders | Yes (FR-002) | Customer | Confidential | Messaging provider | [Period] |
| PD-03 | Device identifier in analytics | End customer | Measure funnel (MET-02) | Review: could aggregate instead | Automatic | Internal | Analytics provider | [Period] |

*Special or sensitive categories of data (as defined in the laws that apply to you): record whether any are collected, and the extra obligations identified.*

## 2. Applicable Obligations (to be identified and verified)

> **Guidance:** Complete with a privacy or legal advisor. Examples of what to look for are given as prompts only.

| Jurisdiction / sector | Law, regulation or contract (name, version) | Applies? (why) | Key obligations identified | Source link | Verified by / date |
|---|---|---|---|---|---|
| [Where users are located] | [e.g. a general data-protection regulation such as the EU GDPR, if it applies] | | | | |
| [Where the company operates] | [Local data-protection or consumer law] | | | | |
| [Sector rules] | [e.g. health, finance, children, if relevant] | | | | |
| [Customer contracts] | [Data processing terms] | | | | |

## 3. Privacy Requirements Catalog

| ID | Topic | Requirement | Source | Priority | Verification |
|---|---|---|---|---|---|
| NFR-0xx | Notice | Users must be told what data is collected, why, and by whom at or before collection, in plain language | [Obligation / policy] | Must | Inspection |
| NFR-0xx | Consent / basis | The basis for each purpose is recorded; where consent is the basis it is explicit, specific, recorded and as easy to withdraw as to give | [Obligation] | Must | Test |
| NFR-0xx | Minimisation | Only data in PD-01…PD-nn is collected; new fields need review | Policy | Must | Inspection |
| NFR-0xx | Retention | Personal data is deleted or anonymised at the end of its retention period, including backups within [N] days | [Obligation / policy] | Must | Test |
| NFR-0xx | Rights handling | Access, correction, deletion and portability requests (as applicable) can be received, verified and fulfilled within [time limit set by applicable law] | [Obligation] | Must | Test |
| NFR-0xx | Processors | Every vendor processing personal data has a signed agreement and an entry in the Integration Specification | [Obligation] | Must | Inspection |
| NFR-0xx | Cross-border transfer | Transfers outside the region of origin are identified and have a documented mechanism | [Obligation] | Must | Inspection |
| NFR-0xx | Breach handling | Suspected personal-data breaches are triaged, assessed and notified within legal time limits | [Obligation] | Must | Exercise |

Use `NFR-` IDs (category *Privacy*) so requirements join the main chain; summarise them in the NFR document.

## 4. Individual Rights Handling

| Right (as applicable) | How a request is received | Identity check | Systems to search / act on | Owner | Response time |
|---|---|---|---|---|---|
| Access | [Form / e-mail] | | | | [Per law] |
| Correction | | | | | |
| Deletion | | | Data store, backups, logs, vendors | | |
| Portability | | | | | |
| Objection / withdrawal | | | | | |

## 5. Processors, Sharing and Transfers

| Recipient | Role (processor / controller / joint) | Data | Purpose | Agreement | Location | Transfer mechanism |
|---|---|---|---|---|---|---|
| Messaging provider | Processor | PD-02 | Delivery | [Reference] | [Region] | [If applicable] |

## 6. Design Implications

[Features and flows that exist because of privacy: consent prompts, preference centre, deletion tools, masked support views, data export. Reference stories (US-) and screens (S-).]

## 7. Open Questions

| ID | Question | Owner | Due |
|---|---|---|---|
| Q-xx | [e.g. Is a privacy impact assessment required for this product?] | [Name] | [Date] |

## Completion Criteria

- [ ] Every personal data element has a purpose, a justification and a retention period.
- [ ] Applicable laws and contracts are identified with sources and a named reviewer; none are asserted from memory.
- [ ] Requirements cover notice, basis or consent, minimisation, retention, rights handling, processors, transfers and breach handling.
- [ ] Each vendor processing personal data is listed with its agreement and location.
- [ ] Requirements are traceable to stories, design and tests.
- [ ] This document does not claim legal compliance; it records decisions and evidence for a qualified reviewer.
