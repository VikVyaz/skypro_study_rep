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
                            filename=f"{log_name}.txt",
                            filemode="w",
                            format="[%(asctime)s | %(levelname)s]: %(message)s")

    def log_decor(func: typing.Any) -> typing.Any:
        def log_this() -> typing.Any:
            logging.info(f"Function '{func.__name__}' started")
            try:
                func()
                logging.info(f"Function '{func.__name__}' end with result: {func()}")
            except Exception:
                logging.exception("Function ended with error:\n", exc_info=True)

        return log_this

    return log_decor
