# fs-sistem

This project contains small utilities and modules for working with various
services. The repository now includes a simple cryptocurrency data collector
based on the Binance API.

## Requirements

- Python 3.10+
- `requests` library

Install the dependencies using:

```bash
pip install requests
```

## Crypto Data Collector

The `collector/crypto_data.py` module provides helper functions to retrieve the
latest price and 24‑hour volume for a specific trading pair from Binance.

### Configuration

1. **API Key (optional)**
   
   Public Binance endpoints work without authentication. If you have an API key,
   set it with the `BINANCE_API_KEY` environment variable. It will be attached to
   requests as the `X-MBX-APIKEY` header.

2. **Symbol**
   
   Set the `SYMBOL` environment variable to the trading pair you want to query,
   e.g., `BTCUSDT`.

### Usage

Run the module directly to print the latest price and volume:

```bash
python collector/crypto_data.py
```

You can also import the functions in your own scripts:

```python
from collector.crypto_data import get_price, get_volume

price = get_price("ETHUSDT")
volume = get_volume("ETHUSDT")
```

Both functions accept optional `symbol` and `api_key` parameters if you want to
specify them directly.

## Market Screener

The `scanner/market_screener.py` module implements a basic market
scanning routine inspired by the four-layer early detection system.
It fetches 24‑hour ticker data for all Binance pairs and applies
simple filters for volume, price change percentage and RSI. The module
returns coins that appear overbought or oversold according to the
14‑period RSI indicator.

Run it directly to print detected anomalies:

```bash
python scanner/market_screener.py
```

The other modules in the `scanner` package (`pattern_ai.py`,
`onchain_radar.py` and `sentiment_sniper.py`) provide minimal
placeholders that demonstrate how additional layers could be added in
the future.
