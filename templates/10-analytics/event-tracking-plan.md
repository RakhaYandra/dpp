---
id: DPP-10-event-tracking-plan
title: Event Tracking Plan
domain: 10-analytics
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [data-analyst, engineering-lead, designer, privacy-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [analytics-plan, user-flow, privacy-requirements]
feeds: [user-stories, test-scenarios, working-agreements, post-launch-review]
applies_to: [all]
---

# Event Tracking Plan: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | The specification of every analytics event: when it fires, what it carries and why it exists, so engineering implements it consistently and analysts can trust the data. Canonical home for `EVT-` IDs. |
| **When to use** | Before implementation of any flow that must be measured; update whenever tracking changes. |
| **Owner** | Product Manager with an analyst. |
| **Required inputs** | [Analytics Plan](analytics-plan.md) metric definitions; [User Flow](../04-ux-ui/user-flow.md); [Privacy Requirements](../08-security/privacy-requirements.md). |
| **Related documents** | [Wireframe Spec](../04-ux-ui/wireframe-spec.md) · [User Stories](../03-requirements/user-stories.md) · [Working Agreements](../06-project-mgmt/working-agreements.md) (Definition of Done) |

</details>

> **Guidance:** Track **few, well-defined events** that answer the questions in the Analytics Plan; every event must feed at least one metric. Use consistent naming (`object_action`, lowercase, past tense). **Never put personal data or free text in event properties** unless the privacy requirements allow it.

## 1. Naming and Property Conventions

| Topic | Convention |
|---|---|
| Event name | `object_action` in snake_case, e.g. `booking_confirmed` |
| Property names | snake_case; units in name where relevant (`duration_min`) |
| Timestamps | UTC, ISO 8601, generated server-side where possible |
| Identifiers | Pseudonymous account and session ids only |
| Versioning | `schema_version` property; never reuse an event name with a changed meaning |
| Environments | Events from non-production are labelled and excluded from reports |

## 2. Common Properties (sent with every event)

| Property | Type | Description | PII? |
|---|---|---|---|
| timestamp | datetime | When the event occurred | No |
| session_id | string | Pseudonymous session | No |
| account_id | string | Business account (not a person) | No |
| platform | enum | web / ios / android | No |
| schema_version | integer | | No |

## 3. Event Catalog

| ID | Event name | Trigger (exactly when) | Source | Properties | Feeds metric | Flow / screen | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| EVT-001 | `service_selected` | Customer selects a service on S-01 | Client | service_id | MET-02 funnel | UF-01 / S-01 | PM | Specified |
| EVT-002 | `booking_confirmed` | Server confirms a reservation | Server | booking_source (enum), lead_time_h | MET-02 | UF-01 / S-04 | PM | Specified |
| EVT-004 | `booking_completed` | Owner marks completed | Server | | MET-01 | | | |
| EVT-005 | `booking_no_show` | Owner marks no-show | Server | | MET-01 | | | |

### Property Detail (key events)

| Event | Property | Type | Allowed values | Required | PII? | Notes |
|---|---|---|---|---|---|---|
| `booking_confirmed` | booking_source | enum | customer, owner | Yes | No | |

## 4. Funnels and Reports Supported

| Funnel | Steps (EVT-) | Metric |
|---|---|---|
| Customer booking | EVT-001 → EVT-002 | Conversion |

## 5. Implementation and Validation

| Topic | Rule |
|---|---|
| Implementation rule | Server-side where an event reflects a business fact; client-side for interaction events |
| QA | Each event verified in test environment before release (see [Test Scenarios](../07-quality/test-scenarios.md)) |
| Monitoring | Alert if volume of key events drops unexpectedly |
| Consent | Events are suppressed or anonymized when consent is not given, per privacy requirements |
| Change process | Changes via pull request; analyst reviews |

## Completion Criteria

- [ ] Every metric in the Analytics Plan has events (or another source) that feed it.
- [ ] Every event has a precise trigger, owner, properties and a metric it supports.
- [ ] No event carries personal data or free text beyond what privacy requirements allow.
- [ ] Naming, versioning and implementation rules are defined.
- [ ] Events are included in the Definition of Done and test scenarios.
