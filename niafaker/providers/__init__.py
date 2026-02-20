"""Base provider for all NiaFaker data generators."""

from __future__ import annotations

import json
from importlib import resources
from typing import Any


SUPPORTED_LOCALES = ("tz", "ke", "ng", "za", "gh", "ug", "rw", "et", "eg", "ma")

LOCALE_NAMES: dict[str, str] = {
    "tz": "Tanzania",
    "ke": "Kenya",
    "ng": "Nigeria",
    "za": "South Africa",
    "gh": "Ghana",
    "ug": "Uganda",
    "rw": "Rwanda",
    "et": "Ethiopia",
    "eg": "Egypt",
    "ma": "Morocco",
}


class BaseProvider:
    """Base class that handles locale data loading for all providers."""

    data_file: str = ""

    def __init__(self, locale: str) -> None:
        if locale not in SUPPORTED_LOCALES:
            raise ValueError(
                f"Unsupported locale '{locale}'. "
                f"Supported: {', '.join(SUPPORTED_LOCALES)}"
            )
        self.locale = locale
        self._data = self._load_data()

    def _load_data(self) -> dict[str, Any]:
        ref = resources.files("niafaker.locales") / self.locale / self.data_file
        return json.loads(ref.read_text(encoding="utf-8"))
