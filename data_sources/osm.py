"""OSM / Nominatim adapter placeholder."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class OSMPlaceResult:
    name: str
    lat: Optional[float] = None
    lon: Optional[float] = None
    city: Optional[str] = None
    country: Optional[str] = None


def lookup_place(name: str) -> OSMPlaceResult:
    """Stub for future implementation."""
    return OSMPlaceResult(name=name)
