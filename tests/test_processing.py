from src.processing import filter_by_state, sort_by_date


executed_test = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                 ]
canceled_test = [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                 ]
sorted_date_test = [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
                    ]


def test_filter_by_state_1(data_in_processing_py):
    """Тест сортировки по ключу EXECUTED"""

    assert filter_by_state(data_in_processing_py) == executed_test


def test_filter_by_state_2(data_in_processing_py):
    """Тест сортировки по ключу CANCELED"""

    assert filter_by_state(data_in_processing_py, state='CANCELED') == canceled_test


def test_sort_by_date(data_in_processing_py):
    """Тест сортировки по дате(по возрастанию)"""

    assert sort_by_date(data_in_processing_py) == sorted_date_test
