---
id: DPP-PKG-mobile-app-store-release
title: App Store Release Requirements
domain: package-mobile
tier: package
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, legal, marketing, qa-lead]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [platform-and-device-support, release-plan, privacy-requirements]
feeds: [release-plan, launch-and-support-plan, operational-readiness]
applies_to: [mobile]
---

# App Store Release Requirements: [App Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Plans everything needed to get the app into, and keep it in, the public app stores: accounts, listing content, policy and privacy declarations, review lead times, release channels and update strategy. |
| **When to use** | At least a few weeks before the first store submission, and for each release that changes permissions, data practices or monetisation. |
| **Owner** | Product Manager with Engineering. |
| **Required inputs** | [Release Plan](../../templates/09-release-ops/release-plan.md); [Privacy Requirements](../../templates/08-security/privacy-requirements.md); [Platform & Device Support](platform-and-device-support.md); **current** store developer policies and guidelines. |
| **Related documents** | [Launch & Support Plan](../../templates/09-release-ops/launch-and-support-plan.md) · [Operational Readiness](../../templates/09-release-ops/operational-readiness.md) |

</details>

> **Guidance:** Store rules **change frequently**; this template lists *what to check*, not the rules themselves. Before each submission, read the current published guidelines for each store you target and record the date and version you checked. Allow **review time and rejection cycles** in your schedule; do not tie a launch date to an uncertain approval.

## 1. Accounts and Ownership

| Item | Store A | Store B |
|---|---|---|
| Developer account owner (organisation, not an individual's personal account where avoidable) | | |
| Fees, renewals and verification requirements | | |
| Who can publish; two-person control; recovery contacts | | |
| Signing keys / certificates: location, custodian, backup, rotation | | |

## 2. Listing Content

| Asset | Requirement | Owner | Status |
|---|---|---|---|
| Name, subtitle, description | Accurate; no unverifiable claims | | |
| Screenshots and preview media | Sizes per store; localised | | |
| Icon and branding | | | |
| Category, keywords, age/content rating questionnaire | | | |
| Support URL, marketing URL, privacy policy URL | Live and reachable | | |
| Release notes | | | |

## 3. Policy, Privacy and Compliance Declarations

| Topic | What to prepare | Source of truth |
|---|---|---|
| Data collection and sharing disclosure ("privacy labels" or equivalent) | Must match actual behaviour including third-party SDKs | [Privacy Requirements](../../templates/08-security/privacy-requirements.md) |
| Permission justifications | Reason for each permission | [Platform & Device Support](platform-and-device-support.md) |
| Account deletion and data rights | Store-required mechanisms, if any | |
| In-app purchases and subscriptions | Store billing rules; pricing display | [Subscription & Billing](../saas/subscription-and-billing.md) |
| Content moderation (user-generated content) | | |
| Region-specific requirements | [Verify per market] | |
| Review notes and demo account | Credentials and instructions for reviewers | |

## 4. Release Channels and Rollout

| Stage | Purpose | Audience | Exit criteria |
|---|---|---|---|
| Internal testing | Smoke test builds | Team | |
| Closed beta | Feedback | Invited users | |
| Public staged rollout | Limit blast radius | % of users | Crash and error thresholds (see [Release Plan](../../templates/09-release-ops/release-plan.md)) |
| Full release | | All | |

**Rollback reality:** an app on users' phones cannot be rolled back at will. Plan for **server-side feature flags, backward-compatible APIs, a forced-update mechanism, and expedited fixes**.

## 5. Update Strategy

| Topic | Decision |
|---|---|
| Release cadence | |
| Minimum supported app version and forced updates | |
| Hotfix process and expected review time | |
| Server compatibility window | [See [API Lifecycle & Versioning](../api-platform/api-lifecycle-and-versioning.md)] |
| Crash and diagnostics reporting | [Privacy-compliant] |

## 6. Submission Checklist

- [ ] Build signed with the correct keys; version and build numbers incremented.
- [ ] All declarations match real behaviour (including third-party SDKs).
- [ ] Listing assets complete; URLs live.
- [ ] Reviewer instructions and test account provided.
- [ ] Support channel and privacy policy ready.
- [ ] Rollout plan and monitoring in place.
- [ ] Policy version and date checked: [ ]

## Completion Criteria

- [ ] Accounts, signing keys and publishing rights are owned by the organisation with backup access.
- [ ] Listing, privacy and permission declarations are complete and consistent with the app.
- [ ] Store policy version and date reviewed are recorded.
- [ ] Review lead time and rejection contingency are in the schedule.
- [ ] Staged rollout, forced-update and hotfix strategy are defined.
