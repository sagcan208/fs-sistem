"""Sentiment Sniper module.

Scans social platforms like Twitter, Telegram and Reddit to detect
sudden increases in discussion volume. Keywords such as ``listing`` or
``burn`` can trigger alerts. The current implementation only returns
mock sentiment information and does not perform any network requests.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

@dataclass
class SentimentResult:
    keyword: str
    mentions: int
    is_real_hype: bool


def scan_social_media(keywords: list[str]) -> list[SentimentResult]:
    """Return placeholder sentiment information for given keywords."""
    results = [
        SentimentResult(keyword=k, mentions=42, is_real_hype=True)
        for k in keywords
    ]
    return results

