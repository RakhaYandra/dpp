# Release Gate (Light)

Use before each release after the first (the first release also needs the [Operational Readiness Review](../templates/09-release-ops/operational-readiness.md)).

## Scope and quality
- [ ] Release scope lists requirement and story IDs; deferred items recorded.
- [ ] All *Must* acceptance criteria pass; regression run complete.
- [ ] No open Critical defects; High defects fixed or formally accepted.
- [ ] NFR targets affected by this change are verified (performance, security, accessibility).

## Change safety
- [ ] Data migrations are backward-compatible or sequenced; backup/restore point confirmed.
- [ ] Rollback method, triggers and decision maker confirmed; tested for risky changes.
- [ ] Feature flags or staged rollout used for high-risk changes.

## Operations
- [ ] Monitoring and alerts cover new behaviour; dashboards updated.
- [ ] Runbooks, support articles and known issues updated.
- [ ] Third-party limits, contracts and credentials checked.

## Communication
- [ ] Release notes and customer notices ready and accurate.
- [ ] Support and key stakeholders informed of timing and risks.

## Decision
- [ ] Go / conditional go / no-go recorded with name and date.
