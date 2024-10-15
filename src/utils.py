import json
import logging
import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s | File: %(filename)s | %(levelname)s | Message: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=os.path.join(basedir, 'logs/utils.log'),
                    filemode='w',
                    encoding='utf-8')

utils_logger = logging.getLogger("utils_logger")


def get_finance_data(source: str) -> list:
    """Извлечение данных из .json файла.
    Аргумент функции - ссылка формата:
    ../data/operations.json"""

    utils_logger.info('Извлечение json-данных...')
    try:
        with open(f'{source}', encoding='utf-8') as f:
            transactions_data = json.load(f)
            if isinstance(transactions_data, list) and transactions_data:
                utils_logger.info(f'Извлечено успешно в {source}')
                return transactions_data
            else:
                raise FileNotFoundError
    except FileNotFoundError:
        utils_logger.error('Ошибка')
        return []


if __name__ == "__main__":
    file_name = "../data/operations.json"
    print(get_finance_data(file_name))
