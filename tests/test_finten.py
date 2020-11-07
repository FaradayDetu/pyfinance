import pytest
from pifinance.finten import FinTen


def test_is_backend_reachable():

    finten = FinTen()
    assert finten._is_backend_reachable()

