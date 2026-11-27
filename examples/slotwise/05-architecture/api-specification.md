---
id: SLOTWISE-05-api-specification
title: API Specification
domain: 05-architecture
tier: recommended
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [developers, qa-lead, technical-writer]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [architecture-overview, data-model, authentication-authorization]
feeds: [test-strategy, integration-specification, api-lifecycle-and-versioning, rate-limiting-and-quotas, webhook-specification]
applies_to: [all]
---

# API Specification: SlotWise

## 1. Overview

| | |
|---|---|
| **Consumers** | SlotWise booking web app (public customer pages and the signed-in owner area) |
| **Style** | REST, resource oriented (ADR-0003 for public access and ADR-0005 for ownership checks) |
| **Contract file and format** | OpenAPI document, path is [OPEN: engineering-lead, 2026-12-15] |
| **Base address and environments** | Per environment; see [Environment Strategy](../09-release-ops/environment-strategy.md) |
| **Audience** | Internal only. No partner or public developer API in R1. |

## 2. Conventions

| Topic | Decision |
|---|---|
| Naming (resources, fields, casing) | Lowercase plural resource paths and snake_case JSON fields |
| Identifiers | Opaque, non-sequential and stable; no database sequence in URLs |
| Request/response format | JSON with UTF-8, `Content-Type: application/json` |
| Date, time, currency, locale formats | ISO 8601 UTC timestamps; no currency fields because payments are out of scope (DEC-001) |
| Pagination | Cursor based on slot ID, default limit 20, maximum 100 |
| Filtering, sorting, field selection | Filter by service and date on slot list; ascending start time only |
| Idempotency | `Idempotency-Key` header required on booking create; repeated key returns the first result |
| Concurrency control | Uniqueness rule on staff and start time inside one transaction (ADR-0001) |
| Bulk operations | None in R1 |
| Versioning | Path prefix `/v1`; changes that remove a field or change a status code wait for `/v2` |
| Compatibility policy | Adding an optional response field or a new error code is not breaking |

## 3. Authentication, Authorization and Limits

Public operations are slot lookup and booking create with a contact details check; they are rate limited. Cancel, reschedule and booking detail require the signed manage token from the message (ADR-0003). Owner operations require a signed-in owner session and a business ownership check (ADR-0005). Full rules are in [Authentication & Authorization](authentication-authorization.md). Rate-limit thresholds are [OPEN: engineering-lead, 2026-12-15] and are not taken from another package.

## 4. Resource and Operation Catalog

| ID | Resource | Operation | Purpose | Access | Idempotent | Story / FR | Notes |
|---|---|---|---|---|---|---|---|
| API-001 | Slots | List available slots | Show open times for a service and date | Public | Yes | US-001 / FR-001 | Filter by service and date; cursor pagination |
| API-002 | Bookings | Create booking | Reserve one slot without an account | Public, rate limited | With key | US-001, US-002 / FR-001, FR-002 | 409 on conflict under BR-002 |
| API-003 | Bookings | Cancel booking | Free a slot from the manage link | Manage token | Yes | US-003 / FR-003 | 409 after cutoff; ADR-0004 |
| API-004 | Bookings | Reschedule booking | Move a booking to another slot | Manage token | With key | US-003 / FR-003 | Releases the old slot in one transaction |
| API-005 | Availability | Update hours, time off, staff and services | Publish real availability | Owner session | Yes | US-004 / FR-004 | Warns on conflict with a booking |
| API-006 | Bookings | Mark completed or no-show | Record attendance | Owner session | Yes | US-005 / FR-005 | Counts no-show in MET-01 |

### Operation detail (key operations only)

**API-002: Create booking**

| Aspect | Specification |
|---|---|
| Input | Slot identifier, customer name, phone or email, `Idempotency-Key` header |
| Success | `201` with booking identifier, status, service, start and end time |
| Validation | Name 1 to 80 characters; phone or email format (BR-006) |
| Errors | `validation_error` 422; `slot_unavailable` 409; `rate_limited` 429; `server_error` 500 |
| Side effects | Confirmation and reminder messages enqueued (ADR-0002), EVT-002 emitted on success |
| Business rules | BR-001, BR-002, BR-003 |

**API-003: Cancel booking**

| Aspect | Specification |
|---|---|
| Input | Manage token from the message, booking identifier in the path |
| Success | `200` with status cancelled and the freed slot identifier |
| Validation | Token scope covers only this booking (ADR-0003) |
| Errors | `cutoff_passed` 409 with the salon phone number; `invalid_token` 401; `already_cancelled` 409 |
| Side effects | Slot freed immediately, cancellation message enqueued |
| Business rules | Cutoff is an owner setting enforced by ADR-0004 |

## 5. Error Model

| Element | Decision |
|---|---|
| Error structure | `code`, `message`, `details`, `correlation_id`, all in JSON |
| Status/code conventions | 400 for malformed requests, 401 or 403 for access, 409 for state conflicts, 422 for validation, 429 for limits, 500 for server faults |
| Error catalog | `slot_unavailable` offers nearest alternatives; `validation_error` names the field; `cutoff_passed` shows the salon phone; `invalid_token` asks for the latest message; `rate_limited` says when to retry |
| Sensitive information | No phone numbers, email addresses, tokens or internal stack traces in error bodies |

## 6. Events and Webhooks

The booking service emits EVT-001 when a service is selected by the client and EVT-002 when the server confirms a booking. Delivery uses the queue and worker in ADR-0002. There are no outbound webhooks in R1; a partner contract is [OPEN: engineering-lead, 2026-12-15].

## 7. Non-Functional Characteristics

| NFR | Target for API | Verified by |
|---|---|---|
| NFR-001 | Slot lookup p95 under 800 ms at 50 concurrent users | TS-005 |
| NFR-002 | Booking page available during salon hours | TS-010 |
| NFR-003 | Zero double bookings in 1,000 concurrent attempts | TS-002 |
| NFR-004 | Customer data deletable within 30 days | TS-006 |
| NFR-005 | Booking flow usable by keyboard and screen reader | TS-007 |

## 8. Documentation and Developer Experience

The OpenAPI document is generated from route definitions and reviewed with each release. Example requests use clearly labelled placeholder values, never real customer data. A sandbox is [OPEN: engineering-lead, 2026-12-15]; R1 verification uses the test environment in the Environment Strategy document.

## Completion Criteria

- [x] Every operation traces to a story or requirement; every story needing an API has operations.
- [x] Conventions (naming, pagination, errors, idempotency, versioning) are explicit and applied consistently.
- [x] Access level is stated per operation; rate limits are left open with an owner.
- [x] Errors are catalogued with client actions.
- [ ] The machine-readable contract exists and matches this document.
- [x] No personal data is exposed beyond the classification rules.
