"""Simple on-chain monitoring utilities.

These functions use public blockchain explorer APIs to look for
large transfers or token unlock events. They are intentionally
lightweight and serve as placeholders for a more complete system.
"""

import os
import requests

ETHERSCAN_API = "https://api.etherscan.io/api"
API_KEY = os.getenv("ETHERSCAN_API_KEY")


def get_token_transfers(address: str, limit: int = 10) -> list[dict]:
    """Return recent transfers involving ``address``."""
    if not API_KEY:
        raise RuntimeError("ETHERSCAN_API_KEY not set")
    params = {
        "module": "account",
        "action": "tokentx",
        "address": address,
        "page": 1,
        "offset": limit,
        "sort": "desc",
        "apikey": API_KEY,
    }
    resp = requests.get(ETHERSCAN_API, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json().get("result", [])


def has_large_transfer(address: str, threshold: float = 1_000_000) -> bool:
    """Return ``True`` if ``address`` sent or received a large transfer."""
    try:
        transfers = get_token_transfers(address, 5)
    except Exception:
        return False
    for t in transfers:
        value = float(t.get("value", 0)) / (10 ** int(t.get("tokenDecimal", 0)))
        if value >= threshold:
            return True
    return False


if __name__ == "__main__":
    addr = os.getenv("ADDRESS")
    if addr:
        print(has_large_transfer(addr))
    else:
        print("Set ADDRESS env var")
