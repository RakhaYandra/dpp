---
id: SLOTWISE-08-privacy-requirements
title: Privacy Requirements
domain: 08-security
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [legal, security-lead, engineering-lead, designer]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [data-classification, data-model]
feeds: [security-requirements, compliance-assessment, user-stories, event-tracking-plan, backup-and-recovery, data-governance]
applies_to: [all]
---

# Privacy Requirements: SlotWise

## 1. Personal Data Inventory

| ID | Data element | Whose data | Purpose of use | Necessary? (why) | Source | Sensitivity | Shared with | Retention |
|---|---|---|---|---|---|---|---|---|
| PD-01 | Customer name | End customer (PER-02) | Identify the booking for the salon | Yes, the owner needs to know who is arriving | Customer at booking | Confidential | Business owner (PER-01) | 90 days after appointment |
| PD-02 | Customer phone | End customer (PER-02) | Send confirmations and reminders under FR-002 | Yes, it is the delivery channel chosen by the customer | Customer at booking | Confidential | DEP-01 messaging provider | 90 days after appointment, deletion on request within 30 days |
| PD-03 | Pseudonymous session identifier in analytics | End customer (PER-02) | Measure the booking funnel for MET-02 | Needed for funnel measurement, but aggregated booking source data is preferred where it answers the question | Generated automatically | Internal | Reporting dashboard only | 12 months |

SlotWise does not knowingly collect special category data in R1. Customers are not asked for health or identity documents, and payments are excluded by DEC-001.

## 2. Applicable Obligations (to be identified and verified)

| Jurisdiction / sector | Law, regulation or contract (name, version) | Applies? (why) | Key obligations identified | Source link | Verified by / date |
|---|---|---|---|---|---|
| Location of the three pilot salons | Law applicable where pilot salons operate, to be identified by qualified counsel | To be confirmed before the pilot starts | Notice, lawful basis, retention, individual rights | [OPEN: product-manager, 2026-12-15] | [OPEN: product-manager, 2026-12-15] |
| Company operating location | Local data-protection and consumer law, to be identified by qualified counsel | To be confirmed before the pilot starts | Notices, deletion requests, complaint handling | [OPEN: product-manager, 2026-12-15] | [OPEN: product-manager, 2026-12-15] |
| DEP-01 provider agreement | Data processing terms and current version | Applies because PD-02 is shared with the provider | Processor duties, breach notice, sub-processors | Provider account documents | [OPEN: engineering-lead, 2026-12-15] |
| Pilot salon terms | Signed pilot agreement | Applies to owner access to customer data | Confidentiality and permitted use | PM records | 2027-02-05 |

This document records questions and evidence for a qualified reviewer. It does not assert legal compliance.

## 3. Privacy Requirements Catalog

All rows are facets of NFR-004, the single privacy NFR in [Non-Functional Requirements](../03-requirements/non-functional-requirements.md). A new privacy NFR needs an approved change to that document; no new NFR IDs are created here.

| ID | Topic | Requirement | Source | Priority | Verification |
|---|---|---|---|---|---|
| NFR-004 | Notice | The booking form states that the name and phone number are used for booking messages and shows who sends them, before the customer submits | NFR-004, US-001 | Must | Inspection |
| NFR-004 | Consent / basis | The customer agrees to booking messages at submission; withdrawal is possible by cancelling the booking or contacting the salon | NFR-004, AC-003.1 | Must | TC-006 |
| NFR-004 | Minimisation | Only PD-01 to PD-03 are collected; a new field needs PM and security review before it is added | NFR-004 | Must | Inspection |
| NFR-004 | Retention | Personal data is anonymised or deleted 90 days after the appointment and on request within 30 days, including backup copies as described in [Backup & Recovery](../09-release-ops/backup-and-recovery.md) | NFR-004 | Must | TC-006 |
| NFR-004 | Rights handling | Access, correction and deletion requests are received, verified and answered within 30 days | NFR-004 | Must | TC-006 |
| NFR-004 | Processors | DEP-01 has signed processing terms before any real phone number is sent | DEP-01 | Must | Inspection |
| NFR-004 | Cross-border transfer | The location where DEP-01 processes PD-02 is identified and a mechanism is documented before pilot launch | DEP-01 | Must | Inspection |
| NFR-004 | Breach handling | Suspected personal-data breaches are triaged under the [Incident Management Plan](../09-release-ops/incident-management.md) with a named notifier | NFR-004 | Must | Exercise |

## 4. Individual Rights Handling

| Right (as applicable) | How a request is received | Identity check | Systems to search / act on | Owner | Response time |
|---|---|---|---|---|---|
| Access | Customer contacts the salon or the product contact address | Booking link token or salon-confirmed details | Booking data store, DEP-01 message log | PM | 30 days |
| Correction | Customer contacts the salon | Booking link token | Booking data store | PM | 30 days |
| Deletion | Customer contacts the salon or uses the cancellation link | Booking link token | Booking data store, backups, logs, DEP-01 | PM | 30 days, per NFR-004 |
| Portability | Customer requests a copy of their booking record | Salon-confirmed details | Booking data store | PM | 30 days |
| Objection / withdrawal | Customer cancels the booking or contacts the salon | Booking link token | Message queue and DEP-01 | PM | Next business day |

## 5. Processors, Sharing and Transfers

| Recipient | Role (processor / controller / joint) | Data | Purpose | Agreement | Location | Transfer mechanism |
|---|---|---|---|---|---|---|
| DEP-01 messaging provider | Processor | PD-02 | Delivery of confirmations and reminders | [OPEN: engineering-lead, 2026-12-15] | [OPEN: engineering-lead, 2026-12-15] | [OPEN: engineering-lead, 2026-12-15] |
| Pilot salon owner (PER-01) | Controller for their own customer list | PD-01, PD-02 | Running the salon calendar | Pilot salon agreement, due 2027-02-05 | Pilot salon location | Not applicable |

## 6. Design Implications

The booking form carries a short notice and consent line before submission, taken from US-001 and AC-001.3. The cancellation link supports withdrawal of consent under US-003 and AC-003.1. Support views mask PD-02 until approval under SR-007. A deletion action is available to the PM for rights requests under NFR-004. The relevant screens are the booking entry and confirmation screens in the agreed information architecture. EVT-001 to EVT-003 carry no direct identifiers, per the [Event Tracking Plan](../10-analytics/event-tracking-plan.md).

## 7. Open Questions

| ID | Question | Owner | Due |
|---|---|---|---|
| [OPEN: product-manager, 2026-12-15] | Is a privacy impact assessment required for this pilot? | PM | 2026-12-15 |

## Completion Criteria

- [x] Every personal data element has a purpose, a justification and a retention period.
- [ ] Applicable laws and contracts are identified with sources and a named reviewer; none are asserted from memory.
- [x] Requirements cover notice, basis or consent, minimisation, retention, rights handling, processors, transfers and breach handling.
- [x] Each vendor processing personal data is listed with its agreement and location.
- [x] Requirements are traceable to stories, design and tests.
- [x] This document does not claim legal compliance; it records decisions and evidence for a qualified reviewer.
