---
id: SLOTWISE-10-event-tracking-plan
title: Event Tracking Plan
domain: 10-analytics
tier: recommended
status: draft
version: 0.1.0
owner: product-manager
contributors: [data-analyst, engineering-lead, designer, privacy-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [analytics-plan, user-flow, privacy-requirements]
feeds: [user-stories, test-scenarios, working-agreements, post-launch-review]
applies_to: [all]
---

# Event Tracking Plan: SlotWise

## 1. Naming and Property Conventions

| Topic | Convention |
|---|---|
| Event name | `object_action` in snake_case, for example `booking_confirmed` |
| Property names | snake_case; units in the name where relevant, for example `lead_time_min` |
| Timestamps | UTC, ISO 8601, generated server-side where possible |
| Identifiers | Pseudonymous salon account and session ids only, never customer names or phone numbers |
| Versioning | `schema_version` property; an existing event name is never reused with a changed meaning |
| Environments | Events from non-production are labelled and excluded from reports |

## 2. Common Properties (sent with every event)

| Property | Type | Description | PII? |
|---|---|---|---|
| timestamp | datetime | When the event occurred | No |
| session_id | string | Pseudonymous session | No |
| account_id | string | Salon account, not a person | No |
| platform | enum | web only in R1 | No |
| schema_version | integer | Starts at 1 for R1 | No |

## 3. Event Catalog

| ID | Event name | Trigger (exactly when) | Source | Properties | Feeds metric | Flow / screen | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| EVT-001 | `service_selected` | Customer selects a service on the booking entry screen | Client | service_id, salon_id | MET-02 funnel | UF-01, booking entry screen | PM | Specified |
| EVT-002 | `booking_confirmed` | The booking service commits a reservation after the uniqueness guard in ADR-0001 | Server | booking_source, lead_time_min, salon_id | MET-02 | UF-01, confirmation screen | PM | Specified |
| EVT-003 | `booking_status_marked` | Owner saves a completed or no-show status for a past appointment | Server | status, salon_id | MET-01 | UF-03, owner calendar | PM | Specified |

### Property Detail (key events)

| Event | Property | Type | Allowed values | Required | PII? | Notes |
|---|---|---|---|---|---|---|
| `booking_confirmed` | booking_source | enum | customer, owner | Yes | No | Set from the creation path in API-002 |
| `booking_confirmed` | lead_time_min | integer | 0 to 10080 | Yes | No | Minutes between confirmation and start time |
| `booking_status_marked` | status | enum | completed, no_show | Yes | No | Derived from AC-005.1, never a free-text field |
| `service_selected` | service_id | string | Salon service identifier | Yes | No | Opaque identifier |

## 4. Funnels and Reports Supported

| Funnel | Steps (EVT-) | Metric |
|---|---|---|
| Customer booking | EVT-001 then EVT-002 | MET-02 and conversion from selection to confirmation |
| Appointment outcome | EVT-002 then EVT-003 | MET-01, using the status property |

## 5. Implementation and Validation

| Topic | Rule |
|---|---|
| Implementation rule | Server-side for EVT-002 and EVT-003 because they are business facts; client-side for EVT-001 interaction |
| QA | Each event payload is verified in the test environment before release, using TC-001 for EVT-001 and EVT-002 and TC-009 for EVT-003 |
| Monitoring | MON-005 alerts if daily EVT-002 volume drops by more than 50% compared with the previous week |
| Consent | Events are suppressed or anonymised when consent is not given, per NFR-004 and [Privacy Requirements](../08-security/privacy-requirements.md) |
| Change process | Changes go through a pull request and are reviewed by the data analyst and PM |

## Completion Criteria

- [x] Every metric in the Analytics Plan has events (or another source) that feed it.
- [x] Every event has a precise trigger, owner, properties and a metric it supports.
- [x] No event carries personal data or free text beyond what privacy requirements allow.
- [x] Naming, versioning and implementation rules are defined.
- [x] Events are included in the Definition of Done and test scenarios.
