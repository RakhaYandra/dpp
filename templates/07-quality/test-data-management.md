---
id: DPP-07-test-data-management
title: Test Data Management
domain: 07-quality
tier: optional
status: draft
version: 0.1.0
owner: qa-lead
contributors: [engineering-lead, security-lead, data-engineer]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [test-strategy, data-model]
feeds: [test-plan, test-case, performance-test-plan, security-test-plan]
applies_to: [all]
---

# Test Data Management: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines what data testing needs, where it comes from, how it is created, protected, refreshed and removed. Prevents unreliable tests and, above all, personal or sensitive data leaking into non-production environments. |
| **When to use** | When tests need more than trivial data: realistic volumes, relationships, time-dependent data, or personal data is involved. Small products can reduce this to the rules in sections 2–3. |
| **Owner** | QA Lead, with Security and Engineering. |
| **Required inputs** | [Data Model](../05-architecture/data-model.md); [Data Classification](../08-security/data-classification.md); [Privacy Requirements](../08-security/privacy-requirements.md); [Test Strategy](test-strategy.md). |
| **Related documents** | [Test Plan](test-plan.md) · [Test Case](test-case.md) · [Performance Test Plan](performance-test-plan.md) · [Environment Strategy](../09-release-ops/environment-strategy.md) |

</details>

> **Guidance:** The default rule is **no real personal data outside production**. If you ever need production-derived data, it must be irreversibly anonymized or masked, approved by the data owner, and handled under your privacy obligations (verify these with qualified advice). Prefer **synthetic data generated from the data model** because it is safe, repeatable and can be created at any volume.

## 1. Data Needs

| ID | Data set | Used by (scenario / test type) | Entities (from Data Model) | Volume | Characteristics (edge cases, time dependence) |
|---|---|---|---|---|---|
| DS-booking-01 | Services with open and full slots across two time zones | TS-001–TS-006 | Service, Slot | 20 services, 2,000 slots | Includes last slot of day, daylight-saving boundary |
| DS-perf-01 | Production-like volume | TS-030, TS-031 | Business, Booking, Customer | 500 businesses, 1 M bookings | Skewed distribution: 5% of businesses hold 50% of bookings |

## 2. Sourcing Rules

| Source | Allowed? | Conditions |
|---|---|---|
| Synthetic generation | **Preferred** | Generated from schema and rules; deterministic seeds for repeatability |
| Hand-crafted fixtures | Yes | For specific edge cases; stored in version control |
| Anonymized / masked production data | Only with approval | Irreversible; re-identification risk assessed; approved by [data owner]; documented below |
| Raw production data | **Not allowed** outside production | — |
| Public datasets | If licence permits | Record licence |

## 3. Protection Rules by Classification

| Classification (see [Data Classification](../08-security/data-classification.md)) | In test environments |
|---|---|
| Public / internal | Allowed |
| Confidential (e.g. contact details) | Synthetic only; realistic format, fictitious values |
| Restricted (e.g. credentials, payment data) | Never real; use provider test credentials and documented test values |

Also: test accounts and credentials are not shared with production, are rotated, and are removed after use.

## 4. Masking and Anonymization (only if production-derived data is approved)

| Field | Technique | Validation |
|---|---|---|
| Phone | Replace with generated value in valid format | No real numbers remain; format checks pass |
| Free text | Remove or replace | |

Approval record: [Who approved, when, scope, retention, deletion date.]

## 5. Provisioning and Refresh

| Item | Approach |
|---|---|
| How data is loaded | [Scripted seed; reproducible from version control] |
| Reset between runs | [Per test, per suite, nightly] |
| Refresh schedule | [When and by whom] |
| Time-dependent data | [Relative dates generated at load time] |
| Data for third-party sandboxes | [Provider test values] |
| Environment parity | [How closely volumes and distributions match production; see [Environment Strategy](../09-release-ops/environment-strategy.md)] |

## 6. Ownership and Retention

| Data set | Owner | Retention | Deletion method |
|---|---|---|---|

## 7. Risks

| ID | Risk | Mitigation |
|---|---|---|
| RISK-xx | Test data drifts from the schema and tests fail for the wrong reason | Generate from schema; validate on each release |

## Completion Criteria

- [ ] Each test type has identified data sets with volume and edge-case characteristics.
- [ ] The no-real-personal-data rule and any exception process are explicit.
- [ ] Protection rules match the data classification.
- [ ] Data creation is scripted and repeatable; refresh and reset are defined.
- [ ] Ownership, retention and deletion are assigned.
