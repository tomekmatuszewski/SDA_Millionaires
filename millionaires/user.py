import os
from abc import ABC

from baza.baza import Database
from millionaires.utils import *
from millionaires.viewer import Printer


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
        os.environ["login"] = "admin"
        os.environ["password"] = "admin777"
        if os.environ["login"] == self.nick and os.environ["password"] == self.password:
            return True
        return False

    @classmethod
    def create_admin(cls, nick, password):
        return Admin(nick, password)


if __name__ == "__main__":
    pass
