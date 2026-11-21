---
id: DPP-09-maintenance-plan
title: Maintenance Plan
domain: 09-release-ops
tier: optional
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [operations-lead, security-lead, product-manager]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [operational-readiness, technology-stack]
feeds: [roadmap, resource-plan, risk-register]
applies_to: [all]
---

# Maintenance Plan: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Plans the recurring work needed to keep the product healthy after launch: updates, security patches, dependency upgrades, data housekeeping, support rotation, certificate and licence renewals, and technical-debt reduction. Ensures that run costs and effort are budgeted, not ignored. |
| **When to use** | Before launch; reviewed quarterly. Optional for short-lived or prototype products, essential for anything that will live more than a few months. |
| **Owner** | Engineering Lead. |
| **Required inputs** | [Technology Stack](../05-architecture/technology-stack.md) (components and support dates); [Operational Readiness](operational-readiness.md); [Resource Plan](../06-project-mgmt/resource-plan.md). |
| **Related documents** | [Roadmap](../02-strategy/roadmap.md) · [Incident Management](incident-management.md) · [Risk Register](../06-project-mgmt/risk-register.md) |

</details>

> **Guidance:** Maintenance is not "nothing happening". Reserve a **standing share of capacity** (for example a fixed percentage of each iteration) so maintenance is not always displaced by features. Track expiring items by date.

## 1. Maintenance Categories

| Category | Examples | Frequency | Owner | Capacity share |
|---|---|---|---|---|
| Security patching | OS, runtime, dependencies | Continuous / monthly | | |
| Dependency and platform upgrades | Major versions, end-of-life migrations | Quarterly | | |
| Data housekeeping | Archival, purging, index maintenance | | | |
| Certificates, domains, licences, keys | Renewals, rotations | By expiry date | | |
| Backup and recovery tests | See Backup & Recovery | Quarterly | | |
| Performance and capacity review | | Quarterly | | |
| Support and bug fixing | Triage and fix | Weekly | | |
| Technical debt | Refactoring, clean-up | Planned | | |
| Documentation | Keep docs current | Per release | | |

## 2. Expiry and Renewal Register

| Item | Type | Expires / end of support | Owner | Action date |
|---|---|---|---|---|
| [Domain / certificate / runtime version] | | | | |

## 3. Patch and Upgrade Policy

| Topic | Policy |
|---|---|
| Critical security fixes | Apply within [N] days of availability after testing |
| Routine updates | [Cadence] |
| Major upgrades | Planned as projects with test and rollback |
| Emergency changes | [Process, approval, retro-documentation] |

## 4. Support Model

[Support tiers, hours, response targets, ownership hand-offs; link to [Launch & Support Plan](launch-and-support-plan.md).]

## 5. Budget and Capacity

| Item | Monthly cost / effort | Notes |
|---|---|---|

## 6. End-of-Life and Sunset Considerations

[Conditions under which the product or a feature would be retired; customer notice period; data export and deletion; contractual obligations.]

## Completion Criteria

- [ ] Recurring maintenance tasks have owners, cadence and reserved capacity.
- [ ] Expiring items (certificates, licences, end-of-support dates) are listed with action dates.
- [ ] Patch and emergency-change policies are defined.
- [ ] Run costs and effort are included in the Resource Plan.
