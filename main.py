from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card  # Импорт из src/widget.py
from src.widget import get_date

if __name__ == "__main__":
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    # Определяем переменные sorted_desc и sorted_asc
    sorted_desc = sort_by_date(transactions)  # Сортировка по убыванию
    sorted_asc = sort_by_date(
        transactions, descending=False
    )  # Сортировка по возрастанию


if __name__ == "__main__":
    print(get_mask_account(7000792289606361))
    print(get_mask_card_number(7000792289606361))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    date_input = "2018-07-11T02:26:18.671407"
    formatted_date = get_date(date_input)
    print(formatted_date)  # Ожидаемый результат: "11.07.2018"
    print(filter_by_state(transactions, "EXECUTED"))
    print(filter_by_state(transactions, "CANCELED"))
    print("\nСортировка по убыванию:", sorted_desc)
    print("\nСортировка по возрастанию:", sorted_asc)

# Тестовые данные (как в фикстуре sample_transactions)
sample_transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}},
    {"operationAmount": {"currency": {"code": "EUR"}}},
    {"operationAmount": {"currency": {"code": "USD"}}},
    {"operationAmount": {}},  # Транзакция без валюты
    {},  # Пустой словарь
]


# Фильтруем транзакции по "USD"
filtered_transactions = list(filter_by_currency(sample_transactions, "USD"))

# 📌 Выводим результат в консоль
print("\nОтфильтрованные транзакции (USD):")
for tx in filtered_transactions:
    print(tx)

# Проверка: если передан пустой список (ожидаем [])
print("\nФильтр для пустого списка:", list(filter_by_currency([], "USD")))

# Проверка: если в транзакциях нет нужной валюты (ожидаем [])
print("\nФильтр для валюты GBP:", list(filter_by_currency(sample_transactions, "GBP")))

# Тестовые данные
transactions = [
    {"description": "Перевод со счета на счет"},
    {"description": "Оплата услуг"},
    {},  # Транзакция без description
]

# Запускаем генератор
descriptions = transaction_descriptions(transactions)

# Выводим все описания
print("\nОписания транзакций:")
for desc in descriptions:
    print(desc)

# Передаем пустой список транзакций
empty_transactions: list = []

# Запускаем генератор
descriptions = transaction_descriptions(empty_transactions)

# Преобразуем генератор в список и печатаем результат
print("\nОписания для пустого списка транзакций:", list(descriptions))


# Проверка генерации одного номера (1234)
print("\nОдин номер карты:")
print(next(card_number_generator(1234, 1234)))  # Ожидаем "0000 0000 0000 1234"

# Проверка генерации нескольких номеров (1-3)
print("\nГенерация номеров от 1 до 3:")
for card in card_number_generator(1, 3):
    print(
        card
    )  # Ожидаем "0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"

# Проверка перехода через 10000
print("\nГенерация номеров от 9999 до 10000:")
for card in card_number_generator(9999, 10000):
    print(card)  # Ожидаем "0000 0000 0000 9999", "0000 0000 0001 0000"
