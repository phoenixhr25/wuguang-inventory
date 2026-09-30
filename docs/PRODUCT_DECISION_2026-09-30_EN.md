# Product Decision Record: From Personal Inventory to a Personal Belongings Archive

[中文](PRODUCT_DECISION_2026-09-30.md) · English

**Date:** 30 September 2026  
**Status:** Hypothesis under validation  
**Decision scope:** Product positioning, category-specific engagement loops, sharing, and platform direction  
**Evidence level:** One strong qualitative signal; insufficient for a strategic pivot

## Executive Summary

Wuguang began as a photo-first personal inventory MVP: help people see what they own, reduce duplicate purchases, and make better use of existing belongings. Early feedback revealed a possible second source of value: people may also want to preserve the provenance, memories, and emotional meaning attached to individual objects.

The decision is to test this archival layer without abandoning the original utility proposition. Wuguang will remain a web product in the near term. WeChat and Xiaohongshu will serve as acquisition and content channels rather than the system of record. The first experiment will add an optional “About this item” field and a privacy-controlled story-card export. Broader platform investment will depend on observed retention, sharing, synchronisation, and willingness-to-pay signals.

## Triggering Signal

After the public WeChat article, one reader wrote:

> This is the kind of app I have always wanted: a place to catalogue every object. I feel an emotional attachment to the things I own.

This feedback suggests that Wuguang may serve two related needs:

1. **Inventory utility:** understand what is owned, where it is, whether it is duplicated, and whether it is still in use.
2. **Personal archive:** remember where an item came from, why it matters, and why it has been kept.

A single comment does not establish market demand. It is treated as a product hypothesis to test cheaply, not as evidence for an immediate repositioning.

## Decision

Wuguang will extend from personal inventory toward a personal belongings archive while preserving its original purpose: reduce waste and improve the use of what people already own.

The working product promise is:

> Wuguang helps people see what they own and remember why they chose to keep it.

The two layers should reinforce each other rather than compete for attention:

| Layer | User question | Primary capabilities |
|---|---|---|
| Practical | What do I own, where is it, is it duplicated, and do I still use it? | Capture, classification, value, search, usage, maintenance, and lifecycle records |
| Personal | Where did it come from, why did I keep it, and what does it mean to me? | “About this item”, dates, stories, photographs, timelines, and story cards |

## Product Principles

The archive direction must not recreate the data-entry burden that Wuguang was designed to remove.

- Story fields remain optional.
- The product asks for one meaningful detail before introducing structured metadata.
- AI may suggest labels or summaries, but the user remains the authority on identity and meaning.
- Private data stays private by default.
- Sharing requires explicit item and field selection.
- Category-specific activity is measured through meaningful events, not a universal click counter.
- New platform investment follows demonstrated behaviour rather than speculative feature breadth.

## Product Surface and Distribution Channels

The web application remains the product and system of interaction in the near term. Distribution channels should send people to Wuguang rather than own the underlying inventory data.

| Surface | Role | Current decision |
|---|---|---|
| Web, with a possible future PWA | Inventory, photographs, stories, and core workflows | Remains the primary product |
| WeChat Official Account | Existing audience, education, onboarding, and feedback | Remains the primary acquisition channel |
| Xiaohongshu | Object stories, spaces, outfits, and demand discovery | Content and acquisition channel only |
| WeChat Mini Program | In-WeChat capture, login, sharing, and synchronisation | Consider after retention and in-WeChat demand are demonstrated |
| Native mobile app | Camera integration, notifications, on-device inference, and subscriptions | Consider only after frequent use and a paid loop emerge |

Recommended sequence:

```text
WeChat / Xiaohongshu / direct sharing
                  ↓
              Wuguang Web
                  ↓
  Validate retention and cross-device demand
                  ↓
        PWA or WeChat Mini Program
                  ↓
       Native app only if justified
```

## Experiment 1: “About This Item”

Add one optional free-text field to every item. It can capture provenance, the person who gave it, a memory, a use experience, or the reason it remains worth keeping.

