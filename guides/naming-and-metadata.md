---
id: DPP-GUIDE-naming-metadata
title: Naming and Metadata Standards
status: approved
version: 0.1.0
---

# Naming and Metadata Standards

These rules keep every document in the framework predictable, scriptable and easy to find. They apply to templates in this repository and to documents you create from them.

## 1. Naming

| Item | Rule | Example |
|---|---|---|
| Domain folder | `NN-kebab-case`, two-digit prefix gives reading order | `03-requirements/` |
| Document file | `kebab-case.md`, same name as its template | `user-stories.md` |
| Package folder | `kebab-case`, under `packages/` | `packages/api-platform/` |
| Repeating records | `prefix-NNNN-short-title.md` | `adr-0007-use-event-queue.md` |
| Machine-readable specs | Standard extension, same stem | `api-specification.yaml` |
| Product-instance folder | Mirrors the template domain folders | `docs/03-requirements/prd.md` |

- Use lowercase ASCII; no spaces, no underscores in file names.
- A file name describes the *document type*, not the product. The product name goes in the title.
- Never put dates or versions in file names; use frontmatter and Git history.

## 2. Frontmatter

Every document starts with YAML frontmatter.

```yaml
---
id: DPP-03-prd              # template id: DPP-<domain>-<name>; project copies keep it
title: Product Requirements Document (PRD)
domain: 03-requirements
tier: mandatory             # mandatory | recommended | optional | package
status: draft               # see section 3
version: 0.1.0              # semantic: major = scope change, minor = additions, patch = fixes
owner: product-manager      # a role; in an instance, add a person's name
contributors: []
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: []              # file stems that must be reasonably complete first
feeds: []                   # file stems that consume this document
applies_to: [all]           # all | saas | mobile | api-platform | enterprise | developer-tools
---
```

| Field | Required | Notes |
|---|---|---|
| `id`, `title`, `domain`, `tier`, `status`, `version`, `owner`, `last_updated` | Yes | Checked by `validate-metadata` |
| `depends_on`, `feeds` | Yes (may be empty) | Must reference existing file stems; drives the dependency map |
| `contributors`, `created`, `applies_to` | Recommended | |
| Extra fields (e.g. `prd_mode`) | Optional | Template-specific; document them in the template |

## 3. Status Values

| Status | Meaning | Allowed next |
|---|---|---|
| `draft` | Being written; may change freely | `in-review` |
| `in-review` | Complete enough to be reviewed | `draft`, `approved` |
| `approved` | Reviewed and agreed; changes need a new version and a decision-log entry | `superseded`, `archived`, `in-review` |
| `superseded` | Replaced by a newer document (link it) | `archived` |
| `archived` | Kept for history only | — |
| `not-applicable` | Deliberately skipped for this product; add a one-line reason in the manifest | `draft` |

"Not applicable" is a valid and healthy outcome: not every product needs every document.

## 4. Template Structure

Every template contains, in this order:

1. Frontmatter
2. **About this template** block: purpose, when to use, owner, required inputs, related documents
3. The fill-in body, with `> **Guidance:**` blockquotes and illustrative *Example* blocks
4. **Completion Criteria** checklist

Guidance and examples can be removed with `scripts/strip-guidance`. Examples use the fictional product *SlotWise* and are never normative.

## 5. Writing Conventions

- Prefer tables for catalogs (requirements, risks, metrics) and prose for reasoning.
- One fact, one home. Summarize elsewhere and link; never copy.
- Use *must / should / may* consistently in requirements; avoid *fast, easy, robust, intuitive* without a measurable definition.
- Define project terms once in the project glossary and use them identically everywhere.
- Prefer relative links so documents work in any Git host.
- Diagrams use Mermaid in fenced blocks so they diff and render on GitHub.
