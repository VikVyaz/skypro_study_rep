def filter_by_state(info: list, state="EXECUTED") -> list:
    """Функция сортировки по ключу state(по умолчанию - EXECUTED)"""

    final_dict = []
    for dicts_in_info in info:
        for key, value in dicts_in_info.items():
            if value == state:
                final_dict.append(dicts_in_info)

    return final_dict


def sort_by_date(input_):
    """Функция сортировки по дате(по умолчанию - убывание)"""

    pass


if __name__ == "__main__":
    input_data = input("Введите данные(в виде списка словарей):\n")
    input_state = input("Введите сортировочный ключ(если оставить поле пустым - по умолчанию EXECUTED):\n")
    true_data = eval(input_data)
    if input_state != "":
        correct_state = input_state.upper()
        print(f'Отсортированные по ключу данные: {filter_by_state(true_data, correct_state)}')
    else:
        print(f'Отсортированные по ключу данные: {filter_by_state(true_data)}')
