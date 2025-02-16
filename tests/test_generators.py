import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


@pytest.fixture
def sample_transactions():
    return [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {}},  # Транзакция без валюты
        {},  # Пустой словарь
    ]


def test_filter_by_currency(sample_transactions):
    filtered = list(filter_by_currency(sample_transactions, "USD"))
    assert len(filtered) == 2
    assert all("operationAmount" in tx for tx in filtered)
    assert all("currency" in tx["operationAmount"] for tx in filtered)
    assert all(tx["operationAmount"]["currency"]["code"] == "USD" for tx in filtered)


def test_filter_by_currency_empty():
    assert list(filter_by_currency([], "USD")) == []


def test_filter_by_currency_no_matching(sample_transactions):
    assert list(filter_by_currency(sample_transactions, "GBP")) == []


def test_transaction_descriptions():
    transactions = [
        {"description": "Перевод со счета на счет"},
        {"description": "Оплата услуг"},
    ]
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Оплата услуг"


def test_transaction_descriptions_with_missing_description():
    transactions = [
        {"description": "Перевод со счета на счет"},
        {"description": "Оплата услуг"},
        {},  # Пустая транзакция без description
    ]
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Оплата услуг"
    assert next(generator) == "Нет описания"


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


def test_card_number_generator():
    cards = list(card_number_generator(1, 3))
    assert cards == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


def test_card_number_generator_format():
    card = next(card_number_generator(1234, 1234))
    assert card == "0000 0000 0000 1234"


@pytest.mark.parametrize(
    "start, stop, expected_cards",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (1234, 1234, ["0000 0000 0000 1234"]),
        (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
    ],
)
def test_card_number_generator_parametrized(start, stop, expected_cards):
    generated_cards = list(card_number_generator(start, stop))
    assert generated_cards == expected_cards