The first version should not introduce several mandatory fields. Structured attributes such as acquisition date, acquisition method, source person, or keepsake status should be considered only after users naturally produce enough content to justify them.

### Questions to answer

- What percentage of active users write anything?
- Which categories receive stories most often?
- Do users write practical notes, emotional narratives, or both?
- Does writing a story increase return visits, later edits, or sharing?
- Does the field add meaningful value without increasing abandonment during capture?

## Experiment 2: Privacy-Controlled Item Story Cards

The initial sharing mechanism should generate an image locally rather than publish a public item page. The user selects one item, chooses which fields to reveal, and exports a PNG for WeChat, Xiaohongshu, or private messaging.

### Default content

- Item photograph;
- Item name;
- “About this item” text;
- Wuguang attribution.

### Optional content

- Acquisition or ownership duration;
- Category;
- Category-relevant usage or maintenance information.

### Hidden by default

- Price or purchase value;
- Precise storage location;
- Serial numbers and device identifiers;
- Receipts and invoices;
- Network information;
- Other items and the full inventory.

Story cards can support expression and acquisition. Retention is more likely to come from revisiting stories, maintenance reminders, warranty dates, loans, returns, and periodic review.

## Category-Specific Engagement Loops

A clothing action such as “I wore this today” should not be copied mechanically to every category. Each category needs events that represent real value.

| Major category | Core loop | Meaningful events |
|---|---|---|
| Clothing | Compose → wear → learn | Worn, outfit, occasion |
| Furniture and home | Place → maintain → change | Moved, cleaned, repaired, restored, rearranged |
| Digital devices | Use → maintain → lifecycle decision | Activated, retired, repaired, charged, lent, returned, disposed |
| All belongings | Archive → remember → share | Story, acquisition date, photographs, story card |

### Furniture and Home

Furniture may be used every day, so daily check-ins create work without useful information. More meaningful records include:

- Current room or space;
- Status such as active, occasional, stored, needs repair, or ready to leave;
- Last cleaning, repair, move, restoration, or rearrangement;
- Next maintenance date;
- Ownership duration and item story;
- Space-level compositions such as a reading corner or work area.

Shareable narratives can focus on change: restoring an old chair, creating a reading corner, or identifying which objects remain valuable across rented homes.

### Digital Devices

Frequently used devices such as phones and computers are better represented by status, age, warranty, repair, and accessory relationships than by a daily “used” button. Lower-frequency equipment such as cameras, game consoles, and projectors can retain explicit usage events.

Relevant capabilities include:

- Primary, backup, occasional, idle, under repair, and retired states;
- Last confirmation that the device remains active;
- Warranty and repair history;
- Device-and-accessory kits;
- Lending and return records;
- Ownership duration and disposal decisions.

Device story cards may show long-term experience, commuting kits, or travel photography setups. Serial numbers, receipts, exact location, and network details must remain hidden by default.

## Measurement and Domain Model

A universal `useCount` is not meaningful across categories. The model should distinguish at least three concepts:

1. **Usage events:** actual occurrences for clothing, cameras, game consoles, camping equipment, and similar items.
2. **Status confirmation:** whether always-on or high-frequency items remain active and relevant.
3. **Maintenance events:** the elapsed time since cleaning, charging, servicing, or repair.

Candidate cross-category fields:

```text
story                 Optional user-authored narrative
status                Current lifecycle state
lastMeaningfulUseAt   Most recent category-relevant use
events[]              Typed events: use, maintenance, move, repair, lend, return, etc.
```

An event should carry an explicit `type`, timestamp, optional note, and provenance. Analytics must not combine a repair, a daily use, and a location change into one undifferentiated “usage” metric.

## Technical Implications

The experiments can remain local-first, but implementation should preserve a path to synchronisation.

