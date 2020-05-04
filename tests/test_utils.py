import pytest

from millionaires.utils import *


def test_check_username():
    username = "A"
    assert check_username(username) == "A"


def test_check_username1():
    username = "P"
    assert check_username(username) == "P"


@pytest.mark.parametrize(
    "test_input,expected",
    [("tm", "tm"), ("nick1", "nick1"), ("username12", "username12")],
)
def test_nick(test_input, expected):
    assert check_player_nick(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("C", "C"), ("S", "S"),])
def test_choice(test_input, expected):
    assert check_user_choice(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("Y", "Y"), ("N", "N"),])
def test_chooser(test_input, expected):
    assert check_chooser(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("Y", "Y"), ("N", "N"),])
def test_hint(test_input, expected):
    assert check_hint(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected", [("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")]
)
def test_answer(test_input, expected):
    assert check_correct_answer(test_input) == expected


def test_check_id1():
    assert check_id(77) == 77
