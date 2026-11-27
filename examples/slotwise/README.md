# Worked Example: SlotWise

SlotWise is a **fictional** appointment-booking SaaS for small salons. This folder shows a complete team-profile planning set, generated with `scripts/scaffold --profile team --types saas` and then filled in.

- 59 planning documents across 11 domains, plus one SaaS package and one optional prototype review.
- A [project manifest](00-foundation/project-manifest.yaml) and an interactive [HTML prototype](04-ux-ui/ui-prototype.html).
- Every document carries frontmatter (`id`, `domain`, `tier`, `status`, `depends_on`, `feeds`) and a `## Completion Criteria` section.
- The set validates with 0 errors and 0 warnings.

## Document map

| Domain | Key documents |
|---|---|
| [00 Foundation](00-foundation/) | [Project Manifest](00-foundation/project-manifest.yaml) · [Glossary](00-foundation/glossary.md) · [Decision Log](00-foundation/decision-log.md) · [Planning Readiness Review](00-foundation/planning-readiness-review.md) |
| [01 Discovery](01-discovery/) | [Product Brief](01-discovery/product-brief.md) · [Persona](01-discovery/persona.md) · [User Research](01-discovery/user-research.md) · [Assumption Map](01-discovery/assumption-map.md) · [Competitor Analysis](01-discovery/competitor-analysis.md) |
| [02 Strategy](02-strategy/) | [Vision & Value Proposition](02-strategy/vision-and-value-proposition.md) · [Goals & Metrics](02-strategy/goals-and-metrics.md) · [MVP & Prioritization](02-strategy/mvp-and-prioritization.md) · [Roadmap](02-strategy/roadmap.md) · [Business Model](02-strategy/business-model.md) |
| [03 Requirements](03-requirements/) | [PRD](03-requirements/prd.md) · [User Stories](03-requirements/user-stories.md) · [Business Rules](03-requirements/business-rules.md) · [Non-Functional Requirements](03-requirements/non-functional-requirements.md) · [RTM](03-requirements/requirements-traceability-matrix.md) |
| [04 UX/UI](04-ux-ui/) | [Information Architecture](04-ux-ui/information-architecture.md) · [User Flow](04-ux-ui/user-flow.md) · [Wireframe Spec](04-ux-ui/wireframe-spec.md) · [UI Design](04-ux-ui/ui-design.md) · [HTML Prototype](04-ux-ui/ui-prototype.html) · [Design System](04-ux-ui/design-system.md) · [Accessibility](04-ux-ui/accessibility-and-responsive.md) · [Prototype Review](04-ux-ui/prototype-review.md) |
| [05 Architecture](05-architecture/) | [Architecture Overview](05-architecture/architecture-overview.md) · [ADRs](05-architecture/adr.md) · [Data Model](05-architecture/data-model.md) · [API Specification](05-architecture/api-specification.md) · [Auth](05-architecture/authentication-authorization.md) · [Infrastructure](05-architecture/infrastructure-and-scalability.md) · [Technology Stack](05-architecture/technology-stack.md) |
| [06 Project Management](06-project-mgmt/) | [Charter](06-project-mgmt/project-charter.md) · [Milestone Plan](06-project-mgmt/milestone-plan.md) · [Working Agreements](06-project-mgmt/working-agreements.md) · [Risk Register](06-project-mgmt/risk-register.md) |
| [07 Quality](07-quality/) | [Test Strategy](07-quality/test-strategy.md) · [Test Plan](07-quality/test-plan.md) · [Test Scenarios](07-quality/test-scenarios.md) · [Test Cases](07-quality/test-case.md) · [UAT Plan](07-quality/uat-plan.md) |
| [08 Security](08-security/) | [Data Classification](08-security/data-classification.md) · [Privacy Requirements](08-security/privacy-requirements.md) · [Threat Model](08-security/threat-model.md) · [Security Requirements](08-security/security-requirements.md) · [Access Control Matrix](08-security/access-control-matrix.md) |
| [09 Release & Ops](09-release-ops/) | [Environment Strategy](09-release-ops/environment-strategy.md) · [Deployment Plan](09-release-ops/deployment-plan.md) · [Release Plan](09-release-ops/release-plan.md) · [Observability](09-release-ops/observability-strategy.md) · [Incident Management](09-release-ops/incident-management.md) · [Backup & Recovery](09-release-ops/backup-and-recovery.md) · [Operational Readiness](09-release-ops/operational-readiness.md) |
| [10 Analytics](10-analytics/) | [Analytics Plan](10-analytics/analytics-plan.md) · [Event Tracking Plan](10-analytics/event-tracking-plan.md) · [Post-Launch Review](10-analytics/post-launch-review.md) |
| [SaaS Package](packages/saas/) | [Multi-Tenancy](packages/saas/multi-tenancy-and-isolation.md) · [Subscription & Billing](packages/saas/subscription-and-billing.md) · [Usage Metering](packages/saas/usage-metering.md) |

## Follow one thread

1. Problem and evidence: [Product Brief](01-discovery/product-brief.md)
2. Measurable goal: GOAL-01 and MET-01 in [Goals & Metrics](02-strategy/goals-and-metrics.md)
3. Requirement: FR-002 in the [PRD](03-requirements/prd.md)
4. Story and criteria: US-002, AC-002.1 to AC-002.3 in [User Stories](03-requirements/user-stories.md)
5. Quality target: NFR-003 in [Non-Functional Requirements](03-requirements/non-functional-requirements.md)
6. Design decision: ADR-0001 in [Architecture Overview](05-architecture/architecture-overview.md)
7. Screen design: [UI Design](04-ux-ui/ui-design.md) and the clickable [HTML Prototype](04-ux-ui/ui-prototype.html)
8. Design review: [Prototype Review](04-ux-ui/prototype-review.md)
9. Test: TS-002 in [Test Scenarios](07-quality/test-scenarios.md), executed per [Test Case](07-quality/test-case.md)
10. Risk and release gate: [Risk Register](06-project-mgmt/risk-register.md), [Release Plan](09-release-ops/release-plan.md), [Planning Readiness Review](00-foundation/planning-readiness-review.md)
11. Decisions: [Decision Log](00-foundation/decision-log.md)

Check it yourself from the repository root:

```
scripts/check-traceability examples/slotwise
scripts/validate-metadata examples/slotwise
scripts/check-links examples/slotwise
```
