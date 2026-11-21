---
id: DPP-09-environment-strategy
title: Environment Strategy
domain: 09-release-ops
tier: recommended
status: draft
version: 0.1.0
owner: engineering-lead
contributors: [operations-lead, qa-lead, security-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [architecture-overview, infrastructure-and-scalability]
feeds: [deployment-plan, test-plan, test-data-management, release-plan, operational-readiness]
applies_to: [all]
---

# Environment Strategy: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines the environments the product runs in (development through production): what each is for, how closely it mirrors production, who can access it, what data it holds and how changes are promoted between them. |
| **When to use** | After the architecture and infrastructure approach; before test planning and the deployment plan. Solo or small products may use only two or three environments; document the minimum you need. |
| **Owner** | Engineering Lead or Operations Lead. |
| **Required inputs** | [Architecture Overview](../05-architecture/architecture-overview.md); [Infrastructure & Scalability](../05-architecture/infrastructure-and-scalability.md); [Test Strategy](../07-quality/test-strategy.md) needs; [Data Classification](../08-security/data-classification.md). |
| **Related documents** | [Deployment Plan](deployment-plan.md) · [Test Data Management](../07-quality/test-data-management.md) · [Release Plan](release-plan.md) |

</details>

> **Guidance:** Every environment must have a **purpose** that justifies its cost. The closer an environment is to production, the more it protects you from release surprises. **Never use real personal data in non-production environments** unless it is protected to production standards and formally approved.

## 1. Environment Catalog

| Environment | Purpose | Used by | Production parity | Data | Access | Deployed from | Lifetime |
|---|---|---|---|---|---|---|---|
| Local / development | Build and debug | Developers | Low | Synthetic | Developer | Working copy | Per developer |
| Integration / test | Automated and manual testing | QA, developers | Medium | Synthetic, resettable | Team | Main branch builds | Persistent |
| Staging / pre-production | Release rehearsal, UAT, performance checks | QA, business | **High** (config, topology, versions) | Anonymized or synthetic | Restricted | Release candidates | Persistent |
| Production | Real users | Customers | — | Real | Least privilege, audited | Approved releases | Persistent |
| Preview (optional) | Review of a single change | Reviewers | Low | Synthetic | Reviewers | Pull requests | Short-lived |

## 2. Parity and Differences

| Aspect | Staging vs production | Accepted difference and risk |
|---|---|---|
| Topology, scale | | |
| Versions and configuration | | |
| Third-party integrations | [Sandbox vs live] | |
| Data volume | | |

## 3. Promotion and Configuration

| Topic | Decision |
|---|---|
| Promotion path | [Which build moves environment to environment; same artifact in all] |
| Configuration and secrets | [Per-environment config separate from code; secrets never in the repository] |
| Environment creation | [Reproducible from versioned definitions] |
| Database changes | [Migration approach per environment] |
| Feature flags | [Where used] |

## 4. Access and Security

| Environment | Who may access | How (approval, audit) | Data restrictions |
|---|---|---|---|

## 5. Cost and Housekeeping

[Budget, shutdown schedules, cleanup of short-lived environments, ownership of each environment.]

## Completion Criteria

- [ ] Each environment has a purpose, owner, access rule and data rule.
- [ ] Production-parity gaps are listed with their risk.
- [ ] Promotion path uses the same build artifact across environments.
- [ ] No real personal data in lower environments without approval and equal protection.
- [ ] Configuration and secrets handling is defined.
