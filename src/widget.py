from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(acc_and_numbers: str) -> str:
    """Функция маскировки типа и номера счета/карты"""

    numbers = ''
    letters = ''
    for symbol in acc_and_numbers:
        if symbol.isdigit():
            numbers += symbol
        else:
            letters += symbol

    if 'Счет' in acc_and_numbers:
        numbers = get_mask_account(int(numbers))
    else:
        numbers = get_mask_card_number(int(numbers))

    return f'{letters}{numbers}'


def get_date(date: str) -> str:
    """Функция расчета даты по вводу"""

    return f'{date[8:10]}.{date[5:7]}.{date[:4]}'


if __name__ == "__main__":
    acc_and_card_number_input = input("Введите данные:\n")
    date_input = input("Введите дату:\n")
    print(
        f'\nЗамаскированные данные:\n'
        f'{mask_account_card(acc_and_card_number_input)}\n'
        f'Дата:\n'
        f'{get_date(date_input)}'
    )
