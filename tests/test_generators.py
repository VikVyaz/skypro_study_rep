import builtins
import random
import typing
from unittest import mock

import pytest

from src.generators import (card_number_generator, filter_by_currency, get_user_inputs, to_print_result,
                            transaction_descriptions)

usd_expected = [
    {
        "id": 3960261,
        "state": "EXECUTED",
        "date": "2020-04-12T17:56:59Z",
        "amount": 18611.0,
        "currency_name": "Dollar",
        "currency_code": "USD",
        "from": 0,
        "to": "Счет 05766968807462300151",
        "description": "Открытие вклада"
    }
]

rub_expected = [
    {
        "id": 4234093,
        "state": "EXECUTED",
        "date": "2021-07-08T07:31:21Z",
        "amount": 23182.0,
        "currency_name": "Ruble",
        "currency_code": "RUB",
        "from": "Visa 0773092093872450",
        "to": "Discover 8602781449570491",
        "description": "Перевод с карты на карту"
    }
]

transactions = [
    {
        "id": 4234093,
        "state": "EXECUTED",
        "date": "2021-07-08T07:31:21Z",
        "amount": 23182.0,
        "currency_name": "Ruble",
        "currency_code": "RUB",
        "from": "Visa 0773092093872450",
        "to": "Discover 8602781449570491",
        "description": "Перевод с карты на карту"
    },
    {
        "id": 3960261,
        "state": "EXECUTED",
        "date": "2020-04-12T17:56:59Z",
        "amount": 18611.0,
        "currency_name": "Dollar",
        "currency_code": "USD",
        "from": 0,
        "to": "Счет 05766968807462300151",
        "description": "Открытие вклада"
    }
]


@pytest.mark.parametrize("trans, code, expected", [
    (transactions, "USD", usd_expected),
    (transactions, "RUB", rub_expected),
    ([], "USD", "Транзакции отсутствуют"),
    (transactions, "RB", "Введена неизвестная валюта")
])
def test_filter_by_currency(trans: list, code: str, expected: list) -> None:
    generator = filter_by_currency(trans, code)
    for iteration in generator:
        assert iteration in expected


def test_transaction_descriptions(descriptions_expected: list) -> None:
    generator = transaction_descriptions(transactions)
    for iteration in generator:
        assert iteration in descriptions_expected


def test_card_number_generator(card_number_expected: list) -> None:
    random_start = random.randint(0, 5)
    random_stop = random.randint(6, 10)
    generator = card_number_generator(str(random_start), str(random_stop))
    for iteration in generator:
        assert iteration in card_number_expected


def test_get_user_inputs() -> None:
    """Тест get_user_inputs"""

    with mock.patch.object(builtins, 'input', lambda _: 'test'):
        assert get_user_inputs() == ["test", "test", "test", "test"]


def test_to_print_result(capsys: typing.Any) -> None:
    def generator() -> typing.Generator:
        for i in range(2):
            yield i

    to_print_result(generator())
    captured = capsys.readouterr()
    assert captured.out == "0\n1\n"
