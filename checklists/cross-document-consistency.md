# Cross-Document Consistency Checklist

Run through this when several documents are ready for review together. Most planning failures hide in the gaps *between* documents. Where a script can check an item, it is noted.

## 1. Goals, metrics and measurement

- [ ] Every `GOAL-` has at least one `MET-` with baseline, target, time frame and owner.
- [ ] Every `MET-` has a definition and data source in the Analytics Plan, and events in the Event Tracking Plan. *(manual)*
- [ ] Expected results in the PRD agree with targets in Goals & Metrics.
- [ ] Guardrail metrics exist for quality, performance or cost, and appear in the Release Plan's go/no-go criteria.

## 2. Requirements and scope

- [ ] Every `FR-` links to a goal and a persona; none exist "because someone asked".
- [ ] PRD scope (in / out / deferred) agrees with MVP & Prioritization and with the Release Plan's scope.
- [ ] Project Charter scope covers the work to deliver the PRD scope, and nothing else.
- [ ] No requirement is defined in two documents with different wording; the PRD, Business Rules and NFR documents each hold their own, others link.
- [ ] Priorities (Must / Should / Could) are identical in the PRD, User Stories and Release Plan.

## 3. Stories, criteria and tests

- [ ] Every *Must* `FR-` has at least one `US-`. *(check-traceability)*
- [ ] Every `US-` has at least one `AC-`. *(check-traceability)*
- [ ] Every `AC-` is covered by at least one `TS-`. *(check-traceability)*
- [ ] Every business rule `BR-` that affects behaviour appears in at least one acceptance criterion or test scenario.
- [ ] Failure and boundary cases exist for data entry, permissions and concurrency.
- [ ] Test Strategy quality gates match the Release Plan go/no-go criteria.

## 4. Non-functional requirements

- [ ] Every *Must* `NFR-` has a verification method: a test scenario, a monitoring rule, or an inspection.
- [ ] Each architectural driver cites the `FR-`/`NFR-`/`BR-` that causes it.
- [ ] Recovery targets (RPO/RTO) in NFRs, Backup & Recovery and Infrastructure agree.
- [ ] Availability targets in NFRs agree with the SLOs in the Observability Strategy.
- [ ] Accessibility target (standard, version, level) is identical in NFRs, Accessibility & Responsive and Test Strategy.

## 5. Design, data and interfaces

- [ ] Screens in the Wireframe Spec map to requirements; every UI-facing *Must* `FR-` has screens. 
- [ ] Entities in the Data Model, fields in the API Specification and terms in the UI use the same names (see the Glossary).
- [ ] Every personal-data field has a classification and appears in the privacy inventory with a purpose and retention.
- [ ] Every API operation traces to a story or requirement and states its access level.
- [ ] External systems in the Architecture Overview's context diagram all appear in the Integration Specification.

## 6. Security and privacy

- [ ] Threats in the Threat Model have mitigations that appear as `SR-` or `NFR-` requirements, and tests.
- [ ] Roles in the Access Control Matrix, Authentication & Authorization and personas agree.
- [ ] Privacy obligations identified with qualified advice are reflected in requirements, retention, backups and deletion processes.
- [ ] Data classification handling rules are applied in logging, analytics, test data and backups.

## 7. Delivery and risk

- [ ] Milestone dates agree with the Roadmap, Charter constraints and Release Plan dates.
- [ ] High risks in the Risk Register have owners and mitigations; the PRD's top risks match.
- [ ] Every open question (`Q-`) has an owner and date; resolved ones point to a `DEC-`.
- [ ] Definition of Done includes the events, tests and documentation updates that other documents require.

## 8. Release and operations

- [ ] Rollback triggers and method in the Release Plan match the Deployment Plan's technical procedure.
- [ ] Every alert (`MON-`) has a response; every *Must* SLO has an alert or report.
- [ ] Operational Readiness items link to evidence, and open gaps are accepted by a named decision maker.
- [ ] Launch & Support, Release Plan and Incident Management agree on who communicates what, to whom.

## 9. Terminology and housekeeping

- [ ] Each term has one meaning and one spelling across documents (check the project Glossary).
- [ ] Every document has status, owner, version and a current `last_updated`.
- [ ] `depends_on` / `feeds` lists are accurate. *(validate-metadata)*
- [ ] No broken links. *(check-links)*
- [ ] No leftover placeholders in documents marked approved. *(validate-metadata warnings)*
