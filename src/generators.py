import typing


def filter_by_currency(transactions: list, code: str) -> typing.Generator:
    """Генератор вывода транзакция по code"""

    if transactions:
        if code in ["USD", "RUB"]:
            filter_transaction = [i for i in transactions if i['operationAmount']['currency']['code'] == code]
            if filter_transaction:
                for i in range(len(filter_transaction)):
                    yield filter_transaction[i]
            else:
                yield f"Транзакции по {code} отсутствуют"
        else:
            yield "Введена неизвестная валюта"
    else:
        yield "Транзакции отсутствуют"


def transaction_descriptions(transactions: list) -> typing.Generator:
    """Генератор вывода описаний к транзакциям"""

    descriptions = [value for i in transactions for key, value in i.items() if key == 'description']
    for i in range(len(descriptions)):
        yield descriptions[i]


def card_number_generator(start: str, stop: str) -> typing.Generator:
    """Функция генератора номеров карт"""

    if start.isdigit() and stop.isdigit():
        if start == "":
            start = "1"
        if stop == "":
            stop = "9999999999999999"

        start_number = '0000000000000000'
        result = []
        start_list = list(start_number)
        for i in range(int(stop) - int(start) + 1):
            y_1 = int(start) + i
            start_list[-len(str(y_1)):] = str(y_1)
            z = ''.join(start_list)
            result.append(f"{z[:4]} {z[4:8]} {z[8:12]} {z[12:]}")

        for i in range(len(result)):
            yield result[i]
    else:
        yield 'Введите корректные данные'


def to_print_result(func: typing.Generator) -> None:
    """Функция вывода"""

    for value in func:
        print(value)


if __name__ == "__main__":
    transactions_input = input("Введите транзакции: \n")
    code_input = input("Введите валюту(USD или RUB): \n")
    card_num_start_input = input(
        "Генерация номера карты."
        "Укажите начальные цифры(целое число, по умолчанию 0000 0000 0000 0001): \n"
    )
    card_num_stop_input = input(
        "И конечные цифры(целое число, по умолчанию 9999 9999 9999 9999): \n"
    )

    transactions_list = eval(transactions_input)

    filter_gen = filter_by_currency(transactions_list, code_input)
    to_print_result(filter_gen)

    description_func = transaction_descriptions(transactions_list)
    to_print_result(description_func)

    card_num_gen = card_number_generator(card_num_start_input, card_num_stop_input)
    to_print_result(card_num_gen)
