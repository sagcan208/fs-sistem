"""Basic social media sentiment utilities.

These are placeholders that illustrate how sentiment scanning could be
integrated. They rely on environment variables for API keys and do not
handle authentication or rate limits.
"""

import os
import requests

X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")


def search_x(keyword: str, limit: int = 10) -> list[dict]:
    """Search recent posts on X (Twitter) containing ``keyword``."""
    if not X_BEARER_TOKEN:
        raise RuntimeError("X_BEARER_TOKEN not set")
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {X_BEARER_TOKEN}"}
    params = {"query": keyword, "max_results": limit}
    resp = requests.get(url, headers=headers, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json().get("data", [])


def keyword_mention_count(keyword: str) -> int:
    """Return how many times ``keyword`` is mentioned recently."""
    try:
        posts = search_x(keyword, limit=100)
    except Exception:
        return 0
    return len(posts)


if __name__ == "__main__":
    print(keyword_mention_count("listing"))
