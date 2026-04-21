from typing import Iterable

from .schemas import ValidationResult


IMPORTANT_FIELDS = ["name", "city", "type"]


def validate_cross_source(records: Iterable[dict]) -> ValidationResult:
    records = list(records)
    if len(records) < 2:
        return ValidationResult(
            cross_source_check="not_completed",
            conflict_notes="insufficient_sources",
        )

    conflicts = []
    for field in IMPORTANT_FIELDS:
        values = {record.get(field) for record in records if record.get(field)}
        if len(values) > 1:
            conflicts.append(f"{field}_conflict")

    return ValidationResult(
        cross_source_check="completed",
        conflict_notes=", ".join(conflicts) if conflicts else None,
    )
