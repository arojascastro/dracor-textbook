# utils/dracor_client.py
from __future__ import annotations
import time
from typing import Dict, List, Any, Optional
import requests

BASE = "https://dracor.org/api/v1"
UA = "dracor-textbook/0.1 (+https://github.com/arojascastro/dracor-textbook)"

def _get(path: str, params: Optional[Dict[str, Any]] = None, retries: int = 2, backoff: float = 0.6) -> Any:
    url = f"{BASE}{path}"
    last_exc = None
    for attempt in range(retries + 1):
        try:
            r = requests.get(
                url,
                params=params,
                headers={"Accept": "application/json", "User-Agent": UA},
                timeout=15,
            )
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            msg = (getattr(e, "response", None).text or "")[:200] if getattr(e, "response", None) else ""
            last_exc = requests.HTTPError(f"{e}; body: {msg}")
        except requests.RequestException as e:
            last_exc = e
        if attempt < retries:
            time.sleep(backoff * (2 ** attempt))
    raise last_exc

def corpora() -> List[Dict[str, Any]]:
    data = _get("/corpora")
    out = []
    for c in data:
        slug = c.get("name") or c.get("id") or c.get("corpus")
        if slug:
            d = dict(c)
            d["slug"] = slug
            out.append(d)
    return out

def corpus_plays(corpus_slug: str) -> List[Dict[str, Any]]:
    return _get(f"/corpora/{corpus_slug}/plays")

def play_metadata(corpus_slug: str, play_id: str) -> Dict[str, Any]:
    return _get(f"/corpora/{corpus_slug}/plays/{play_id}")

def play_characters(corpus_slug: str, play_id: str) -> List[Dict[str, Any]]:
    return _get(f"/corpora/{corpus_slug}/plays/{play_id}/characters")
