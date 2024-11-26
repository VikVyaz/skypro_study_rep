from src.file_reader import to_read_a_file
from src.generators import filter_by_currency
from src.processing import sort_by_date
from src.search_and_count import to_sort_by_description
from src.widget import get_date, mask_account_card


def main() -> None:
    """Функция логики проекта и связи функциональности"""

    print('Добро пожаловать в программу работы с банковскими транзакциями.')

    file_type = to_choose_type_of_reading()
    path = f'./data/transactions.{file_type}'
    transactions = to_read_a_file(path)
    filtered_transaction = state_filtration(transactions)
    clear_transactions = to_clarify_the_sorting(filtered_transaction)

    if clear_transactions:
        print(
            'Распечатываю итоговый список транзакций...\n'
            f'Всего банковских операций в выборке: {len(clear_transactions)}\n')
        counter = input(
            'Укажите количество отображаемых транзакций(целое число):\n'
            '(0 или буквы - по умолчанию - все транзакции)\n'
        )

        if counter.isdigit():
            if int(counter) > 0:
                to_print_results(clear_transactions[:int(counter)])
            else:
                to_print_results(clear_transactions)
        else:
            print('Нужно ввести число')
    else:
        print('Не найдено ни одной транзакции,'
              'подходящей под ваши условия фильтрации')


def to_choose_type_of_reading() -> str:
    """Функция выбора формата файла с транзакциями"""

    file_types = ['json', 'csv', 'xlsx']

    while True:
        file_choice = input(
            'Выберите необходимый пункт меню:\n'
            '1. Получить информацию о транзакциях из JSON-файла\n'
            '2. Получить информацию о транзакциях из CSV-файла\n'
            '3. Получить информацию о транзакциях из XLSX-файла\n'
        )

        if file_choice not in ['1', '2', '3']:
            print('Ошибка. Надо выбрать из 3 вариантов\n')
        else:
            result = file_types[int(file_choice) - 1]
            print(f'Для обработки выбран {result.upper()}-файл\n')
            return result


def state_filtration(data: list) -> list:
    """Функция фильтрации по статусу:
    EXECUTED, CANCELED или PENDING"""

    while True:
        ask_state = input(
            'Введите статус, по которому необходимо выполнить фильтрацию\n'
            'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n'
        ).upper()
        if ask_state in ['EXECUTED', 'CANCELED', 'PENDING']:
            result = list(filter(lambda x: x['state'] == ask_state, data))
            return result
        else:
            print(f'Статус операции "{ask_state}" недоступен')


def to_clarify_the_sorting(data: list) -> list:
    """Функция уточнения для:
    - Сортировки по дате(по умолчанию - по возрастанию)
    - Вывод только РУБ транзакции
    - Фильтрация по определенному слову в описании"""

    # Сортировка по дате
    sort_needed = input(
        'Отсортировать операции по дате? Да/Нет\n'
    ).lower()

    result = data
    if sort_needed == 'да':
        sorting_method = input(
            'Отсортировать по возрастанию или по убыванию?\n'
        ).lower()

        if sorting_method == 'по возрастанию':
            result = sort_by_date(data)
        else:
            result = sort_by_date(data, True)
    # Сортировка по RUB
    only_rub = input(
        'Выводить только рублевые транзакции? Да/Нет\n'
    ).lower()

    if only_rub == 'да':
        result = filter_by_currency(result, "RUB")
    # Сортировка по слову в описании
    sort_by_description = input(
        'Отфильтровать список транзакций '
        'по определенному слову в описании? Да/Нет\n'
    ).lower()

    if sort_by_description == 'да':
        word_to_sort = input(
            'Введите слово:\n'
            'Например, "перевод" или "вклад"\n'
        )

        result = to_sort_by_description(result, word_to_sort)

    return result


def to_print_results(data: list) -> None:
    """Функция вывода результатов по шаблону:

    08.12.2019 Открытие вклада
    Счет **4321
    Сумма: 40542 руб.

    12.11.2019 Перевод с карты на карту
    MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
    Сумма: 130 USD
    """

    result = data
    for transaction in result:
        if 'вклад' in transaction['description'].lower():
            second_row = f'{mask_account_card(transaction['to'])}'
        else:
            second_row = (
                f'{mask_account_card(transaction['from'])}'
                ' -> '
                f'{mask_account_card(transaction['to'])}'
            )

        print(
            f'{get_date(transaction['date'])} {transaction['description']}\n'
            f'{second_row}\n'
            f'Сумма: {transaction['amount']} {transaction['currency_code']}\n'
        )


if __name__ == '__main__':
    main()
