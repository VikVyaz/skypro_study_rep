from unittest import mock


from src.utils import get_finance_data


@mock.patch("src.utils.json.load")
@mock.patch("src.utils.open")
def test_get_finance_data(mock_open, mock_json_load):
    mock_json_load.return_value = [{"test": "test"}]
    assert get_finance_data("../data/operations.json") == [{"test": "test"}]

    mock_json_load.return_value = []
    assert get_finance_data("../data/operations.json") == []
