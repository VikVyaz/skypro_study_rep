import os.path
from typing import Any

import pandas as pd


def to_read_a_file(path: str) -> Any:
    """Функция для считывания CSV и Excel файлов"""

    if os.path.isfile(f'../{path}'):
        if '.csv' in path.lower():
            csv_df = pd.read_csv(f'../{path}', delimiter=';')
            return csv_df.to_dict('records')
        elif '.xlsx' in path.lower():
            xlsx_df = pd.read_excel(f'../{path}')
            return xlsx_df.to_dict('records')
        else:
            return 'Неверный формат. Нужен CSV или Excel файл.'

    else:
        return 'Файл не найден или ошибка ввода. Повторите еще.'


if __name__ == "__main__":
    # x = 'data/transactions.csv'
    file_path = input('Введите путь к файлу формата "<Папка>/<Имя файла>":\n')
    print(to_read_a_file(file_path))
