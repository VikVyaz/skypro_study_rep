import logging
import typing


def log(log_name: str = "") -> typing.Any:
    """Декоратор логирования функций"""

    if not log_name:
        logging.basicConfig(level=logging.INFO,
                            filemode="w",
                            format="[%(asctime)s | %(levelname)s]: %(message)s")
    else:
        logging.basicConfig(level=logging.INFO,
                            filename=f"{log_name}",
                            filemode="w",
                            format="[%(asctime)s | %(levelname)s]: %(message)s")

    def log_decor(func: typing.Any) -> typing.Any:
        def log_this(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
            try:
                func(*args, **kwargs)
                logging.info(f"'{func.__name__}' ok")
            except Exception as e:
                logging.info(f"'{func.__name__}' error: {e}. Inputs: {*args, kwargs}")
                raise Exception("Error")

        return log_this

    return log_decor
