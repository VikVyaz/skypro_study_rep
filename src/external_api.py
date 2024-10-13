import os
import random
from typing import Union

from dotenv import load_dotenv
import requests
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
            return response.json()["result"]
        except requests.exceptions.RequestException:
            return 'Something goes wrong'


if __name__ == "__main__":
    pass
    # print(to_convert(get_finance_data("../data/operations.json")[random.randint(0, 10)]))
