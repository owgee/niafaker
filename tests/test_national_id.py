"""Tests for NationalIDProvider."""

from niafaker import NiaFaker


class TestNationalID:
    def test_national_id_type(self, locale: str) -> None:
        fake = NiaFaker(locale)
        nid = fake.national_id()
        assert isinstance(nid, str)
        assert len(nid) > 5

    def test_national_id_name(self, locale: str) -> None:
        fake = NiaFaker(locale)
        name = fake.national_id_name()
        assert isinstance(name, str)
        assert len(name) > 3

    def test_tanzania_nida_format(self) -> None:
        fake = NiaFaker("tz")
        nid = fake.national_id()
        parts = nid.split("-")
        assert len(parts) == 4
        assert len(parts[0]) == 8
        assert len(parts[1]) == 5
        assert len(parts[2]) == 5
        assert len(parts[3]) == 2

    def test_kenya_id_length(self) -> None:
        fake = NiaFaker("ke")
        nid = fake.national_id()
        assert len(nid) == 8
        assert nid.isdigit()

    def test_nigeria_nin_length(self) -> None:
        fake = NiaFaker("ng")
        nid = fake.national_id()
        assert len(nid) == 11
        assert nid.isdigit()

    def test_south_africa_id_length(self) -> None:
        fake = NiaFaker("za")
        nid = fake.national_id()
        assert len(nid) == 13
        assert nid.isdigit()

    def test_ghana_card_format(self) -> None:
        fake = NiaFaker("gh")
        nid = fake.national_id()
        assert nid.startswith("GHA-")
        assert nid[-2] == "-"
