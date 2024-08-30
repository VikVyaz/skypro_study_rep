from datetime import datetime
from widget import get_date


def filter_by_state(info: list, state="EXECUTED") -> list:
    """Функция сортировки по ключу state(по умолчанию - EXECUTED)"""

    final_dict = []
    for dicts_in_info in info:
        for key, value in dicts_in_info.items():
            if value == state:
                final_dict.append(dicts_in_info)

    return final_dict


def sort_by_date(info: list, reverse=True) -> list:
    """Функция сортировки по дате(по умолчанию - убывание)"""

    list_to_return = {}
    info_for_this_def = info
    for dictat in info_for_this_def:
        for key_1, value_1 in dictat.items():
            if key_1 == 'id':
                list_to_return[value_1] = dictat['date']
            if key_1 == 'date':
                dictat[key_1] = get_date(value_1)

    sorted_list = sorted(
        info_for_this_def,
        key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), reverse=reverse
    )

    for dictat in sorted_list:
        for key_2, value_2 in dictat.items():
            for key_3, value_3 in list_to_return.items():
                if value_2 == key_3:
                    dictat['date'] = list_to_return[key_3]

    return sorted_list


if __name__ == "__main__":
    input_data = input("Введите данные(в виде списка словарей):\n")
    input_state = input("Введите сортировочный ключ(если оставить поле пустым - по умолчанию EXECUTED):\n")
    input_reverse_date = input("Отсортировать данные по дате по убыванию? (yes/no)\n")

    true_data = eval(input_data)
    if input_state != "":
        correct_state = input_state.upper()
        print(f'Отсортированные данные по ключу:\n{filter_by_state(true_data, correct_state)}')
    else:
        print(f'Отсортированные данные по ключу:\n{filter_by_state(true_data)}')

    if input_reverse_date.lower() == 'no':
        print(f'Отсортированные данные по дате(по возрастанию):\n'
              f'{sort_by_date(true_data, reverse=False)}')
    else:
        print(f'Сортировка происходит по умолчанию(по убыванию):\n'
              f'{sort_by_date(true_data)}')
