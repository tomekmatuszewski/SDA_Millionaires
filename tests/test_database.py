import json
import os
import pytest
from millionaires.user import Player
from baza.baza import Database


@pytest.fixture(name="database")
def setup_database():
    database = Database()
    return database


def test_database():
    database = Database()
    assert database


def test_question_database_cols(database):
    exp_database_cols = ['ID', 'Question', 'A', 'B', 'C', 'D', 'Answer']
    assert list(database.questions_base.columns) == exp_database_cols


def test_question_database_index1(database):
    exp_database_index1 = ['Geografia', 'Historia', 'Nauka i Technika', 'Sport']
    assert sorted(list(set(database.questions_base.index.get_level_values(0)))) == exp_database_index1


def test_question_database_index2(database):
    exp_database_index2 = [1, 2, 3, 4, 5, 6]
    assert sorted(list(set(database.questions_base.index.get_level_values(1)))) == exp_database_index2


def test_categories(database):
    expected_categories = ['Geografia', 'Historia', 'Nauka i Technika', 'Sport']
    assert database.categories == expected_categories


def test_quantity_questions(database):
    expected_quantity = 21
    assert len(database.questions_base['ID']) == expected_quantity


def test_load_rank(database):
    assert isinstance(database.rank, dict)


def test_add_rank(database):
    if not os.path.exists(database.rank_path):
        player = Player('user')
        database.add_result_to_rank(player, 100)
        database1 = Database()
        exp_rank = {'user' : '100 PLN'}
        assert database1.rank == exp_rank
    pass


def test_rank_file():
    with open('/home/tm/PycharmProjects/Millionaires/baza/rank.json', "w") as file:
        json.dump({'tm': '100 PLN', 'az': '200 PLN', 'pz': '100 PLN'}, file)
    database2 = Database()
    assert database2.rank == {'tm': '100 PLN', 'az': '200 PLN', 'pz': '100 PLN'}
    assert isinstance(database2.rank, dict)






