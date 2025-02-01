from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card  # Импорт из src/widget.py
from src.widget import get_date
from src.processing import filter_by_state, sort_by_date


if __name__ == '__main__':
    transactions = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
# Определяем переменные sorted_desc и sorted_asc
    sorted_desc = sort_by_date(transactions)  # Сортировка по убыванию
    sorted_asc = sort_by_date(transactions, descending=False)  # Сортировка по возрастанию


if __name__ == "__main__":
    print(get_mask_account(7000792289606361))
    print(get_mask_card_number(7000792289606361))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    date_input = "2018-07-11T02:26:18.671407"
    formatted_date = get_date(date_input)
    print(formatted_date)  # Ожидаемый результат: "11.07.2018"
    print(filter_by_state(transactions,  "EXECUTED"))
    print(filter_by_state(transactions,  "CANCELED"))
    print("Сортировка по убыванию:", sorted_desc)
    print("Сортировка по возрастанию:", sorted_asc)
