"""Mobile money account generator — M-Pesa, MTN MoMo, Airtel Money, etc."""

from __future__ import annotations

import random

from niafaker.providers import BaseProvider
from niafaker.providers.phone import generate_number


class MobileMoneyProvider(BaseProvider):

    data_file = "mobile_money.json"

    def account(self) -> dict[str, str]:
        """Generate a mobile money account with provider and number."""
        provider = random.choice(self._data["providers"])
        number = generate_number(
            self._data["country_code"],
            provider["prefixes"],
            self._data["subscriber_digits"],
        )
        return {"provider": provider["name"], "number": number}

    def transaction_id(self) -> str:
        prefix = self._data.get("tx_prefix", "TXN")
        digits = "".join(str(random.randint(0, 9)) for _ in range(10))
        return f"{prefix}{digits}"
