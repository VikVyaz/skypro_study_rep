def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""

    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""

    return f"**{str(account_number)[-4:]}"


def get_user_input() -> list:
    """Получение данных от пользователя"""

    card_number_input = input("Введите номер карты(16 цифр):\n")
    account_number_input = input("Введите номер счета(цифрами):\n")

    return [card_number_input, account_number_input]


def checking_the_input(check_list: list) -> list:
    """Проверка введенных данных"""

    if check_list[0].isdigit() and check_list[1].isdigit() and len(check_list[0]) == 16:
        return check_list
    elif check_list[0].isdigit() and len(check_list[0]) != 16:
        print(
            "Некорректный ввод. Номер карты состоит из 16 цифр."
        )
    else:
        print(
            "Некорректный ввод. Введите цифрами."
        )
    return []  # Заплатка, тк mypy ругался, что нет return.
    # Другие способы, которые приходили в голову, не убирали ошибку.


def print_the_masks(card_number: int, account_number: int) -> None:
    """Вывод замаскированных данных о карте и счете"""

    print(
        f"Замаскированный номер карты: {get_mask_card_number(card_number)}\n"
        f"Замаскированный номер счета: {get_mask_account(account_number)}"
    )


if __name__ == "__main__":  # В видео урока, комментах и на Хабре рекомендуют такую конструкцию
    CARD_AND_ACCOUNT_INFO = checking_the_input(get_user_input())
    if CARD_AND_ACCOUNT_INFO:
        CARD_NUMBER = int(CARD_AND_ACCOUNT_INFO[0])
        ACCOUNT_NUMBER = int(CARD_AND_ACCOUNT_INFO[1])
        print_the_masks(CARD_NUMBER, ACCOUNT_NUMBER)
