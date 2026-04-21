from core.proxy_standardization import build_proxy_basis


def test_build_proxy_basis_uses_standard_template():
    value = build_proxy_basis(
        direct_evidence="official listing",
        inference="premium user concentration likely",
        proxy_anchor="top-tier hotel classification",
        stretch="medium",
    )
    assert value == (
        "Direct evidence: official listing | Inference: premium user concentration likely | "
        "Proxy anchor: top-tier hotel classification | Stretch: medium"
    )
