from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from typing import Any, Dict, Optional


DEFAULT_HEADERS = {
    'User-Agent': 'isite-research-engine/0.1 (+https://github.com/syoumoku/isite-research-engine)',
    'Accept': 'application/json',
}


def http_get_json(url: str, params: Optional[Dict[str, Any]] = None, timeout: int = 20) -> Any:
    query = ''
    if params:
        query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    full_url = f'{url}?{query}' if query else url
    request = urllib.request.Request(full_url, headers=DEFAULT_HEADERS)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = response.read().decode('utf-8')
    return json.loads(payload)


def polite_sleep(seconds: float = 1.0) -> None:
    time.sleep(seconds)