- Add schema versioning and migration for new item and event fields.
- Include stories and typed events in complete JSON export and restore.
- Generate story cards client-side where feasible so private images and text do not need to leave the device.
- Treat event type as a controlled value and preserve unknown future types during import.
- Keep identifiers stable across backup and restore to support future sync and deduplication.
- Separate share-card presentation data from the full inventory record.
- Never expose secrets or private inventory data through telemetry, logs, public issues, or share URLs.

If cloud sync is introduced, the design will also require authentication, encrypted transport, object storage, deletion semantics, conflict resolution, auditability, and explicit household permissions.

## Delivery Plan and Decision Gates

### Phase 1: Low-Cost Validation

- Add optional “About this item” to all categories;
- Include it in edit, display, search, export, and restore;
- Generate a single-item story card locally;
- Hide sensitive fields by default;
- Measure story-field completion, card generation, and stated sharing intent.

**Gate:** proceed only if users complete the field or generate cards often enough to justify additional product complexity.

### Phase 2: Category Events

- Add cleaning, repair, moving, and rearrangement for home items;
- Add device status, repair, lending, and return;
- Show category-specific summaries;
- Build an item timeline from typed events.

**Gate:** proceed when users revisit these records or reminders cause meaningful return usage.

### Phase 3: Reminders and Synchronisation

- Maintenance, warranty, lending, and return reminders;
- Accounts and cross-device synchronisation;
- Household spaces and permissions;
- Platform decision among PWA, Mini Program, and native app.

**Gate:** invest only after sustained retention, cross-device demand, or credible willingness to pay appears.

## Success Signals

The following signals should be reviewed by cohort and category rather than as aggregate vanity metrics:

- Story-field completion rate among users who add an item;
- Median and distribution of story length;
- Categories most likely to receive stories;
- Repeat views or edits after a story is added;
- Story-card generation and completed save/share rate;
- First successful item capture attributable to a shared card;
- Return visits caused by maintenance, warranty, or lending reminders;
- Requests and willingness to pay for cloud sync, household sharing, or AI-assisted organisation.

Low adoption should lead to simplification or removal, not to more mandatory fields.

## Risks and Mitigations

| Risk | Consequence | Mitigation |
|---|---|---|
| One emotional comment is overgeneralised | Product loses focus | Treat the direction as an experiment with explicit gates |
| Story fields increase capture effort | Lower onboarding completion | Keep optional and outside the minimum capture path |
| Sharing exposes private household information | Loss of trust or personal risk | Local generation, explicit field selection, sensitive fields hidden by default |
| A universal usage metric creates false conclusions | Misleading recommendations | Use typed events and category-specific measures |
| Premature app development consumes scarce capacity | Slower learning and higher maintenance | Keep Web as the product until retention and payment signals justify expansion |
| Third-party platform dependence limits ownership | Channel or policy changes disrupt access | Keep inventory and export under the user's control |

## Open-Source References

These projects are references for public product and workflow patterns. Their inclusion does not mean Wuguang has copied or incorporated their code. Any future code reuse requires a separate licence review and the required notices.

- [HomeBox](https://github.com/sysadminsmedia/homebox): household inventory, locations, custom fields, warranties, and maintenance;
- [HomeInventory](https://github.com/asdteke/HomeInventory): rooms, lending, maintenance, activity history, QR workflows, and privacy levels;
- [Grocy](https://github.com/grocy/grocy): recurring tasks, execution history, due dates, batteries, and household operations;
- [Shelf](https://github.com/Shelf-nu/shelf.nu): asset custody, locations, kits, reminders, and audit history;
- [DumbAssets](https://github.com/DumbWareio/DumbAssets): devices, components, warranties, and maintenance reminders;
- [itemLens](https://github.com/romland/itemLens): low-friction capture and prompts around location, purpose, and purchase rationale;
- [toop-closet](https://github.com/akleventis/toop-closet): public links for individual items and combinations, with explicit public-read boundaries.

## Review Cadence

Review this decision after the first two targeted validation rounds or when enough usage exists to compare users who add stories with those who do not. Record whether the hypothesis is confirmed, narrowed, revised, or rejected. Do not silently convert an experiment into permanent scope.
