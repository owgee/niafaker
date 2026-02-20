"""Tests for CompanyProvider."""

from niafaker import NiaFaker


class TestCompany:
    def test_company_name(self, locale: str) -> None:
        fake = NiaFaker(locale)
        name = fake.company()
        assert isinstance(name, str)
        assert len(name) > 3

    def test_company_type(self, locale: str) -> None:
        fake = NiaFaker(locale)
        ctype = fake.company_type()
        assert isinstance(ctype, str)

    def test_registration_number(self, locale: str) -> None:
        fake = NiaFaker(locale)
        reg = fake.registration_number()
        assert isinstance(reg, str)
        assert len(reg) > 3
