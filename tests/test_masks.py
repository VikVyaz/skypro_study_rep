import pytest
from src.masks import get_mask_card_number, get_mask_account, checking_the_input


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'


def test_get_mask_account(acc_number):
    assert get_mask_account(acc_number) == '**4305'


@pytest.mark.parametrize('data, expected', [
    (['7000792289606361', '73654108430135874305'], ['7000792289606361', '73654108430135874305']),
    (['700079228960636', '73654108430135874305'], []),
    (['onetwothree', '73654108430135874305'], [])
])
def test_checking_the_input(data, expected):
    assert checking_the_input(data) == expected
