import logging
import typing
from functools import wraps


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
        @wraps(func)
        def log_this(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
            try:
                if log_name:
                    logging.info(f"Function '{func.__name__}' complete successfully. Result: {func(*args, **kwargs)}")
                    return func(*args, **kwargs)
                else:
                    logging.info(f"Function '{func.__name__}' complete successfully. Result:")
                    return func(*args, **kwargs)
            except Exception as e:
                logging.info(f"'{func.__name__}' error: {e}. Inputs: {*args, kwargs}")
                raise Exception("Error")

        return log_this

    return log_decor
