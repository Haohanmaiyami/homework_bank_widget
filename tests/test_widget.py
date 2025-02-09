import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "info,expected",
    [
        ("Счет 12345678", "Счет **5678"),
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
    ],
)
def test_mask_account_card(info, expected):
    assert mask_account_card(info) == expected


@pytest.mark.parametrize(
    "date_str,expected",
    [
        ("2025-02-01T12:00:00.000", "01.02.2025"),
        ("2025-12-31T23:59:59.999", "31.12.2025"),
    ],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
