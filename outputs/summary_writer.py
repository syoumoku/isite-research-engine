from __future__ import annotations

from typing import Iterable

from core.schemas import PropertyScanRecord


def build_summary(records: Iterable[PropertyScanRecord]) -> str:
    rows = list(records)
    if not rows:
        return 'No records processed.'

    high_priority = [r for r in rows if r.dis_recommendation == 'recommended']
    return (
        f'Processed {len(rows)} properties. '
        f'Recommended {len(high_priority)} for DIS. '
        f'Categories covered: {", ".join(sorted({r.property_category for r in rows}))}.'
    )
