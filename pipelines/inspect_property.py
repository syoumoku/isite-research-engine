from __future__ import annotations

from core.cross_source_validation import validate_cross_source
from core.entity_resolution import resolve_entity
from core.evidence_grading import assign_evidence_grade
from core.poi_classification import classify_property
from core.schemas import PropertyScanRecord


def inspect_property(candidate: dict) -> PropertyScanRecord:
    entity = resolve_entity(
        standardized_property_name=candidate['name'],
        alias_names=candidate.get('aliases', []),
        city=candidate.get('city'),
        country=candidate.get('country'),
        coordinates=candidate.get('coordinates'),
    )
    classification = classify_property(
        property_category=candidate['property_category'],
        secondary_category=candidate.get('secondary_category'),
        scene_hints=candidate.get('scene_hints', []),
    )
    validation = validate_cross_source(candidate.get('source_records', []))
    evidence = assign_evidence_grade(
        entity_clear=True,
        type_clear=bool(candidate.get('property_category')),
        value_signal_clear=bool(candidate.get('heat_signal_basis')),
        cross_checked=validation.cross_source_check == 'completed' and not validation.conflict_notes,
        proxy_level=candidate.get('proxy_level', 'mixed_proxy'),
        direct_evidence=candidate.get('entity_resolution_basis', 'candidate input normalized'),
        inference=candidate.get('recommendation_reason', 'DIS suitability inferred from scenario signals'),
        proxy_anchor=candidate.get('proxy_anchor', 'public multi-source scan'),
        stretch=candidate.get('proxy_stretch', 'medium'),
    )
    return PropertyScanRecord(
        standardized_property_name=entity.standardized_property_name,
        city=entity.city,
        country=entity.country,
        property_category=classification.property_category,
        secondary_category=classification.secondary_category,
        dis_recommendation=candidate.get('dis_recommendation', 'recommended'),
        dis_architecture=classification.dis_architecture,
        remote_unit_type=classification.remote_unit_type or 'mixed',
        recommendation_reason=candidate.get('recommendation_reason', ''),
        entity_resolution_basis=candidate.get('entity_resolution_basis', ''),
        classification_basis=candidate.get('classification_basis', ''),
        heat_signal_basis=candidate.get('heat_signal_basis', ''),
        macro_context_basis=candidate.get('macro_context_basis', ''),
        cross_source_check=validation.cross_source_check,
        conflict_notes=validation.conflict_notes,
        evidence_grade=evidence.evidence_grade,
        proxy_level=evidence.proxy_level,
        standardized_proxy_basis=evidence.standardized_proxy_basis,
    )
