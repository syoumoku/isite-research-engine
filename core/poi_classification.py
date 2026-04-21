from .schemas import ClassificationResult


PURE_INDOOR_CATEGORIES = {
    'mall', 'office', 'hotel', 'convention', 'indoor_venue', 'transport_hub', 'airport'
}

SEMI_OPEN_HINTS = {
    'arrival_zone', 'drop_off_zone', 'portico', 'semi_open_corridor', 'canopy',
    'waterfront_edge', 'outdoor_connected_podium_edge'
}


def determine_indoor_dominance(scene_hints: list[str] | None = None) -> str:
    hints = set(scene_hints or [])
    return 'semi_open' if hints & SEMI_OPEN_HINTS else 'indoor'


def select_remote_unit_type(
    property_category: str,
    scene_hints: list[str] | None = None,
) -> str:
    hints = set(scene_hints or [])
    if hints & SEMI_OPEN_HINTS:
        return 'hRRU'
    if property_category in PURE_INDOOR_CATEGORIES:
        return 'pRRU'
    return 'mixed'


def classify_property(
    property_category: str,
    secondary_category: str | None = None,
    scene_hints: list[str] | None = None,
) -> ClassificationResult:
    remote_unit_type = select_remote_unit_type(property_category, scene_hints)
    indoor_dominance = determine_indoor_dominance(scene_hints)
    return ClassificationResult(
        property_category=property_category,
        secondary_category=secondary_category,
        indoor_dominance=indoor_dominance,
        remote_unit_type=remote_unit_type,
    )
