---
id: DPP-07-security-test-plan
title: Security Test Plan
domain: 07-quality
tier: optional
status: draft
version: 0.1.0
owner: security-lead
contributors: [qa-lead, engineering-lead, operations-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [security-requirements, threat-model, test-strategy]
feeds: [test-plan, release-plan, risk-register, operational-readiness]
applies_to: [all]
---

# Security Test Plan: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Plans how the product's security requirements and threat mitigations will be verified: scope, test types, who tests, how findings are handled and when retesting happens. |
| **When to use** | For any product that handles personal or sensitive data, accounts, payments, or is internet-facing. The depth should match the risk. Small low-risk products can cover this inside the Test Strategy. |
| **Owner** | Security Lead (solo projects: the developer, with an external review for high-risk products). |
| **Required inputs** | [Security Requirements](../08-security/security-requirements.md); [Threat Model](../08-security/threat-model.md); [Authentication & Authorization](../05-architecture/authentication-authorization.md); [Test Strategy](test-strategy.md). |
| **Related documents** | [Test Plan](test-plan.md) · [Risk Register](../06-project-mgmt/risk-register.md) · [Release Plan](../09-release-ops/release-plan.md) · [Compliance Assessment](../08-security/compliance-assessment.md) |

</details>

> **Guidance:** Test what the **threat model says matters**. Use published, community-maintained lists of common weaknesses (for example OWASP lists for web applications and APIs) as **checklists to verify against the current published version**, not as a complete definition of security. **Penetration testing must be carried out by suitably qualified people and with written authorization** from whoever owns the systems being tested, including any third-party services. This template does not substitute for professional security assessment.

## 1. Scope

| Item | In scope | Out of scope (and why) |
|---|---|---|
| Applications and APIs | [Web client, public API] | [Third-party provider internals] |
| Environments | Staging (production-like) | Production (only passive checks unless authorized) |
| Components from threat model | [Component list with THREAT references] | |
| Data | Synthetic only | |

## 2. Test Objectives and Sources

| Objective | Source requirement / threat | Verified by (test type) |
|---|---|---|
| Authentication cannot be bypassed or brute-forced | NFR-008; authentication design | Dynamic test, manual review |
| Users cannot access others' data | NFR-008; BR-005 | Authorization tests, TS-004 |
| Personal data is protected in transit and at rest | NFR-008 | Configuration review |
| Dependencies are free of known critical vulnerabilities | Security requirements | Dependency scan |
| Rate limiting and abuse protection work | Threat: abuse of public booking | Dynamic test |

## 3. Test Types

| Type | What it does | When | Who | Output |
|---|---|---|---|---|
| Design / threat-model review | Check mitigations exist for identified threats | Before build, on change | Security + Eng | Review notes |
| Code review (security focus) | Look for insecure patterns | Per change; before release for sensitive areas | Developers | Findings |
| Static analysis | Automated source checks | Every change | Engineering (CI) | Report |
| Dependency and licence scan | Known vulnerable components | Every change; scheduled | Engineering (CI) | Report |
| Secrets scanning | Credentials in code/config | Every change | Engineering (CI) | Report |
| Dynamic analysis | Automated tests against a running system | Per release | QA / Security | Report |
| Authorization and business-logic testing | Role and ownership checks, abuse of workflows | Per release | QA / Security | Scenarios, results |
| Configuration and infrastructure review | Hardening, exposure, access | Per release | Ops / Security | Checklist |
| Penetration test | Simulated attack by qualified testers | Before launch of high-risk products; periodically | Qualified internal/external testers | Report |

## 4. Coverage Checklist (examples to verify against current published lists)

| Weakness area (example categories) | Relevant? | Test(s) | Result |
|---|---|---|---|
| Broken access control / object-level authorization | | TS-004, … | |
| Authentication and session management | | | |
| Injection and unsafe input handling | | | |
| Security misconfiguration | | | |
| Vulnerable and outdated components | | | |
| Cryptographic failures and data exposure | | | |
| Logging and monitoring gaps | | | |
| Server-side request and unsafe external calls | | | |
| API-specific: excessive data exposure, missing rate limits, mass assignment | | | |

Check the current edition of the list you adopt and record its name, version and date: [ ].

## 5. Rules of Engagement and Authorization

| Item | Detail |
|---|---|
| Authorization | [Written approval from system owner(s); includes third parties and hosting provider policies where required] |
| Testers | [Names/organization, qualifications] |
| Allowed techniques and time windows | |
| Prohibited actions | [No production data destruction; no denial of service unless explicitly approved; no social engineering unless approved] |
| Data handling | [Test data only; evidence stored securely; deleted after] |
| Contacts and stop conditions | [Who to call if something breaks] |

## 6. Findings Management

| Severity | Definition | Target response |
|---|---|---|
| Critical | Exploitable now with serious impact on data, accounts or availability | Block release; fix immediately |
| High | Likely exploitable; significant impact | Fix before release unless risk accepted in writing |
| Medium | Limited exploitability or impact | Schedule fix |
| Low / informational | Hardening advice | Backlog |

Each finding: ID, description, evidence, affected component, severity, recommended fix, owner, status, retest result. High risks that remain are recorded in the [Risk Register](../06-project-mgmt/risk-register.md). Do not publish exploit details outside the team.

## 7. Retest and Release Criteria

| Gate | Criteria |
|---|---|
| Ready to release | No open Critical findings; High fixed or formally accepted by [decision maker]; critical fixes retested |
| Ongoing | Scheduled scans; re-run penetration test after major changes or [interval] |

## 8. Schedule and Responsibilities

| Activity | Owner | Date |
|---|---|---|

## Completion Criteria

- [ ] Scope names components, environments and exclusions, with reasons.
- [ ] Each objective traces to a security requirement or threat.
- [ ] Test types, owners and timing are defined; penetration testing, if needed, is assigned to qualified testers.
- [ ] Written authorization and rules of engagement exist before any active testing.
- [ ] Any weakness checklist used is named with its version and date.
- [ ] Severity scale, finding workflow, retest and release criteria are agreed.
