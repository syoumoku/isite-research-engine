# iSite v3.2 Skill

## Purpose

Use a consistent, scalable method to identify high-value properties that should be prioritized for indoor coverage construction, especially **DIS (digital indoor system)** deployments.

This skill is for **planning-grade scanning and prioritization**. It is not an implementation design standard.

The goal is not to find the tallest or most famous building. The goal is to find properties with the best combination of:

- high commercial value
- high network value
- high brand or portal effect
- high build return potential
- clear indoor coverage or capacity need

---


### DIS architecture selection rule

Use **DIS (digital indoor system)** as the standard English term for 数字化室分.

When DIS is recommended, explicitly map the scene to the remote unit type:

- **pRRU**: use for pure indoor environments such as enclosed malls, office towers, hotels, convention halls, indoor venues, underground retail, and indoor transport concourses.
- **hRRU**: use for semi-open environments such as open-sided canopies, arrival or drop-off zones, porticos, semi-open corridors, outdoor-connected podium edges, and other spaces with strong outdoor coupling.

Selection rule:
- If the target area is primarily enclosed and indoor-dominant, prefer **pRRU**.
- If the target area is semi-open, partially exposed, or strongly coupled with outdoor propagation, prefer **hRRU**.
- Do not describe DIS generically without mapping the scene to **pRRU** or **hRRU**.
- If both indoor core areas and semi-open edge areas are important, allow a mixed recommendation, but specify the dominant unit type by sub-scene.

---

## Core recommendation principle

Always prioritize **objective, explainable, and repeatable screening** over descriptive richness.

Recommendations must be based on:

1. scenario value
2. user value
3. traffic or capacity likelihood
4. build complexity and suitability
5. evidence quality

Do not force precision when public evidence is limited. Preserve uncertainty and distinguish direct evidence from proxy-based inference.

---

## Five-dimensional scoring model

Use five dimensions to structure evaluation:

1. property value
2. traffic and capacity potential
3. user and brand value
4. engineering and deployment fit
5. strategic and demonstrative value

The score is used to organize judgment, not replace judgment.

---

## DIS trigger rules

Recommend DIS when one or more of the following are clearly present:

### Hard triggers
- multi-operator sharing is likely necessary
- the property is large, multi-building, or operationally complex
- high concurrent indoor traffic is likely
- premium users, business travelers, or international users are concentrated
- the site has portal effect, landmark value, or strong reputation spillover

### Soft triggers
- the site is not extreme in size but is high value and brand sensitive
- the site is a top property within a city or country category
- upgrade potential is high because existing indoor coverage is likely insufficient
- a neutral-host or digital architecture would improve long-term scalability

If neither hard nor soft triggers are present, do not force a DIS recommendation.

---

## Country-level scan structure

Default structure for one country:

- at least 10 recommended properties
- cover multiple categories where possible
- avoid over-concentration in one single city unless national value is truly concentrated

Preferred category mix:
- airport / transport hub
- flagship mall / retail complex
- Grade A office / HQ cluster / mixed-use complex
- premium hotel / integrated hospitality complex
- convention / exhibition / landmark venue

Adjust category weights based on country profile.

---

## Country profile adaptation

Before large-scale scanning, form a country profile:

- portal-type country
- tourism-led country
- HQ / capital-led country
- resource-led country
- multi-core urban country

Then adjust category priority accordingly.

---

## Standard workflow

### Step 1: build candidate pool
Create a broad candidate set before ranking.

### Step 2: resolve entity
Confirm the property identity, aliases, and city location.

### Step 3: classify property
Determine property type and built-form complexity.

### Step 4: collect value signals
Gather commercial, user, brand, and portal signals.

### Step 5: apply public-search augmentation
Use public multi-source validation before final recommendation.

### Step 6: score and recommend
Use the scoring structure plus narrative reasoning.

### Step 7: output structured recommendation
Write the result in standardized fields.

---

## Proxy basis rule

Every recommendation must distinguish among:

- direct evidence
- indirect evidence
- same-category proxy
- city-level proxy
- country-level proxy

Do not mix them casually.

Use a standardized proxy statement that explains:
- what is directly observed
- what is inferred
- what the inference anchor is
- how far the inference stretches

---

## Evidence grade rule

### Grade A
- entity is clear
- type is clear
- value signals are clear
- multi-source cross-check completed

### Grade B
- entity is clear
- type is mostly clear
- some value signals rely on proxy

### Grade C
- major parts still rely on indirect signals
- suitable only for candidate retention or watchlist use

---

## Output rules

Each recommended property should support the following structured fields:

- standardized property name
- city / country
- property category
- DIS recommendation
- dominant remote unit type: pRRU / hRRU
- recommendation reason
- entity resolution basis
- classification basis
- heat signal basis
- macro context basis
- cross-source check
- conflict notes
- evidence grade
- proxy level
- standardized proxy basis

Do not repeat generic scoring explanations at property-row level unless a property has a special note.

---

## Public Search Augmentation

Use public search augmentation as an upstream evidence-acquisition layer.

### Layer 1: entity resolution
Confirm:
- canonical name
- aliases / local-language names
- coordinates
- city / country
- same-name ambiguity

### Layer 2: classification and built form
Confirm:
- property category
- multi-building / tower / podium / underground / semi-open traits
- whether indoor coverage complexity is likely high

### Layer 3: heat and commercial signals
Collect:
- popularity / review intensity / prominence
- premium positioning
- portal or landmark effect
- surrounding high-value activity density

### Layer 4: macro context
Collect:
- country and city economic importance
- capital / CBD / gateway role
- tourism, business, exhibition, or transport relevance

### Cross-source rule
Do not rely on one public source unless evidence is unusually direct and strong.
At least two source types should support important claims where possible.

### Conflict rule
If sources disagree, preserve the conflict note and lower confidence when necessary.

---

## Recommendation discipline

Do not recommend DIS just because a property is famous.
Do not equate consumer popularity with wireless capacity need.
Do not treat city importance as sufficient proof of single-property priority.

Always convert evidence into a structured recommendation, not a pile of search notes.
