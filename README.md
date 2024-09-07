# Банковский виджет

## Описание

Банковский виджет - виджет, который может:
* Маскировать номер карты или аккаунта пользователя и выводить дату операции;
* Сортировать операции по заданному ключу и дате.

Имеет функционал для тестирования кода

## Установка

1. Клонировать репозиторий
```
git clone https://github.com/VikVyaz/skypro_study_rep.git
```
2. Установка зависимостей
````
pip install -r requirements.txt
````

## Использование

Следуйте пункту ***Установка***
* Для маскировки номер карты или аккаунта пользователя и выводить дату операции, запустите `widget.py` в `src`
* Для сортировки операции по заданному ключу и дате, запустите `processing.py` в `src`
* Для тестирования пропишите в консоле (в виртуальном окружении) `pytest`,
а для вывода процента покрытия `pytest --cov`.

## Примеры работы с виджетом

При выполнении пункта ***Использование*** поэтапно покажутся строки с инструкциями для заполнения:

* `widget.py`:
    ````
    Введите данные(тип и номера счета/карты):
    ***
    Введите дату:
    ***
    ````
* `processing.py`:
    ````
    Введите данные(в виде списка словарей):
    ***
    Введите сортировочный ключ(если оставить поле пустым - по умолчанию EXECUTED):
    ***
    Отсортировать данные по дате по убыванию? (yes/no)
    ***
    ````
* Пример отчета о тестировании:
  * При вводе `pytest`
    ```
    ================ test session starts ================
    platform win32 -- Python 3.12.4, pytest-8.3.2, pluggy-1.5.0
    rootdir: C:\Users\***\PycharmProjects\pythonProject
    configfile: pyproject.toml
    plugins: cov-5.0.0
    collected 17 items                                   
  
    tests\test_masks.py .....                      [ 29%]
    tests\test_processing.py ...                   [ 47%]
    tests\test_widget.py .........                 [100%]
  
    ================ 17 passed in 0.05s =================
    ```
  * При вводе `pytest --cov`
    ````
    ================ test session starts ================
    platform win32 -- Python 3.12.4, pytest-8.3.2, pluggy-1.5.0
    rootdir: C:\Users\***\PycharmProjects\pythonProject
    configfile: pyproject.toml
    plugins: cov-5.0.0
    collected 17 items                                   

    tests\test_masks.py .....                      [ 29%] 
    tests\test_processing.py ...                   [ 47%]
    tests\test_widget.py .........                 [100%]
      
    ---------- coverage: platform win32, python 3.12.4-final-0 -----------
    Name                       Stmts   Miss  Cover        
    ----------------------------------------------        
    src\__init__.py                0      0   100%        
    src\masks.py                  23      9    61%        
    src\processing.py             37     11    70%        
    src\widget.py                 18      3    83%        
    tests\__init__.py              0      0   100%        
    tests\conftest.py             14      0   100%        
    tests\test_masks.py            9      0   100%        
    tests\test_processing.py      10      0   100%        
    tests\test_widget.py           7      0   100%        
    ----------------------------------------------        
    TOTAL                        118     23    81%        


    ================ 17 passed in 0.12s =================
    ````