---
id: DPP-GUIDE-profiles
title: Planning Profiles
status: approved
version: 0.1.0
---

# Planning Profiles

Not every project should complete every document. A **profile** is a ready-made selection of documents sized to a kind of team and level of risk. Choose one in your [project manifest](../templates/00-foundation/project-manifest.yaml); the scaffold script creates only those documents.

A profile is a **starting point**. Add documents when a risk or requirement justifies them; mark documents *not applicable* (with a one-line reason) when they do not.

## Choosing a Profile

| Question | Solo | Team | Enterprise |
|---|---|---|---|
| People building it | 1–2 | 3–15 | Many teams or external parties |
| Users | Few, known, or an early experiment | Public or business customers | Large organisation, regulated or contractual |
| Cost of failure | Low–moderate, easy to fix | Moderate–high | High: legal, financial, safety, reputation |
| Need for sign-offs and audit evidence | Minimal | Some | Formal |
| Documents (core) | about 14 | up to about 55 | about 70 |

If two columns fit, take the lighter one and add documents where you feel risk.

## Solo (about 14 core documents)

Purpose: think clearly and leave enough trail to resume work after a break, without bureaucracy.

| Document | Notes for solo use |
|---|---|
| Product Brief | One page |
| Goals & Metrics | 1–2 goals, 2–3 metrics |
| PRD (`prd_mode: lite`) | Skip sections marked *Full only* |
| User Stories | Must requirements only |
| Non-Functional Requirements | Short, but still measurable |
| Architecture Overview | Context diagram and building blocks |
| Risk Register | Top 5–10 risks |
| Test Strategy | Half a page |
| Release Plan | Including rollback |
| Planning Readiness Review | ★ items only |
| Persona | One primary persona |
| MVP & Prioritization | The hypothesis and cut line |
| User Flow | The main journeys |
| Decision Log | Short entries |

Add when applicable: Data Model (any stored data), API Specification (if you expose an API), Security Requirements and Privacy Requirements (any personal data), Deployment Plan and Backup & Recovery (anything live), Assumption Map (high uncertainty), Event Tracking Plan (if you will measure).

## Team (up to about 55 documents)

Purpose: align several people across disciplines and keep requirements, design, architecture and tests connected.

- Everything in **Solo**, in full mode (`prd_mode: full`).
- The scaffold for this profile creates all mandatory and recommended documents (about 55). **Most teams will mark several of them not applicable**; that is expected. Prune in the manifest rather than leaving empty documents.
- **All recommended documents** relevant to the product, notably: Persona, User Research, Competitor Analysis, Vision & Value Proposition, Business Model (commercial products), Roadmap, Business Rules, Requirements Traceability Matrix, Information Architecture, Wireframe Spec, Design System, Accessibility & Responsive, ADRs, Data Model, API Specification, Authentication & Authorization, Infrastructure & Scalability, Technology Stack, Project Charter, Milestone Plan, Working Agreements, Test Plan, Test Scenarios, Test Case, UAT Plan, Security Requirements, Threat Model, Data Classification, Privacy Requirements, Access Control Matrix, Environment Strategy, Deployment Plan, Observability Strategy, Incident Management, Backup & Recovery, Operational Readiness, Analytics Plan, Event Tracking Plan, Post-Launch Review.
- Relevant **packages** for your product type.
- Optional documents only when their trigger applies.

## Enterprise (about 70 documents)

Purpose: governance, audit evidence and coordination across teams, vendors and customers.

- Everything in **Team**.
- Requirements Traceability Matrix is **required**, with the traceability check enforced in your pipeline.
- Add the optional documents that support control and risk management: Compliance Assessment, Use Cases, Component Design, Integration Specification, Security Test Plan, Performance Test Plan, Test Data Management, WBS, Resource Plan, Communication Plan, Sprint Planning (if applicable), Maintenance Plan, Launch & Support Plan, User Feedback Plan, Market Research, Opportunity Assessment, Prototype Review.
- The **enterprise** package, plus others as relevant.
- Formal approvals recorded in each document, and the Planning Readiness Review conducted as a meeting with named approvers.

## Customising a Profile

1. Start from the nearest profile in your manifest.
2. For each document you skip, set `status: not-applicable` and add a one-line `reason`.
3. For each document you add, set its status and owner.
4. Record the choice in the [Decision Log](../templates/00-foundation/decision-log.md) if others will wonder why.

## What Never Changes

Whatever the profile, keep: a clear problem statement with evidence, measurable success criteria, explicit scope, testable requirements, measurable non-functional requirements, identified risks and a rollback plan. Those are the minimum that makes planning worth doing.
