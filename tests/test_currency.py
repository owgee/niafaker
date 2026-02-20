"""Tests for CurrencyProvider."""

from niafaker import NiaFaker


class TestCurrency:
    def test_amount_format(self, locale: str) -> None:
        fake = NiaFaker(locale)
        amount = fake.amount(min_val=1000, max_val=5000)
        assert isinstance(amount, str)
        assert len(amount) > 3

    def test_amount_custom_range(self, locale: str) -> None:
        fake = NiaFaker(locale)
        amount = fake.amount(min_val=1, max_val=10)
        assert isinstance(amount, str)
