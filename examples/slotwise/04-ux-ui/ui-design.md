---
id: SLOTWISE-04-ui-design
title: UI Design and Interactive Prototype
domain: 04-ux-ui
tier: recommended
status: draft
version: 0.1.0
owner: designer
contributors: [product-manager, engineering-lead, qa-lead, ux-researcher]
created: 2026-11-27
last_updated: 2026-11-27
depends_on: [prd, persona, information-architecture, user-flow, design-system, accessibility-and-responsive]
feeds: [wireframe-spec, prototype-review, test-scenarios, event-tracking-plan]
applies_to: [all]
---

# UI Design and Interactive Prototype: SlotWise

## 1. Direction and Inputs

| Item | Source | Decision for this product |
|---|---|---|
| Product and audience | Product Brief, PRD | SlotWise is a booking page for PER-01 Maya and her customers PER-02 Dani, used mostly on a phone |
| Visual direction | No DESIGN.md exists in this project | None supplied, so the prototype is a draft without direction |
| Flows in scope | User Flow | UF-01, UF-02, UF-03; the prototype covers the UF-01 screens |
| Tokens and components | Design System | One accent, system type stack, native controls |
| Accessibility target | Accessibility and Responsive Guidelines | WCAG 2.2 Level AA for NFR-005 |

Direction status: [ ] Direction exists [x] Draft without direction. The prototype is a working draft, not a finished design. Dials: ENERGY 1 / RHYTHM 1 / MOTION 1.

## 2. Screen Inventory

| Prototype route | Wireframe screen | Screen name | Flow | Requirement | States covered | Status |
|---|---|---|---|---|---|---|
| list | S-01 | Slot list | UF-01 | FR-001 | default, loading, empty, error | draft |
| detail | S-02 | Booking detail | UF-01 | FR-001 | default, slot taken | draft |
| form | S-03 | Booking confirmation form | UF-01 | FR-001 | default, validation error, slot taken, success | draft |

Routes are the button labels in the prototype file and stay stable so review notes point to the same screen. S-04 is documented in the wireframe spec but has no separate prototype route; its confirmation text appears as form feedback.

## 3. Screen Design

### Screen S-01: Slot list

| Item | Detail |
|---|---|
| Decision the user makes here | Pick a service and a time that is open, or pick another date |
| Wireframe and flow | S-01, UF-01 |
| Layout regions | Header with product name and screen buttons, one panel with filters, state switch and slot list |
| Components and tokens | Select, date input, table, state buttons; accent used only on the pressed state control |
| Content and copy | Customer copy in Bahasa Indonesia; M-21 for empty, M-23 for loading, M-20 for error |
| Interaction and feedback | State buttons switch real panels; retry moves to loading then back to the list; state changes are announced with role status |
| Responsive behaviour | One column and a scrollable table below 640 px; theme toggle stays in the header |
| Keyboard and screen-reader path | Skip link, native selects and buttons, visible focus ring, heading focused on screen change |

### States

| State | What the user sees | Cause | Next action |
|---|---|---|---|
| Default | Slot rows with placeholder labels and a detail action | Slots loaded | Choose a row to open S-02 |
| Loading | "Memuat slot untuk tanggal yang dipilih." | Lookup in progress | Wait, or retry from the error state |
| Empty | "Belum ada slot tersedia untuk tanggal ini. Pilih tanggal lain." | No open slots for the date | Use "Coba tanggal lain" |
| Error | "Slot tidak dapat dimuat. Periksa koneksi, lalu coba lagi." | Lookup failed | Use "Coba lagi" |
| Confirmation | Not applicable on this screen | No booking yet | Continue to S-02 |

### Screen S-02: Booking detail

| Item | Detail |
|---|---|
| Decision the user makes here | Check the summary and continue, or go back |
| Wireframe and flow | S-02, UF-01 |
| Layout regions | Single panel with a summary list and two actions |
| Components and tokens | Description list, primary and secondary buttons, one accent on the primary action |
| Content and copy | Placeholder labels for service, date, time, staff and duration; M-14 when the slot is taken |
| Interaction and feedback | Demo control simulates a slot taken by another customer; the continue button then shows M-14 and offers alternate times |
| Responsive behaviour | Summary stays one column at every width |
| Keyboard and screen-reader path | Focus moves to the heading on entry; buttons use native Enter and Space behavior |

