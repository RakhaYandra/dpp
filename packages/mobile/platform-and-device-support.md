---
id: DPP-PKG-mobile-platform-and-device-support
title: Platform and Device Support
domain: package-mobile
tier: package
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, qa-lead, designer]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [prd, non-functional-requirements]
feeds: [test-strategy, accessibility-and-responsive, app-store-release, technology-stack, test-plan]
applies_to: [mobile]
---

# Platform and Device Support: [App Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines which mobile platforms, operating-system versions and device classes the app supports, which hardware and OS capabilities it needs, and how support will be tested and phased out. Combines "platform requirements" and "device compatibility". |
| **When to use** | Before technology selection and design for any native, cross-platform or installable mobile app. |
| **Owner** | Product Manager with Engineering Lead. |
| **Required inputs** | Target-audience device data (from research or analytics); [NFRs](../../templates/03-requirements/non-functional-requirements.md); platform vendors' current published requirements. |
| **Related documents** | [Test Strategy](../../templates/07-quality/test-strategy.md) · [Accessibility & Responsive](../../templates/04-ux-ui/accessibility-and-responsive.md) · [App Store Release](app-store-release.md) · [Technology Stack](../../templates/05-architecture/technology-stack.md) |

</details>

> **Guidance:** Choose support levels from **your users' real devices**, not from the newest hardware on your desk. Every supported version costs testing effort; every unsupported one excludes users. Record the **decision rule** (for example "support OS versions used by at least X% of our users, and the vendor-supported versions"), and verify current platform requirements and store policies at the time of decision.

## 1. Platforms and Delivery

| Platform | Support? | Delivery (native / cross-platform / web wrapper / PWA) | Rationale | Decision |
|---|---|---|---|---|
| iOS | | | | ADR-xxxx |
| Android | | | | |
| Tablet | | | | |
| Wearable / other | | | | |

## 2. Support Matrix

| Dimension | Minimum | Fully tested | Best-effort | Source of data |
|---|---|---|---|---|
| OS versions | | | | [Analytics / research date] |
| Device classes / screen sizes | | | | |
| Memory / storage | | | | |
| Network conditions | [e.g. unreliable 3G] | | | |
| Languages and locales | | | | |

**Device test set:** [Representative physical devices and emulators; who maintains the pool.]

## 3. Required Capabilities and Permissions

| Capability | Why needed | Required or optional | Behaviour if denied / unavailable | Privacy note |
|---|---|---|---|---|
| Notifications | Reminders | Optional | In-app message centre | See [Push Notifications](push-notifications.md) |
| Camera / photos | | | | |
| Location | | | | |
| Contacts / calendar | | | | |
| Biometrics | | | | |
| Background execution | | | | |

> **Guidance:** Ask for a permission **at the moment of need**, explain why, and make the app work without it where possible. Collect nothing you do not need.

## 4. Platform Conventions

[Navigation, gestures, accessibility features, dark mode, text scaling and system settings the app will respect; where it deliberately diverges.]

## 5. Version Policy

| Topic | Policy |
|---|---|
| Adopting new OS versions | [Test within N weeks of release] |
| Dropping old OS versions | [Criteria; notice to users; in-app prompt] |
| Minimum supported app version | [Forced update policy; server-side compatibility; see [API Lifecycle & Versioning](../api-platform/api-lifecycle-and-versioning.md)] |

## 6. Performance and Resource Budgets

[Launch time, responsiveness, battery, data usage, app size targets; reference NFR IDs.]

## Completion Criteria

- [ ] Platforms, OS versions and device classes are chosen with evidence and a stated rule.
- [ ] Support levels (tested / best-effort) are defined with a test device set.
- [ ] Every capability and permission has a purpose and a denied-state behaviour.
- [ ] Version adoption and drop policies exist.
- [ ] Performance and resource budgets are linked to NFRs.
