from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card  # Импорт из src/widget.py

if __name__ == "__main__":
    print(get_mask_account(7000792289606361))
    print(get_mask_card_number(7000792289606361))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 35383033474447895560"))




