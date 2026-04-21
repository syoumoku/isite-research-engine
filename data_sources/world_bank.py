from __future__ import annotations

from .http_utils import http_get_json, polite_sleep


WORLD_BANK_COUNTRY_URL = 'https://api.worldbank.org/v2/country'


def get_country_context(country: str) -> dict:
    data = http_get_json(
        f'{WORLD_BANK_COUNTRY_URL}/{country}',
        params={'format': 'json'},
    )
    polite_sleep(0.5)
    if not isinstance(data, list) or len(data) < 2 or not data[1]:
        return {'country': country, 'context': {}}
    record = data[1][0]
    return {
        'country': country,
        'context': {
            'name': record.get('name'),
            'region': (record.get('region') or {}).get('value'),
            'income_level': (record.get('incomeLevel') or {}).get('value'),
            'capital_city': record.get('capitalCity'),
            'longitude': record.get('longitude'),
            'latitude': record.get('latitude'),
        },
    }
