import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number,expected",
    [
        (1234567812345678, "1234 56** **** 5678"),
        (9876543212345678, "9876 54** **** 5678"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number,expected", [(12345678, "**5678"), (987654321, "**4321")]
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
