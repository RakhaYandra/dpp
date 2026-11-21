---
id: DPP-08-access-control-matrix
title: Access Control Matrix
domain: 08-security
tier: recommended
status: draft
version: 0.1.0
owner: security-lead
contributors: [product-manager, engineering-lead, qa-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [authentication-authorization, data-classification]
feeds: [user-stories, test-scenarios, security-test-plan, audit-logging, wireframe-spec]
applies_to: [all]
---

# Access Control Matrix: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | The authoritative table of **who may do what to which resources**, including ownership and tenant rules and privileged access. It turns the model chosen in [Authentication & Authorization](../05-architecture/authentication-authorization.md) into concrete permissions that stories, screens and tests can reference. This is the universal home for the role-based matrix; the enterprise package extends it with audit logging rather than repeating it. |
| **When to use** | Whenever the product has more than one role or any user-specific data. Skip for a single-role product, and say so in the PRD. |
| **Owner** | Security Lead or Product Manager. |
| **Required inputs** | [Authentication & Authorization](../05-architecture/authentication-authorization.md) model; [Persona](../01-discovery/persona.md) roles; [Data Classification](data-classification.md); [User Stories](../03-requirements/user-stories.md). |
| **Related documents** | [Security Requirements](security-requirements.md) · [Security Test Plan](../07-quality/security-test-plan.md) · [Audit Logging](../../packages/enterprise/audit-logging.md) (enterprise package) |

</details>

> **Guidance:** Apply **least privilege** and **default deny**: anything not granted is forbidden. Express permissions in terms of **business actions** (cancel a booking), not technical operations. Keep roles few; a role explosion usually means the model should be attribute- or ownership-based. Every cell in the matrix should be testable.

## 1. Roles

| Role | Description | Assigned how | Principal type | Persona / actor |
|---|---|---|---|---|
| Guest customer | Books without an account; manages a booking via a link token | Implicit | Human | PER-01 |
| Business owner | Manages one business | Account creation | Human | PER-02 |
| Staff member | Manages bookings for one business, no billing or settings | Invited by owner | Human | |
| Support agent | Helps customers; time-limited, audited access | Internal | Human | |
| Platform administrator | Operates the platform | Internal, approved | Human | |
| Integration client | Calls the API on behalf of a business | Credential issued by owner | Service | |

## 2. Permission Matrix

**Actions:** **C** create · **R** read · **U** update · **D** delete · **X** execute a special action (named) · **–** no access · **own** only own records · **tenant** only within own business.

| Resource | Guest customer | Business owner | Staff member | Support agent | Platform admin | Integration client |
|---|---|---|---|---|---|---|
| Service catalogue | R (public) | C R U D (tenant) | R (tenant) | R (view, audited) | R, X: suspend | R (tenant, scoped) |
| Availability / slots | R (public) | C R U D (tenant) | R U (tenant) | R (audited) | – | R U (tenant, scoped) |
| Booking | C, R own, X: cancel own | C R U D (tenant) | C R U (tenant) | R (audited, time-limited) | – | C R U (tenant, scoped) |
| Customer contact details | R own | R (tenant) | R (tenant, masked) | R (masked; unmask requires approval) | – | R (tenant, scoped) |
| Business settings | – | R U (tenant) | – | R (audited) | R, X: override | – |
| Billing information | – | R U (tenant) | – | R (masked) | R | – |
| Audit log | – | R (own tenant) | – | R | R | – |
| Credentials / API keys | – | C R D (tenant) | – | – | – | – |

*(Replace with your resources. Every permission should map to at least one story and one test.)*

## 3. Ownership and Tenant Rules

| ID | Rule | Applies to | Business rule / SR |
|---|---|---|---|
| BR-005 | A user may act only on resources belonging to their own business (tenant boundary) | All tenant resources | SR-002 |
| BR-0xx | A guest may manage a booking only with its unguessable link token | Booking | SR-001 |
| BR-0xx | A staff member cannot change roles, billing or deletion of the business | Business settings | |

## 4. Privileged Access

| Access | Who | Approval | Duration | Audit / alert |
|---|---|---|---|---|
| Support views customer data | Support agent | Case reference required | Up to [N] hours | Every access logged; reviewed weekly |
| Production data-store access | Platform admin | Change request | Per task | Session recorded |
| Break-glass emergency access | Named on-call engineers | Post-hoc review within [N] hours | Minimal | Alert to security lead |

## 5. Lifecycle and Review

| Event | Required action |
|---|---|
| Role granted or changed | Recorded with approver; effective immediately; audited |
| Staff member leaves a business | Owner removes access; sessions revoked |
| Internal staff leave or change role | Access removed within [N] hours |
| Periodic review | [Quarterly]: owners and platform admins review who has which roles; results recorded |
| Dormant accounts | [Disabled after N days] |

## 6. Verification

| Check | Method | Scenario |
|---|---|---|
| Each "–" in the matrix is denied | Automated authorisation tests per role and resource | TS-0xx |
| Cross-tenant access attempts fail | Negative tests with two tenants | TS-0xx |
| Privileged access is logged | Inspection of audit events | TS-0xx |

## Completion Criteria

- [ ] Every role in the PRD, personas and API has a row or column; no undefined roles exist.
- [ ] Every resource in the data model has permissions per role, with default deny stated.
- [ ] Ownership and tenant rules reference business-rule and requirement IDs.
- [ ] Privileged and emergency access are controlled, time-limited and audited.
- [ ] A review cadence and joiner/leaver process exist.
- [ ] Each permission is covered by a story and by an automated or manual test.
