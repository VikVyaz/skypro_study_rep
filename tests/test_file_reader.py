import os.path
from unittest.mock import Mock

import pandas as pd

from src.file_reader import to_read_a_file

post_df = [
    {'A': 1, 'B': 4, 'C': 7},
    {'A': 2, 'B': 5, 'C': 8},
    {'A': 3, 'B': 6, 'C': 9}
]

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

file_not_found = 'Файл не найден или ошибка ввода. Повторите еще.'
format_error = 'Нужен JSON, CSV или Excel файл.'

csv_path = '../data/transactions.csv'
xlsx_path = '../data/transactions.xlsx'
wrong_path = 'anyway'


def test_if_true_csv() -> None:
    mock_true_read = Mock(return_value=True)
    os.path.isfile = mock_true_read
    mock_read_df = Mock(return_value=df)
    pd.read_csv = mock_read_df
    assert to_read_a_file(csv_path) == post_df


def test_if_true_xlsx() -> None:
    mock_true_read = Mock(return_value=True)
    os.path.isfile = mock_true_read
    mock_read_df = Mock(return_value=df)
    pd.read_excel = mock_read_df
    assert to_read_a_file(xlsx_path) == post_df


def test_format_error() -> None:
    mock_true_read = Mock(return_value=True)
    os.path.isfile = mock_true_read
    mock_read_df = Mock(return_value=df)
    pd.read_csv = mock_read_df
    assert to_read_a_file(wrong_path) == format_error


def test_if_false() -> None:
    mock_false_read = Mock(return_value=False)
    os.path.isfile = mock_false_read
    assert to_read_a_file(wrong_path) == file_not_found
