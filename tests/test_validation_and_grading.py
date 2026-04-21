from core.cross_source_validation import validate_cross_source
from core.evidence_grading import assign_evidence_grade


def test_cross_source_validation_detects_conflict():
    result = validate_cross_source(
        [
            {"name": "Property A", "city": "Lagos", "type": "mall"},
            {"name": "Property A", "city": "Abuja", "type": "mall"},
        ]
    )
    assert result.cross_source_check == "completed"
    assert result.conflict_notes == "city_conflict"


def test_assign_evidence_grade_returns_a_for_strong_case():
    result = assign_evidence_grade(
        entity_clear=True,
        type_clear=True,
        value_signal_clear=True,
        cross_checked=True,
        proxy_level="direct",
        direct_evidence="official property identity confirmed",
        inference="high-value traffic likely",
        proxy_anchor="multi-source public records",
        stretch="low",
    )
    assert result.evidence_grade == "A"
    assert "Direct evidence:" in result.standardized_proxy_basis
