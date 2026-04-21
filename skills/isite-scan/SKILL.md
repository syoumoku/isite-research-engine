---
name: isite-scan
description: Use this skill for country-level high-value property scanning, DIS recommendation structuring, public-search augmentation, and evidence-standardized outputs.
---

# iSite Scan Skill

## When to use

Use this skill when the task involves:
- scanning a country or city for high-value properties
- assessing whether a property should be recommended for indoor coverage construction
- determining whether DIS is justified
- structuring evidence, proxy basis, and recommendation fields
- exporting standardized scan results

## How to work

1. Read the files in `references/` before producing final outputs.
2. Resolve the entity before judging value.
3. Use public-search augmentation when evidence is not direct.
4. Keep direct evidence, proxy inference, and confidence level separate.
5. If DIS is recommended, explicitly map the scene to **pRRU** or **hRRU**.
6. Keep outputs structured and reusable.

## Reference files

- `references/iSite_v3_2_skill.md`
- `references/iSite_v3_2_field_metric_dictionary.md`
- `references/iSite_v3_2_public_search_augmentation_spec.md`
