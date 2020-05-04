from random import choice, randint, shuffle

from baza.baza import Database


class Game:
    counter = 0

    def __init__(self):
        self.name = "Millionaires"
        self.levels = [
            500,
            1000,
            2000,
            5000,
            10000,
            20000,
            40000,
            75000,
            125000,
            250000,
            500000,
            1000000,
        ]
        self.base = Database()
        self.ans_in_game = []
        self.max_number_hints = 2
        self.player_acc = 0

    def select_new_question(self, category, number_question):
        id_ans = self.base.questions_base.loc[(category, number_question), "ID"]
        if id_ans not in self.ans_in_game:
            self.ans_in_game.append(id_ans)
            return True
        return False

    def draw_category(self):
        return choice(self.base.categories)

    def draw_number_question(self, category):
        return randint(1, len(self.base.questions_base.loc[category, :]))

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

    def check_number_of_hints(self):
        if self.max_number_hints > 0:
            return True
        return False

    def check_question(self, category, number_question, answer):
        if self.is_correct_answer(category, number_question, answer):
            self.add_player_cash()
            self.counter += 1
            return True
        return False

    def is_correct_answer(self, category, number_question, answer):
        if (
            self.base.questions_base.loc[(category, number_question), answer]
            == self.base.questions_base.loc[(category, number_question), "Answer"]
        ):
            return True
        return False

    def end_game(self, player):
        self.base.add_result_to_rank(player, self.player_acc)

    def add_player_cash(self):
        self.player_acc = self.levels[self.counter]


if __name__ == "__main__":
    pass
