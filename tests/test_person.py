"""Tests for PersonProvider."""

import pytest

from niafaker import NiaFaker


class TestPerson:
    def test_name_returns_full_name(self, locale: str) -> None:
        fake = NiaFaker(locale)
        assert " " in fake.name()

    def test_name_male(self, locale: str) -> None:
        fake = NiaFaker(locale)
        assert len(fake.name(gender="male")) > 2

    def test_name_female(self, locale: str) -> None:
        fake = NiaFaker(locale)
        assert len(fake.name(gender="female")) > 2

    def test_name_shorthand_m(self, locale: str) -> None:
        fake = NiaFaker(locale)
        assert len(fake.name(gender="m")) > 2

    def test_name_shorthand_f(self, locale: str) -> None:
        fake = NiaFaker(locale)
        assert len(fake.name(gender="f")) > 2

    def test_name_invalid_gender_raises(self) -> None:
        fake = NiaFaker("tz")
        with pytest.raises(ValueError, match="Unknown gender"):
            fake.name(gender="X")

    def test_first_name_no_space(self, locale: str) -> None:
        fake = NiaFaker(locale)
        assert " " not in fake.first_name()

    def test_last_name(self, locale: str) -> None:
        fake = NiaFaker(locale)
        assert len(fake.last_name()) > 1

    def test_email_format(self, locale: str) -> None:
        fake = NiaFaker(locale)
        email = fake.email()
        assert "@" in email
        assert "." in email.split("@")[1]

    def test_email_custom_domain(self, locale: str) -> None:
        fake = NiaFaker(locale)
        assert fake.email(domain="test.org").endswith("@test.org")