### States

| State | What the user sees | Cause | Next action |
|---|---|---|---|
| Default | Service, date, time, staff and duration with "Lanjut ke konfirmasi" | Slot is open | Continue to S-03 |
| Loading | Not applicable, the list loading state is reused | No request on this screen | Return to S-01 |
| Empty | Not applicable | A slot must be chosen first | Return to S-01 |
| Error | "Slot baru saja diambil. Pilih waktu terdekat." | Demo control marks the slot as taken | Use "Lihat waktu terdekat" |
| Confirmation | Form opens with the summary carried forward | Continue succeeded | Fill the form |

### Screen S-03: Booking confirmation form

| Item | Detail |
|---|---|
| Decision the user makes here | Provide contact details and confirm the reservation |
| Wireframe and flow | S-03, UF-01 |
| Layout regions | Single panel with booking summary, two labelled fields and one primary action |
| Components and tokens | Text inputs with visible labels, inline feedback, accent only on submit |
| Content and copy | M-12 for invalid contact details, M-14 for a taken slot, M-22 for success |
| Interaction and feedback | novalidate plus custom validation; focus moves to the first bad field; success announces the confirmation and the manage link in the message |
| Responsive behaviour | Full-width inputs and a single column below 640 px |
| Keyboard and screen-reader path | Label before each input, error linked with aria-describedby, role status on feedback |

### States

| State | What the user sees | Cause | Next action |
|---|---|---|---|
| Default | Empty fields and a summary with placeholders | Normal use | Enter name and phone or email |
| Loading | "Mengirim..." on the button, fields disabled | Submit in progress | Wait, double submit is blocked |
| Empty | Not applicable, fields are always present | No data state on this screen | Enter details |
| Error | M-12 or M-14 with a visible action | Invalid input or taken slot | Fix the field or view other times |
| Confirmation | M-22 with the manage link instruction | Booking confirmed | Use the link in the message to change the booking |

## 4. Prototype Artefact

| | |
|---|---|
| File | `ui-prototype.html` |
| Format | One HTML file with inline CSS and vanilla JavaScript, no build step and no external assets |
| Status | Draft without direction, not production code, dials ENERGY 1 / RHYTHM 1 / MOTION 1 |
| Open it | Open the file in a browser. No server is required. |

Choices and reasons:

| Choice | Reason |
|---|---|
| Neutral surface with one accent on primary actions only | With no design direction, one accent avoids a sterile page without inventing a brand |
| System UI type stack | No external font dependency and text stays readable at 200% zoom |
| Slot list, detail and form screens | These match UF-01 and expose the empty, loading and error states without adding invented data |
| Bahasa Indonesia customer copy | The example copy in the brief is in Bahasa Indonesia and matches Dani's context |
| Motion limited to hover and focus | MOTION 1 keeps review on decisions rather than animation |
| Light and dark theme toggle | Both themes are checked for AA contrast and keep the same layout |

Before review, completed checks:

- [x] The product label was replaced with SlotWise, and every screen label is SlotWise language.
- [x] Prototype routes use the labels from the screen inventory in section 2.
- [x] CSS values follow the tokens in the Design System.
- [x] State copy names a real cause and a next action from the wireframe message catalog.
- [x] Every control was clicked, including keyboard activation, and does what its label says.
- [x] The layout was checked at a narrow width and at 200% zoom.

## 5. Handoff to Prototype Review

Create a copy of the `prototype-review` framework template when the prototype is ready. Use that review to answer the questions in section 1, not to collect opinions about colours. Record every finding against a screen ID from section 2 and move Critical or Major findings back into this document and into the wireframe spec. The review document is not part of this team-profile example and is [OPEN: designer, 2026-12-15].

## Completion Criteria

- [x] Direction is stated as a draft without direction, with dials ENERGY 1 / RHYTHM 1 / MOTION 1.
- [x] Every screen in the inventory has a design block and a state table.
- [x] Screen IDs match the wireframe spec and flows.
- [x] The prototype file opens in a browser with no external dependencies.
- [x] No placeholder is presented as final content.
- [x] Every control has a real action, and each state names its cause and next action.
- [x] Keyboard path, narrow width and 200% zoom were checked.
- [ ] Findings from prototype review have a screen ID and an owner once the review is scheduled.
