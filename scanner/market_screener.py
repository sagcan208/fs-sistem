import os
import requests

BINANCE_TICKER_URL = "https://api.binance.com/api/v3/ticker/24hr"
BINANCE_KLINE_URL = "https://api.binance.com/api/v3/klines"


def fetch_all_tickers() -> list[dict]:
    """Return 24hr ticker data for all trading pairs."""
    resp = requests.get(BINANCE_TICKER_URL, timeout=10)
    resp.raise_for_status()
    return resp.json()


def fetch_klines(symbol: str, interval: str = "1h", limit: int = 100) -> list[dict]:
    """Return klines for ``symbol`` using the given ``interval``."""
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    resp = requests.get(BINANCE_KLINE_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


def rsi(prices: list[float], period: int = 14) -> float:
    """Compute a simple RSI value for ``prices``."""
    if len(prices) < period + 1:
        raise ValueError("Not enough data for RSI")
    gains = 0.0
    losses = 0.0
    for i in range(1, period + 1):
        diff = prices[-i] - prices[-i - 1]
        if diff > 0:
            gains += diff
        else:
            losses += -diff
    avg_gain = gains / period
    avg_loss = losses / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def screen_market(volume_min: float = 1_000_000.0,
                  price_change_min: float = 5.0,
                  rsi_period: int = 14,
                  overbought: float = 70.0,
                  oversold: float = 30.0) -> list[dict]:
    """Screen all Binance pairs and return anomalies."""
    anomalies = []
    tickers = fetch_all_tickers()
    for t in tickers:
        symbol = t["symbol"]
        volume = float(t["quoteVolume"])
        change = float(t["priceChangePercent"])
        if volume < volume_min or abs(change) < price_change_min:
            continue
        try:
            data = fetch_klines(symbol, "1h", rsi_period + 1)
            closes = [float(c[4]) for c in data]
            rsi_val = rsi(closes, rsi_period)
        except Exception:
            continue
        if rsi_val > overbought or rsi_val < oversold:
            anomalies.append({
                "symbol": symbol,
                "volume": volume,
                "change": change,
                "rsi": rsi_val
            })
    return anomalies


if __name__ == "__main__":
    results = screen_market()
    for item in results:
        print(item)
