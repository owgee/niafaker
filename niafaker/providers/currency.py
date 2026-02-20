"""Currency generator — codes, symbols, formatted amounts."""

from __future__ import annotations

import random

from niafaker.providers import BaseProvider


class CurrencyProvider(BaseProvider):

    data_file = "currency.json"

    def currency_code(self) -> str:
        return self._data["code"]

    def currency_name(self) -> str:
        return self._data["name"]

    def symbol(self) -> str:
        return self._data["symbol"]

    def amount(self, min_val: int = 100, max_val: int = 1_000_000) -> str:
        """Generate a formatted currency amount."""
        value = random.randint(min_val, max_val)
        sep = self._data.get("thousands_sep", ",")
        formatted = f"{value:,}".replace(",", sep)
        symbol = self._data["symbol"]
        if self._data.get("symbol_after", False):
            return f"{formatted} {symbol}"
        return f"{symbol} {formatted}"
