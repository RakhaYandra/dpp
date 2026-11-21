---
id: SLOTWISE-goals-and-metrics
title: Goals and Metrics: SlotWise
domain: 02-strategy
tier: mandatory
status: approved
version: 1.0.0
owner: product-manager
contributors: []
created: 2026-09-01
last_updated: 2026-11-10
depends_on: [product-brief]
feeds: [prd, test-scenarios]
applies_to: [saas]
---

# Goals and Metrics: SlotWise

## Goals

| ID | Goal | Why it matters |
|---|---|---|
| GOAL-01 | Reduce no-shows for pilot salons | No-shows are the largest direct revenue loss named by owners |
| GOAL-02 | Make online booking the default way customers book | Saves owner time and enables reminders |

## Metrics

| ID | Metric | Goal | Baseline | Target | Source | Review |
|---|---|---|---|---|---|---|
| MET-01 | No-show rate (no-shows ÷ completed + no-shows) | GOAL-01 | 18% | ≤ 10% within 90 days of launch | Appointment status in booking data | Monthly |
| MET-02 | Share of appointments booked online | GOAL-02 | 0% | ≥ 50% within 90 days | Booking source field | Monthly |
| MET-03 | Paying salons after 90 days | GOAL-02 | 0 | 40 | Billing records | Monthly |

## Completion Criteria

- [x] Every goal has at least one metric with baseline, target, date and source
- [x] Metrics are defined once here and referenced elsewhere by ID
