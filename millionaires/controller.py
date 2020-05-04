from millionaires.model import Game
from millionaires.user import Admin, Player
from millionaires.utils import *
from millionaires.viewer import Printer


class Millionaires:
    def __init__(self):
        self.game = Game()
        self.printer = Printer()
        self._player = None
        self._admin = None

    def correct_answer(self, category, number_question):
        correct_answer = check_correct_answer(input("Select correct answer [A - D]: "))
        if self.game.check_question(category, number_question, correct_answer):
            self.printer.print_win_info(self.game)
            return True
        return False

    def incorrect_answer(self, player):
        self.game.end_game(player)
        self.printer.print_looser_info(self.game)

    def play_game(self, player):
        while self.game.counter < len(self.game.levels):
            category = self.game.draw_category()
            number_question = self.game.draw_number_question(category)
            if self.game.select_new_question(category, number_question):
                self.printer.print_question(self.game, category, number_question)
                if self.game.check_number_of_hints():
                    hint = self.printer.print_hint_info(self.game)
                    if hint == "Y":
                        self.printer.print_hint(self.game, category, number_question)
                        if self.correct_answer(category, number_question):
                            continue
                        self.incorrect_answer(player)
                        break
                    elif hint == "N":
                        if self.correct_answer(category, number_question):
                            continue
                        self.incorrect_answer(player)
                        break
                else:
                    if self.correct_answer(category, number_question):
                        continue
                    self.incorrect_answer(player)
                    break
            else:
                continue
        else:
            self.game.end_game(player)

    def run_game(self):
        self.printer.print_title(self.game)
        username = self.printer.print_user_choice()
        if username == "A":
            admin = self.add_admin()
            if admin.authorization():
                self.printer.correct_login()
                self.add_question(admin)
            else:
                self.printer.incorrect_login()
                self.incorrect_log_next_action()
        elif username == "P":
            player = self.add_player()
            self.play_game(player)

    def add_question(self, admin):
        while True:
            chooser = self.printer.adding_question_to_base()
            if chooser == "Y":
                id_ = check_id(input("Select the ID: "))
                category = input("Select the category: ")
                question = input("Select the question: ")
                a_ans = input("A ans: ")
                b_ans = input("B ans: ")
                c_ans = input("C ans: ")
                d_ans = input("D ans: ")
                right_ans = input("Select correct answer: ")
                admin.database.add_question_to_base(
                    id_, category, question, a_ans, b_ans, c_ans, d_ans, right_ans
                )
                continue
            elif chooser == "N":
                return False

    def incorrect_log_next_action(self):
        while True:
            log_out = input("Enter 'S' to stop 'C' to try log in again: ")
            if log_out == "S":
                break
            elif log_out == "C":
                admin = self.add_admin()
                if admin.authorization():
                    self.printer.correct_login()
                    if not self.add_question(admin):
                        break
                else:
                    continue

    @staticmethod
    def add_player():
        nick = input("Enter your nick (max 10 chars [a-Z, 0-9]): ")
        player = Player.create_player(nick)
        return player

    @staticmethod
    def add_admin():
        nick = input("Enter your nick: ")
        password = input("Enter your password: ")
        admin = Admin.create_admin(nick, password)
        return admin
