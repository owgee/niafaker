"""Phone number generator with real carrier prefixes."""

from __future__ import annotations

import random

from niafaker.providers import BaseProvider


class PhoneProvider(BaseProvider):

    data_file = "phone.json"

    def phone_number(self, carrier: str | None = None) -> str:
        """Generate a phone number with a real carrier prefix.

        Args:
            carrier: Filter by carrier name (e.g. "Safaricom", "MTN").
                     If None, picks a random carrier.
        """
        country_code = self._data["country_code"]
        carriers = self._data["carriers"]

        if carrier:
            matches = [c for c in carriers if c["name"].lower() == carrier.lower()]
            if not matches:
                raise ValueError(
                    f"Unknown carrier '{carrier}' for locale '{self.locale}'. "
                    f"Available: {', '.join(c['name'] for c in carriers)}"
                )
            carrier_data = random.choice(matches)
        else:
            carrier_data = random.choice(carriers)

        prefix = random.choice(carrier_data["prefixes"])
        remaining = self._data["subscriber_digits"] - len(prefix)
        suffix = "".join(str(random.randint(0, 9)) for _ in range(remaining))
        return f"+{country_code}{prefix}{suffix}"

    def carrier_name(self) -> str:
        return random.choice(self._data["carriers"])["name"]
