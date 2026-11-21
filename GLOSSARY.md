# Glossary

Terms used across the framework. For the vocabulary of *your* product, use the project [Glossary template](templates/00-foundation/glossary.md).

| Term | Meaning |
|---|---|
| **Acceptance criterion (AC)** | An observable, pass/fail statement that must be true for a user story to count as done. Defined in [User Stories](templates/03-requirements/user-stories.md), ID `AC-<story>.<n>`. |
| **ADR (Architecture Decision Record)** | A short record of one significant architectural decision: context, options, decision, consequences. ID `ADR-NNNN`. |
| **Assumption** | A belief the plan depends on that has not been verified. ID `ASM-`. Tracked in the [Assumption Map](templates/01-discovery/assumption-map.md). |
| **Business rule** | An atomic policy, constraint, calculation or authorization the product must enforce, independent of technology. ID `BR-`. |
| **Canonical source** | The single document where a fact is defined. Other documents link to it. |
| **Completion criteria** | The checklist at the end of each template that tells you when the document is good enough. |
| **Constraint** | A fixed limit on the solution or project (deadline, budget, mandated platform, regulation). ID `CON-`. |
| **Decision log** | Chronological record of product and project decisions (`DEC-`), distinct from architecture decisions (ADRs). |
| **Definition of Done (DoD)** | The agreed checklist a work item must satisfy to count as finished. See [Working Agreements](templates/06-project-mgmt/working-agreements.md). |
| **Definition of Ready (DoR)** | The agreed checklist a work item must satisfy before the team starts it. |
| **Dependency (document)** | A document that should be reasonably complete before another is written; declared in `depends_on`. |
| **Dependency (project)** | Something outside the team's control that the work relies on. ID `DEP-`. |
| **Domain** | One of the numbered groups of templates (01 Discovery … 10 Analytics). |
| **Epic-level requirement** | A capability stated at the level of the PRD, broken into stories later. Here: a functional requirement `FR-`. |
| **Frontmatter** | The YAML metadata block at the top of each document. See [naming and metadata](guides/naming-and-metadata.md). |
| **Functional requirement (FR)** | What the system must do. ID `FR-`, defined in the [PRD](templates/03-requirements/prd.md). |
| **Gate (planning readiness)** | The checkpoint that decides whether planning is sufficient to start building. See [Planning Readiness Review](templates/00-foundation/planning-readiness-review.md). |
| **Goal** | An outcome the product must achieve. ID `GOAL-`, defined in [Goals & Metrics](templates/02-strategy/goals-and-metrics.md). |
| **Guardrail metric** | A metric that must not get worse while pursuing a goal (for example error rate). |
| **Guidance block** | A `> **Guidance:**` blockquote in a template explaining how to fill a section. Removable with `scripts/strip-guidance`. |
| **Hub document** | The document that summarises and links the others for a topic. The PRD is the hub for requirements. |
| **KPI** | Key performance indicator: a metric used to judge progress against a goal. Defined in [Goals & Metrics](templates/02-strategy/goals-and-metrics.md) (target) and the [Analytics Plan](templates/10-analytics/analytics-plan.md) (method). |
| **Manifest** | `project-manifest.yaml`, the register of which documents a project uses and their status. |
| **Metric (MET)** | A measurable indicator with baseline, target and time frame. ID `MET-`. |
| **MoSCoW** | Prioritisation as Must / Should / Could / Won't (this release). |
| **MVP** | The smallest release that can test the core hypothesis. Framed as an experiment in [MVP & Prioritization](templates/02-strategy/mvp-and-prioritization.md). |
| **Non-functional requirement (NFR)** | A measurable quality attribute: performance, availability, security, accessibility, and so on. ID `NFR-`. |
| **Package** | A set of optional, product-type-specific templates in `packages/`. |
| **Persona** | A research-based archetype of a user group. ID `PER-`. |
| **PRD** | Product Requirements Document: the hub stating what will be built, for whom, why, and how success is judged. |
| **Product scope vs project scope** | Product scope is what the product does (PRD). Project scope is what the delivery effort covers (Project Charter). |
| **Profile** | A ready-made selection of documents (solo, team, enterprise). See [profiles](guides/profiles.md). |
| **Release (R1, R2…)** | A planned increment delivered to users, defined in the [Release Plan](templates/09-release-ops/release-plan.md). |
| **Risk** | An uncertain future event with a consequence, written "If … then … resulting in …". ID `RISK-`. |
| **RPO / RTO** | Recovery point objective (maximum acceptable data loss, in time) / recovery time objective (maximum acceptable time to restore service). |
| **RTM** | Requirements Traceability Matrix: the single table joining goals, requirements, stories, design, architecture and tests. |
| **SLI / SLO** | Service level indicator (a measurement of service health) / objective (the target for it). |
| **Tier** | A document's importance: mandatory, recommended, optional or package. |
| **Threat model** | A structured analysis of what could go wrong with security and how it is mitigated. Threat ID `TH-`. |
| **Traceability** | The ability to follow a requirement up to its goal and down to its tests via IDs. See [traceability](guides/traceability.md). |
| **Use case** | A description of an actor's complete interaction with the system to reach a goal, including alternative and failure paths. ID `UC-`. |
| **User story** | A short statement "As a [persona], I want [capability] so that [benefit]" with acceptance criteria. ID `US-`. |
| **WBS** | Work Breakdown Structure: decomposition of project deliverables into work packages. |
