"""
Polymarket CLOB wrapper using py-clob-client.
Auth via private key + API credentials.
"""

import os
from typing import Any, Optional

try:
    from py_clob_client.client import ClobClient
    from py_clob_client.clob_types import (
        ApiCreds,
        OrderArgs,
        OrderType,
    )
    from py_clob_client.order_builder.constants import BUY, SELL

    HAS_CLOB = True
except ImportError:
    HAS_CLOB = False

from config import PolymarketConfig


class PolymarketClient:
    """Thin wrapper around py-clob-client for the Polymarket CLOB."""

    CLOB_URL = "https://clob.polymarket.com"

    def __init__(self, config: PolymarketConfig):
        if not HAS_CLOB:
            raise ImportError("py-clob-client not installed. pip install py-clob-client")
        self.config = config
        self.client = self._build_client()

    def _build_client(self) -> "ClobClient":
        creds = ApiCreds(
            api_key=self.config.api_key,
            api_secret=self.config.api_secret,
            api_passphrase=self.config.api_passphrase,
        ) if self.config.api_key else None

        client = ClobClient(
            self.CLOB_URL,
            key=self.config.private_key or None,
            chain_id=self.config.chain_id,
            creds=creds,
            funder=self.config.funder or None,
        )

        # Derive API creds if we don't have them yet
        if not creds and self.config.private_key:
            try:
                client.set_api_creds(client.derive_api_key())
            except Exception:
                pass  # read-only mode

        return client

    # ── Markets ───────────────────────────────────────────────────────

    def get_markets(self, next_cursor: str = "", limit: int = 100) -> dict:
        """Fetch active markets from the CLOB."""
        return self.client.get_markets(next_cursor=next_cursor)

    def get_market(self, condition_id: str) -> dict:
        return self.client.get_market(condition_id)

    def get_orderbook(self, token_id: str) -> dict:
        return self.client.get_order_book(token_id)

    def get_simplified_markets(self) -> list[dict]:
        return self.client.get_simplified_markets()

    # ── Trading ───────────────────────────────────────────────────────

    def place_limit_order(
        self,
        token_id: str,
        side: str,       # "buy" or "sell"
        price: float,    # 0.01 - 0.99
        size: float,     # number of shares
    ) -> dict:
        """Place a limit order on the CLOB."""
        order_side = BUY if side.lower() == "buy" else SELL
        order_args = OrderArgs(
            price=price,
            size=size,
            side=order_side,
            token_id=token_id,
        )
        signed = self.client.create_order(order_args)
        return self.client.post_order(signed, OrderType.GTC)

    def cancel_order(self, order_id: str) -> dict:
        return self.client.cancel(order_id)

    def cancel_all(self) -> dict:
        return self.client.cancel_all()

    # ── Positions / Portfolio ─────────────────────────────────────────

    def get_positions(self) -> list[dict]:
        """Get current positions. Returns list of balances by token."""
        try:
            # py-clob-client ≥ 0.14
            return self.client.get_balances()
        except AttributeError:
            # Fallback: call REST directly
            try:
                return self.client.get_positions()
            except Exception:
                return []

    def get_open_orders(self) -> list[dict]:
        return self.client.get_orders()

    def get_trades(self, limit: int = 100) -> list[dict]:
        try:
            return self.client.get_trades(limit=limit)
        except Exception:
            return []

    # ── Address monitoring (public, no auth needed) ───────────────────

    @staticmethod
    def get_address_positions(address: str) -> list[dict]:
        """
        Fetch positions for an arbitrary Polymarket address.
        Uses the public Polymarket profile API.
        """
        import requests
        url = f"https://polymarket.com/api/profile/{address}/positions"
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            return r.json()
        except Exception:
            # Fallback: gamma-api
            try:
                url2 = f"https://gamma-api.polymarket.com/positions?user={address}"
                r2 = requests.get(url2, timeout=10)
                r2.raise_for_status()
                return r2.json()
            except Exception:
                return []
