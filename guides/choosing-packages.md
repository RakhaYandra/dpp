---
id: DPP-GUIDE-choosing-packages
title: Choosing Product-Specific Packages
status: approved
version: 0.1.0
---

# Choosing Product-Specific Packages

Packages in [`packages/`](../packages/) hold documents that only some kinds of product need. A product often matches **more than one** package: a mobile app with a public API and subscriptions needs three. List the ones you use under `packages:` in your [project manifest](../templates/00-foundation/project-manifest.yaml).

## Quick Selector

| If your product… | Use package | Why |
|---|---|---|
| Serves several customer organisations from one deployment and charges them | **saas** | Tenant isolation, billing and metering shape the architecture |
| Is installed on phones or tablets | **mobile** | Device support, notifications, offline behaviour and store rules are specific to mobile |
| Exposes an API or webhooks to people outside your team | **api-platform** | Versioning, credentials, limits and webhooks are promises to third parties |
| Runs inside an organisation (internal system) or sells to large organisations | **enterprise** | Identity, audit, data governance and adoption need explicit plans |
| Is a CLI, SDK, library, plugin or other tool used by developers | **developer-tools** | Developer experience and distribution are the product |
| Is a plain website or web application | *(none required)* | Browser support and accessibility live in the universal NFR and UX documents |

## Package Contents

| Package | Documents | Typical timing |
|---|---|---|
| **saas** | Multi-Tenancy & Isolation (early, before the data model is fixed) · Subscription & Billing · Usage Metering | Architecture and specification phases |
| **mobile** | Platform & Device Support · Push Notifications · Offline & Sync · App Store Release | Platform choice precedes design; store release 4+ weeks before launch |
| **api-platform** | API Lifecycle & Versioning · Consumer Authentication · Rate Limiting & Quotas · Webhook Specification | Before the first external consumer integrates |
| **enterprise** | Audit Logging · Enterprise Integration · Data Governance · Change Management & Training | Integration and audit early; change management well before go-live |
| **developer-tools** | Developer Experience · Distribution & Compatibility | Before the first public release |

## How Packages Relate to Universal Templates

Packages **extend** the universal documents; they do not repeat them. When a package document builds on a universal one, it links to it and records only the additional decisions.

| Package document | Extends | Division of responsibility |
|---|---|---|
| Multi-Tenancy & Isolation | Architecture Overview, Authentication & Authorization | Package: isolation model and enforcement. Universal: overall structure and access mechanisms |
| Consumer Authentication | Authentication & Authorization | Package: developer-facing credentials and scopes. Universal: how the product authenticates its own users |
| Rate Limiting & Quotas | Infrastructure & Scalability | Package: limits and behaviour. Universal: capacity model |
| Enterprise Integration | Integration Specification | Package: SSO, provisioning, enterprise constraints. Universal: the register and detail of each integration |
| Audit Logging | Observability Strategy, Security Requirements | Package: tamper-evident audit trail. Universal: operational logs |
| Data Governance | Data Classification, Privacy Requirements | Package: ownership and lifecycle policy. Universal: classification scheme and privacy duties |
| Platform & Device Support | Accessibility & Responsive, NFRs | Package: mobile platforms and permissions. Universal: general compatibility targets |

## Adding Packages to an Existing Project

1. Add the package name to the manifest.
2. Run `scripts/scaffold --add-package <name>` (or copy the files manually).
3. Review the new documents' `depends_on` lists, then update the universal documents they influence (for example, add NFRs for tenant isolation).

## Proposing a New Package

Packages must add documents that are **needed by a recognisable class of products and not covered elsewhere**. Open an issue using the *New template* form with: the product type, the decisions that are hard to reverse for it, and why a universal document cannot hold them. Candidates under consideration: data/ML platforms, marketplaces, game products, hardware-connected (IoT) products.
