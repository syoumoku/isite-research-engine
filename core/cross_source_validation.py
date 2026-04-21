from __future__ import annotations

from itertools import combinations
from typing import Iterable

from .entity_resolution import canonical_key
from .schemas import ValidationResult


IMPORTANT_FIELDS = ['name', 'city', 'type']
STOPWORDS = {'of', 'and', 'the'}


def _name_tokens(value: str) -> list[str]:
    return [token for token in canonical_key(value).split() if token]


def _acronym(value: str) -> str:
    tokens = [token for token in _name_tokens(value) if token not in STOPWORDS]
    return ''.join(token[0] for token in tokens if token)


def names_equivalent(left: str | None, right: str | None) -> bool:
    if not left or not right:
        return left == right
    left_key = canonical_key(left)
    right_key = canonical_key(right)
    if left_key == right_key:
        return True

    left_joined = left_key.replace(' ', '')
    right_joined = right_key.replace(' ', '')
    if left_joined == _acronym(right) or right_joined == _acronym(left):
        return True

    left_tokens = set(_name_tokens(left))
    right_tokens = set(_name_tokens(right))
    if left_tokens and right_tokens:
        if left_tokens.issubset(right_tokens) or right_tokens.issubset(left_tokens):
            return True
    return False


def validate_cross_source(records: Iterable[dict]) -> ValidationResult:
    records = [record for record in records if record]
    if len(records) < 2:
        return ValidationResult(
            cross_source_check='not_completed',
            conflict_notes='insufficient_sources',
            source_count=len(records),
        )

    conflicts = []

    names = [record.get('name') for record in records if record.get('name')]
    if names:
        for left, right in combinations(names, 2):
            if not names_equivalent(left, right):
                conflicts.append('name_conflict')
                break

    for field in ['city', 'type']:
        values = {record.get(field) for record in records if record.get(field)}
        if len(values) > 1:
            conflicts.append(f'{field}_conflict')

    return ValidationResult(
        cross_source_check='completed',
        conflict_notes=', '.join(dict.fromkeys(conflicts)) if conflicts else None,
        source_count=len(records),
    )
