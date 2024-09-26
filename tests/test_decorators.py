import typing

import pytest

from src.decorators import log


@log("123")
def func() -> None:
    raise ZeroDivisionError("Error")


def test_log() -> None:
    with pytest.raises(Exception, match="Error"):
        func()


def test_console_log(capsys: typing.Any) -> None:
    @log("")
    def unit() -> None:
        print("123")

    unit()
    captured = capsys.readouterr()
    assert captured.out == "123\n"
