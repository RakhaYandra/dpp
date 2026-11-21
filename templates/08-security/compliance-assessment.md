---
id: DPP-08-compliance-assessment
title: Compliance Assessment
domain: 08-security
tier: optional
status: draft
version: 0.1.0
owner: compliance-lead
contributors: [legal, security-lead, product-manager, engineering-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [security-requirements, privacy-requirements]
feeds: [risk-register, release-plan, operational-readiness, data-governance, project-charter]
applies_to: [all]
---

# Compliance Assessment: [Product Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Records which laws, regulations, standards and contractual requirements apply to the product, how well the current plan meets them, what evidence exists, and what decisions were made (for example whether to pursue a certification). It is a **screening and tracking tool**, not a statement of compliance. |
| **When to use** | When the product handles regulated data, serves regulated customers, is sold to organisations that demand certifications, or operates in regulated sectors or regions. Optional for small internal tools with no external obligations; revisit when the market or data changes. |
| **Owner** | Compliance Lead, Legal, or the founder (with qualified advice). |
| **Required inputs** | [Privacy Requirements](privacy-requirements.md) obligations; [Security Requirements](security-requirements.md); customer contracts and questionnaires; [PRD](../03-requirements/prd.md) scope (markets, data, users). |
| **Related documents** | [Risk Register](../06-project-mgmt/risk-register.md) · [Release Plan](../09-release-ops/release-plan.md) · [Data Governance](../../packages/enterprise/data-governance.md) · [Accessibility & Responsive](../04-ux-ui/accessibility-and-responsive.md) |

</details>

> **Guidance:** **This template does not state what any law or standard requires and is not legal advice.** The names listed below are only examples of things to *evaluate*; do not assume any of them applies to you, and do not add requirements you have not confirmed from the authoritative source. For each item you decide applies, record the **exact source, version and date checked**, and who verified your interpretation. Never claim compliance or certification that you have not obtained; use "assessed", "in progress" or "gap identified".

## 1. Applicability Screening

| Framework / regulation / standard (example prompts) | Why it might apply | Applies? (Yes / No / Unsure) | Decision basis and source | Confirmed by / date |
|---|---|---|---|---|
| Data-protection law of regions where users live (e.g. the EU GDPR) | Personal data of people in the region | | | |
| Accessibility standards or laws (e.g. WCAG as a technical standard; local accessibility legislation) | Public-facing services | | | |
| Information security management standard (e.g. ISO/IEC 27001) | Customer or market expectation | | | |
| Service-organisation assurance report (e.g. SOC 2) | Enterprise buyers request it | | | |
| Payment-card industry standard (e.g. PCI DSS) | Card data handled or stored | | | |
| Sector rules (health, finance, education, children's data) | [Sector] | | | |
| Consumer protection, e-commerce and tax rules | Selling to consumers | | | |
| Customer contractual requirements | Enterprise agreements | | | |

**Screening questions:** What data do we hold, about whom, where? Where are our users and our company? Which sectors do customers operate in? Do contracts impose standards? Do we process payments or sensitive categories? Do we use sub-processors in other regions?

## 2. Requirements Register (only for items that apply)

| ID | Source (name, version, clause) | Obligation in our words | Applies to (FR / NFR / SR / process) | Owner | Priority |
|---|---|---|---|---|---|
| CMP-01 | [Authoritative source reference] | [Plain-language summary, checked by Legal] | NFR-0xx | | Must |

*Use `CMP-` as a local numbering convention within this document only; each obligation should also be reflected as an `NFR-` or `SR-` requirement where it affects the product.*

## 3. Gap Assessment

| Obligation | Current state (Met / Partly / Not met / Unknown) | Evidence | Gap and remediation | Owner | Due | Risk ID |
|---|---|---|---|---|---|---|
| CMP-01 | Partly | [Link to design, test result, policy] | [What is missing] | | | RISK-xx |

## 4. Evidence Register

| Evidence | Demonstrates | Location | Owner | Retention | Last updated |
|---|---|---|---|---|---|
| Access review records | Role review performed (see Access Control Matrix) | [Link] | | | |
| Test reports | Security tests executed | [Link] | | | |
| Vendor agreements | Processor terms in place | [Link] | | | |

## 5. Certification and Attestation Decisions

| Option | Driver (customer demand, market, policy) | Cost and effort estimate | Timing | Decision | Decision log |
|---|---|---|---|---|---|
| [Certification / attestation] | | | | ☐ Pursue ☐ Defer ☐ Not needed | DEC-xx |

## 6. Ongoing Compliance

| Activity | Frequency | Owner |
|---|---|---|
| Re-screen applicability (new market, new data, new feature) | At each release planning and annually | |
| Review regulatory or standards changes | [Frequency] | |
| Evidence refresh and internal checks | | |
| Vendor review | | |

## Completion Criteria

- [ ] Every framework, law, standard and contract considered has an applicability decision with source and reviewer.
- [ ] Obligations that apply are recorded with authoritative source references and reflected in `NFR-` or `SR-` requirements.
- [ ] Gaps have owners, dates and linked risks.
- [ ] Evidence locations are recorded for each obligation claimed as met.
- [ ] Certification decisions are recorded as decisions, with rationale.
- [ ] No statement claims compliance or certification that has not been obtained and verified.
