# Documentation Guide

How to write, review and maintain the documents in this framework. Read this once before filling in your first template; return to it when something feels unclear.

## 1. Principles

1. **Write for a decision.** Every document exists so someone can decide or act. If you cannot say who will use a section and for what, delete it.
2. **One fact, one home.** Define each fact in exactly one document and link to it from others. Duplicated facts drift apart. The "Canonical source" notes in templates tell you where each fact lives.
3. **Say it measurably.** Replace *fast, simple, secure, scalable* with a metric, a target and a condition.
4. **Show uncertainty.** Write "Unknown" or "Assumption" and attach an owner and a date to resolve it. Confident-sounding guesses are the most dangerous content in planning documents.
5. **Be concrete.** Prefer a realistic example to a general statement.
6. **Keep it small enough to maintain.** A short document that is true beats a long one that is stale.
7. **Technology-agnostic by default.** Name technologies only in the Technology Stack and ADRs.

## 2. Anatomy of a Template

Every template has the same shape, so you always know where to look:

| Part | Purpose |
|---|---|
| **Frontmatter** | Machine-readable metadata: id, tier, status, version, owner, dependencies ([standard](guides/naming-and-metadata.md)) |
| **About this template** | Purpose, when to use, owner, required inputs, related documents |
| **Body with guidance** | Sections to complete. `> **Guidance:**` blocks explain how; *Example* blocks illustrate using the fictional product SlotWise |
| **Completion Criteria** | A checklist that tells you when the document is good enough |

When you copy a template into your project, keep the frontmatter and the body; remove *About this template*, guidance and examples when you no longer need them (`scripts/strip-guidance`).

## 3. Working With Placeholders

| Convention | Meaning |
|---|---|
| `[Square brackets]` | Replace with your content |
| `YYYY-MM-DD` | Replace with a date |
| `xx` in an ID (`RISK-xx`, `ASM-xx`) | Replace with a real ID or delete |
| *Example* rows and blocks | Delete or overwrite; they are illustrative and not normative |
| `TBC` | To be confirmed; must have an owner and date |
| `Not applicable` | Allowed with a one-line reason |

Leftover placeholders in an *approved* document are validation warnings.

## 4. Metadata, Status and Versions

- Set `status` honestly. Move to `in-review` only when the Completion Criteria are essentially met.
- **Version** (`major.minor.patch`): *major* when scope or meaning changes, *minor* when sections are added, *patch* for corrections.
- Update `last_updated` on every substantive change.
- `depends_on` lists documents that should be reasonably complete first; `feeds` lists documents that consume this one. Keep both accurate: they power the document map and impact analysis.

## 5. IDs and Traceability

- Use the prefixes in the [traceability guide](guides/traceability.md); define an ID in its canonical document only.
- Never reuse or renumber an ID; retire it instead.
- Refer to items by ID in other documents. When reading a requirement, you should be able to follow its ID up to a goal and down to a test.

## 6. Writing Style

| Do | Avoid |
|---|---|
| Short sentences, active voice, plain words | Jargon, hedging, long paragraphs |
| *must / should / may* used consistently in requirements | Vague verbs (*support, handle, manage*) |
| Tables for catalogs, prose for reasoning | Tables of long prose |
| Defined terms from the project glossary | Several words for one concept |
| Units and conditions on every number | Unsourced statistics |
| Neutral, blameless tone for incidents and reviews | Naming individuals as causes |

**Requirement wording.** A good requirement is singular (one thing), necessary, unambiguous, testable and traceable. *"The system must send a confirmation message within 60 seconds of a booking being confirmed (NFR-009)."*

## 7. Diagrams

Use **Mermaid** in fenced code blocks so diagrams are versioned and rendered by GitHub. Keep each diagram under about 15 nodes; split when larger. Always add a sentence stating what the diagram shows. For design artefacts that need a design tool, link to the source file and describe behaviour in text.

## 8. Linking

- Use **relative links** between documents.
- Link to a document's *canonical* section instead of copying.
- Link to external sources with a title and, for facts that change (laws, policies, prices), the date you checked.

## 9. Standards, Laws and Compliance

This framework never states legal or regulatory requirements as facts. When a topic depends on jurisdiction or industry (privacy, tax, accessibility law, payments, breach notification):

1. Identify what may apply (the templates provide prompts).
2. Have a qualified person confirm applicability and interpretation.
3. Record the **authoritative source**, the **version** and the **date reviewed**.
4. Convert obligations into testable requirements (`NFR-`, `SR-`, `BR-`).

## 10. Review and Approval

| Step | Practice |
|---|---|
| Self-review | Walk the Completion Criteria; fix gaps |
| Peer review | A reader from a *consuming* discipline (an engineer reading the PRD, a tester reading the stories) |
| Approval | Named approvers record a decision; solo projects record a dated self-review |
| After approval | Changes go through a new version and a Decision Log entry |

Review questions that catch most problems: *Could I build or test this from the document alone? What would I have to ask? What is missing that would change a decision? Does anything contradict another document?*

## 11. Keeping Documents Alive

- Assign an owner per document, and review dates for living documents (Risk Register, Roadmap, Test Plan).
- Update the document in the same change as the decision, not later.
- Archive rather than delete; mark superseded documents and link to their replacement.
- Run the validation scripts regularly (they are fast): metadata, links, traceability.

## 12. Common Mistakes

| Mistake | Better |
|---|---|
| Filling every template because they exist | Choose a profile; mark not-applicable with a reason |
| Writing the Executive Summary first | Write it last |
| Features instead of outcomes in goals | State the outcome and metric; features come later |
| NFRs left vague ("fast") | Metric, target, condition, verification method |
| Acceptance criteria that restate the story | Observable pass/fail statements incl. failure paths |
| Copying details between documents | Link to the canonical source |
| Documents with no owner or date | Owner, status and last-updated in every frontmatter |
| Treating the gate as a formality | Use it to decide, and record carried-forward gaps |
