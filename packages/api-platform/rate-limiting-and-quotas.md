---
id: DPP-PKG-api-platform-rate-limiting-and-quotas
title: Rate Limiting and Quotas
domain: package-api-platform
tier: package
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [product-manager, operations-lead, security-lead, finance]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [api-specification, non-functional-requirements, infrastructure-and-scalability]
feeds: [usage-metering, multi-tenancy-and-isolation, test-strategy, performance-test-plan, observability-strategy]
applies_to: [api-platform, saas]
---

# Rate Limiting and Quotas: [API / Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines how much each consumer may use the API or product, over what time windows, how limits are enforced and communicated, and what happens when limits are reached. Protects availability, ensures fairness between tenants and supports pricing. This is the single home for rate limiting; the SaaS package refers here. |
| **When to use** | For any API open to third parties or to many tenants, and for any public endpoint exposed to abuse (such as a guest booking endpoint). |
| **Owner** | Engineering Lead with Product Manager. |
| **Required inputs** | [NFRs](../../templates/03-requirements/non-functional-requirements.md) (capacity, availability); [Infrastructure & Scalability](../../templates/05-architecture/infrastructure-and-scalability.md) capacity model; [Business Model](../../templates/02-strategy/business-model.md) tiers. |
| **Related documents** | [Usage Metering](../saas/usage-metering.md) · [Multi-Tenancy](../saas/multi-tenancy-and-isolation.md) · [Consumer Authentication](consumer-authentication.md) · [Performance Test Plan](../../templates/07-quality/performance-test-plan.md) |

</details>

> **Guidance:** Distinguish **rate limits** (requests per time window, protecting the system in real time) from **quotas** (total allowance per billing period, tied to plans). Set limits from **measured capacity and consumer needs**, not guesses, and start generous with monitoring before tightening. Limits must be **predictable and visible** to consumers.

## 1. Goals and Principles

| Goal | Requirement |
|---|---|
| Protect availability | A single consumer cannot exhaust shared capacity (NFR-xxx) |
| Fairness | Tenants/consumers receive their entitled share |
| Abuse prevention | Unauthenticated and credential-stuffing traffic is constrained |
| Commercial tiers | Limits differ by plan (see [Subscription & Billing](../saas/subscription-and-billing.md)) |

## 2. Limit Dimensions and Values

| Scope | Identifier | Limit | Window | Burst | Plan / tier | Applies to |
|---|---|---|---|---|---|---|
| Per API credential | credential id | [N] requests | per minute | [M] | Standard | All operations |
| Per tenant | tenant id | [N] | per minute | | | Aggregate of its credentials |
| Per IP (unauthenticated) | client address | [N] | per minute | | | Public endpoints (API-001, API-002) |
| Expensive operations | credential | [N] | per hour | | | Exports, searches |
| Concurrency | credential | [N] in-flight | — | | | |
| Quota | tenant | [N] | per month | | Per plan | Billable actions |

Document the **basis** for each number (measured capacity, cost per request, competitor norms) and the date of review.

## 3. Algorithm and Enforcement

| Topic | Decision |
|---|---|
| Algorithm | [Fixed window / sliding window / token bucket / leaky bucket] and why |
| Enforcement point | [Edge, gateway, application; layered defence] |
| State storage | [Shared counter store; behaviour if it fails: fail open or closed, by endpoint sensitivity] |
| Distributed consistency | [Accuracy tolerance across instances] |
| Time windows | [Clock source; boundaries] |
| Exemptions | [Internal services, health checks, trusted partners] |

## 4. Consumer Experience

| Topic | Decision |
|---|---|
| Response when limited | [Clear status, machine-readable error code, retry guidance] |
| Limit information in responses | [Remaining allowance and reset time provided on every response] |
| Documentation | [Limits published per plan; examples of backoff handling] |
| Warnings | [Notify at 80% of quota; usage dashboard] |
| Requesting higher limits | [Process, criteria] |

## 5. Over-Limit Behaviour

| Situation | Behaviour |
|---|---|
| Short burst above limit | Reject excess with retry guidance |
| Sustained abuse | Temporary block, notify, escalate to revocation per [Consumer Authentication](consumer-authentication.md) |
| Quota exceeded | [Block / throttle / bill overage] |
| Critical operations (security, billing webhooks) | [Never silently dropped] |

## 6. Monitoring and Operations

| Item | Requirement |
|---|---|
| Metrics | Allowed/limited counts by consumer, endpoint and tier (MON-xx) |
| Alerts | Spikes in limited requests; consumers near quota; limiter failures |
| Tuning process | [Monthly review; change notice per [API Lifecycle & Versioning](api-lifecycle-and-versioning.md)] |

## 7. Testing

[Load tests verifying enforcement under concurrency; tests for window boundaries, burst behaviour, limiter-store failure, correct headers/errors; abuse scenarios.]

## Completion Criteria

- [ ] Limits and quotas are defined per scope with values, windows, bursts and a stated basis.
- [ ] Enforcement points, algorithm and failure behaviour are chosen with reasons.
- [ ] Consumers receive clear limit information and can request changes.
- [ ] Over-limit and abuse handling are defined; critical operations are protected.
- [ ] Limits are monitored, reviewed and tested.
