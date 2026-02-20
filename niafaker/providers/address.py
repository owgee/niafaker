"""Address generator — cities, regions, street addresses."""

from __future__ import annotations

import random

from niafaker.providers import BaseProvider


class AddressProvider(BaseProvider):

    data_file = "address.json"

    def city(self) -> str:
        return random.choice(self._data["cities"])

    def region(self) -> str:
        return random.choice(self._data["regions"])

    def street_address(self) -> str:
        patterns = self._data.get("street_patterns", ["{number} {street}"])
        pattern = random.choice(patterns)
        return pattern.format(
            number=random.randint(1, 9999),
            street=random.choice(self._data.get("streets", ["Main Street"])),
        )

    def address(self) -> str:
        parts = [self.street_address(), self.city(), self.region()]
        postal = self._data.get("postal_codes")
        if postal:
            parts.append(random.choice(postal))
        return ", ".join(parts)

    def country(self) -> str:
        from niafaker.providers import LOCALE_NAMES
        return LOCALE_NAMES[self.locale]
