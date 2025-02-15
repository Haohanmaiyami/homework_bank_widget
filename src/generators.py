def filter_by_currency(transactions, currency_code):
    """Генерирует транзакции с указанной валютой."""
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and transaction["operationAmount"]["currency"]["code"] == currency_code
        ):
            yield transaction


def transaction_descriptions(transactions):
    """Генерирует описания операций из списка транзакций."""
    for transaction in transactions:
        yield transaction.get("description", "Нет описания")


def card_number_generator(start, stop):
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""
    for num in range(start, stop + 1):
        card_number = f"{num:016}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
