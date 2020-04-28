from baza.baza import categories, questions_base
from random import choice, randint
import json, os
from user.user import Player


class Game:
    def __init__(self):
        self.name = "Millionaires"
        self.levels = [500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000]
        self.categories = categories
        self.rank = self.load_ranking()

    @staticmethod
    def load_ranking():
        file_path = os.path.join(os.path.dirname(__file__), "rank.json")
        with open(file_path) as file:
            rank = json.load(file)
        return rank

    def select_category(self):
        return choice(self.categories)

    def draw_question(self):
        category = self.select_category()
        number_question = randint(1, len(questions_base.loc[category, :]))
        return questions_base.loc[(category, number_question), "Question"]

    def add_result(self, user):
        self.rank[user.nick] = user.result













# game = Game()
# #print(game.draw_question())
# game.load_ranking()
# user = Player("tm")
# game.add_result(user)
# print(game.rank)