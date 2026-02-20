"""Phone number generator with real carrier prefixes."""

from __future__ import annotations

import random

from niafaker.providers import BaseProvider


def generate_number(country_code: str, prefixes: list[str], subscriber_digits: int) -> str:
    """Build a phone number from country code, prefix pool, and digit count."""
    prefix = random.choice(prefixes)
    remaining = subscriber_digits - len(prefix)
    suffix = "".join(str(random.randint(0, 9)) for _ in range(remaining))
    return f"+{country_code}{prefix}{suffix}"


class PhoneProvider(BaseProvider):

    data_file = "phone.json"

    def phone_number(self, carrier: str | None = None) -> str:
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

        return generate_number(
            self._data["country_code"],
            carrier_data["prefixes"],
            self._data["subscriber_digits"],
        )
