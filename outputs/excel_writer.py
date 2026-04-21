from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from core.schemas import PropertyScanRecord


def write_csv(records: Iterable[PropertyScanRecord], output_path: str) -> Path:
    rows = [r.to_dict() for r in records]
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        fieldnames = ['standardized_property_name']
    else:
        fieldnames = list(rows[0].keys())
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path
