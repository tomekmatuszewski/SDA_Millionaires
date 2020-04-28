from abc import ABC, abstractmethod
import os
import csv


class User(ABC):

    def __init__(self, nick: str):
        self.nick = nick


class Player(User):

    def __init__(self, *args):
        super().__init__(*args)
        self.result = 0





class Admin(User):

    def __init__(self, nick, password):
        super().__init__(nick)
        self.password = password

    def authorization(self):
        if self.nick == os.environ['login'] and os.environ['password'] == self.password:
            print("Zalogowano")

            return True
        else:
            raise "Złe dane"

    def add_question(self):
        file_path = os.path.join(os.path.abspath(__file__ + "/../../"), "baza/baza.csv")
        with open(file_path, 'a+') as file:
            base = csv.writer(file, delimiter=";")
            id = int(input("Select the ID: "))
            category = input("Select the category: ")
            question = input("Select the question: ")
            a_ans = input("A ans: ")
            b_ans = input("B ans: ")
            c_ans = input("C ans: ")
            d_ans = input("D ans: ")
            right_ans = input("Select correct answear: ")
            base.writerow([id, category, question, a_ans, b_ans, c_ans, d_ans, right_ans])



