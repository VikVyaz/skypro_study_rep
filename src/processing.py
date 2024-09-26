from datetime import datetime

from src.widget import get_date


def filter_by_state(info: list, state: str = "EXECUTED") -> list:
    """Функция сортировки по ключу state(по умолчанию - EXECUTED)"""

    final_dict = []
    for dicts_in_info in info:
        for key, value in dicts_in_info.items():
            if value == state:
                final_dict.append(dicts_in_info)

    return final_dict


def sort_by_date(info: list, reverse: bool = False) -> list:
    """Функция сортировки по дате(по умолчанию - возрастанию)"""

    list_to_return = {}
    info_for_this_def = info
    for dictat in info_for_this_def:
        for id_or_date, value_of_id_or_date in dictat.items():
            if id_or_date == 'id':
                list_to_return[value_of_id_or_date] = dictat['date']
            if id_or_date == 'date':
                dictat[id_or_date] = get_date(value_of_id_or_date)

    sorted_list = sorted(
        info_for_this_def,
        key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), reverse=reverse
    )

    for dictat in sorted_list:
        for sorted_key, sorted_value in dictat.items():
            for key_to_return, value_to_return in list_to_return.items():
                if sorted_value == key_to_return:
                    dictat['date'] = list_to_return[key_to_return]

    return sorted_list


def get_user_input() -> list:
    """Пользовательский ввод"""

    input_data = input("Введите данные(в виде списка словарей):\n")
    input_state = input("Введите сортировочный ключ(если оставить поле пустым - по умолчанию EXECUTED):\n")
    input_reverse_date = input("Отсортировать данные по дате по возрастанию? (yes/no)\n")

    return [input_data, input_state, input_reverse_date]


if __name__ == "__main__":
    incoming_data = get_user_input()

    true_data = eval(incoming_data[0])  # str -> list with dict
    if incoming_data[1] != "":
        correct_state = incoming_data[1].upper()
        print(f'Отсортированные данные по ключу:\n{filter_by_state(true_data, correct_state)}')
    else:
        print(f'Отсортированные данные по ключу:\n{filter_by_state(true_data)}')

    # Проверка для reverse
    if incoming_data[2].lower() == 'no':
        print(f'Отсортированные данные по дате(по убыванию):\n'
              f'{sort_by_date(true_data, reverse=True)}')
    else:
        print(f'Сортировка происходит по умолчанию(по возрастанию):\n'
              f'{sort_by_date(true_data)}')
