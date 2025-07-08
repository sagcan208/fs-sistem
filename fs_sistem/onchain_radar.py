"""On-chain behaviour monitoring module.

This component watches for notable blockchain events such as whale
transfers, dormant wallet activity, miner sales or token unlocks.
The implementation is greatly simplified and uses mock events.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

@dataclass
class OnChainEvent:
    address: str
    event: str
    amount: float


def scan_blockchain() -> List[OnChainEvent]:
    """Return a list of placeholder on-chain events."""
    dummy_events = [
        OnChainEvent(address="0xWhale1", event="transfer", amount=1000.0),
        OnChainEvent(address="0xMiner2", event="sale", amount=50.0),
    ]
    return dummy_events

