from core.entity_resolution import resolve_entity


def test_resolve_entity_keeps_aliases_unique():
    entity = resolve_entity(
        "Mid Valley Megamall",
        alias_names=["Mid Valley Megamall", "Mid Valley Mall"],
        city="Kuala Lumpur",
        country="Malaysia",
    )
    assert entity.standardized_property_name == "Mid Valley Megamall"
    assert len(entity.alias_names) == 2
    assert entity.city == "Kuala Lumpur"
