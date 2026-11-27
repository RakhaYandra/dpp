# Changelog

All notable changes to this project are recorded here. The project follows [semantic versioning](https://semver.org/) for the framework as a whole: **major** = restructured domains or breaking changes to the ID scheme or frontmatter, **minor** = new templates or guides, **patch** = corrections and clarifications.

## [Unreleased]

### Added
- UI Design and Interactive Prototype template in `04-ux-ui`, with a self-contained HTML prototype starter. The scaffold copies both for solo, team and enterprise profiles.

### Changed
- Prototype Review now uses the UI design document and its prototype artefact as required inputs.

## [0.1.0] - Initial release

### Added
- Repository structure with 10 documentation domains plus a foundation domain.
- 71 universal templates (10 mandatory, 44 recommended, 17 optional) and a project manifest.
- 17 product-specific templates in 5 packages: SaaS, mobile, API platform, enterprise, developer tools.
- Guides: naming and metadata, traceability and ID scheme, document map, profiles, planning workflow, choosing packages.
- Root documents: README, DOCUMENTATION_GUIDE, GLOSSARY, CONTRIBUTING, CODE_OF_CONDUCT, LICENSE.
- Scripts (Python standard library only): validate-metadata, check-links, check-traceability, strip-guidance, generate-document-map, scaffold.
- Checklists, issue forms, pull-request template and validation workflow.
- Worked example: SlotWise (`examples/slotwise/`), a fictional product with 10 connected documents.
