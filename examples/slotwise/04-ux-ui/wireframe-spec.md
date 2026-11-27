---
id: SLOTWISE-04-wireframe-spec
title: Wireframe Specification
domain: 04-ux-ui
tier: recommended
status: draft
version: 0.1.0
owner: designer
contributors: [product-manager, engineering-lead, qa-lead]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [user-flow, information-architecture]
feeds: [prototype-review, user-stories, test-scenarios, design-system]
applies_to: [all]
---

# Wireframe Specification: SlotWise

Screen IDs are defined once in the [Information Architecture](information-architecture.md). This document references them.

## 1. Screen Inventory

| Name | Screen ID | Flow | Requirements | Design link | Fidelity | Status |
|---|---|---|---|---|---|---|
| Slot list | S-01 | UF-01 | FR-001 | [UI design](ui-design.md) | Low | Draft |
| Booking detail | S-02 | UF-01 | FR-001 | [UI design](ui-design.md) | Low | Draft |
| Confirmation form | S-03 | UF-01 | FR-001 | [UI design](ui-design.md) | Low | Draft |
| Confirmation and manage link | S-04 | UF-01, UF-02 | FR-002, FR-003 | [UI design](ui-design.md) | Low | Draft |

## 2. Screen Specification

### Screen S-01: Slot list

| | |
|---|---|
| **Purpose** | Choose a service and a time that is actually open |
| **Who sees it / access** | Public customer, no account |
| **Entry from / exit to** | Shared booking link to S-02; manage link returns here for rescheduling |
| **Requirements / stories** | FR-001; US-001; AC-001.1 |

**Content and components**

| Element | Type | Content / data source | Required | Validation / rule | Notes |
|---|---|---|---|---|---|
| Service select | Select | I-01 service list | Yes | Empty first option forces a choice | Selection emits EVT-001 |
| Date select | Date input | Customer choice | Yes | Date must not be in the past | Date format is [OPEN: designer, 2026-12-15] |
| Slot rows | List | I-02 open slots | Yes | Inside published hours, no booked or time-off slots (BR-001, BR-002) | Each row has a detail action |
| Empty message | Text | M-21 | No | Shown only when the list has no rows | Offers another date |
| Retry action | Button | Local state control | No | Returns to loading, then the default list | Used in the error state |

**States**

| State | Behaviour |
|---|---|
| Default | Service and date chosen, slot rows shown, detail actions enabled |
| Loading | "Memuat slot untuk tanggal yang dipilih." with role status; controls disabled |
| Empty | "Belum ada slot tersedia untuk tanggal ini. Pilih tanggal lain." with a working date-change action |
| Error | "Slot tidak dapat dimuat. Periksa koneksi, lalu coba lagi." with a working retry action |
| Success | Selecting a row opens S-02 |

**Interactions and behaviour:** the service and date selects are first in keyboard order; each row action is a native button with a visible focus ring; the browser back button keeps both selections. **Responsive behaviour:** the slot table scrolls horizontally inside its panel at compact widths and stacks its columns below 640 px; see the [Accessibility and Responsive Guidelines](accessibility-and-responsive.md). **Content and copy:** customer text is in Bahasa Indonesia and is catalogued below. **Analytics events:** EVT-001 when a service is selected. **Open questions:** [OPEN: designer, 2026-12-15] for the default date shown on first load.

### Screen S-02: Booking detail

| | |
|---|---|
| **Purpose** | Let the customer check the chosen time before giving contact details |
| **Who sees it / access** | Public customer, no account |
| **Entry from / exit to** | S-01 to S-03 |
| **Requirements / stories** | FR-001; US-001; AC-001.1 |

**Content and components**

| Element | Type | Content / data source | Required | Validation / rule | Notes |
|---|---|---|---|---|---|
| Booking summary | Read-only list | Service, date, time, staff, duration | Yes | BR-003 sets end time | Values are labelled placeholders in the prototype |
| Continue action | Primary button | Local state control | Yes | Disabled if the slot was taken | Moves to S-03 |
| Back action | Button | Local state control | No | Returns to S-01 with selections kept | |
| Slot-taken notice | Text | M-14 | No | Shown when the chosen slot was taken | Offers nearest alternatives |

**States**

| State | Behaviour |
|---|---|
| Default | Summary shown, continue enabled |
| Loading | No request on this screen; the previous list loading state is reused on return |
| Empty | Not applicable, because a slot must be chosen before entry |
| Error | M-14 shown, continue replaced by a link to alternate times |
| Success | Continue opens S-03 |

**Interactions and behaviour:** focus lands on the heading on entry; Enter and Space activate the buttons. **Responsive behaviour:** the summary list uses one column below 640 px. **Content and copy:** M-14. **Analytics events:** none on this screen. **Open questions:** [OPEN: owner, 2026-12-15] for whether staff name is shown to customers.

### Screen S-03: Confirmation form

