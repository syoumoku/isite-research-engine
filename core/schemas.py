from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ResolvedEntity:
    standardized_property_name: str
    alias_names: List[str] = field(default_factory=list)
    city: Optional[str] = None
    country: Optional[str] = None
    ambiguity_notes: Optional[str] = None


@dataclass
class ClassificationResult:
    property_category: str
    secondary_category: Optional[str] = None
    indoor_dominance: Optional[str] = None
    remote_unit_type: Optional[str] = None


@dataclass
class ValidationResult:
    cross_source_check: str
    conflict_notes: Optional[str] = None


@dataclass
class EvidenceResult:
    evidence_grade: str
    proxy_level: str
    standardized_proxy_basis: str
