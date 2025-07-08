import requests
import numpy as np

from .market_screener import fetch_klines


def deviation_score(symbol: str, interval: str = "1h", lookback: int = 48) -> float:
    """Return a simple deviation score for the last half vs previous half."""
    data = fetch_klines(symbol, interval, lookback * 2)
    closes = [float(c[4]) for c in data]
    if len(closes) < lookback * 2:
        return 0.0
    first = np.array(closes[:lookback])
    second = np.array(closes[lookback:])
    first_norm = first / first[0]
    second_norm = second / second[0]
    deviation = np.mean(np.abs(second_norm - first_norm))
    return float(deviation)


def pump_dump_risk(symbol: str) -> dict:
    """Return a naive pump/dump risk score for ``symbol``."""
    score = deviation_score(symbol)
    return {
        "symbol": symbol,
        "risk_score": round(score * 100, 2)
    }


if __name__ == "__main__":
    print(pump_dump_risk("BTCUSDT"))
