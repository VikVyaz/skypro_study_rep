import typing


def filter_by_currency(transactions: list, code: str) -> typing.Any:
    """Генератор вывода транзакция по code"""

    filter_transaction = [i for i in transactions if i['operationAmount']['currency']['code'] == code]
    for i in range(len(filter_transaction)):
        yield filter_transaction[i]


def transaction_descriptions(transactions: list) -> typing.Any:
    """Генератор вывода описаний к транзакциям"""

    descriptions = [value for i in transactions for key, value in i.items() if key == 'description']
    for i in range(len(descriptions)):
        yield descriptions[i]


if __name__ == "__main__":
    transactions_input = "([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}, {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}, {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}, {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}])"
    # input("Введите транзакции: "))
    code_input = "USD"
    # input("Введите валюту(USD или RUB): "))
    transactions_list = eval(transactions_input)
    if code_input in ["USD", "RUB"]:
        filter_gen = filter_by_currency(transactions_list, code_input)
        for i1 in range(len([i for i in transactions_list if i['operationAmount']['currency']['code'] == code_input])):
            print(next(filter_gen))
        func = transaction_descriptions(transactions_list)
        for i2 in range(len([value for i in transactions_list for key, value in i.items() if key == 'description'])):
            print(next(func))
    else:
        print("Введите корректную валюту")
