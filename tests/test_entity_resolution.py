from core.entity_resolution import detect_ambiguity, normalize_name, resolve_entity


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


def test_resolve_entity_supports_local_language_names_and_context_normalization():
    entity = resolve_entity(
        "  Mid Valley Megamall ",
        alias_names=["Mid Valley Mall"],
        local_language_names=["美佳广场", "  美佳广场 "],
        city="  Kuala Lumpur  ",
        country="  Malaysia ",
    )
    assert entity.standardized_property_name == "Mid Valley Megamall"
    assert entity.alias_names == ["Mid Valley Megamall", "Mid Valley Mall", "美佳广场"]
    assert entity.local_language_names == ["美佳广场"]
    assert entity.city == "Kuala Lumpur"
    assert entity.country == "Malaysia"


def test_detect_ambiguity_flags_same_name_conflict():
    ambiguity = detect_ambiguity(["Harbor Center", "Harbour Centre"])
    assert ambiguity == "possible_same_name_conflict"


def test_normalize_name_collapses_whitespace():
    assert normalize_name("  The   Exchange   TRX ") == "The Exchange TRX"
