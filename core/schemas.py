from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional


@dataclass
class ResolvedEntity:
    standardized_property_name: str
    alias_names: List[str] = field(default_factory=list)
    city: Optional[str] = None
    country: Optional[str] = None
    coordinates: Optional[str] = None
    ambiguity_notes: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ClassificationResult:
    property_category: str
    secondary_category: Optional[str] = None
    indoor_dominance: Optional[str] = None
    remote_unit_type: Optional[str] = None
    dis_architecture: str = 'DIS'

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ValidationResult:
    cross_source_check: str
    conflict_notes: Optional[str] = None
    source_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class EvidenceResult:
    evidence_grade: str
    proxy_level: str
    standardized_proxy_basis: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PropertyScanRecord:
    standardized_property_name: str
    city: Optional[str]
    country: Optional[str]
    property_category: str
    secondary_category: Optional[str]
    dis_recommendation: str
    dis_architecture: str
    remote_unit_type: str
    recommendation_reason: str
    entity_resolution_basis: str
    classification_basis: str
    heat_signal_basis: str
    macro_context_basis: str
    cross_source_check: str
    conflict_notes: Optional[str]
    evidence_grade: str
    proxy_level: str
    standardized_proxy_basis: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
