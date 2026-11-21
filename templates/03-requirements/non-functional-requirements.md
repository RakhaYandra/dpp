---
id: DPP-03-non-functional-requirements
title: Non-Functional Requirements (NFR)
domain: 03-requirements
tier: mandatory
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, qa-lead, security-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [prd]
feeds: [architecture-overview, test-strategy, performance-test-plan, security-requirements, observability-strategy]
applies_to: [all]
---

# Non-Functional Requirements: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | States the quality attributes the product must meet (speed, availability, security, accessibility, scale, and so on) as **measurable** requirements. Architecture and test planning are driven by this document. |
| **When to use** | Alongside the PRD, before architecture decisions. Skipping it is the most common reason performance and security problems are found late. |
| **Owner** | Product Manager, with Engineering Lead (feasibility), QA Lead (testability) and Security Lead. |
| **Required inputs** | [PRD](prd.md) goals, scope and expected scale; known regulatory or contractual obligations; user and device context from [Persona](../01-discovery/persona.md). |
| **Related documents** | [Architecture Overview](../05-architecture/architecture-overview.md) · [Test Strategy](../07-quality/test-strategy.md) · [Security Requirements](../08-security/security-requirements.md) · [Accessibility & Responsive Guidelines](../04-ux-ui/accessibility-and-responsive.md) |

</details>

> **Guidance:** A good NFR has a **metric, a target value, a condition and a way to verify it**. "The system should be fast" is a wish. "95% of booking page loads complete in under 2 seconds on a mid-range phone over a 4G connection" is a requirement. If you do not yet know the right number, write a provisional target marked **TBC** with an owner and a date to confirm it. Provisional is better than empty.

## 1. Operating Context

| Item | Value |
|---|---|
| Expected users (launch / 6 months / 12 months) | [e.g. 50 / 500 / 2,000 businesses; 20× that in end customers] |
| Peak load assumption | [e.g. 30 bookings/min at 9–10 am local time] |
| Data volume assumption | [e.g. 1 M booking records/year] |
| Geographic / time-zone footprint | [Regions, time zones] |
| User devices and connectivity | [Mid-range phones, desktop; 4G] |

## 2. Requirements Catalog

**Priority:** Must / Should / May. **Verification:** Test (T), Inspection (I), Analysis (A), Monitoring (M).

| ID | Category | Requirement | Metric and target | Condition | Priority | Verification | Status |
|---|---|---|---|---|---|---|---|
| NFR-001 | Performance | Booking page loads quickly | p95 interactive ≤ 2 s | Mid-range phone, 4G, cold cache | Must | T, M | Proposed |
| NFR-002 | Performance | Booking API responds quickly | p95 ≤ 400 ms, p99 ≤ 1 s | At peak load (NFR-006) | Must | T, M | Proposed |
| NFR-004 | Availability | Booking remains available | ≥ 99.5% monthly | Excludes announced maintenance | Must | M | Proposed |
| NFR-005 | Recoverability | Data loss limited after failure | RPO ≤ 15 min; RTO ≤ 4 h | Single-region failure | Should | T, I | Proposed |
| NFR-006 | Scalability | Support growth without redesign | 10× launch load with no architectural change | Horizontal scaling | Should | A, T | TBC |
| NFR-008 | Security | Protect personal data | Encrypted in transit and at rest; access limited by role | All environments | Must | I, T | Proposed |
| NFR-011 | Accessibility | Usable with assistive technology | WCAG 2.2 AA for booking flow | Public pages | Must | T, I | Proposed |
| NFR-013 | Compatibility | Works on supported platforms | Latest two major versions of major browsers | Desktop and mobile | Must | T | Proposed |

*(Delete the example rows and add your own. Use the category checklist below to find gaps.)*

## 3. Category Checklist

> **Guidance:** For each category, either write at least one NFR or mark it *Not applicable* with a reason. Do not leave categories silently blank.

| Category | Questions to answer | Written / N/A |
|---|---|---|
| Performance | Response/load times, throughput, batch windows | |
| Scalability | Growth in users, data, tenants; elasticity | |
| Availability and reliability | Uptime target, maintenance windows, failure behaviour, degradation | |
| Recoverability | Backup frequency, RPO, RTO; see [Backup & Recovery](../09-release-ops/backup-and-recovery.md) | |
| Security | Authentication, authorization, encryption, audit, secure development; see [Security Requirements](../08-security/security-requirements.md) | |
| Privacy and compliance | Personal data handling, retention, consent, regulations that apply (verify with qualified advice) | |
| Accessibility | Target conformance level, keyboard and screen-reader support | |
| Usability | Task time, error rate, learnability (only if measurable) | |
| Compatibility | Browsers, OS versions, devices, API clients, integrations | |
| Localization | Languages, time zones, currencies, date/number formats, text direction | |
| Observability | Logging, metrics, tracing, alerting needs; see [Observability Strategy](../09-release-ops/observability-strategy.md) | |
| Maintainability | Modularity, documentation, upgrade effort, test coverage expectations | |
| Portability / deployability | Environments, deployment frequency, vendor independence | |
| Data | Retention, integrity, migration, archival | |
| Capacity and cost | Resource and cost ceilings per user/tenant | |

## 4. Trade-offs and Conflicts

[Where NFRs pull against each other or against functional scope (e.g. strict availability vs. cost; strong security vs. frictionless booking) and how you resolved them. Record significant outcomes as DEC- or ADR- entries.]

## 5. Open Items

| ID | Open point | Owner | Due |
|---|---|---|---|
| Q-xx | [e.g. Confirm availability target with sponsor] | [Name] | [Date] |

## Completion Criteria

- [ ] Every category in the checklist has at least one NFR or a recorded reason it does not apply.
- [ ] Every NFR has an ID, a measurable target, a condition and a verification method.
- [ ] Targets are either confirmed or marked TBC with an owner and date.
- [ ] Operating context (users, load, data) is stated, since targets depend on it.
- [ ] Conflicts with functional scope or other NFRs are recorded.
- [ ] Engineering has confirmed feasibility and QA has confirmed testability of the *Must* items.
