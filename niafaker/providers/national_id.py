"""National ID number generator — structurally valid per country."""

from __future__ import annotations

import random

from niafaker.providers import BaseProvider


class NationalIDProvider(BaseProvider):

    data_file = "national_id.json"

    def national_id(self) -> str:
        """Generate a structurally valid national ID number."""
        pattern = self._data["pattern"]
        result = []
        for char in pattern:
            if char == "D":
                result.append(str(random.randint(0, 9)))
            elif char == "L":
                result.append(chr(random.randint(65, 90)))
            else:
                result.append(char)
        return "".join(result)

    def id_name(self) -> str:
        """Return the official name of the national ID system."""
        return self._data["system_name"]
