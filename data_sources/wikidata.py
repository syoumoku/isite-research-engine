from __future__ import annotations

from .http_utils import http_get_json, polite_sleep


WIKIDATA_SEARCH_URL = 'https://www.wikidata.org/w/api.php'


def search_entity(name: str) -> dict:
    data = http_get_json(
        WIKIDATA_SEARCH_URL,
        params={
            'action': 'wbsearchentities',
            'search': name,
            'language': 'en',
            'format': 'json',
            'limit': 10,
        },
    )
    polite_sleep(0.5)
    return {'name': name, 'entities': data.get('search', []) if isinstance(data, dict) else []}
