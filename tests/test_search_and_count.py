from src.search_and_count import to_count_categories, to_sort_by_description

test = [
    {'description': 'test'},
    {'description': 'tets'}
]

test_2 = [
    {'description': 'test'},
    {'description': 'tets'},
    {'description': 'test'},
    {'description': 'tets'}
]


def test_to_sort_by_description():
    assert to_sort_by_description(test, 'test') == [{'description': 'test'}]
    assert to_sort_by_description(test, 'tets') == [{'description': 'tets'}]


def test_to_count_categories():
    assert to_count_categories(
        test_2,
        ['test', 'tets']
    ) == {'test': 2, 'tets': 2}
