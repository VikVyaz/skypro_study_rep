"""Тк все проверки на ввод были проделаны до вызовов функций,
в самом mask.py, return и тесты без проверок"""

import pytest


# Фикстуры для masks.py
@pytest.fixture
def card_number() -> int:
    """input-фикстура для test_get_mask_card_number"""

    return 7000792289606361


@pytest.fixture
def acc_number() -> int:
    """input-фикстура для test_get_mask_account"""

    return 73654108430135874305


# Фикстура для widget.py
@pytest.fixture
def date() -> str:
    """input-фикстура для test_get_date"""

    return "2024-03-11T02:26:18.671407"


# Фикстуры для processing.py
@pytest.fixture
def data_in_processing_py() -> list:
    """input-фикстура для test_filter_by_state и test_sort_by_date"""

    x = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
         ]
    return x


# Фикстуры для generators.py
@pytest.fixture
def descriptions_expected() -> list:
    """Фикстура для test_transaction_descriptions"""

    x = ['Перевод организации',
         'Перевод со счета на счет',
         'Перевод со счета на счет',
         'Перевод с карты на карту',
         'Перевод организации'
         ]
    return x


@pytest.fixture
def card_number_expected() -> list:
    """Фикстура для test_card_number_generator"""

    x = ['0000 0000 0000 0000',
         '0000 0000 0000 0001',
         '0000 0000 0000 0002',
         '0000 0000 0000 0003',
         '0000 0000 0000 0004',
         '0000 0000 0000 0005',
         '0000 0000 0000 0006',
         '0000 0000 0000 0007',
         '0000 0000 0000 0008',
         '0000 0000 0000 0009',
         '0000 0000 0000 0010'
         ]

    return x
