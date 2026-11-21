---
id: SLOTWISE-risk-register
title: Risk Register: SlotWise
domain: 06-project-mgmt
tier: mandatory
status: approved
version: 1.0.0
owner: project-manager
contributors: []
created: 2026-09-01
last_updated: 2026-11-10
depends_on: [prd]
feeds: [release-plan]
applies_to: [saas]
---

# Risk Register: SlotWise

Scoring: probability and impact 1 (low) – 3 (high); score = product.

| ID | Risk | Prob. | Impact | Score | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| RISK-01 | Customers ignore reminders, so MET-01 does not improve | 2 | 3 | 6 | Test timings in pilot (Q-001); add cancel link to every message (FR-003) | Product | Open |
| RISK-02 | Message provider outage delays reminders | 2 | 2 | 4 | Queue with retries (ADR-0002); alert on backlog | Eng lead | Open |
| RISK-03 | Double booking under load erodes trust | 1 | 3 | 3 | Transactional slot guard (ADR-0001); concurrency test TS-002 | Eng lead | Mitigated |
| RISK-04 | Two engineers cannot deliver R1 in 14 weeks (CON-01) | 2 | 3 | 6 | Hold FR-006 for R2; weekly scope check | PM | Open |

## Completion Criteria

- [x] Each risk has a mitigation, owner and status
