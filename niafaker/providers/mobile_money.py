"""Mobile money account generator — M-Pesa, MTN MoMo, Airtel Money, etc."""

from __future__ import annotations

import random

from niafaker.providers import BaseProvider


class MobileMoneyProvider(BaseProvider):

    data_file = "mobile_money.json"

    def account(self) -> dict[str, str]:
        """Generate a mobile money account with provider and number."""
        country_code = self._data["country_code"]
        provider = random.choice(self._data["providers"])
        prefix = random.choice(provider["prefixes"])
        remaining = self._data["subscriber_digits"] - len(prefix)
        suffix = "".join(str(random.randint(0, 9)) for _ in range(remaining))
        return {
            "provider": provider["name"],
            "number": f"+{country_code}{prefix}{suffix}",
        }

    def provider_name(self) -> str:
        return random.choice(self._data["providers"])["name"]

    def transaction_id(self) -> str:
        """Generate a realistic transaction reference."""
        prefix = self._data.get("tx_prefix", "TXN")
        digits = "".join(str(random.randint(0, 9)) for _ in range(10))
        return f"{prefix}{digits}"