| | |
|---|---|
| **Purpose** | Collect the minimum contact details and reserve the slot |
| **Who sees it / access** | Public customer, no account |
| **Entry from / exit to** | S-02 to S-04 |
| **Requirements / stories** | FR-001; US-001, US-002; AC-001.2, AC-001.3, AC-002.1 |

**Content and components**

| Element | Type | Content / data source | Required | Validation / rule | Notes |
|---|---|---|---|---|---|
| Name | Text field | Customer input | Yes | 1 to 80 characters | Label always visible |
| Phone or email | Text field | Customer input | Yes | Valid format, BR-006 | Inline error M-12 |
| Booking summary | Read-only text | Chosen slot from S-02 | Yes | Matches BR-001 and BR-003 | Rechecked on submit |
| Confirm | Primary button | Local state control | Yes | Prevents double submit | Reserves in one transaction (ADR-0001) |

**States**

| State | Behaviour |
|---|---|
| Default | Fields empty, focus on Name, summary visible |
| Loading / submitting | Button shows "Mengirim...", fields disabled, double submit blocked |
| Validation error | M-12 beside the field, focus on the first error |
| Slot taken | M-14, return to S-01 with alternatives |
| Offline / error | M-20, retry keeps entered data |
| Success | Navigate to S-04 |

**Interactions and behaviour:** field order follows the visual order; the form uses novalidate so the same inline messages appear for mouse and keyboard users; browser back keeps entered data. **Responsive behaviour:** the form uses one column and full-width inputs below 640 px. **Content and copy:** M-12, M-14, M-20. **Analytics events:** EVT-002 on server confirmation. **Open questions:** none.

### Screen S-04: Confirmation and manage link

| | |
|---|---|
| **Purpose** | Confirm the booking and explain how to change it later |
| **Who sees it / access** | Public customer, no account; manage link carries a signed token |
| **Entry from / exit to** | S-03; manage link returns to S-01 for rescheduling |
| **Requirements / stories** | FR-002, FR-003; US-002, US-003; AC-002.1, AC-003.1, AC-003.2 |

**Content and components**

| Element | Type | Content / data source | Required | Validation / rule | Notes |
|---|---|---|---|---|---|
| Confirmation text | Text | Booking result | Yes | Shows the slot and the salon name | M-22 |
| Delivery note | Text | Confirmation and reminder state | Yes | Confirmation queued within one minute (AC-002.1) | Retry is a worker concern (ADR-0002) |
| Manage instruction | Text | Signed link in the message | Yes | Cutoff enforced server side | Salon phone shown after cutoff (AC-003.2) |

**States**

| State | Behaviour |
|---|---|
| Default | Confirmed details and manage instruction visible |
| Loading | Confirmation is being created, shown before navigation from S-03 |
| Empty | Not applicable, because a confirmed booking is required |
| Error | Booking failed, M-20 shown with a return to S-01 |
| Success | Confirmation message queued and manage link ready |

**Interactions and behaviour:** the screen has one primary action, returning to the slot list when the customer wants another booking. **Responsive behaviour:** single column at all widths. **Content and copy:** M-22. **Analytics events:** EVT-002 is emitted by the server when the booking is confirmed. **Open questions:** [OPEN: owner, 2026-12-15] for the reminder timing to display on this screen.

## 3. Message Catalog

| ID | Context | Text | Notes |
|---|---|---|---|
| M-12 | Invalid phone or email | "Masukkan nomor telepon atau email yang valid agar kami dapat mengirim pengingat." | Linked to the field with aria-describedby |
| M-14 | Slot taken | "Slot baru saja diambil. Pilih waktu terdekat." | Offers alternatives instead of a dead end |
| M-20 | Offline or failed request | "Slot tidak dapat dimuat. Periksa koneksi, lalu coba lagi." | Retry keeps entered data |
| M-21 | No slots for the date | "Belum ada slot tersedia untuk tanggal ini. Pilih tanggal lain." | Empty state on S-01 |
| M-22 | Confirmed booking | "Booking dikonfirmasi. Pesan konfirmasi dan pengingat akan dikirim." | Shown on S-04 |
| M-23 | Loading slots | "Memuat slot untuk tanggal yang dipilih." | role status on S-01 |

## 4. Review and Traceability

| Requirement | Screens | Complete? |
|---|---|---|
| FR-001 | S-01, S-02, S-03 | Yes |
| FR-002 | S-03, S-04 | Yes |
| FR-003 | S-01, S-04 | Yes |

Waiting list work is held for R2 and has no wireframe in this set.

## Completion Criteria

- [x] Every screen maps to at least one requirement; every UI-facing FR maps to screens.
- [x] Each screen documents content, validation, access and all relevant states.
- [x] Responsive and accessibility behaviour is specified or referenced.
- [x] Copy is catalogued and consistent with the glossary.
- [x] Design links resolve to the UI design document of this project.
- [ ] Owner review of shown staff name and reminder wording is complete.
