---
id: SLOTWISE-release-plan
title: Release Plan: SlotWise R1
domain: 09-release-ops
tier: mandatory
status: approved
version: 1.0.0
owner: project-manager
contributors: []
created: 2026-09-01
last_updated: 2026-11-10
depends_on: [architecture-overview, risk-register, test-scenarios]
feeds: []
applies_to: [saas]
---

# Release Plan: SlotWise R1 (pilot)

## Scope

FR-001 – FR-005 (see [PRD](../03-requirements/prd.md)). FR-006 is deferred to R2.

## Go / no-go criteria

| # | Criterion | Evidence |
|---|---|---|
| 1 | All Must scenarios pass (TS-001 – TS-004, TS-008) | Test report |
| 2 | NFR-001 and NFR-003 verified (TS-002, TS-005) | Test report |
| 3 | No open risk scoring 6 or more without an owner decision | [Risk Register](../06-project-mgmt/risk-register.md) |
| 4 | Rollback rehearsed | Rollback section below |

## Rollout

1. Three pilot salons for 2 weeks.
2. Ten salons for 4 weeks if MET-01 trends down.
3. Open sign-up.

## Rollback

If double bookings or failed confirmations exceed 1% of bookings in any day: disable the public booking link (owners keep their calendar), notify pilot salons, fix, and re-enable after TS-002 and TS-003 pass.

## Completion Criteria

- [x] Scope, go/no-go criteria, rollout and rollback defined
