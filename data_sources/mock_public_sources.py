from __future__ import annotations

from typing import List

from .base import SourceEntityRecord, SourceEvidence


class MockOSMAdapter:
    source_type = 'base_map'
    source_name = 'mock_osm'

    def search_country_inventory(self, country: str, city: str | None = None) -> List[SourceEntityRecord]:
        if country.lower() != 'south africa':
            return []
        rows = [
            ('OR Tambo International Airport', 'Johannesburg', 'airport', ['arrival_zone']),
            ('Sandton City', 'Johannesburg', 'mall', []),
            ('Cape Town International Convention Centre', 'Cape Town', 'convention', []),
        ]
        return [
            SourceEntityRecord(
                source_type=self.source_type,
                source_name=self.source_name,
                canonical_name=name,
                city=row_city,
                country='South Africa',
                property_category=category,
                scene_hints=scene_hints,
                evidences=[
                    SourceEvidence(
                        source_type=self.source_type,
                        source_name=self.source_name,
                        claim_type='entity_presence',
                        raw_value=name,
                        normalized_value=name,
                        confidence=0.7,
                        is_direct=False,
                    )
                ],
            )
            for name, row_city, category, scene_hints in rows
            if city is None or row_city == city
        ]


class MockWikidataAdapter:
    source_type = 'structured_knowledge'
    source_name = 'mock_wikidata'

    def search_country_inventory(self, country: str, city: str | None = None) -> List[SourceEntityRecord]:
        if country.lower() != 'south africa':
            return []
        rows = [
            ('OR Tambo International Airport', 'Johannesburg', 'airport', ['arrival_zone']),
            ('Sandton City', 'Johannesburg', 'mall', []),
            ('Cape Town International Convention Centre', 'Cape Town', 'convention', []),
        ]
        return [
            SourceEntityRecord(
                source_type=self.source_type,
                source_name=self.source_name,
                canonical_name=name,
                city=row_city,
                country='South Africa',
                property_category=category,
                scene_hints=scene_hints,
                evidences=[
                    SourceEvidence(
                        source_type=self.source_type,
                        source_name=self.source_name,
                        claim_type='classification',
                        raw_value=category,
                        normalized_value=category,
                        confidence=0.75,
                        is_direct=False,
                    )
                ],
            )
            for name, row_city, category, scene_hints in rows
            if city is None or row_city == city
        ]


def get_default_mock_adapters():
    return [MockOSMAdapter(), MockWikidataAdapter()]
