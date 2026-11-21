---
id: DPP-PKG-api-platform-webhook-specification
title: Webhook Specification
domain: package-api-platform
tier: package
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [technical-writer, security-lead, product-manager]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [api-specification, consumer-authentication]
feeds: [test-strategy, integration-specification, api-lifecycle-and-versioning, observability-strategy]
applies_to: [api-platform, saas]
---

# Webhook Specification: [API / Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Specifies the outgoing event notifications (webhooks) your product sends to consumers: events, payloads, delivery guarantees, security, retries and consumer responsibilities. Also useful for documenting incoming webhooks from providers you rely on. |
| **When to use** | When consumers need to be told about changes without polling. Write it before building: delivery semantics are hard to change later. |
| **Owner** | Engineering Lead with a technical writer. |
| **Required inputs** | [API Specification](../../templates/05-architecture/api-specification.md) resources and errors; [Consumer Authentication](consumer-authentication.md); consumer integration needs. |
| **Related documents** | [API Lifecycle & Versioning](api-lifecycle-and-versioning.md) · [Integration Specification](../../templates/05-architecture/integration-specification.md) (incoming webhooks) · [Observability Strategy](../../templates/09-release-ops/observability-strategy.md) |

</details>

> **Guidance:** Assume **at-least-once delivery, possible duplicates and out-of-order arrival**, and design the contract so consumers can cope. Include **no unnecessary personal data** in payloads; consider sending identifiers and letting consumers fetch details with proper authorisation. Treat the consumer's endpoint as untrusted and slow.

## 1. Event Catalog

| Event type | Trigger | Resource | Frequency | Sensitivity | Introduced in version |
|---|---|---|---|---|---|
| `booking.created` | A booking is confirmed | Booking | High | Medium | v1 |
| `booking.cancelled` | A booking is cancelled | Booking | Medium | Medium | v1 |

Naming: `resource.action`, past tense, lowercase; event names are never reused with changed meaning.

## 2. Payload Format

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique event id (for deduplication) |
| `type` | string | Event type |
| `created_at` | timestamp (UTC) | When the event occurred |
| `api_version` | string | Version of the schema |
| `tenant_id` | string | Owning tenant |
| `data` | object | Event data or reference to the resource; schema per event type |

Payload schemas are in the machine-readable contract: [path]. Additive changes follow the [compatibility policy](api-lifecycle-and-versioning.md).

## 3. Subscription Management

| Topic | Decision |
|---|---|
| Creating endpoints | [Self-service via API/portal; HTTPS required] |
| Event selection | [Per endpoint filters] |
| Verification | [Challenge when registering an endpoint] |
| Limits | [Endpoints per tenant; payload size] |
| Testing tools | [Send test event; sandbox] |
| Enable/disable and deletion | |

## 3a. Security

| Topic | Requirement |
|---|---|
| Authenticity | Every delivery is signed with a per-endpoint secret; signature and timestamp headers allow verification |
| Replay protection | Timestamp tolerance; event id deduplication by consumer |
| Transport | TLS only |
| Secret management | Rotation with overlapping validity; shown once |
| Network | [Published source addresses if offered; protection against abuse of the sender such as requests to internal addresses] |
| Data minimisation | |

## 4. Delivery Semantics

| Topic | Specification |
|---|---|
| Guarantee | At least once; ordering not guaranteed (consumers use `created_at` and resource versions) |
| Success definition | HTTP success response within [N] seconds |
| Retry schedule | [Exponential backoff for up to N hours/days] |
| Failure handling | After retries, mark failed; endpoint auto-disabled after [threshold] with notification |
| Replay | [Consumers can re-request events for the last N days] |
| Rate and concurrency | [Per endpoint limits; see [Rate Limiting & Quotas](rate-limiting-and-quotas.md)] |

## 5. Consumer Responsibilities (publish in the developer documentation)

- Respond quickly with a success code, then process asynchronously.
- Verify the signature and timestamp; reject others.
- Deduplicate by event id; handle out-of-order and unknown event types gracefully.
- Treat payloads as untrusted input; fetch authoritative state when needed.

## 6. Observability

[Delivery log per endpoint available to consumers; internal metrics: success rate, latency, retries, disabled endpoints (MON-xx); alerting.]

## 7. Testing

[Contract tests per event, signature verification tests, failure and retry simulations, duplicate and out-of-order scenarios, load tests.]

## Completion Criteria

- [ ] Every event has a type, trigger, schema and sensitivity classification.
- [ ] Delivery semantics (guarantees, retries, ordering, replay) are explicit and documented for consumers.
- [ ] Signing, replay protection and secret rotation are specified.
- [ ] Endpoint management, limits and failure handling exist.
- [ ] Consumer responsibilities and observability are documented and tested.
