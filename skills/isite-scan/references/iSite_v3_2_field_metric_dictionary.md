# iSite v3.2 Field and Metric Dictionary

## Scope

This document defines standardized output fields, field meanings, allowed value ranges, and writing discipline for iSite v3.2 outputs.

Use this dictionary for:
- country scan tables
- city scan tables
- single-property deep dives
- insight cards
- DIS recommendation outputs
- Excel exports

---

## Core identification fields

### `standardized_property_name`
Use the most stable, public-facing property name.

### `alias_names`
Record major English, local-language, or legacy aliases when relevant.

### `city`
Use the commonly accepted city name.

### `country`
Use the standard English country name.

### `coordinates`
Prefer decimal latitude and longitude when available.

### `property_category`
Use one primary category:
- airport
- mall
- office
- hotel
- mixed_use
- convention
- stadium
- transport_hub
- landmark_public
- other

### `secondary_category`
Use when the property clearly spans multiple scenarios.

---

## Recommendation fields

### `dis_recommendation`
Allowed values:
- recommended
- candidate
- observe
- not_recommended

### `dis_architecture`
Allowed values:
- DIS
- traditional_indoor
- uncertain

### `remote_unit_type`
Allowed values:
- pRRU
- hRRU
- mixed
- not_applicable

Rule:
- Use **pRRU** for pure indoor environments.
- Use **hRRU** for semi-open environments.
- Use `mixed` only when the recommendation explicitly covers both indoor core zones and semi-open edge zones.

### `recommendation_reason`
A short structured reason, not marketing copy.

---

## Value and scenario fields

### `property_value_level`
Allowed values:
- very_high
- high
- medium
- low

### `traffic_capacity_signal`
Describe likely traffic or capacity demand.

### `premium_user_signal`
Describe evidence or proxy for premium, business, or international user concentration.

### `portal_effect_signal`
Describe whether the property has landmark, gateway, or reputation spillover value.

### `engineering_complexity_signal`
Describe whether the built form is likely to create complex indoor coverage demand.

---

## Evidence fields

### `entity_resolution_basis`
Explain how name, city, and location identity were confirmed.

### `classification_basis`
Explain how property type was judged.

### `heat_signal_basis`
Explain how popularity, prominence, or high-value activity signals were judged.

### `macro_context_basis`
Explain how country/city context was judged.

### `cross_source_check`
State whether cross-source validation was completed.
Suggested values:
- completed
- partial
- not_completed

### `conflict_notes`
Record important source conflicts.

### `evidence_grade`
Allowed values:
- A
- B
- C

### `proxy_level`
Allowed values:
- direct
- same_category_proxy
- city_proxy
- country_proxy
- mixed_proxy

### `standardized_proxy_basis`
Use a fixed sentence pattern that separates direct evidence from inferred evidence.

Recommended template:
`Direct evidence: ... | Inference: ... | Proxy anchor: ... | Stretch: ...`

---

## Writing discipline

- Keep fields short and structured.
- Do not repeat generic scoring rules row by row.
- Do not turn uncertainty into false precision.
- Do not hide conflicts.
- Make pRRU / hRRU choice explicit whenever DIS is recommended.

---

## Output quality check

Before final export, ensure:
- all recommended properties have a DIS recommendation field
- all DIS recommendations have a remote unit type field
- all rows have an evidence grade
- all proxy-based judgments state the proxy level and standardized proxy basis
