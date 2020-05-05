import csv
import json
import os

import pandas as pd

pd.set_option("display.max_colwidth", 100)
pd.set_option("display.max_columns", 500)


class Database:
    def __init__(self):
        self.base_file_path = os.path.join(os.path.dirname(__file__), "baza.csv")
        self._questions_base = None
        self._categories = None
        self.rank_path = os.path.join(os.path.dirname(__file__), "rank.json")
        self.rank = self.load_rank()

    # modified database
    @property
    def questions_base(self):
        self._questions_base = pd.read_csv(self.base_file_path)
        self._questions_base["Category"] = self._questions_base["Category"].astype(
            "category"
        )
        self._questions_base["Number"] = (
            self._questions_base.groupby(by="Category").cumcount() + 1
        )
        self._questions_base = self._questions_base.set_index(
            ["Category", "Number"]
        ).sort_index()
        return self._questions_base

    # list of categories from database
    @property
    def categories(self):
        self._categories = sorted(
            list(set(self.questions_base.index.get_level_values(0)))
        )
        return self._categories

    # loading player ranking
    def load_rank(self):
        if not os.path.exists(self.rank_path):
            with open(self.rank_path, "w") as file:
                file.write("{}")
        with open(self.rank_path) as file:
            rank = json.load(file)
        return rank

    # adding result of player after ending the game
    def add_result_to_rank(self, player, player_acc):
        self.rank[player.player_nick] = f"{player_acc} PLN"
        with open(self.rank_path, "w+") as file_json:
            json.dump(self.rank, file_json)

    # adding question to database by admin
    def add_question_to_base(
        self, id_, category, question, a_ans, b_ans, c_ans, d_ans, right_ans
    ):
        with open(self.base_file_path, "a+", newline="") as file:
            base = csv.writer(file, delimiter=",")
            base.writerow(
                [id_, category, question, a_ans, b_ans, c_ans, d_ans, right_ans]
            )


if __name__ == "__main__":
    data = Database()
    print(data.rank_path)
