"""Simple alerting utilities for FS Kripto Taramasi."""
from __future__ import annotations

import sys


def send_alert(message: str) -> None:
    """Print message to stdout as a placeholder for real alerts."""
    print(f"[ALERT] {message}", file=sys.stdout)

