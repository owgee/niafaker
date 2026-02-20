"""Company name and registration number generator."""

from __future__ import annotations

import random
import string

from niafaker.providers import BaseProvider


class CompanyProvider(BaseProvider):

    data_file = "company.json"

    def company_name(self) -> str:
        name = random.choice(self._data["names"])
        suffix = random.choice(self._data["suffixes"])
        return f"{name} {suffix}"

    def company_type(self) -> str:
        return random.choice(self._data["suffixes"])

    def registration_number(self) -> str:
        pattern = self._data.get("registration_pattern", "REG-{digits:06d}")
        digits = random.randint(0, 999999)
        letters = "".join(random.choices(string.ascii_uppercase, k=3))
        return pattern.format(digits=digits, letters=letters)
