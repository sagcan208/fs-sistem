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
