# iSite v3.2 Public Search Augmentation Specification

## Goal

Strengthen the input layer of iSite by using public multi-source search and cross-validation.

The purpose is to improve:
- entity accuracy
- property classification stability
- proxy consistency
- evidence quality
- recommendation explainability

This module feeds scoring and recommendation. It does not replace them.

---

## Core principles

### 1. Multi-source before conclusion
Do not finalize important claims from one weak source.

### 2. Resolve entity before judging value
First confirm what the property is and where it is.

### 3. Separate evidence from inference
Never present proxy inference as direct fact.

### 4. Preserve conflicts
If public sources disagree, keep the conflict visible.

### 5. Search for decision support, not information pileup
Only collect signals that support recommendation quality.

---

## Four-layer evidence model

### Layer 1: Entity Resolution
Target outputs:
- canonical property name
- alias names
- local-language names if relevant
- coordinates
- city / country
- ambiguity notes

### Layer 2: Classification and Built Form
Target outputs:
- property type
- multi-building or tower complexity
- underground or podium traits
- semi-open vs indoor-dominant traits
- likely indoor coverage complexity

### Layer 3: Heat and Commercial Signals
Target outputs:
- prominence or popularity signals
- premium positioning clues
- portal or landmark clues
- surrounding high-value activity density

### Layer 4: Macro Context
Target outputs:
- city role
- gateway / CBD / capital context
- tourism or business context
- national priority relevance

---

## Recommended source pools

### Base map and POI sources
Use for location, identity, and surrounding context:
- OpenStreetMap / Nominatim
- Overpass
- Overture Maps
- GeoNames

### Structured knowledge sources
Use for landmarks, airports, stadiums, major venues, and complex public properties:
- Wikidata
- Wikipedia / MediaWiki API

### Commercial heat sources
Use for malls, hotels, attractions, and consumer-facing landmarks:
- Google Places
- Tripadvisor
- other stable public local directories when needed

### Macro context sources
Use for country and city context:
- World Bank indicators
- other high-trust public macro sources

---

## Execution sequence

### Step 1: Name normalization
Normalize the primary name, aliases, and city context.

### Step 2: Geospatial confirmation
Confirm coordinates and surrounding functional context.

### Step 3: Property classification
Classify primary and secondary scenario type.

### Step 4: Heat and value signal enrichment
Add commercial and prominence clues.

### Step 5: Macro sanity check
Check whether country/city context supports the scenario weight.

### Step 6: Cross-source validation
Check for consistency across name, city, type, and value signals.

### Step 7: Evidence grading
Assign A / B / C evidence grade.

---

## Validation rules

### Important claims that should be cross-checked
Try to cross-check:
- property existence
- property category
- landmark or gateway status
- popularity or premium signals
- suitability for DIS recommendation

### When single-source acceptance is allowed
Allowed only when:
- the source is unusually direct and authoritative
- the result is used only for candidate retention, not strong recommendation

### Conflict handling
When sources conflict, record:
- the conflict item
- source-level differences
- adopted working interpretation
- reason for adoption
- whether evidence grade is lowered

---

## Required structured fields

Every property should support these outputs:
- entity_resolution_basis
- classification_basis
- heat_signal_basis
- macro_context_basis
- cross_source_check
- conflict_notes
- evidence_grade
- proxy_level
- standardized_proxy_basis

---

## DIS-specific selection note

When public-search augmentation indicates a DIS recommendation, also classify the deployment edge:

- **pRRU** for pure indoor environments
- **hRRU** for semi-open environments

Do not stop at `DIS recommended`. Always map the scene to the likely remote unit type.
