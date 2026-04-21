from __future__ import annotations

import json
from pathlib import Path

from core.evidence_collection import collect_country_inventory
from data_sources.mock_public_sources import get_default_mock_adapters


def run_country_inventory_collection(country: str, output_path: str, city: str | None = None) -> dict:
    bundles = collect_country_inventory(country=country, adapters=get_default_mock_adapters(), city=city)
    rows = [bundle.to_candidate_dict() for bundle in bundles]
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({'country': country, 'candidates': rows}, indent=2), encoding='utf-8')
    return {'country': country, 'candidate_count': len(rows), 'output_path': str(path)}


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Collect country inventory candidates from public-source adapters.')
    parser.add_argument('--country', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--city', required=False)
    args = parser.parse_args()
    result = run_country_inventory_collection(country=args.country, output_path=args.output, city=args.city)
    print(json.dumps(result, indent=2))
