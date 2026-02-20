"""Person data generator — names, emails."""

from __future__ import annotations

import random

from niafaker.providers import BaseProvider

_MALE = {"male", "m"}
_FEMALE = {"female", "f"}


class PersonProvider(BaseProvider):

    data_file = "person.json"

    def first_name(self, gender: str | None = None) -> str:
        if gender is None:
            pool = self._data["male_first_names"] + self._data["female_first_names"]
        elif gender.lower() in _MALE:
            pool = self._data["male_first_names"]
        elif gender.lower() in _FEMALE:
            pool = self._data["female_first_names"]
        else:
            raise ValueError(
                f"Unknown gender '{gender}'. Use 'male'/'m' or 'female'/'f'."
            )
        return random.choice(pool)

    def last_name(self) -> str:
        return random.choice(self._data["last_names"])

    def name(self, gender: str | None = None) -> str:
        return f"{self.first_name(gender)} {self.last_name()}"

    def email(self, domain: str | None = None) -> str:
        first = self.first_name().lower()
        last = self.last_name().lower()
        if domain is None:
            domains = self._data.get("email_domains", ["gmail.com", "yahoo.com", "outlook.com"])
            domain = random.choice(domains)
        return f"{first}.{last}{random.randint(1, 999)}@{domain}"
