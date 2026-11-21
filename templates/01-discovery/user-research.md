---
id: DPP-01-user-research
title: User Research Plan and Findings
domain: 01-discovery
tier: recommended
status: draft
version: 0.1.0
owner: ux-researcher
contributors: [product-manager, designer]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [product-brief]
feeds: [persona, assumption-map, prd, information-architecture, user-flow, prototype-review]
applies_to: [all]
---

# User Research: [Product Name] — [Study Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Plans a research study, records what was done, and synthesizes findings into insights that change decisions. Covers both product discovery and UX research (interviews, surveys, observation, usability tests); use one copy per study. |
| **When to use** | Before major commitments (discovery), and again before and after design milestones (usability). |
| **Owner** | UX Researcher or Product Manager. |
| **Required inputs** | [Product Brief](product-brief.md); the riskiest items in the [Assumption Map](assumption-map.md). |
| **Related documents** | [Persona](persona.md) · [Assumption Map](assumption-map.md) · [Prototype Review](../04-ux-ui/prototype-review.md) · [User Feedback Plan](../10-analytics/user-feedback-plan.md) |

</details>

> **Guidance:** Start from decisions, not methods. "What will we do differently depending on what we learn?" If nothing, skip the study. Store raw notes and recordings outside the repo if they contain personal data; keep only anonymized summaries here.

## 1. Research Goals and Decisions

| Research question | Decision it informs | Related ASM-/Q- |
|---|---|---|
| [e.g. How do owners currently handle no-shows?] | [Whether reminders or deposits are the first feature] | ASM-02 |

## 2. Method

| Item | Plan |
|---|---|
| Method(s) | ☐ Interviews ☐ Survey ☐ Observation / contextual inquiry ☐ Diary study ☐ Usability test ☐ Analytics review ☐ Support-ticket analysis |
| Why this method | [Fit to the question; qualitative for *why*, quantitative for *how many*] |
| Participants | [Target number, segments, recruitment source, screening criteria] |
| Incentives and consent | [Consent wording; how recordings and personal data are handled and deleted] |
| Materials | [Discussion guide / survey / prototype link] |
| Schedule and owner | [Dates, who runs and who takes notes] |

**Discussion guide outline** (interviews): context → recent real example → current workflow → pain and workarounds → what they tried → wrap-up. Ask about **past behaviour**, not hypothetical preferences; avoid leading questions.

## 3. Participants

| ID | Segment | Relevant traits | Date | Notes link |
|---|---|---|---|---|
| P01 | [Solo salon owner] | [5 yrs, phone bookings] | [Date] | [Link] |

## 4. Findings

> **Guidance:** Separate **observation** (what happened) from **interpretation** (what it means). State how many participants showed each pattern.

| ID | Observation | Evidence (participants) | Severity / frequency | Interpretation |
|---|---|---|---|---|
| F-01 | Owners re-confirm every booking by message the day before | 7 of 9 | Frequent, time-consuming | Automating reminders addresses a daily chore |

**Representative quotes:** [Short, anonymized.]

## 5. Insights and Implications

| Insight | Implication for product | Action | Owner |
|---|---|---|---|
| [Supported conclusion] | [e.g. Reminder messaging is an MVP requirement] | [Update FR-002; change ASM-02 to Validated] | |

## 6. Assumptions Updated

| Assumption | Previous status | New status | Basis |
|---|---|---|---|
| ASM-01 | Unvalidated | Validated / Invalidated / Inconclusive | F-01, F-03 |

## 7. Limitations and Next Steps

[Sample size, bias, what remains unknown, follow-up studies.]

## Completion Criteria

- [ ] Every study states the decision it informs.
- [ ] Method and sample fit the question; consent and data handling are recorded.
- [ ] Findings separate observation from interpretation and state counts.
- [ ] Insights lead to concrete actions or document updates (Persona, Assumption Map, PRD).
- [ ] Limitations are stated honestly.
- [ ] No identifiable personal data is stored in the repository.
