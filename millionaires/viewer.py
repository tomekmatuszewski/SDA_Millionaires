from millionaires.utils import *


class Printer:
    @staticmethod
    def print_question(game, category, number_question):
        print(f"\nRound {game.counter + 1}! {game.levels[game.counter]} PLN to win.")
        print(f"Category: {category}")
        print(game.base.questions_base.loc[(category, number_question), "Question"])
        for column in game.base.questions_base[["A", "B", "C", "D"]]:
            print(
                f"{column}: {game.base.questions_base.loc[(category, number_question), column]}"
            )

    @staticmethod
    def print_hint(game, category, number_question):
        cols = game.hint(category, number_question)
        print()
        for col in cols:
            print(
                f"{col}: {game.base.questions_base.loc[(category, number_question), col]}"
            )

    @staticmethod
    def print_hint_info(game):
        print()
        hint = check_hint(
            input(
                f"You have {game.max_number_hints} hint{'s' if game.max_number_hints == 2 else ''} "
                f"50/50 - do you want to use? [Y/N]: "
            )
        )
        return hint

    @staticmethod
    def print_win_info(game):
        print(f"Great, you won {game.levels[game.counter - 1]} PLN!")

    @staticmethod
    def print_looser_info(game):
        print(f"You lost! Your score is {game.player_acc} PLN")

    @staticmethod
    def print_title(game):
        print(f"Welcome in game {game.name} !!!")

    @staticmethod
    def print_user_choice():
        username = check_username(
            input("Enter [P] if you want to play [A] if you want to log as Admin: ")
        )
        return username

    @staticmethod
    def correct_login():
        print("Login correct !")

    @staticmethod
    def incorrect_login():
        print("Login incorrect!! Enter correct username and password")

    @staticmethod
    def adding_question_to_base():
        chooser = check_chooser(input("Do you want to add question to base [Y/N] :"))
        return chooser
