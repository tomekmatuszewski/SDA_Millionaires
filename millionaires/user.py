from abc import ABC
from millionaires.utils import *
import os, csv


class User(ABC):

    def __init__(self, nick: str):
        self.nick = nick


class Player(User):

    def __init__(self, *args):
        super().__init__(*args)
        self.result = 0

    def add_cash(self, cash):
        self.result = cash

    @property
    def get_result(self):
        return self.result

    @property
    def get_player_nick(self):
        return self.nick

    @classmethod
    def create_player(cls, nick):
        nick_imp = check_player_nick(nick)
        return Player(nick_imp)


class Admin(User):

    def __init__(self, nick, password):
        super().__init__(nick)
        self.password = password

    def authorization(self):
        if self.nick == os.environ['login'] and os.environ['password'] == self.password:
            print("Login correct !")
            return True
        while True:
            if self.nick != os.environ['login'] or os.environ['password'] != self.password:
                print("Login incorrect!! Enter correct username and password")
                log_out = check_user_choice(input("enter [S] to logout [C] to continue: "))
                if log_out == "S":
                    return False
                elif log_out == "C":
                    correct_nick = input("Enter your nick: ")
                    correct_password = input("Enter your password: ")
                    if correct_nick == os.environ['login'] and os.environ['password'] == correct_password:
                        setattr(self, 'nick', correct_nick)
                        setattr(self, 'password', correct_password)
                        print("Login correct !")
                        return True
                    else:
                        continue

    @staticmethod
    def add_question():
        while True:
            chooser = check_chooser(input("Do you want to add question to base [Y/N] :"))
            if chooser == "Y":
                file_path = os.path.join(os.path.abspath(__file__ + "/../../"), "baza/baza.csv")
                with open(file_path, 'a+') as file:
                    base = csv.writer(file, delimiter=",")
                    id = int(input("Select the ID: "))
                    category = input("Select the category: ")
                    question = input("Select the question: ")
                    a_ans = input("A ans: ")
                    b_ans = input("B ans: ")
                    c_ans = input("C ans: ")
                    d_ans = input("D ans: ")
                    right_ans = input("Select correct answear: ")
                    base.writerow([id, category, question, a_ans, b_ans, c_ans, d_ans, right_ans])
                    continue
            elif chooser == "N":
                break

    @classmethod
    def create_admin(cls, nick, password):
        return Admin(nick, password)




