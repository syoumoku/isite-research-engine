from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from outputs.excel_writer import write_csv
from outputs.summary_writer import build_summary
from pipelines.inspect_property import inspect_property


def scan_candidates(candidates: Iterable[dict]):
    return [inspect_property(candidate) for candidate in candidates]


def run_country_scan(input_path: str, output_dir: str) -> dict:
    path = Path(input_path)
    with path.open('r', encoding='utf-8') as f:
        payload = json.load(f)

    records = scan_candidates(payload['candidates'])
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = write_csv(records, str(out_dir / 'scan_results.csv'))
    summary = build_summary(records)
    summary_path = out_dir / 'summary.txt'
    summary_path.write_text(summary, encoding='utf-8')
    return {'csv_path': str(csv_path), 'summary_path': str(summary_path), 'record_count': len(records)}


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Run a minimal iSite country scan.')
    parser.add_argument('--input', required=True, help='Path to input JSON file')
    parser.add_argument('--output-dir', required=True, help='Directory for outputs')
    args = parser.parse_args()
    result = run_country_scan(args.input, args.output_dir)
    print(json.dumps(result, indent=2))
