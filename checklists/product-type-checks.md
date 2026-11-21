# Product-Type Checks

Quick confirmations of the decisions that are hardest to reverse for each product type. Each item points to the package document that covers it.

## SaaS (`packages/saas`)
- [ ] Tenant definition and isolation model chosen and recorded as an ADR *(Multi-Tenancy & Isolation)*.
- [ ] Every data path (API, jobs, caches, search, exports) carries tenant context; cross-tenant tests exist.
- [ ] Plans, entitlements, trial, failed-payment and cancellation rules are written as testable rules *(Subscription & Billing)*.
- [ ] Tax, invoicing and payment-data obligations are identified with qualified advice.
- [ ] Billable meters are defined, idempotent and reconcilable *(Usage Metering)*.
- [ ] Per-tenant limits protect other tenants *(Rate Limiting & Quotas)*.

## Mobile (`packages/mobile`)
- [ ] Supported OS versions and devices chosen from user data, with a drop policy *(Platform & Device Support)*.
- [ ] Every permission has a purpose and a denied-state behaviour.
- [ ] Offline level chosen per feature; conflict rules defined *(Offline & Sync)*.
- [ ] Forced-update and backward-compatible API strategy exists (old apps live for years).
- [ ] Notifications have consent, preferences, fallback channel and no sensitive lock-screen content *(Push Notifications)*.
- [ ] Store accounts, signing keys, listing, privacy declarations and review lead time planned; current store policy version recorded *(App Store Release)*.

## API platform (`packages/api-platform`)
- [ ] Compatibility policy (what is breaking) published before the first consumer *(API Lifecycle & Versioning)*.
- [ ] Deprecation process and minimum notice defined and affordable.
- [ ] Credential types, scopes, rotation and revocation designed; standard mechanisms named in ADRs *(Consumer Authentication)*.
- [ ] Limits, quotas and over-limit behaviour published *(Rate Limiting & Quotas)*.
- [ ] Webhook delivery semantics (at-least-once, retries, signing, replay) documented for consumers *(Webhook Specification)*.
- [ ] Machine-readable contract exists and breaking changes are detected in CI.

## Enterprise / internal (`packages/enterprise`)
- [ ] Identity, single sign-on, provisioning and role mapping agreed with IT *(Enterprise Integration)*.
- [ ] Every connected system has an owner, test environment and lead time.
- [ ] Audit objectives, events, integrity and retention (with stated basis) defined *(Audit Logging)*.
- [ ] Data owners, retention and sharing policies named *(Data Governance)*.
- [ ] Training, champions, cut-over and adoption measures planned *(Change Management & Training)*.

## Developer tools (`packages/developer-tools`)
- [ ] Time-to-first-success target set and tested with real developers *(Developer Experience)*.
- [ ] Quickstart and examples tested in CI.
- [ ] Supported environments, versioning promise and public interface defined *(Distribution & Compatibility)*.
- [ ] Artefact signing, dependency policy and vulnerability reporting in place.
- [ ] Licence chosen and dependency licences checked with qualified advice.

## Web application (no package)
- [ ] Supported browsers and devices stated as NFRs; responsive breakpoints defined *(Accessibility & Responsive)*.
- [ ] Accessibility target (standard, version, level) named and tested.
- [ ] Performance budget set for the main journey on realistic devices and networks.
