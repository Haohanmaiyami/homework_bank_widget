from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card  # Импорт из src/widget.py
from src.widget import get_date

if __name__ == "__main__":
    print(get_mask_account(7000792289606361))
    print(get_mask_card_number(7000792289606361))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    date_input = "2018-07-11T02:26:18.671407"
    formatted_date = get_date(date_input)
    print(formatted_date)  # Ожидаемый результат: "11.07.2018"
