"""Integration tests — NiaFaker class and backward-compatible functions."""

import pytest

from niafaker import (
    NiaFaker,
    generate_address,
    generate_city,
    generate_country,
    generate_email,
    generate_name,
    generate_phone_number,
)
from niafaker.providers import SUPPORTED_LOCALES


class TestNiaFakerClass:
    def test_all_locales_instantiate(self) -> None:
        for locale in SUPPORTED_LOCALES:
            assert NiaFaker(locale).locale == locale

    def test_invalid_locale_raises(self) -> None:
        with pytest.raises(ValueError, match="Unsupported locale"):
            NiaFaker("xx")

    def test_locales_returns_all(self) -> None:
        locales = NiaFaker.locales()
        assert len(locales) == 10
        assert "tz" in locales

    def test_repr(self) -> None:
        assert repr(NiaFaker("ke")) == "NiaFaker(locale='ke')"

    def test_case_insensitive_locale(self) -> None:
        assert NiaFaker("TZ").locale == "tz"

    def test_seed_produces_reproducible_output(self) -> None:
        a = NiaFaker("tz", seed=42).name()
        b = NiaFaker("tz", seed=42).name()
        assert a == b


class TestBackwardCompatibility:
    def test_generate_name(self) -> None:
        assert " " in generate_name()

    def test_generate_email(self) -> None:
        assert "@" in generate_email()

    def test_generate_phone_number(self) -> None:
        assert generate_phone_number().startswith("+")

    def test_generate_city(self) -> None:
        assert len(generate_city()) > 1

    def test_generate_address(self) -> None:
        assert "," in generate_address()

    def test_generate_country(self) -> None:
        assert len(generate_country()) > 2
