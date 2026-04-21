from __future__ import annotations

from typing import List

from .base import SourceEntityRecord, SourceEvidence
from .overpass import build_country_inventory_query, query_elements


def infer_property_category(tags: dict) -> tuple[str, str | None, list[str]]:
    if tags.get('aeroway') == 'aerodrome':
        return 'airport', 'transport_hub', ['arrival_zone']
    if tags.get('shop') == 'mall':
        return 'mall', None, []
    if tags.get('tourism') == 'hotel':
        return 'hotel', None, ['portico']
    if tags.get('amenity') == 'conference_centre':
        return 'convention', None, []
    if tags.get('building') == 'office':
        return 'office', None, []
    return 'other', None, []


def infer_city(tags: dict) -> str | None:
    for key in ['addr:city', 'city', 'is_in:city', 'addr:suburb']:
        if tags.get(key):
            return tags.get(key)
    return None


class OverpassInventoryAdapter:
    source_type = 'base_map'
    source_name = 'overpass_inventory'

    def search_country_inventory(self, country: str, city: str | None = None) -> List[SourceEntityRecord]:
        query = build_country_inventory_query(country)
        result = query_elements(query)
        rows: List[SourceEntityRecord] = []
        for element in result.get('elements', []):
            tags = element.get('tags', {})
            name = tags.get('name')
            if not name:
                continue
            inferred_city = infer_city(tags)
            if city and inferred_city and inferred_city.lower() != city.lower():
                continue
            property_category, secondary_category, scene_hints = infer_property_category(tags)
            lat = element.get('lat') or (element.get('center') or {}).get('lat')
            lon = element.get('lon') or (element.get('center') or {}).get('lon')
            coordinates = f'{lat},{lon}' if lat is not None and lon is not None else None
            rows.append(
                SourceEntityRecord(
                    source_type=self.source_type,
                    source_name=self.source_name,
                    canonical_name=name,
                    aliases=[],
                    city=inferred_city,
                    country=country,
                    coordinates=coordinates,
                    property_category=property_category,
                    secondary_category=secondary_category,
                    scene_hints=scene_hints,
                    evidences=[
                        SourceEvidence(
                            source_type=self.source_type,
                            source_name=self.source_name,
                            claim_type='inventory_presence',
                            raw_value=tags,
                            normalized_value=name,
                            confidence=0.7,
                            is_direct=False,
                            metadata={'osm_type': element.get('type'), 'osm_id': element.get('id')},
                        )
                    ],
                    metadata={'tags': tags},
                )
            )
        return rows


def get_default_real_adapters():
    return [OverpassInventoryAdapter()]
