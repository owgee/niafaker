"""Tests for PersonProvider."""

from niafaker import NiaFaker


class TestPerson:
    def test_name_returns_string(self, locale: str) -> None:
        fake = NiaFaker(locale)
        name = fake.name()
        assert isinstance(name, str)
        assert " " in name

    def test_name_male(self, locale: str) -> None:
        fake = NiaFaker(locale)
        name = fake.name(gender="male")
        assert isinstance(name, str)
        assert len(name) > 2

    def test_name_female(self, locale: str) -> None:
        fake = NiaFaker(locale)
        name = fake.name(gender="female")
        assert isinstance(name, str)
        assert len(name) > 2

    def test_first_name(self, locale: str) -> None:
        fake = NiaFaker(locale)
        first = fake.first_name()
        assert isinstance(first, str)
        assert " " not in first

    def test_last_name(self, locale: str) -> None:
        fake = NiaFaker(locale)
        last = fake.last_name()
        assert isinstance(last, str)
        assert len(last) > 1

    def test_email_format(self, locale: str) -> None:
        fake = NiaFaker(locale)
        email = fake.email()
        assert "@" in email
        assert "." in email.split("@")[1]

    def test_email_custom_domain(self, locale: str) -> None:
        fake = NiaFaker(locale)
        email = fake.email(domain="test.org")
        assert email.endswith("@test.org")
