TEMPLATE = "Direct evidence: {direct_evidence} | Inference: {inference} | Proxy anchor: {proxy_anchor} | Stretch: {stretch}"


def build_proxy_basis(
    direct_evidence: str,
    inference: str,
    proxy_anchor: str,
    stretch: str,
) -> str:
    return TEMPLATE.format(
        direct_evidence=direct_evidence,
        inference=inference,
        proxy_anchor=proxy_anchor,
        stretch=stretch,
    )
