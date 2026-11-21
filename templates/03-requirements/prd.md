---
id: DPP-03-prd
title: Product Requirements Document (PRD)
domain: 03-requirements
tier: mandatory            # mandatory | recommended | optional | package
status: draft              # draft | in-review | approved | superseded | archived
version: 0.1.0
owner: product-manager
contributors: []           # roles or names
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [product-brief, goals-and-metrics]
feeds: [user-stories, non-functional-requirements, architecture-overview, test-strategy, release-plan]
applies_to: [all]
prd_mode: full             # full | lite  (lite = sections marked "Full only" may be skipped)
---

# PRD: [Product or Feature Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | The single hub document that states *what* will be built, *for whom*, *why*, and *how success is judged*. It summarizes and links; it does not duplicate the detail kept in other documents. |
| **When to use** | After the Product Brief and Goals & Metrics exist, before architecture, detailed design and test planning begin. Skip a full PRD for trivial changes (bug fixes, copy tweaks); use `prd_mode: lite` for small features or solo projects. |
| **Owner** | Product Manager (solo projects: the founder/developer). |
| **Required inputs** | [Product Brief](../01-discovery/product-brief.md), [Goals & Metrics](../02-strategy/goals-and-metrics.md). Helpful: Personas, User Research, Competitor Analysis, MVP & Prioritization. |
| **Related documents** | [User Stories](user-stories.md) · [Non-Functional Requirements](non-functional-requirements.md) · [Business Rules](business-rules.md) · [Traceability Matrix](requirements-traceability-matrix.md) · [Risk Register](../06-project-mgmt/risk-register.md) · [Architecture Overview](../05-architecture/architecture-overview.md) · [Release Plan](../09-release-ops/release-plan.md) |

**How this template works**

- **One home per fact.** If a section says "Canonical source: X", write the detail in X and keep only a summary plus IDs here.
- **Everything gets an ID** (`GOAL-`, `MET-`, `PER-`, `FR-`, `NFR-`, `BR-`, `RISK-`, `DEC-`). IDs are what make traceability possible. Never reuse or renumber an ID; retire it instead.
- **Guidance** appears as blockquotes starting with `Guidance:`. Examples use the fictional product *SlotWise* (booking software for small service businesses) and are illustrative only. Both can be removed with `scripts/strip-guidance`.
- **Fill in this order:** 3 → 5 → 4 → 6 → 2 → 7–12 → 1 (the Executive Summary last).

</details>

---

## 1. Executive Summary

> **Guidance:** Write this last. A stakeholder who reads only this section should know the problem, the solution, the expected impact and the target date. Max ~150 words. Do not introduce anything that is not in the sections below.

| | |
|---|---|
| **Product / feature** | [Name] |
| **Problem** | [2–3 sentences: who has the problem, what it costs them, evidence. Canonical source: Product Brief] |
| **Proposed solution** | [2–3 sentences: the approach and why it is the right one] |
| **Primary success metrics** | [MET-01 summary] · [MET-02 summary] |
| **Target release** | [Quarter or date; refer to Release Plan] |

> *Example:* Small service businesses lose revenue to missed appointments; owners report no-show rates of roughly one in five bookings. SlotWise lets customers self-book and sends automated confirmations and reminders so owners stop chasing by phone. We expect no-shows to fall from 18% to 10% within three months of launch (MET-01).

---

## 2. Context and Rationale

> **Guidance:** Keep this to one screen. The evidence lives in discovery documents; link to them instead of pasting. Replace generic statements ("the market is growing") with specific, sourced facts.

### 2.1 Why Now
[What changed—market timing, a customer commitment, a platform shift, an internal capability—that makes this the right moment? If nothing, say so; the reason may be weak.]

### 2.2 Evidence Summary

