from __future__ import annotations

import re
import unicodedata
from typing import Iterable, List

from .schemas import ResolvedEntity


def normalize_name(name: str) -> str:
    value = unicodedata.normalize('NFKC', name or '')
    value = ' '.join(value.strip().split())
    return value


def ascii_fold(value: str) -> str:
    normalized = unicodedata.normalize('NFKD', value)
    return ''.join(ch for ch in normalized if not unicodedata.combining(ch))


def canonical_key(name: str) -> str:
    base = ascii_fold(normalize_name(name)).lower()
    base = re.sub(r'[^a-z0-9]+', ' ', base)
    return ' '.join(base.split())


def extract_aliases(*names: str) -> List[str]:
    aliases: List[str] = []
    seen = set()
    for raw in names:
        if not raw:
            continue
        value = normalize_name(raw)
        key = canonical_key(value)
        if key and key not in seen:
            aliases.append(value)
            seen.add(key)
    return aliases


def detect_ambiguity(candidates: Iterable[str]) -> str | None:
    keys = [canonical_key(x) for x in candidates if x]
    if not keys:
        return None
    return 'possible_same_name_conflict' if len(set(keys)) > 1 else None


def resolve_entity(
    standardized_property_name: str,
    alias_names: Iterable[str] | None = None,
    city: str | None = None,
    country: str | None = None,
    coordinates: str | None = None,
) -> ResolvedEntity:
    aliases = extract_aliases(standardized_property_name, *(alias_names or []))
    ambiguity = detect_ambiguity(aliases)
    return ResolvedEntity(
        standardized_property_name=normalize_name(standardized_property_name),
        alias_names=aliases,
        city=normalize_name(city) if city else None,
        country=normalize_name(country) if country else None,
        coordinates=coordinates,
        ambiguity_notes=ambiguity,
    )
