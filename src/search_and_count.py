import re
from collections import Counter

from src.file_reader import to_read_a_file


def to_sort_by_description(data: list, target: str) -> list:
    """Функция фильтрации транзакция по строке поиска в описании транзакции"""

    pattern = re.compile(target, flags=re.IGNORECASE)
    result = [
        transaction
        for transaction in data
        if pattern.search(transaction['description'])
    ]

    return result


def to_count_categories(data: list, categories: list) -> dict:
    """Функция подсчета количества транзакций по категориям"""

    list_of_categories = []
    for category in categories:
        one_category_list = [
            transaction['description']
            for transaction in data
            if category in transaction['description'].lower()
        ]
        list_of_categories.extend(one_category_list)

    result = Counter(list_of_categories)

    return dict(result)


if __name__ == '__main__':
    print(to_sort_by_description(to_read_a_file('data/transactions.csv'), 'перевод'))
    print(to_count_categories(to_read_a_file('data/transactions.csv'), ['перевод']))
