## What and why

<!-- Describe the problem this solves and who it helps. Link the issue: Fixes #123 -->

## Type of change

- [ ] Fix (typo, broken link, unclear guidance)
- [ ] Improvement to an existing template, guide or example
- [ ] New template or package (issue linked and discussed first)
- [ ] Tooling (scripts, workflow)
- [ ] Documentation only

## What changed

<!-- Files or templates touched and the key decisions. -->

## How I checked it

- [ ] `scripts/validate-metadata` passes
- [ ] `scripts/check-links` passes
- [ ] `scripts/check-traceability examples/slotwise` passes (if examples or the ID scheme changed)
- [ ] `scripts/generate-document-map --check` passes (if tier, owner or dependencies changed)

## Quality checklist

- [ ] Template structure follows the standard: frontmatter, About, body with guidance, Completion Criteria
- [ ] `depends_on` / `feeds` are accurate; new IDs are registered in `guides/traceability.md`
- [ ] Facts have one canonical home; I link instead of duplicating
- [ ] Technology-agnostic (technology named only where justified)
- [ ] Examples use SlotWise; no real brands or people; no unsourced statistics
- [ ] No legal, regulatory or standards claims stated as fact (only as examples to verify)
- [ ] Terms match `GLOSSARY.md`
- [ ] Content is my own wording and I may license it under CC BY 4.0 (scripts: MIT)
- [ ] `CHANGELOG.md` updated under *Unreleased*
