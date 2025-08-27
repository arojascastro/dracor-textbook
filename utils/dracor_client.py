import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_URL = "https://dracor.org/api/v1"

def _session(timeout: float = 15.0) -> requests.Session:
    s = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    s.mount("https://", HTTPAdapter(max_retries=retries))
    return s

S = _session()

def get(path: str, **params):
    url = f"{BASE_URL.rstrip('/')}/{path.lstrip('/')}"
    r = S.get(url, params=params, timeout=15)
    r.raise_for_status()
    return r.json()

def corpora():
    return get("corpora")

def corpus_plays(corpus_id: str):
    return get(f"corpora/{corpus_id}/plays")

def characters(corpus_id: str, play_id: str):
    return get(f"corpora/{corpus_id}/plays/{play_id}/characters")

if __name__ == "__main__":
    print([c["name"] for c in corpora()][:5])
