from __future__ import annotations

import json
from pathlib import Path

from core.evidence_collection import collect_country_inventory
from data_sources.mock_public_sources import get_default_mock_adapters
from data_sources.real_public_sources import get_default_real_adapters


def run_country_inventory_collection(
    country: str,
    output_path: str,
    city: str | None = None,
    use_real_sources: bool = True,
) -> dict:
    adapters = get_default_real_adapters() if use_real_sources else get_default_mock_adapters()
    bundles = collect_country_inventory(country=country, adapters=adapters, city=city)
    rows = [bundle.to_candidate_dict() for bundle in bundles]
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({'country': country, 'candidates': rows}, indent=2), encoding='utf-8')
    return {
        'country': country,
        'candidate_count': len(rows),
        'output_path': str(path),
        'source_mode': 'real' if use_real_sources else 'mock',
    }


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Collect country inventory candidates from public-source adapters.')
    parser.add_argument('--country', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--city', required=False)
    parser.add_argument('--mock', action='store_true', help='Use mock adapters instead of real public sources')
    args = parser.parse_args()
    result = run_country_inventory_collection(
        country=args.country,
        output_path=args.output,
        city=args.city,
        use_real_sources=not args.mock,
    )
    print(json.dumps(result, indent=2))
