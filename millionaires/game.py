from baza.baza import Database
from random import choice, randint, shuffle
import json
from millionaires.utils import *


class Game:

    counter = 0

    def __init__(self):
        self.name = "Millionaires"
        self.levels = [500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000]
        self.base = Database()
        self.ans_in_game = []
        self.max_number_hints = 2
        self.player_acc = 0
    
    def play_game(self, player):
        while self.counter < len(self.levels):
            category = choice(self.base.categories)
            number_question = randint(1, len(self.base.questions_base.loc[category, :]))
            if self.select_new_question(category, number_question):
                print(f"\nRound {self.counter + 1}! {self.levels[self.counter]} PLN to win.")
                print(f"Category: {category}")
                print(self.base.questions_base.loc[(category, number_question), "Question"])
                for column in self.base.questions_base[["A", "B", "C", "D"]]:
                    print(f"{column}: {self.base.questions_base.loc[(category, number_question), column]}")
                if self.max_number_hints > 0:
                    hint = check_hint(input(f"You have {self.max_number_hints} hint{'s' if self.max_number_hints == 2 else ''} "
                                 f"50/50 - do you want to use? [Y/N]: "))
                    if hint == "Y":
                        self.print_hint(self.hint(category, number_question), category, number_question)
                        correct_answer = check_correct_answer(input("Select correct answer [A - D]: "))
                        if self.check_question(category, number_question, correct_answer):
                            print(f'Great, you won {self.levels[self.counter]} PLN!')
                            continue
                        self.lost_game(player)
                        print(f"You lost! Your score is {player.get_result} PLN")
                        break
                    elif hint == "N":
                        correct_answer = check_correct_answer(input("Select correct answer [A - D]: "))
                        if self.check_question(category, number_question, correct_answer):
                            print(f'Great, you won {self.levels[self.counter]} PLN!')
                            continue
                        self.lost_game(player)
                        print(f"You lost! Your score is {player.get_result} PLN")
                        break
                else:
                    correct_answer = check_correct_answer(input("Select correct answer [A - D]: "))
                    if self.check_question(category, number_question, correct_answer):
                        print(f'Great, you won {self.levels[self.counter]} PLN!')
                        continue
                    self.lost_game(player)
                    print(f"You lost! Your score is {player.get_result} PLN")
                    break
            else:
                continue
        self.base.add_result_to_rank(player, self.player_acc)

    def __repr__(self):
        return f"Welcome in game {self.name} !!!"

    def select_new_question(self, category, number_question):
        id_ans = self.base.questions_base.loc[(category, number_question), "ID"]
        if id_ans not in self.ans_in_game:
            self.ans_in_game.append(id_ans)
            return True
        return False

    def hint(self, category, number_question):
        cols_lst = []
        lst_col = list(self.base.questions_base[["A", "B", "C", "D"]].columns)
        for column in lst_col:
            if self.is_correct_answer(category, number_question, column):
                cols_lst.append(column)
        while True:
            sec_col = choice(lst_col)
            if sec_col not in cols_lst:
                cols_lst.append(sec_col)
                break
        self.max_number_hints -= 1
        shuffle(cols_lst)
        return cols_lst

    def print_hint(self, cols, category, number_question):
        print("\n")
        for col in cols:
            print(f"{col}: {self.base.questions_base.loc[(category, number_question), col]}")

    def check_question(self, category, number_question, answer):
        if self.is_correct_answer(category, number_question, answer):
            self.add_player_cash()
            self.counter += 1
            return True
        return False

    def is_correct_answer(self, category, number_question, answer):
        if self.base.questions_base.loc[(category, number_question), answer] == self.base.questions_base.loc[
            (category, number_question), 'Answer']:
            return True
        return False

    def lost_game(self, player):
        self.base.add_result_to_rank(player, self.player_acc)

    def add_player_cash(self):
        self.player_acc = self.levels[self.counter]


if __name__ == '__main__':
    pass