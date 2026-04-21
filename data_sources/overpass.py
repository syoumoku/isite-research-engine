from __future__ import annotations

from .http_utils import http_get_json, polite_sleep


OVERPASS_URL = 'https://overpass-api.de/api/interpreter'


def build_country_inventory_query(country: str) -> str:
    return f'''
[out:json][timeout:60];
area["name"="{country}"]["boundary"="administrative"]->.searchArea;
(
  nwr["aeroway"="aerodrome"](area.searchArea);
  nwr["shop"="mall"](area.searchArea);
  nwr["tourism"="hotel"](area.searchArea);
  nwr["amenity"="conference_centre"](area.searchArea);
  nwr["building"="office"](area.searchArea);
);
out center tags;
'''.strip()


def query_elements(query: str) -> dict:
    data = http_get_json(OVERPASS_URL, params={'data': query}, timeout=60)
    polite_sleep(1.0)
    return {'query': query, 'elements': data.get('elements', []) if isinstance(data, dict) else []}
