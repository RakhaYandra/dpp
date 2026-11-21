---
id: DPP-PKG-mobile-push-notifications
title: Push Notification Strategy
domain: package-mobile
tier: package
status: draft
version: 0.1.0
owner: product-manager
contributors: [engineering-lead, designer, privacy-lead, marketing]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: [prd, platform-and-device-support, privacy-requirements]
feeds: [user-stories, event-tracking-plan, test-scenarios, integration-specification]
applies_to: [mobile]
---

# Push Notification Strategy: [App Name]

<details>
<summary><strong>About this template</strong> (delete this block in your copy)</summary>

| | |
|---|---|
| **Purpose** | Defines when and why the app sends notifications, how users control them, how they are delivered and measured, and the rules that stop them becoming spam. |
| **When to use** | When the app sends push notifications (or other out-of-app messages that interact with them: e-mail, SMS). Decide the strategy before building so that consent, preferences and content rules are designed in. |
| **Owner** | Product Manager. |
| **Required inputs** | [PRD](../../templates/03-requirements/prd.md); [Platform & Device Support](platform-and-device-support.md) permission rules; [Privacy Requirements](../../templates/08-security/privacy-requirements.md); platform vendors' current notification guidelines. |
| **Related documents** | [Event Tracking Plan](../../templates/10-analytics/event-tracking-plan.md) · [Integration Specification](../../templates/05-architecture/integration-specification.md) · [Offline & Sync](offline-and-sync.md) |

</details>

> **Guidance:** A notification is an **interruption**: send it only when it is timely, relevant and actionable. Separate **transactional** notifications (a user's booking changed) from **promotional** ones; the latter usually need explicit consent and extra rules that vary by jurisdiction, so verify with qualified advice. Never put sensitive data in the notification text, which may be visible on a locked screen.

## 1. Notification Catalog

| ID | Notification | Type (transactional / reminder / engagement / promotional) | Trigger | Audience | Content (summary) | Action on tap | Priority | Channel fallback |
|---|---|---|---|---|---|---|---|---|
| N-01 | Booking reminder | Reminder | 24 h before booking | Customer | "Reminder: [service] tomorrow at [time]" | Open booking | Normal | SMS/e-mail |
| N-02 | Booking cancelled by business | Transactional | On cancel | Customer | | Open booking | High | E-mail |

## 2. Permission and Preferences

| Topic | Decision |
|---|---|
| When permission is requested | [After a moment of value, with a pre-prompt explaining benefit] |
| If denied | [In-app message centre; periodic gentle reminder with limits] |
| User controls | [Per category toggles, quiet hours, frequency caps, easy opt-out] |
| Consent records | [What is stored; retention; links to privacy requirements] |

## 3. Delivery Design

| Topic | Decision |
|---|---|
| Delivery services | [Platform push services via a provider; see [Integration Specification](../../templates/05-architecture/integration-specification.md)] |
| Token handling | [Registration, refresh, deletion on logout/uninstall; security of tokens] |
| Reliability | [Retries, expiry (time-to-live), deduplication, ordering; push is best-effort so critical information needs a fallback] |
| Throttling and frequency caps | [Per user per day; bundling] |
| Time zones and quiet hours | |
| Localization | [Language chosen by user setting] |
| Rich content and deep links | [Links must handle logged-out state and missing content] |

## 4. Content Rules

[Tone, length, no personal or sensitive data on lock screens, clear sender, accessibility of actions, copy owned in the message catalog.]

## 5. Measurement

| Metric | Definition | Event |
|---|---|---|
| Delivery rate | Delivered ÷ sent | EVT-xxx |
| Open / action rate | | EVT-xxx |
| Opt-out rate | Disabled notifications ÷ enabled | EVT-xxx |
| Outcome impact | [e.g. effect on MET-01] | |

Guardrail: opt-out rate and uninstall rate after notifications must not rise beyond [threshold]; pause campaigns if so.

## 6. Testing and Rollout

[Device and OS matrix for notifications, background/killed states, token refresh, permission-denied paths, staged rollout of new notification types.]

## Completion Criteria

- [ ] Every notification has a trigger, audience, content rule, priority and fallback.
- [ ] Permission requests, preferences, opt-out and consent records are defined.
- [ ] Delivery handling covers tokens, retries, expiry, frequency caps and time zones.
- [ ] No sensitive data appears in notification content.
- [ ] Metrics and guardrails exist for delivery, engagement and opt-out.
