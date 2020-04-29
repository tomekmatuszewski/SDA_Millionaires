from baza.baza import categories, questions_base
from random import choice, randint
import json, os
from user.user import Player, Admin
from millionaires.utils import *

counter = 0


class Game:
    def __init__(self):
        self.name = "Millionaires"
        self.levels = [500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000]
        self.categories = categories
        self.ans_in_game = []
        self.player = None
        self.fifty_fifty = 2
        self.rank_path = os.path.join(os.path.dirname(__file__), "rank.json")
        self.rank = self.load_ranking()
        print(repr(self))
        username = input("Enter [P] if you want to play [A] if you want to log as Admin: ")
        username = check_username(username)
        if username == "P":
            self.player = self.create_player()
        elif username == "A":
            self.admin = self.create_admin()
            if self.admin.authorization():
                self.admin.add_question()
        if self.player:
            self.play_game()

    def play_game(self):
        global counter
        while counter < len(self.levels):
            category = choice(self.categories)
            number_question = randint(1, len(questions_base.loc[category, :]))
            id_ans = questions_base.loc[(category, number_question), "ID"]
            if id_ans not in self.ans_in_game:
                print(f"\nRound {counter+1}! {self.levels[counter]} PLN to win.")
                print(f"Category: {category}")
                print(questions_base.loc[(category, number_question), "Question"])
                for column in questions_base[["A", "B", "C", "D"]]:
                    print(f"{column}: {questions_base.loc[(category, number_question), column]}")
                self.ans_in_game.append(id_ans)
                if self.fifty_fifty > 0:
                    hint = input(f"You have {self.fifty_fifty} hint{'s' if self.fifty_fifty == 2 else ''} "
                                 f"50/50 - do you want to use? [Y/N]: ")
                    hint = check_hint(hint)
                    if hint == "Y":
                        self.hint(category, number_question)
                        if self.check_question(category, number_question):
                            continue
                        self.lost_game()
                        break
                    elif hint == "N":
                        if self.check_question(category, number_question):
                            continue
                        self.lost_game()
                        break
                else:
                    if self.check_question(category, number_question):
                        continue
                    self.lost_game()
                    break
            else:
                continue
        self.add_result()

    def __repr__(self):
        return "Welcome in game Millionaires !!!"

    def add_result(self):
        self.rank[self.player.get_player_nick()] = f"{self.player.get_result()} PLN"
        with open(self.rank_path, "w+") as file_json:
            json.dump(self.rank, file_json)

    def load_ranking(self):
        with open(self.rank_path, "r") as file:
            rank = json.load(file)
        return rank

    def hint(self, category, number_question):
        cols_lst = []
        lst_col = list(questions_base[["A", "B", "C", "D"]].columns)
        for column in lst_col:
            if questions_base.loc[(category, number_question), column] == questions_base.loc[
                                                        (category, number_question), 'Answer']:
                print(f"\n{column}: {questions_base.loc[(category, number_question), column]}")
                cols_lst.append(column)
        while True:
            sec_col = choice(lst_col)
            if sec_col not in cols_lst:
                print(f"{sec_col}: {questions_base.loc[(category, number_question), sec_col]}")
                break
        self.fifty_fifty -= 1

    def check_question(self, category, number_question):
        global counter
        correct_answer = input("Select correct answer [A - D]: ")
        correct_answer = check_correct_answer(correct_answer)
        if questions_base.loc[(category, number_question), correct_answer] == questions_base.loc[
            (category, number_question), 'Answer']:
            print(f'Great, you won {self.levels[counter]} PLN!')
            self.player.add_cash(self.levels[counter])
            counter += 1
            return True
        return False

    def lost_game(self):
        self.add_result()
        print(f"You lost! Your score is {self.player.get_result()} PLN")

    @staticmethod
    def create_player():
        nick = input("Enter your nick (max 10 chars [a-Z, 0-9]): ")
        nick = check_player_nick(nick)
        return Player(nick)

    @staticmethod
    def create_admin():
        nick = input("Enter your nick: ")
        password = input("Enter your password: ")
        return Admin(nick, password)
