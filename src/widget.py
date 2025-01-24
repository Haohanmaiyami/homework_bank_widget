from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счёта в зависимости от входной строки.
    """
    if info.startswith("Счет"):
        # Работа с номером счёта
        account_number = info.split()[-1]  # Извлекаем номер счёта
        masked_account = get_mask_account(int(account_number))
        return f"Счет {masked_account}"
    else:
        # Работа с номером карты
        parts = info.rsplit(" ", 1)  # Разделяем строку на тип карты и номер
        card_type = parts[0]
        card_number = parts[1]
        masked_card = get_mask_card_number(int(card_number))
        return f"{card_type} {masked_card}"

from datetime import datetime

def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой из формата ISO 8601 в формат ДД.ММ.ГГГГ.
    """
    # Преобразуем строку в объект datetime
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    # Возвращаем строку в формате "ДД.ММ.ГГГГ"
    return dt.strftime("%d.%m.%Y")