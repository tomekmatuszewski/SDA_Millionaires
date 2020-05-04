from abc import ABC
from millionaires.viewer import Printer
from millionaires.utils import *
from baza.baza import Database
import os


class User(ABC):

    def __init__(self, nick: str):
        self.nick = nick


class Player(User):

    def __init__(self, *args):
        super().__init__(*args)

    @property
    def player_nick(self):
        return self.nick

    @classmethod
    def create_player(cls, nick):
        nick_imp = check_player_nick(nick)
        return Player(nick_imp)


class Admin(User):

    def __init__(self, nick, password):
        super().__init__(nick)
        self.password = password
        self.printer = Printer()
        self.database = Database()

    def authorization(self):
        if os.environ.get('login', self.nick) and os.environ.get('password', self.password):
            return True
        return False

    def adding_question(self, id_, category, question, a_ans, b_ans, c_ans, d_ans, right_ans):
        while True:
            chooser = self.printer.adding_question_to_base()
            if chooser == "Y":
                self.database.add_question_to_base(id_, category, question, a_ans, b_ans, c_ans, d_ans, right_ans)
                continue
            elif chooser == "N":
                break

    @classmethod
    def create_admin(cls, nick, password):
        return Admin(nick, password)
