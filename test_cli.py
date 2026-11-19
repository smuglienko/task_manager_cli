import pytest
from cli import main


def test_add_command_prints_title(capsys: pytest.CaptureFixture[str]) -> None:
    main(args=["add", "Купить хлеб"])
    captured = capsys.readouterr()
    assert captured.out == "[ ] Купить хлеб\n"


def test_unknown_command_prints_error(capsys: pytest.CaptureFixture[str]) -> None:
    main(args=["delete", "Купить хлеб"])
    captured = capsys.readouterr()
    assert captured.out == "Неизвестная команда\n"


def test_missing_title(capsys: pytest.CaptureFixture[str]) -> None:
    main(args=["add"])
    captured = capsys.readouterr()
    assert captured.out == "Укажите команду и название задачи\n"


def test_blank_title_prints_error(capsys: pytest.CaptureFixture[str]) -> None:
    main(args=["add", " "])
    captured = capsys.readouterr()
    assert captured.out == "Название задачи не должно быть пустым\n"
