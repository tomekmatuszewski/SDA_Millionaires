from baza.baza import categories, questions_base
from random import choice, randint
import json, os
from user.user import Player, Admin


class Game:
    def __init__(self):
        self.name = "Millionaires"
        self.levels = [500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000]
        self.categories = categories
        self.ans_in_game = []
        self.fifty_fifty = 2
        self.rank_path = os.path.join(os.path.dirname(__file__), "rank.json")
        self.rank = self.load_ranking()
        repr(self)
        choice = input("Enter [P] if you want to play [A] if you want to log as Admin: ")
        if choice == "P":
            self.player = self.create_player()
        elif choice == "A":
            self.admin = self.create_admin()
            self.admin.authorization()
            self.admin.add_question()
        if self.player:
            self.play_game()

    def play_game(self):
        counter = 0
        while counter < len(self.levels):
            category = self.select_category()
            number_question = randint(1, len(questions_base.loc[category, :]))
            id_ans = questions_base.loc[(category, number_question), "ID"]
            if not id_ans in self.ans_in_game:
                print(questions_base.loc[(category, number_question), "Question"])
                for column in questions_base[["A", "B", "C", "D"]]:
                    print(f"{column}: {questions_base.loc[(category, number_question), column]}")
                self.ans_in_game.append(id_ans)
                if self.fifty_fifty > 0:
                    hint = input(f"You have {self.fifty_fifty} hints 50/50 - do you want to use? [Y/N] ")
                    if hint == "Y":
                        self.hint(category, number_question)
                        correct_answer = input("Select correct answer: ")
                        if questions_base.loc[(category, number_question), correct_answer] == questions_base.loc[
                            (category, number_question), 'Answer']:
                            print(f'Great, you won {self.levels[counter]} PLN!')
                            self.player.add_cash(self.levels[counter])
                            counter += 1
                            continue
                        else:
                            self.add_result()
                            print(f"You lost! Your score is {self.player.get_result()} PLN")
                            self.add_result()
                            break
                    elif hint == "N":
                        correct_answer = input("Select correct answer [A - D]: ")
                        if questions_base.loc[(category, number_question), correct_answer] == questions_base.loc[(category, number_question), 'Answer']:
                            print(f'Great, you won {self.levels[counter]} PLN!')
                            self.player.add_cash(self.levels[counter])
                            counter += 1
                            continue
                        else:
                            self.add_result()
                            print(f"You lost! Your score is {self.player.get_result()} PLN")
                            self.add_result()
                            break
                else:
                    correct_answer = input("Select correct answer [A - D]: ")
                    if questions_base.loc[(category, number_question), correct_answer] == questions_base.loc[
                        (category, number_question), 'Answer']:
                        print(f'Great, you won {self.levels[counter]} PLN!')
                        self.player.add_cash(self.levels[counter])
                        counter += 1
                        continue
                    else:
                        self.add_result()
                        print(f"You lost! Your score is {self.player.get_result()} PLN")
                        self.add_result()
                        break
            else:
                continue

    def __repr__(self):
        return "Welcome in game Millionaires !!!"

    def select_category(self):
        category = choice(self.categories)
        print(f"\nCategory: {category}")
        return category

    def add_result(self):
        self.rank[self.player.get_player_nick()] = self.player.get_result()
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
            if questions_base.loc[(category, number_question), column] == questions_base.loc[(category, number_question), 'Answer']:
                print(f"{column}: {questions_base.loc[(category, number_question), column]}")
                cols_lst.append(column)
        while True:
            sec_col = choice(lst_col)
            if sec_col not in cols_lst:
                print(f"{sec_col}: {questions_base.loc[(category, number_question), sec_col]}")
                break
        self.fifty_fifty -= 1


    @staticmethod
    def create_player():
        nick = input("Enter your nick: ")
        return Player(nick)

    @staticmethod
    def create_admin():
        nick = input("Enter your nick: ")
        password = input("Enter your password: ")
        return Admin(nick, password)



