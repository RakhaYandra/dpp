# Contributing

Thank you for helping improve the Digital Product Planning Framework. Every contribution that makes a template clearer, more accurate or more usable helps every team that uses it.

By participating you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to Contribute

| Contribution | Good for |
|---|---|
| **Fix a mistake or unclear guidance** | First-time contributors; small pull request |
| **Report an inconsistency** between two templates (different terms, conflicting guidance, broken link) | Anyone; open an issue |
| **Improve an example** with more realistic or better-explained content | Practitioners |
| **Propose a new template or package** | Open an issue first (see below) |
| **Improve validation scripts** | Developers |
| **Add a translation** | Bilingual contributors; open an issue to coordinate |
| **Share real-world feedback** (what you skipped, what was missing) | Everyone; this is very valuable |

## Before You Start

- Search existing issues and pull requests.
- For anything larger than a small fix, **open an issue first** and describe the problem, who it affects and your proposed approach. This avoids wasted effort.

## What Makes a Good Template

New or changed templates must meet the framework's quality standard. Every template has:

1. **Frontmatter** with all required fields ([standard](guides/naming-and-metadata.md)).
2. **About this template**: purpose, when to use, owner, required inputs, related documents.
3. **A structured body** with meaningful sections and appropriate placeholders, not an empty outline.
4. **Guidance** on how to fill each non-obvious section.
5. **Realistic examples** using the fictional product SlotWise (not generic filler, never real companies or people).
6. **Completion criteria**: a checklist that defines "good enough".

And it respects these principles:

| Principle | In practice |
|---|---|
| **Needed** | It supports a decision that would otherwise be made badly. If it only repeats another document, merge instead. |
| **No duplication** | Facts have one canonical home; link to it. |
| **Technology-agnostic** | No languages, frameworks, cloud providers or products, except in the Technology Stack, ADR examples, or where a package genuinely requires it. |
| **Consistent** | Same terms, ID prefixes and structure as other templates. Check the [glossary](GLOSSARY.md) and [traceability guide](guides/traceability.md). |
| **Honest about authority** | Do not invent standards, certifications, laws or compliance requirements. Mention real ones only as examples to verify, with a reminder to consult qualified people. |
| **Scalable** | Works for a solo developer and a team: say what can be skipped, and why. |
| **Original** | Write in your own words. Do not copy text from other templates, books or websites. |

## Workflow

1. **Fork** the repository and create a branch: `fix/<short-description>`, `feat/<template-name>` or `docs/<topic>`.
2. Make your change.
3. **Validate locally:**
   ```
   scripts/validate-metadata
   scripts/check-links
   scripts/check-traceability
   ```
   Fix errors; investigate warnings.
4. If you changed a template's tier, owner or dependencies, regenerate the document map: `scripts/generate-document-map`.
5. Update the [changelog](CHANGELOG.md) under *Unreleased*.
6. Open a **pull request** using the template; explain the problem, the change and how you checked it.
7. Respond to review comments. Maintainers aim to respond within about a week.

## Pull Request Checklist

- [ ] The change is focused: one topic per pull request.
- [ ] Frontmatter is complete and `depends_on`/`feeds` are accurate.
- [ ] Template structure follows the standard (About, body, Completion Criteria).
- [ ] Examples use SlotWise; no real brands, people, or copied text.
- [ ] No unsourced statistics; no legal or regulatory claims stated as fact.
- [ ] Terms match the glossary; new IDs are registered in the traceability guide.
- [ ] Links are relative and validation scripts pass.
- [ ] Diagrams are Mermaid and render on GitHub.
- [ ] The changelog is updated.

## Proposing a New Template

Open an issue using the **New template** form. Include:

- the **decision or risk** it addresses and who owns it,
- **when** in the workflow it is needed and **for which product types**,
- why an **existing template cannot** cover it (or how it would be merged),
- the proposed **tier** and **dependencies**,
- an outline of the main sections.

New *packages* must add documents needed by a recognisable class of product that universal templates do not cover.

## Reviewing

Maintainers and reviewers check: correctness, usefulness, consistency with the rest of the framework, scope, tone and the checklist above. Review comments aim to improve the contribution; please keep discussion constructive. Disagreements on direction are decided by maintainers, with reasons recorded in the issue.

## Licensing of Contributions

By submitting a contribution you confirm that you wrote it (or have the right to submit it) and agree that it is licensed under the repository's licenses: **CC BY 4.0** for content and **MIT** for scripts (see [LICENSE](LICENSE)). Do not submit material copied from sources whose licences do not permit this.

## Security and Sensitive Reports

For problems in the validation scripts that could harm users (for example arbitrary file access), report privately to the maintainers at **[maintainer contact placeholder]** instead of a public issue.

## Recognition

Contributors are listed in the repository history and, for significant contributions, in [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md).
