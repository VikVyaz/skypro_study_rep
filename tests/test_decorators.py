import pytest

from src.decorators import log


@log("123")
def func():
    raise ZeroDivisionError


def test_log() -> None:
    with pytest.raises(Exception, match="Error"):
        func()


def test_console_log(capsys):
    @log("")
    def unit():
        print("123")

    unit()
    captured = capsys.readouterr()
    assert captured.out == "123\n"
