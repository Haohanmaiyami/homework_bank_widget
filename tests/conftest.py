import pytest


@pytest.fixture
def sample_transactions():
    return [
        {"state": "EXECUTED", "date": "2025-02-01"},
        {"state": "PENDING", "date": "2025-01-01"},
        {"state": "EXECUTED", "date": "2025-02-05"},
    ]


@pytest.fixture
def sample_card_numbers():
    return [1234567812345678, 9876543212345678]


@pytest.fixture
def sample_account_numbers():
    return [12345678, 987654321]
