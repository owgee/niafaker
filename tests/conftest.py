"""Shared fixtures for NiaFaker tests."""

import pytest

from niafaker.providers import SUPPORTED_LOCALES


@pytest.fixture(params=SUPPORTED_LOCALES)
def locale(request: pytest.FixtureRequest) -> str:
    return request.param
