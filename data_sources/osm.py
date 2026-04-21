from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .http_utils import http_get_json, polite_sleep


NOMINATIM_URL = 'https://nominatim.openstreetmap.org/search'


@dataclass
class OSMPlaceResult:
    name: str
    lat: Optional[float] = None
    lon: Optional[float] = None
    city: Optional[str] = None
    country: Optional[str] = None


class NominatimAdapter:
    source_type = 'base_map'
    source_name = 'nominatim'

    def lookup_place(self, name: str, country: str | None = None, city: str | None = None) -> List[dict]:
        query_parts = [name]
        if city:
            query_parts.append(city)
        if country:
            query_parts.append(country)
        data = http_get_json(
            NOMINATIM_URL,
            params={
                'q': ', '.join(query_parts),
                'format': 'jsonv2',
                'addressdetails': 1,
                'limit': 10,
            },
        )
        polite_sleep(1.0)
        return data if isinstance(data, list) else []

    def search_country_inventory(self, country: str, city: str | None = None) -> list:
        return []


def lookup_place(name: str) -> OSMPlaceResult:
    adapter = NominatimAdapter()
    results = adapter.lookup_place(name=name)
    if not results:
        return OSMPlaceResult(name=name)
    best = results[0]
    address = best.get('address', {})
    city = address.get('city') or address.get('town') or address.get('municipality')
    country = address.get('country')
    return OSMPlaceResult(
        name=best.get('display_name', name),
        lat=float(best['lat']) if best.get('lat') else None,
        lon=float(best['lon']) if best.get('lon') else None,
        city=city,
        country=country,
    )
