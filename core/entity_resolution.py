from __future__ import annotations

from typing import Iterable, List

from .schemas import ResolvedEntity


COMMON_SUFFIXES = [
    "mall",
    "shopping mall",
    "center",
    "centre",
    "hotel",
    "airport",
    "tower",
    "plaza",
]


def normalize_name(name: str) -> str:
    normalized = " ".join(name.strip().split())
    return normalized


def extract_aliases(*names: str) -> List[str]:
    seen = []
    for raw in names:
        if not raw:
            continue
        value = normalize_name(raw)
        if value not in seen:
            seen.append(value)
    return seen


def detect_ambiguity(candidates: Iterable[str]) -> str | None:
    values = [normalize_name(x).lower() for x in candidates if x]
    return "possible_same_name_conflict" if len(set(values)) > 1 else None


def resolve_entity(
    standardized_property_name: str,
    alias_names: Iterable[str] | None = None,
    city: str | None = None,
    country: str | None = None,
) -> ResolvedEntity:
    aliases = extract_aliases(standardized_property_name, *(alias_names or []))
    ambiguity = detect_ambiguity(aliases)
    return ResolvedEntity(
        standardized_property_name=normalize_name(standardized_property_name),
        alias_names=aliases,
        city=city,
        country=country,
        ambiguity_notes=ambiguity,
    )
