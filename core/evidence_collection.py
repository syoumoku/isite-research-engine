from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Tuple

from data_sources.base import PublicSourceAdapter, SourceEntityRecord
from .entity_resolution import canonical_key


@dataclass
class CollectedEntityBundle:
    canonical_name: str
    aliases: List[str] = field(default_factory=list)
    city: str | None = None
    country: str | None = None
    property_category: str | None = None
    secondary_category: str | None = None
    scene_hints: List[str] = field(default_factory=list)
    source_records: List[SourceEntityRecord] = field(default_factory=list)

    @property
    def source_count(self) -> int:
        return len(self.source_records)

    def to_candidate_dict(self) -> dict:
        return {
            'name': self.canonical_name,
            'aliases': self.aliases,
            'city': self.city,
            'country': self.country,
            'property_category': self.property_category or 'other',
            'secondary_category': self.secondary_category,
            'scene_hints': self.scene_hints,
            'dis_recommendation': 'recommended',
            'recommendation_reason': 'Collected from multi-source country inventory flow.',
            'entity_resolution_basis': f'Collected from {self.source_count} public sources.',
            'classification_basis': 'Property category inferred from merged public-source records.',
            'heat_signal_basis': 'Heat and demand signals pending enrichment in next phase.',
            'macro_context_basis': 'Macro context pending enrichment in next phase.',
            'proxy_level': 'mixed_proxy',
            'proxy_anchor': 'multi-source objective collection module',
            'proxy_stretch': 'medium',
            'source_records': [
                {
                    'name': record.canonical_name,
                    'city': record.city,
                    'type': record.property_category,
                }
                for record in self.source_records
            ],
        }


def collect_country_inventory(
    country: str,
    adapters: Iterable[PublicSourceAdapter],
    city: str | None = None,
) -> List[CollectedEntityBundle]:
    grouped: Dict[Tuple[str, str | None], CollectedEntityBundle] = {}

    for adapter in adapters:
        for record in adapter.search_country_inventory(country=country, city=city):
            key = (canonical_key(record.canonical_name), record.city)
            if key not in grouped:
                grouped[key] = CollectedEntityBundle(
                    canonical_name=record.canonical_name,
                    aliases=list(record.aliases),
                    city=record.city,
                    country=record.country,
                    property_category=record.property_category,
                    secondary_category=record.secondary_category,
                    scene_hints=list(record.scene_hints),
                    source_records=[record],
                )
            else:
                bundle = grouped[key]
                bundle.source_records.append(record)
                bundle.aliases = list(dict.fromkeys(bundle.aliases + record.aliases))
                bundle.scene_hints = list(dict.fromkeys(bundle.scene_hints + record.scene_hints))
                if not bundle.property_category and record.property_category:
                    bundle.property_category = record.property_category
                if not bundle.secondary_category and record.secondary_category:
                    bundle.secondary_category = record.secondary_category

    return list(grouped.values())
