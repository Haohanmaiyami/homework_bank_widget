from typing import Dict, List


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Функция фильтрует транзакции"""
    return [transaction for transaction in transactions if transaction["state"] == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.
    descending - порядок сортировки (по умолчанию True - по убыванию)
    return - отсортированный список словарей
    """
    return sorted(data, key=lambda x: x['date'], reverse=descending)
