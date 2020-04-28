from abc import ABC, abstractmethod
import os, time, csv


class User(ABC):

    def __init__(self, nick: str):
        self.nick = nick


class Player(User):

    def __init__(self, *args):
        super().__init__(*args)
        self.result = 0

    def add_cash(self, cash):
        self.result += cash

    def get_result(self):
        return self.result

    def get_player_nick(self):
        return self.nick


class Admin(User):

    def __init__(self, nick, password):
        super().__init__(nick)
        self.password = password

    def authorization(self):
        print("Logging in...")
        time.sleep(2)
        while True:
            if self.nick != os.environ['login'] or os.environ['password'] != self.password:
                print("Login incorrect!! Enter correct username/password")
                correct_nick = input("Enter your nick: ")
                correct_password = input("Enter your password: ")
                if correct_nick == os.environ['login'] and os.environ['password'] == correct_password:
                    setattr(self, 'nick', correct_nick)
                    setattr(self, 'password', correct_password)
                else:
                    continue
            else:
                print("Login correct !")
                break

    @staticmethod
    def add_question():
        while True:
            chooser = input("Do you want to add question to base [Y/N] :")
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




