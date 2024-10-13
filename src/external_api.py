import os
import random
from typing import Union

import requests
from dotenv import load_dotenv

from src.utils import get_finance_data

load_dotenv()


def to_convert(transaction: dict) -> Union[float, str]:
    """Функция вывода суммы транзакции в RUB
    При необходимости - конвертация из USD и EUR"""

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        amount = float(transaction["operationAmount"]["amount"])
        code = transaction["operationAmount"]["currency"]["code"]
        url = "https://api.apilayer.com/exchangerates_data/convert"
        api_key = os.getenv("API_KEY")
        payload = {
            "amount": f"{amount}",
            "from": f"{code}",
            "to": "RUB"
        }
        headers = {
            "apikey": f"{api_key}"
        }
        try:
            response = requests.get(url, headers=headers, params=payload)
            return float(response.json()["result"])
        except requests.exceptions.RequestException:
            return 'Something goes wrong'


if __name__ == "__main__":
    file_name = "../data/operations.json"
    print(to_convert(get_finance_data(file_name)[random.randint(0, 10)]))
