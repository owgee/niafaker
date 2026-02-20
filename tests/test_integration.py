"""Integration tests — NiaFaker class and backward-compatible functions."""

import pytest

from niafaker import (
    NiaFaker,
    generate_address,
    generate_city,
    generate_country,
    generate_email,
    generate_last_name,
    generate_name,
    generate_phone_number,
)
from niafaker.providers import SUPPORTED_LOCALES


class TestNiaFakerClass:
    def test_all_locales_instantiate(self) -> None:
        for locale in SUPPORTED_LOCALES:
            fake = NiaFaker(locale)
            assert fake.locale == locale

    def test_invalid_locale_raises(self) -> None:
        with pytest.raises(ValueError, match="Unsupported locale"):
            NiaFaker("xx")

    def test_locales_returns_all(self) -> None:
        locales = NiaFaker.locales()
        assert len(locales) == 10
        assert "tz" in locales
        assert locales["tz"] == "Tanzania"

    def test_repr(self) -> None:
        fake = NiaFaker("ke")
        assert repr(fake) == "NiaFaker(locale='ke')"

    def test_case_insensitive_locale(self) -> None:
        fake = NiaFaker("TZ")
        assert fake.locale == "tz"


class TestBackwardCompatibility:
    def test_generate_name(self) -> None:
        name = generate_name()
        assert isinstance(name, str)
        assert " " in name

    def test_generate_last_name(self) -> None:
        last = generate_last_name()
        assert isinstance(last, str)

    def test_generate_email(self) -> None:
        email = generate_email()
        assert "@" in email

    def test_generate_phone_number(self) -> None:
        phone = generate_phone_number()
        assert phone.startswith("+")

    def test_generate_city(self) -> None:
        city = generate_city()
        assert isinstance(city, str)

    def test_generate_address(self) -> None:
        address = generate_address()
        assert isinstance(address, str)

    def test_generate_country(self) -> None:
        country = generate_country()
        assert isinstance(country, str)
        assert len(country) > 2
