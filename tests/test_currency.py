"""Tests for CurrencyProvider."""

from niafaker import NiaFaker


class TestCurrency:
    def test_currency_code(self, locale: str) -> None:
        fake = NiaFaker(locale)
        code = fake.currency_code()
        assert isinstance(code, str)
        assert len(code) == 3

    def test_currency_name(self, locale: str) -> None:
        fake = NiaFaker(locale)
        name = fake.currency_name()
        assert isinstance(name, str)
        assert len(name) > 3

    def test_symbol(self, locale: str) -> None:
        fake = NiaFaker(locale)
        sym = fake.currency_symbol()
        assert isinstance(sym, str)
        assert len(sym) >= 1

    def test_amount_format(self, locale: str) -> None:
        fake = NiaFaker(locale)
        amount = fake.amount(min_val=1000, max_val=5000)
        assert isinstance(amount, str)
        assert len(amount) > 3
