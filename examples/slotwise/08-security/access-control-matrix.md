---
id: SLOTWISE-08-access-control-matrix
title: Access Control Matrix
domain: 08-security
tier: recommended
status: draft
version: 0.1.0
owner: security-lead
contributors: [product-manager, engineering-lead, qa-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [authentication-authorization, data-classification]
feeds: [user-stories, test-scenarios, security-test-plan, audit-logging, wireframe-spec]
applies_to: [all]
---

# Access Control Matrix: SlotWise

## 1. Roles

| Role | Description | Assigned how | Principal type | Persona / actor |
|---|---|---|---|---|
| Guest customer | Books without an account; manages a booking through a link token | Implicit | Human | PER-02, Dani |
| Business owner | Manages one salon account and its calendar | Account creation | Human | PER-01, Maya |
| Staff member | Manages bookings for one salon, no billing or settings | Invited by owner | Human | Delegated by PER-01 |
| Support agent | Helps salon owners; time-limited, audited access | Internal assignment | Human | Internal role |
| Platform administrator | Operates the platform | Internal, approved | Human | Internal role |
| Integration client | Calls the API on behalf of a salon | Credential issued by owner | Service | Partner system, R2 candidate |

## 2. Permission Matrix

**Actions:** **C** create · **R** read · **U** update · **D** delete · **X** execute a special action (named) · **none** no access · **own** only own records · **tenant** only within own salon.

| Resource | Guest customer | Business owner | Staff member | Support agent | Platform admin | Integration client |
|---|---|---|---|---|---|---|
| Service catalogue | R (public) | C R U D (tenant) | R (tenant) | R (view, audited) | R, X: suspend | R (tenant, scoped) |
| Availability / slots | R (public) | C R U D (tenant) | R U (tenant) | R (audited) | none | R U (tenant, scoped) |
| Booking | C, R own, X: cancel own | C R U D (tenant) | C R U (tenant) | R (audited, time-limited) | none | C R U (tenant, scoped) |
| Customer contact details | R own booking only | R (tenant) | R (tenant, masked) | R (masked; unmask needs PM approval) | none | R (tenant, scoped) |
| Business settings | none | R U (tenant) | none | R (audited) | R, X: override | none |
| Billing information | none | R U (tenant) | none | R (masked) | R | none |
| Audit log | none | R (own tenant) | none | R | R | none |
| Credentials / API keys | none | C R D (tenant) | none | none | none | none |

Every permission maps to a story or a security requirement: guest booking to US-001 and US-003, owner setup to US-004, tenant boundary to SR-002, audited access to SR-007.

## 3. Ownership and Tenant Rules

| ID | Rule | Applies to | Business rule / SR |
|---|---|---|---|
| Rule 1 | A user may act only on resources belonging to their own salon, even with a valid session | All tenant resources | SR-002 |
| Rule 2 | A guest may manage a booking only with its unguessable link token | Booking | AC-003.1, SR-001 |
| BR-005 | Only the owner or an authorised staff member may edit availability | Availability, US-004 | SR-002 |

## 4. Privileged Access

| Access | Who | Approval | Duration | Audit / alert |
|---|---|---|---|---|
| Support views customer data | Support agent | Case reference and PM approval | Up to 8 hours | Every access logged under SR-007, reviewed weekly |
| Production data-store access | Platform administrator | Change request | Per task | Session recorded, security lead notified |
| Break-glass emergency access | Named on-call engineers | Post-hoc review within 4 hours | Minimal time needed | Alert to security lead and PM |

## 5. Lifecycle and Review

| Event | Required action |
|---|---|
| Role granted or changed | Recorded with approver; effective immediately; audited under SR-007 |
| Staff member leaves a salon | Owner removes access; sessions revoked the same day |
| Internal staff leave or change role | Access removed within 1 working day |
| Periodic review | Every 3 months, owners and the platform administrator review role assignments; results recorded |
| Dormant accounts | Disabled after 30 days without a successful sign-in |

## 6. Verification

| Check | Method | Scenario |
|---|---|---|
| Each "none" in the matrix is denied | Automated authorisation tests per role and resource | TS-001, TS-004 |
| Cross-salon access attempts fail | Negative tests with two synthetic salons | TS-001, TS-008 |
| Privileged access is logged | Inspection of audit events against SR-007 | Audit review before release |

## Completion Criteria

- [x] Every role in the PRD, personas and API has a row or column; no undefined roles exist.
- [x] Every resource in the data model has permissions per role, with default deny stated.
- [x] Ownership and tenant rules reference business-rule and requirement IDs.
- [x] Privileged and emergency access are controlled, time-limited and audited.
- [x] A review cadence and joiner/leaver process exist.
- [x] Each permission is covered by a story and by an automated or manual test.
