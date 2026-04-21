from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Protocol


@dataclass
class SourceEvidence:
    source_type: str
    source_name: str
    claim_type: str
    raw_value: Any
    normalized_value: Any = None
    confidence: float = 0.5
    is_direct: bool = False
    conflict_flag: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SourceEntityRecord:
    source_type: str
    source_name: str
    canonical_name: str
    aliases: List[str] = field(default_factory=list)
    city: Optional[str] = None
    country: Optional[str] = None
    coordinates: Optional[str] = None
    property_category: Optional[str] = None
    secondary_category: Optional[str] = None
    scene_hints: List[str] = field(default_factory=list)
    evidences: List[SourceEvidence] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class PublicSourceAdapter(Protocol):
    source_type: str
    source_name: str

    def search_country_inventory(self, country: str, city: str | None = None) -> List[SourceEntityRecord]:
        ...
