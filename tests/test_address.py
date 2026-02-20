"""Tests for AddressProvider."""

from niafaker import NiaFaker
from niafaker.providers import LOCALE_NAMES


class TestAddress:
    def test_city(self, locale: str) -> None:
        fake = NiaFaker(locale)
        city = fake.city()
        assert isinstance(city, str)
        assert len(city) > 1

    def test_region(self, locale: str) -> None:
        fake = NiaFaker(locale)
        region = fake.region()
        assert isinstance(region, str)
        assert len(region) > 1

    def test_address_contains_city(self, locale: str) -> None:
        fake = NiaFaker(locale)
        address = fake.address()
        assert isinstance(address, str)
        assert "," in address

    def test_country(self, locale: str) -> None:
        fake = NiaFaker(locale)
        country = fake.country()
        assert country == LOCALE_NAMES[locale]
