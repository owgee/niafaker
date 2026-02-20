"""Tests for PhoneProvider."""

import pytest

from niafaker import NiaFaker


class TestPhone:
    def test_phone_starts_with_plus(self, locale: str) -> None:
        fake = NiaFaker(locale)
        phone = fake.phone()
        assert phone.startswith("+")

    def test_phone_is_digits_after_plus(self, locale: str) -> None:
        fake = NiaFaker(locale)
        phone = fake.phone()
        assert phone[1:].isdigit()

    def test_phone_length(self, locale: str) -> None:
        fake = NiaFaker(locale)
        phone = fake.phone()
        assert len(phone) >= 10

    def test_carrier_name(self, locale: str) -> None:
        fake = NiaFaker(locale)
        carrier = fake.carrier()
        assert isinstance(carrier, str)
        assert len(carrier) > 1

    def test_invalid_carrier_raises(self, locale: str) -> None:
        fake = NiaFaker(locale)
        with pytest.raises(ValueError, match="Unknown carrier"):
            fake.phone(carrier="NonExistentCarrier123")
