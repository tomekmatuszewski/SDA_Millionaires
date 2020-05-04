from millionaires.game import Game
from millionaires.user import Player
import pytest
import os


@pytest.fixture(name='game')
def setup():
    os.remove('/home/tm/PycharmProjects/Millionaires/baza/rank.json')
    return Game()


def test_init(game):
    assert game


def test_select_new_question(game):
    assert game.select_new_question("Nauka i Technika", 1)


def test_select_new_question1(game):
    game.select_new_question("Nauka i Technika", 1)
    assert game.select_new_question("Nauka i Technika", 2)


def test_select_new_question2(game):
    game.select_new_question("Nauka i Technika", 1)
    game.select_new_question("Nauka i Technika", 2)
    assert len(game.ans_in_game) == 2


@pytest.mark.parametrize("test_input1, test_input2, expected",
                         (("Nauka i Technika", 1, 2),
                          ("Nauka i Technika", 2, 2),
                          ("Historia", 3, 2),
                          ("Historia", 4, 2),
                          )
                             )
def test_hint(test_input1, test_input2, expected, game):
    cols = game.hint(test_input1, test_input2)
    assert len(cols) == expected


def test_check_number_of_hints(game):
    assert game.check_number_of_hints()


@pytest.mark.parametrize("category, number, answer",
                         (("Nauka i Technika", 1, 'A'),
                          ("Nauka i Technika", 2, 'C'),
                          ("Historia", 3, 'D'),
                          ("Historia", 4, 'C'),
                          )
                             )
def test_iscorrect_answer(game, category, number, answer):
    assert game.is_correct_answer(category, number, answer)


@pytest.mark.parametrize("category, number, answer",
                         (("Nauka i Technika", 1, 'A'),
                          ("Nauka i Technika", 2, 'C'),
                          ("Historia", 3, 'D'),
                          ("Historia", 4, 'C'),
                          )
                             )
def test_check_question(game, category, number, answer):
    assert game.check_question(category, number, answer)


def test_lost_game1(game):
    player = Player('user')
    game.lost_game(player)
    assert game.base.rank == {'user': '0 PLN'}


def test_lost_game2(game):
    player = Player('user')
    game.lost_game(player)
    player2 = Player('user2')
    game.player_acc = 100
    game.lost_game(player2)
    assert game.base.rank == {'user': '0 PLN', 'user2': '100 PLN'}


def test_player_cash(game):
    assert game.player_acc == 0


def test_player_cash2(game):
    game.counter = 2
    game.add_player_cash()
    assert game.player_acc == 2000


def test_win_million(game):
    player = Player("user")
    game.player_acc = 1000000
    game.win_million(player)
    game2 = Game()
    assert game2.base.rank == {"user": "1000000 PLN"}