| Evidence | Summary (1–2 lines) | Canonical source |
|---|---|---|
| User research | [Method, sample size, strongest finding] | [User Research](../01-discovery/user-research.md) |
| Market / competitors | [Key gap this product addresses] | [Competitor Analysis](../01-discovery/competitor-analysis.md) |
| Quantitative data | [Support tickets, requests, usage numbers; state source and date] | [link] |
| Riskiest assumptions | [Top 1–3 assumptions and how they are being validated] | [Assumption Map](../01-discovery/assumption-map.md) |

### 2.3 Related Documents
[Other PRDs, research reports, contracts, regulatory references. Link each with one line on why it matters.]

---

## 3. Goals, Metrics and Scope

### 3.1 Goals

> **Guidance:** Canonical source: [Goals & Metrics](../02-strategy/goals-and-metrics.md). Summarize here. Each goal must connect to at least one metric in 3.2. Write 1–3 business goals and 1–3 user goals; more means no focus.

| ID | Type | Goal | Strategic link |
|---|---|---|---|
| GOAL-01 | Business | [Outcome, not feature. e.g. "Make the product viable for paying small businesses"] | [Vision / OKR / funding milestone] |
| GOAL-02 | User | [What users can now accomplish or no longer suffer] | [Persona PER-01] |

### 3.2 Success Metrics

> **Guidance:** Every metric needs a baseline (or an explicit plan to establish one), a target, a time frame and a measurement method. "Improve engagement" is not a metric. Canonical definitions (formulas, data sources) live in the [Analytics Plan](../10-analytics/analytics-plan.md).

| ID | Goal | Metric | Baseline | Target | By when | Measured by |
|---|---|---|---|---|---|---|
| MET-01 | GOAL-02 | Customer no-show rate | 18% (owner survey, n=40) | ≤ 10% | 3 months after launch | Booking status events |
| MET-02 | GOAL-01 | Paying accounts | 0 | 50 | 6 months after launch | Billing system |

### 3.3 Expected Results

> **Guidance:** State in plain numbers what you expect after launch, so you can check your assumptions later. These are predictions, not commitments; the [Post-Launch Review](../10-analytics/post-launch-review.md) compares them with reality.

[e.g. "In the first 3 months, 30 of 50 pilot businesses activate online booking; at least 15 convert to a paid plan."]

### 3.4 Scope

> **Guidance:** Canonical source for product scope. Be explicit about what is **out**; ambiguity here causes most scope creep. Project-level scope (budget, timeline boundaries) belongs in the [Project Charter](../06-project-mgmt/project-charter.md), not here.

| In scope | Out of scope (non-goals) | Deferred (later release) |
|---|---|---|
| [Capability or boundary] | [Explicitly excluded, with reason] | [Planned for a later release] |

### 3.5 Assumptions and Constraints

| ID | Type | Statement | Impact if wrong / Source |
|---|---|---|---|
| ASM-01 | Assumption | [Something believed true but unverified] | [Consequence; validation plan] |
| CON-01 | Constraint | [Fixed limit: deadline, budget, team size, mandated platform, legal obligation] | [Source] |

---

## 4. Users and Scenarios

> **Guidance:** Canonical sources: [Persona](../01-discovery/persona.md) and [Use Cases](use-cases.md). Do not restate persona details. List who the product is for and which scenarios matter most.

### 4.1 Target Users

| ID | Persona | Priority | One-line need |
|---|---|---|---|
| PER-01 | [Name / role] | Primary | [What they need most] |
| PER-02 | [Name / role] | Secondary | [...] |

### 4.2 Key Scenarios

[3–5 end-to-end scenarios in one or two sentences each, naming the persona. Link to Use Cases or a User Flow for step-by-step detail. Include the main unhappy path.]

---

## 5. Functional Requirements

