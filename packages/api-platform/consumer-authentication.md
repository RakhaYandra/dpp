---
id: DPP-PKG-api-platform-consumer-authentication
title: API Consumer Authentication Strategy
domain: package-api-platform
tier: package
status: draft
version: 0.1.0
owner: security-lead
contributors: [engineering-lead, product-manager, technical-writer]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [authentication-authorization, api-specification, security-requirements]
feeds: [api-specification, test-strategy, security-test-plan, rate-limiting-and-quotas, access-control-matrix]
applies_to: [api-platform]
---

# API Consumer Authentication Strategy: [API Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Extends the product's [Authentication & Authorization design](../../templates/05-architecture/authentication-authorization.md) with the consumer-facing parts of an API platform: how developers and their applications obtain credentials, which scopes they can request, how credentials are issued, rotated and revoked, and how consumers are onboarded. |
| **When to use** | When third parties (partners or public developers) call your API. For internal-only APIs the base authentication document is enough. |
| **Owner** | Security Lead with API product owner. |
| **Required inputs** | [Authentication & Authorization](../../templates/05-architecture/authentication-authorization.md); [API Specification](../../templates/05-architecture/api-specification.md); [Security Requirements](../../templates/08-security/security-requirements.md); consumer types. |
| **Related documents** | [Rate Limiting & Quotas](rate-limiting-and-quotas.md) · [Access Control Matrix](../../templates/08-security/access-control-matrix.md) · [Security Test Plan](../../templates/07-quality/security-test-plan.md) |

</details>

> **Guidance:** Use **established, standardised mechanisms** (name the standards and versions in an ADR) rather than inventing schemes. Distinguish *who the application is* from *on whose behalf it acts*. Issue **least-privilege, narrowly scoped, expiring** credentials, and plan for the day one leaks.

## 1. Consumer Types and Credentials

| Consumer type | Acts as | Credential type | Lifetime | Who issues | Notes |
|---|---|---|---|---|---|
| Server-side partner app | Itself | [Client credentials] | | Developer portal | |
| App acting for a user | User delegated | [Delegated authorisation with user consent] | Short-lived tokens + refresh | | |
| Public / browser or mobile client | User delegated | [Public-client-safe flow] | | | No embedded secrets |
| Personal / testing keys | Developer | [API key, sandbox only] | | | Limited scopes |

## 2. Scopes and Permissions

| Scope | Grants | Sensitivity | Requires user consent? | Requires approval/review? | API operations |
|---|---|---|---|---|---|
| bookings:read | Read bookings of consenting business | Medium | Yes | No | API-001 |
| bookings:write | Create/cancel bookings | High | Yes | Yes (partner review) | API-002/003 |

Design rules: smallest useful scopes; scopes map to the [Access Control Matrix](../../templates/08-security/access-control-matrix.md); tenant boundaries still enforced independently of scopes.

## 3. Onboarding and Governance

| Topic | Decision |
|---|---|
| Developer registration and verification | |
| Application registration (redirect addresses, contacts) | |
| Review for sensitive scopes / production access | [Criteria, SLA] |
| Terms of use, acceptable use, data processing terms | [Legal review] |
| Sandbox vs production credentials | |
| Suspension and revocation rights | [Triggers; notice] |

## 4. Credential Lifecycle

| Stage | Requirement |
|---|---|
| Issuance | Displayed once; hashed storage on our side; secure channel |
| Rotation | Supported without downtime (overlapping validity) |
| Expiry | |
| Revocation | Immediate; self-service and operator-initiated |
| Leak response | Detect (secret scanning notifications), revoke, notify consumer, audit |
| Auditing | Every issuance, use anomaly and revocation logged |

## 5. Consumer-Facing Security Guidance

[What consumers must do: protect secrets, use TLS, validate webhooks, handle token expiry, store tokens safely, report vulnerabilities (contact and process).]

## 6. Threats and Controls

| Threat | Control |
|---|---|
| Stolen or leaked credentials | Short lifetime, scopes, rotation, anomaly detection |
| Over-privileged application | Scope review; consent screens in plain language |
| Token replay or confusion | Audience restrictions, binding where available |
| Abuse by registered developers | Quotas, monitoring, revocation |

## Completion Criteria

- [ ] Consumer types, credential types, lifetimes and issuers are defined.
- [ ] Scopes are minimal, documented, and mapped to operations and to the access control matrix.
- [ ] Onboarding, review and revocation governance exist.
- [ ] Rotation, revocation and leak response are specified and testable.
- [ ] Mechanisms are standard, named in ADRs, and reviewed by a security expert.
