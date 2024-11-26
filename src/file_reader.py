import json
import os.path
from typing import Any

import pandas as pd


def to_read_a_file(path: str) -> Any:
    """Функция для считывания JSON, CSV и XLSX файлов"""

    if os.path.isfile(path):
        if '.json' in path:
            with open(path, encoding='utf-8') as f:
                data = json.load(f)
            return data
        elif '.csv' in path:
            df = pd.read_csv(path, delimiter=';')
        elif '.xlsx' in path:
            df = pd.read_excel(path)
        else:
            return 'Нужен JSON, CSV или Excel файл.'

        df = df.astype('object')
        df.fillna("", inplace=True)
        result = df.to_dict('records')

        for transaction in result:
            for key, value in transaction.items():
                if key == 'id' and value:
                    transaction[key] = int(value)

        return result

    else:
        return 'Файл не найден или ошибка ввода. Повторите еще.'


if __name__ == "__main__":
    file_path = '../data/transactions.csv'
    # file_path = 'data/transactions.xlsx'
    # file_path = input('Введите путь к файлу формата "<Папка>/<Имя файла>":\n')
    print(to_read_a_file(file_path))