> **Guidance:** This is an **epic-level** catalog: capabilities, not tasks. Detailed user stories and acceptance criteria live in [User Stories](user-stories.md) and are linked by ID. Each FR should be understandable on its own, traceable to a goal, and testable. Prioritize with MoSCoW; map to P-levels only if your team uses them (Must = P0, Should = P1, Could = P2, Won't = out of scope this release).

### 5.1 Requirement Catalog

| ID | Requirement (what the system must do) | Persona | Goal | Priority | Release | Stories |
|---|---|---|---|---|---|---|
| FR-001 | [e.g. Customers can book an available time slot for a chosen service without creating an account] | PER-01 | GOAL-02 | Must | R1 | US-001–US-004 |
| FR-002 | [e.g. System sends booking confirmation and reminder messages automatically] | PER-01 | GOAL-02 | Must | R1 | US-005–US-006 |
| FR-003 | [...] | | | Should | R2 | |

> **Writing a good requirement:** one capability per row; use "must / should / may" consistently; state the outcome, not the implementation; avoid vague words (*fast, easy, intuitive, robust*). Quality targets go in 6, not here.

### 5.2 Requirement Detail (only where the table is not enough)

#### FR-001 — [Name]
- **Description:** [Behavior in 2–4 sentences]
- **Business rules:** [BR-001, BR-004 — see [Business Rules](business-rules.md)]
- **Dependencies:** [Other FRs, external systems]
- **Out of scope for this requirement:** [Boundary]
- **Notes / open points:** [Link to open question Q-01, if any]

### 5.3 MVP Boundary

> **Guidance:** Canonical source: [MVP & Prioritization](../02-strategy/mvp-and-prioritization.md). Confirm here that all *Must* requirements together are the smallest release that can test the core hypothesis. If removing a *Must* would not break the hypothesis, it is not a Must.

[One paragraph: the core hypothesis and why the Must set is sufficient.]

---

## 6. Non-Functional Requirements (Summary)

> **Guidance:** Canonical source: [Non-Functional Requirements](non-functional-requirements.md) with `NFR-` IDs and measurable targets. Summarize only the headline targets that shape the product decision.

| Category | Headline target | NFR ID |
|---|---|---|
| Performance | [e.g. Booking page interactive in < 2 s on a mid-range phone over 4G] | NFR-001 |
| Availability / reliability | [e.g. 99.5% monthly availability for booking] | NFR-004 |
| Security & privacy | [Authentication, sensitive-data handling, regulations that apply—verify with qualified advice] | NFR-008 |
| Accessibility | [Target conformance level, e.g. WCAG 2.2 AA] | NFR-011 |
| Scalability | [Expected users/data volume at 6 and 12 months] | NFR-006 |
| Compatibility & localization | [Browsers/devices/OS, languages, time zones, formats] | NFR-013 |

---

## 7. Experience and Design (Full only)

> **Guidance:** Link to design artifacts rather than embedding them. Keep only the principles that should guide every design decision for this product.

- **Information architecture / sitemap:** [link]
- **User flows:** [link]
- **Wireframes / prototype:** [link]
- **Design system and guidelines:** [link]

**Design principles for this product** (2–4, each with a consequence):
1. [e.g. "Booking in three taps or fewer" → no mandatory registration before booking.]

---

## 8. Technical Considerations (Full only)

> **Guidance:** Stay technology-agnostic unless a constraint forces a choice. This section records *constraints and integration needs*, not design. Design lives in the architecture documents.

| Topic | Summary | Canonical source |
|---|---|---|
| Architecture approach | [One or two sentences] | [Architecture Overview](../05-architecture/architecture-overview.md) |
| Data (key entities) | [Names only] | [Data Model](../05-architecture/data-model.md) |
| External integrations | [Service — purpose — owner] | [Integration Specification](../05-architecture/integration-specification.md) |
| Technical constraints | [Existing systems, mandated platforms, legacy limits] | [link] |
| Analytics / tracking needs | [What must be measured to evaluate MET-xx] | [Event Tracking Plan](../10-analytics/event-tracking-plan.md) |

---

## 9. Release and Rollout Summary

> **Guidance:** Canonical sources: [Release Plan](../09-release-ops/release-plan.md) and [Milestone Plan](../06-project-mgmt/milestone-plan.md). Show only what scope lands in which release, plus the target dates.

| Release | Target date | Included requirements | Audience |
|---|---|---|---|
| R1 (MVP) | [Date] | FR-001, FR-002 | [Beta users / all users] |
| R2 | [Date] | FR-003 … | |

**Launch, support and communication:** see [Launch & Support Plan](../09-release-ops/launch-and-support-plan.md) (optional).

---

## 10. Dependencies, Risks and Open Questions

### 10.1 Dependencies

| ID | Dependency | Owner | Needed by | Status | If delayed / mitigation |
|---|---|---|---|---|---|
| DEP-01 | [Team, vendor, approval, data] | [Name] | [Date] | On track / At risk / Blocked | [Impact and fallback] |

### 10.2 Top Risks

> **Guidance:** List the 3–5 risks that could change the product's scope or success. The full register is the [Risk Register](../06-project-mgmt/risk-register.md); use the same IDs.

| ID | Risk | Probability | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| RISK-01 | [If X happens, then Y] | H / M / L | H / M / L | [Action] | [Name] |

### 10.3 Open Questions

> **Guidance:** Anything that must be answered before development starts. Each question needs an owner and a date. Resolved questions move to the Decision Log.

| ID | Question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | [Question] | [Name] | [Date] | Open |

---

## 11. Key Decisions

> **Guidance:** Record product-level decisions that shaped this PRD (scope cuts, priority calls, rejected options). Canonical log: [Decision Log](../00-foundation/decision-log.md). Architecture decisions are recorded separately as ADRs.

| ID | Decision | Date | Rationale | Alternatives rejected |
|---|---|---|---|---|
| DEC-01 | [Decision] | [Date] | [Why] | [Options and why not] |

---

## 12. Post-Launch Plan (Full only)

> **Guidance:** Schedule the checks now, before launch. Metrics come from 3.2; the review itself is run using the [Post-Launch Review](../10-analytics/post-launch-review.md) template.

| When | Review focus | Metrics | Decision it informs |
|---|---|---|---|
| Week 1 | Stability, activation | [MET-xx] | Continue rollout / roll back |
| Week 4 | Adoption, early outcomes | [MET-xx] | Fix vs. extend |
| Week 12 | Goal achievement | [MET-xx] | Iterate, pivot, or sunset |

**Learning goals:** [What do we want to learn from this release, and where will we record it?]

---

## 13. Appendix

### 13.1 Glossary Terms Introduced
[Link new terms to the project [Glossary](../00-foundation/glossary.md); do not define them here.]

### 13.2 Revision History

| Version | Date | Author | Summary of change |
|---|---|---|---|
| 0.1.0 | YYYY-MM-DD | [Name] | Initial draft |

### 13.3 Approvals

> **Guidance:** Approval means "I have read this and agree the scope and goals are right," not "I wrote it." Add or remove roles to fit your team. Solo projects: record self-review and date.

| Role | Name | Decision | Date |
|---|---|---|---|
| Product | | ☐ Approved | |
| Engineering | | ☐ Approved | |
| Design / UX | | ☐ Approved | |
| QA | | ☐ Approved | |
| Business / Sponsor | | ☐ Approved | |

---

## Completion Criteria

The PRD is ready to move to `status: approved` when:

- [ ] The problem is stated with evidence and is not a disguised solution.
- [ ] Every goal has at least one metric with baseline, target, time frame and method.
- [ ] In-scope, out-of-scope and deferred items are explicit.
- [ ] Every FR has an ID, priority, release, persona and goal; every *Must* FR has at least one user story.
- [ ] Requirements are testable and contain no unexplained vague terms.
- [ ] NFRs with measurable targets exist for performance, availability, security/privacy and accessibility (or are explicitly marked not applicable with a reason).
- [ ] Top risks have owners and mitigations; every open question has an owner and a due date.
- [ ] Dependencies on other teams, vendors or approvals are identified.
- [ ] All links resolve and all IDs used here are defined in their canonical document.
- [ ] The Executive Summary matches the body.
- [ ] Required approvers have signed off, or a review date is set.

> **Keeping it alive:** after approval, change requirements through a new version and a Decision Log entry. Never edit approved scope silently.
