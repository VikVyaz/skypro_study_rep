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

    # Проверка того, что введены были цифры и номер карты состоит из 16 цифр
    if card_number_input.isdigit() and account_number_input.isdigit() and len(card_number_input) == 16:
        return [card_number_input, account_number_input]
    else:  # Вывод, относительно того, что именно неправильно ввелось
        if card_number_input.isdigit() and len(card_number_input) != 16:
            print("Некорректный ввод. Номер карты состоит из 16 цифр.\nПопробуем еще раз")
            get_user_input()
        else:
            print("Некорректный ввод. Введите цифрами.\nПопробуем еще раз")
            get_user_input()
    return [] # Заплатка, тк mypy ругался, что нет return.
    # Другие способы, которые приходили в голову, не убирали ошибку.


def print_the_masks(card_number: int, account_number: int) -> None:
    """Вывод замаскированных данных о карте и счете"""

    print(
        f"Замаскированный номер карты: {get_mask_card_number(card_number)}\n"
        f"Замаскированный номер счета: {get_mask_account(account_number)}"
    )


if __name__ == "__main__":  # В видео урока, комментах и на Хабре рекомендуют такую конструкцию
    CARD_AND_ACCOUNT_INFO = get_user_input()  # Добавление констант для последующего использования
    CARD_NUMBER = int(CARD_AND_ACCOUNT_INFO[0])
    ACCOUNT_NUMBER = int(CARD_AND_ACCOUNT_INFO[1])
    print_the_masks(CARD_NUMBER, ACCOUNT_NUMBER)
