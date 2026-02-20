"""NiaFaker — Fake data generator localized for African regions."""

from __future__ import annotations

import random

from niafaker.providers import LOCALE_NAMES, SUPPORTED_LOCALES
from niafaker.providers.address import AddressProvider
from niafaker.providers.company import CompanyProvider
from niafaker.providers.currency import CurrencyProvider
from niafaker.providers.mobile_money import MobileMoneyProvider
from niafaker.providers.national_id import NationalIDProvider
from niafaker.providers.person import PersonProvider
from niafaker.providers.phone import PhoneProvider

__version__ = "1.0.0"
__all__ = [
    "NiaFaker",
    "generate_name",
    "generate_email",
    "generate_phone_number",
    "generate_city",
    "generate_address",
    "generate_country",
]


class NiaFaker:
    """Fake data generator for a specific African locale.

    Args:
        locale: Two-letter country code (e.g. "tz", "ke", "ng").
    """

    def __init__(self, locale: str) -> None:
        self.locale = locale.lower()
        self._person = PersonProvider(self.locale)
        self._phone = PhoneProvider(self.locale)
        self._address = AddressProvider(self.locale)
        self._company = CompanyProvider(self.locale)
        self._mobile_money = MobileMoneyProvider(self.locale)
        self._national_id = NationalIDProvider(self.locale)
        self._currency = CurrencyProvider(self.locale)

    def name(self, gender: str | None = None) -> str:
        return self._person.name(gender)

    def first_name(self, gender: str | None = None) -> str:
        return self._person.first_name(gender)

    def last_name(self) -> str:
        return self._person.last_name()

    def email(self, domain: str | None = None) -> str:
        return self._person.email(domain)

    def phone(self, carrier: str | None = None) -> str:
        return self._phone.phone_number(carrier)

    def city(self) -> str:
        return self._address.city()

    def region(self) -> str:
        return self._address.region()

    def address(self) -> str:
        return self._address.address()

    def country(self) -> str:
        return self._address.country()

    def company(self) -> str:
        return self._company.company_name()

    def registration_number(self) -> str:
        return self._company.registration_number()

    def mobile_money(self) -> dict[str, str]:
        return self._mobile_money.account()

    def transaction_id(self) -> str:
        return self._mobile_money.transaction_id()

    def national_id(self) -> str:
        return self._national_id.national_id()

    def amount(self, min_val: int = 100, max_val: int = 1_000_000) -> str:
        return self._currency.amount(min_val, max_val)

    @staticmethod
    def locales() -> dict[str, str]:
        """Return all supported locales as {code: country_name}."""
        return dict(LOCALE_NAMES)

    def __repr__(self) -> str:
        return f"NiaFaker(locale='{self.locale}')"


# ── Backward-compatible convenience functions ──


def _random_faker() -> NiaFaker:
    return NiaFaker(random.choice(SUPPORTED_LOCALES))


def generate_name(gender: str | None = None) -> str:
    return _random_faker().name(gender)


def generate_email() -> str:
    return _random_faker().email()


def generate_phone_number() -> str:
    return _random_faker().phone()


def generate_city() -> str:
    return _random_faker().city()


def generate_address() -> str:
    return _random_faker().address()


def generate_country() -> str:
    return _random_faker().country()
