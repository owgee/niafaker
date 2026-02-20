"""Tests for MobileMoneyProvider."""

from niafaker import NiaFaker


class TestMobileMoney:
    def test_account_structure(self, locale: str) -> None:
        fake = NiaFaker(locale)
        account = fake.mobile_money()
        assert isinstance(account, dict)
        assert "provider" in account
        assert "number" in account

    def test_account_number_format(self, locale: str) -> None:
        fake = NiaFaker(locale)
        account = fake.mobile_money()
        assert account["number"].startswith("+")
        assert account["number"][1:].isdigit()

    def test_provider_name(self, locale: str) -> None:
        fake = NiaFaker(locale)
        provider = fake.mobile_money_provider()
        assert isinstance(provider, str)
        assert len(provider) > 1

    def test_transaction_id(self, locale: str) -> None:
        fake = NiaFaker(locale)
        tx = fake.transaction_id()
        assert isinstance(tx, str)
        assert len(tx) > 5
