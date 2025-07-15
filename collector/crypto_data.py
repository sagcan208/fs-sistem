import os
import requests

BINANCE_API_URL = 'https://api.binance.com/api/v3/ticker/24hr'

_session = requests.Session()


def fetch_ticker(symbol: str, api_key: str | None = None) -> dict:
    """Fetch 24hr ticker data for the given symbol from Binance.

    Parameters
    ----------
    symbol : str
        Trading pair symbol, e.g., ``'BTCUSDT'``.
    api_key : str | None, optional
        Binance API key if available. Public endpoints do not require it
        but it can be passed via the ``X-MBX-APIKEY`` header.

    Returns
    -------
    dict
        JSON response containing ticker information such as ``lastPrice``
        and ``volume``.
    """
    headers = {}
    if api_key:
        headers['X-MBX-APIKEY'] = api_key

    params = {'symbol': symbol.upper()}
    response = _session.get(BINANCE_API_URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def get_price(symbol: str, api_key: str | None = None) -> float:
    """Return the latest price for ``symbol``."""
    data = fetch_ticker(symbol, api_key)
    return float(data['lastPrice'])


def get_volume(symbol: str, api_key: str | None = None) -> float:
    """Return the traded volume in the last 24 hours for ``symbol``."""
    data = fetch_ticker(symbol, api_key)
    return float(data['volume'])


def get_price_and_volume(symbol: str, api_key: str | None = None) -> tuple[float, float]:
    """Return both the latest price and 24h volume for ``symbol`` in a single API call.
    
    This is more efficient than calling get_price() and get_volume() separately
    as it avoids redundant API requests.
    
    Parameters
    ----------
    symbol : str
        Trading pair symbol, e.g., ``'BTCUSDT'``.
    api_key : str | None, optional
        Binance API key if available.
        
    Returns
    -------
    tuple[float, float]
        A tuple containing (price, volume).
    """
    data = fetch_ticker(symbol, api_key)
    return float(data['lastPrice']), float(data['volume'])


if __name__ == '__main__':
    symbol = os.getenv('SYMBOL', 'BTCUSDT')
    api_key = os.getenv('BINANCE_API_KEY')
    print('Symbol:', symbol)
    price, volume = get_price_and_volume(symbol, api_key)
    print('Price:', price)
    print('Volume:', volume)
