---
id: SLOTWISE-05-adr
title: Architecture Decision Record (ADR)
domain: 05-architecture
tier: recommended
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [architect, product-manager, security-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [architecture-overview, non-functional-requirements]
feeds: [architecture-overview, component-design, technology-stack, infrastructure-and-scalability, test-strategy, threat-model]
applies_to: [all]
---

# ADR-0001: One database transaction guards each slot

## Metadata

| | |
|---|---|
| **Status** | Accepted |
| **Date** | Before 2026-11-10 |
| **Decision makers / consulted** | Engineering lead, Product manager |
| **Related requirements** | NFR-003, AC-001.2, CON-01 |
| **Related ADRs** | ADR-0003 |

## 1. Context

SlotWise books one slot for one customer. Two customers can confirm the same slot at the same time, and NFR-003 allows no double bookings. The team has two engineers and 14 weeks (CON-01), so the guard cannot add a new service to operate. The approved [Architecture Overview](architecture-overview.md) already records this decision and its building blocks.

## 2. Decision Drivers

- No double bookings under concurrent confirmation (NFR-003, AC-001.2).
- Small team and limited operations capacity (CON-01).
- The loser of a race must get nearest alternatives, not an error with no next step (AC-001.2).
- Slot lookup stays under 800 ms at 50 concurrent users (NFR-001).

## 3. Options Considered

| Option | Description | Pros | Cons | Fit with drivers |
|---|---|---|---|---|
| A | One database transaction checks and reserves the slot, with a uniqueness rule on staff and start time | Simple, correct under races, no new component | Single write path limits scale out | Best fit |
| B | Application-level distributed lock around booking creation | Keeps database schema simple | Adds a lock service to run and recover, risky for two engineers | Weak fit with CON-01 |
| C: do nothing / defer | Validate in application code and accept rare races | No work now | Violates NFR-003 and breaks trust (RISK-03) | Not acceptable |

## 4. Decision

We will check and reserve each slot in one database transaction with a uniqueness rule on staff and start time, because that meets NFR-003 without adding an operations burden to a two-engineer team.

## 5. Consequences

| Type | Consequence |
|---|---|
| Positive | Concurrent confirmations resolve to one booking; the loser gets alternatives (AC-001.2). |
| Negative / costs | Writes scale through one primary data store, acceptable at pilot volume. |
| Risks introduced | A hot slot still serializes writes; tracked as RISK-03 in the Risk Register. |
| Required follow-up | Run TS-002 with 1,000 concurrent attempts before go live. |
| What would make us revisit | Repeated write contention at real load, or a target beyond the pilot volume. |

## 6. Validation

TS-002 checks 1,000 concurrent attempts on one slot and expects zero double bookings. NFR-003 is verified by the same scenario.

## ADR Index (keep in `docs/05-architecture/adr/README.md`)

This worked example keeps the index in this document.

| ADR | Title | Status | Date | Supersedes |
|---|---|---|---|---|
| ADR-0001 | One database transaction guards each slot | Accepted | Before 2026-11-10 | None |
| ADR-0002 | Reminders go through a queue and an external provider | Accepted | Before 2026-11-10 | None |
| ADR-0003 | Customers book without an account and manage by signed link | Accepted | 2026-11-27 | None |
| ADR-0004 | Cancellation cutoff is enforced server side | Accepted | 2026-11-27 | None |
| ADR-0005 | Authorization combines roles with business ownership | Proposed | 2026-11-27 | None |

## ADR-0002: Reminders go through a queue and an external provider

### Metadata

| | |
|---|---|
| **Status** | Accepted |
| **Date** | Before 2026-11-10 |
| **Decision makers / consulted** | Engineering lead, Product manager |
| **Related requirements** | FR-002, AC-002.1, AC-002.2, AC-002.3, DEP-01 |
| **Related ADRs** | None |

### 1. Context

FR-002 needs a confirmation within one minute and one reminder before the appointment. Delivery depends on an external email or SMS provider (DEP-01), whose outage must not stop a booking from being created.

### 2. Decision Drivers

- Delivery failure must not block the booking request.
- Cancelled bookings must not receive a reminder (AC-002.3).
- Retries and delivery results need a record for support.

### 3. Options Considered

| Option | Description | Pros | Cons | Fit with drivers |
|---|---|---|---|---|
| A | Booking service enqueues messages, worker sends with retries and records the result | Decouples provider outage from booking; adds retry record | Queue and worker to operate | Best fit |
| B | Send inline during the booking request | No new component | Provider outage fails bookings; slow responses | Weak fit |
| C: do nothing / defer | Rely on customers to remember | No work | Breaks FR-002 and GOAL-01 | Not acceptable |

### 4. Decision

We will enqueue confirmation and reminder messages and send them with a worker that retries and records the result, because delivery failures must not block booking.

### 5. Consequences

| Type | Consequence |
|---|---|
| Positive | Provider outage does not lose a booking; reminder state is visible to support. |
| Negative / costs | Queue and worker need monitoring and alerting on backlog. |
| Risks introduced | Provider outage delays reminders, tracked as RISK-02. |
| Required follow-up | Choose the provider before pilot; decision date is [OPEN: engineering-lead, 2026-12-15]. |
| What would make us revisit | Cost per message above plan, or repeated missed reminders. |

### 6. Validation

TS-003 checks confirmation and reminder timing, including no reminder after cancellation.

## ADR-0003: Customers book without an account and manage by signed link

### Metadata

| | |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-11-27 |
| **Decision makers / consulted** | Product manager, Engineering lead, Designer |
| **Related requirements** | FR-001, FR-003, AC-001.3, DEC-002 |
| **Related ADRs** | ADR-0001, ADR-0004 |

### 1. Context

DEC-002 removes sign-in from the customer path to reduce friction. The customer still needs a way to change or cancel a booking, and the message that confirms the booking is the natural place to put that link.

### 2. Decision Drivers

- A customer books with name and contact details only (AC-001.3).
- The manage link must not reveal another customer's booking.
- Two engineers cannot build and operate a full customer identity system in 14 weeks (CON-01).

### 3. Options Considered

| Option | Description | Pros | Cons | Fit with drivers |
|---|---|---|---|---|
| A | Guest booking plus a signed, single-purpose manage token in the message | No account, scoped access, cheap to build | Token needs rotation and expiry rules | Best fit |
| B | Require a customer account | Reusable identity | Adds friction and conflicts with DEC-002 | Weak fit |
| C: do nothing / defer | Owner changes every booking by phone or message | No work | Owner time is the problem being solved | Not acceptable |

### 4. Decision

We will let customers book without an account and give each booking a signed manage link that permits only cancel or reschedule, because it keeps the booking path short while limiting access to that booking.

### 5. Consequences

| Type | Consequence |
|---|---|
| Positive | Fewer steps on S-01 to S-03; no customer password to reset. |
| Negative / costs | Token handling and expiry must be implemented and tested. |
| Risks introduced | A leaked link allows cancel or reschedule within the cutoff; scope is limited to one booking. |
| Required follow-up | Set token lifetime and rotation policy, owner is [OPEN: engineering-lead, 2026-12-15]. |
| What would make us revisit | Customers ask for a booking history across salons. |

### 6. Validation

TS-001 checks booking without an account; TS-004 checks manage-link behavior before and after the cutoff.

## ADR-0004: Cancellation cutoff is enforced server side

### Metadata

| | |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-11-27 |
| **Decision makers / consulted** | Product manager, Engineering lead |
| **Related requirements** | FR-003, AC-003.1, AC-003.2 |
| **Related ADRs** | ADR-0003 |

### 1. Context

The salon sets a cutoff for cancellations. A customer can open the manage link at any time, so the client cannot be trusted to decide whether a change is allowed.

### 2. Decision Drivers

- A cancellation before the cutoff frees the slot immediately (AC-003.1).
- After the cutoff the salon phone number is shown (AC-003.2).
- The cutoff is an owner setting, not a hard-coded value.

### 3. Options Considered

| Option | Description | Pros | Cons | Fit with drivers |
|---|---|---|---|---|
| A | Check cutoff in the booking service on every manage request using the stored owner setting | Consistent, auditable, works with two tabs | Needs server time and timezone handling | Best fit |
| B | Check cutoff in the browser using the timestamp in the link | Simple | Customer can change the clock or call the API directly | Not acceptable |
| C: do nothing / defer | Allow cancellations at any time | No work | Removes owner control and conflicts with AC-003.2 | Not acceptable |

### 4. Decision

We will enforce the cancellation cutoff in the booking service on every manage request, because the salon setting must hold even when the customer edits the client or uses another tab.

### 5. Consequences

| Type | Consequence |
|---|---|
| Positive | One rule applies to cancel and reschedule, regardless of client. |
| Negative / costs | Timezone handling needs explicit tests. |
| Risks introduced | A wrong salon timezone could apply the cutoff at the wrong hour. |
| Required follow-up | Confirm default cutoff and timezone rule, owner is [OPEN: owner, 2026-12-15]. |
| What would make us revisit | Owners ask for different cutoffs per service. |

### 6. Validation

TS-004 checks cancel and reschedule before and after the cutoff, including the salon phone number path.

## ADR-0005: Authorization combines roles with business ownership

### Metadata

| | |
|---|---|
| **Status** | Proposed |
| **Date** | 2026-11-27 |
| **Decision makers / consulted** | Security lead, Engineering lead |
| **Related requirements** | NFR-004, SR-002, TH-003 |
| **Related ADRs** | None |

### 1. Context

Each salon is a separate business. A signed-in owner must only see records of their own business, and a customer's manage token must only reach that customer's booking. The tenancy rules are described in [Multi-Tenancy and Isolation](../packages/saas/multi-tenancy-and-isolation.md).

### 2. Decision Drivers

- Deny access to another business's records even with a valid session (SR-002, TH-003).
- Keep the model small enough for two engineers.
- Default deny at each enforcement point.

### 3. Options Considered

| Option | Description | Pros | Cons | Fit with drivers |
|---|---|---|---|---|
| A | Role checks plus a business ownership predicate enforced in the booking service and data queries | Explicit boundary, one place to test | Every query must carry the business scope | Best fit |
| B | Edge-only role checks | Fewer service changes | A valid token could still reach another business's record | Not acceptable |
| C: do nothing / defer | Trust the client to send the right business id | No work | Breaks SR-002 | Not acceptable |

### 4. Decision

We will combine role checks with a business ownership predicate enforced in the booking service and in data queries, because a valid session alone must not expose another business's records.

### 5. Consequences

| Type | Consequence |
|---|---|
| Positive | One ownership rule covers bookings, services, staff and availability. |
| Negative / costs | Every query needs a business scope, so tests must assert the negative case. |
| Risks introduced | A missed scope in a new query could leak data. |
| Required follow-up | Security lead reviews the access control matrix before pilot; date is [OPEN: security-lead, 2026-12-15]. |
| What would make us revisit | Support needs cross-business access with audited impersonation. |

### 6. Validation

A security test for cross-business access is [OPEN: security-lead, 2026-12-15]; NFR-004 deletion behavior is checked by TS-006.

## Completion Criteria

- [x] Each decision is stated in one clear sentence.
- [x] Context and drivers reference requirement IDs.
- [x] At least two real options, including a non-action, were compared fairly.
- [x] Negative consequences and follow-up actions are recorded.
- [x] Status and date are set; superseded decisions are linked both ways where they exist.
- [x] The architecture overview and index reflect the decision.
- [ ] Security review of ADR-0005 and provider selection for ADR-0002 are closed.
