from unittest.mock import patch

from src.external_api import to_convert


rub_dict = {
    "operationAmount": {
      "amount": "1.2",
      "currency": {
        "code": "RUB"
      }
    }
}

usd_dict = {
    "operationAmount": {
      "amount": "2.1",
      "currency": {
        "code": "USD"
      }
    }
}


@patch('requests.get')
def test_to_convert(mock_get: dict) -> None:
    mock_get.return_value.json.return_value = {"result": "test"}
    assert to_convert(rub_dict) == 1.2
    assert to_convert(usd_dict) == "test"
