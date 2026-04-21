from __future__ import annotations

from typing import Iterable, List, Protocol

from .schemas import ResolvedEntity


class EntityResolutionAdapter(Protocol):
    """Abstract source adapter for future resolver integrations."""

    def fetch_candidates(
        self,
        name: str,
        city: str | None = None,
        country: str | None = None,
    ) -> list[dict]:
        """Return candidate entity records from an external source."""


def normalize_name(name: str) -> str:
    normalized = " ".join((name or "").strip().split())
    return normalized


def _unique_normalized(values: Iterable[str]) -> List[str]:
    seen = []
    for raw in values:
        if not raw:
            continue
        value = normalize_name(raw)
        if value not in seen:
            seen.append(value)
    return seen


def extract_aliases(
    standardized_property_name: str,
    alias_names: Iterable[str] | None = None,
    local_language_names: Iterable[str] | None = None,
) -> List[str]:
    return _unique_normalized(
        [
            standardized_property_name,
            *(alias_names or []),
            *(local_language_names or []),
        ]
    )


def extract_local_language_names(
    local_language_names: Iterable[str] | None = None,
) -> List[str]:
    return _unique_normalized(local_language_names or [])


def detect_ambiguity(candidates: Iterable[str]) -> str | None:
    values = [normalize_name(x).lower() for x in candidates if x]
    return "possible_same_name_conflict" if len(set(values)) > 1 else None


def resolve_entity(
    standardized_property_name: str,
    alias_names: Iterable[str] | None = None,
    local_language_names: Iterable[str] | None = None,
    city: str | None = None,
    country: str | None = None,
) -> ResolvedEntity:
    normalized_name = normalize_name(standardized_property_name)
    aliases = extract_aliases(
        normalized_name,
        alias_names=alias_names,
        local_language_names=local_language_names,
    )
    local_names = extract_local_language_names(local_language_names)
    ambiguity = detect_ambiguity(aliases)
    return ResolvedEntity(
        standardized_property_name=normalized_name,
        alias_names=aliases,
        local_language_names=local_names,
        city=normalize_name(city) if city else None,
        country=normalize_name(country) if country else None,
        ambiguity_notes=ambiguity,
    )
