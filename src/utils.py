import json


def get_finance_data(source: str) -> list:
    """Извлечение данных из .json файла.
    Аргумент функции - ссылка формата:
    ../data/operations.json"""

    try:
        with open(f"{source}", encoding='utf-8') as f:
            transactions_data = json.load(f)
            if isinstance(transactions_data, list) and transactions_data:
                return transactions_data
            else:
                raise FileNotFoundError
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    pass
    # print(get_finance_data("../data/operations.json"))
