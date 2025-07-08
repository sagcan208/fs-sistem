"""Entry point for FS Kripto Taramasi demo implementation."""
from __future__ import annotations

import argparse

from .alerts import send_alert
from .market_screener import screen_markets
from .pattern_deviation import analyze_pattern
from .onchain_radar import scan_blockchain
from .sentiment_sniper import scan_social_media


def run_screener() -> None:
    results = screen_markets()
    for r in results:
        send_alert(
            f"{r.symbol} volume +{r.volume_change:.1f} RSI {r.rsi} price {r.price_change_pct}%"
        )


def run_deviation(symbol: str) -> None:
    score = analyze_pattern(symbol)
    send_alert(f"{symbol} pump risk {score.pump_risk} dump risk {score.dump_risk}")


def run_onchain() -> None:
    events = scan_blockchain()
    for e in events:
        send_alert(f"{e.event} by {e.address} amount {e.amount}")


def run_sentiment(keywords: list[str]) -> None:
    results = scan_social_media(keywords)
    for res in results:
        send_alert(f"{res.keyword} mentioned {res.mentions}x real hype={res.is_real_hype}")


def main() -> None:
    parser = argparse.ArgumentParser(description="FS Kripto Taramasi demo")
    parser.add_argument("mode", choices=["screener", "deviation", "onchain", "sentiment"])
    parser.add_argument("symbol", nargs="?", help="symbol for deviation mode")
    parser.add_argument("keywords", nargs="*", help="keywords for sentiment mode")

    args = parser.parse_args()
    if args.mode == "screener":
        run_screener()
    elif args.mode == "deviation":
        if not args.symbol:
            parser.error("symbol is required for deviation mode")
        run_deviation(args.symbol)
    elif args.mode == "onchain":
        run_onchain()
    elif args.mode == "sentiment":
        if not args.keywords:
            parser.error("keywords required for sentiment mode")
        run_sentiment(args.keywords)


if __name__ == "__main__":
    main()

