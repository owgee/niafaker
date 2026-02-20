"""Person data generator — names, emails."""

from __future__ import annotations

import random

from niafaker.providers import BaseProvider


class PersonProvider(BaseProvider):

    data_file = "person.json"

    def first_name(self, gender: str | None = None) -> str:
        if gender == "male":
            pool = self._data["male_first_names"]
        elif gender == "female":
            pool = self._data["female_first_names"]
        else:
            pool = self._data["male_first_names"] + self._data["female_first_names"]
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
