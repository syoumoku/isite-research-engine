from .schemas import EvidenceResult
from .proxy_standardization import build_proxy_basis


GRADE_RULES = {
    (True, True, True, True): "A",
    (True, True, True, False): "B",
}


def assign_evidence_grade(
    entity_clear: bool,
    type_clear: bool,
    value_signal_clear: bool,
    cross_checked: bool,
    proxy_level: str,
    direct_evidence: str,
    inference: str,
    proxy_anchor: str,
    stretch: str,
) -> EvidenceResult:
    grade = GRADE_RULES.get(
        (entity_clear, type_clear, value_signal_clear, cross_checked),
        "C",
    )
    return EvidenceResult(
        evidence_grade=grade,
        proxy_level=proxy_level,
        standardized_proxy_basis=build_proxy_basis(
            direct_evidence=direct_evidence,
            inference=inference,
            proxy_anchor=proxy_anchor,
            stretch=stretch,
        ),
    )
