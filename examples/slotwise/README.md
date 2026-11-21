# Worked Example: SlotWise

SlotWise is a **fictional** appointment-booking SaaS for small salons. This folder shows a small, consistent set of filled documents so you can see how the framework's pieces connect. It is intentionally compact (11 documents) and is not a complete team-profile project.

Follow one thread through the documents:

1. Problem and evidence: [Product Brief](01-discovery/product-brief.md)
2. Measurable goal: GOAL-01 and MET-01 in [Goals & Metrics](02-strategy/goals-and-metrics.md)
3. Requirement: FR-002 in the [PRD](03-requirements/prd.md)
4. Story and criteria: US-002, AC-002.1 – AC-002.3 in [User Stories](03-requirements/user-stories.md)
5. Quality target: NFR-003 in [Non-Functional Requirements](03-requirements/non-functional-requirements.md)
6. Design decision: ADR-0001 in [Architecture Overview](05-architecture/architecture-overview.md)
7. Test: TS-002 in [Test Scenarios](07-quality/test-scenarios.md)
8. Risk and release gate: [Risk Register](06-project-mgmt/risk-register.md), [Release Plan](09-release-ops/release-plan.md)
9. Decisions: [Decision Log](00-foundation/decision-log.md)

Check it yourself from the repository root:

```
scripts/check-traceability examples/slotwise
scripts/validate-metadata examples/slotwise
scripts/check-links examples/slotwise
```
