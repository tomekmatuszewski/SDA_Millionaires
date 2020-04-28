import pandas as pd
import os
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 500)

file_path = os.path.join(os.path.dirname(__file__), "baza.csv")

questions_base = pd.read_csv(file_path, index_col='ID')
questions_base['Category'] = questions_base['Category'].astype('category')

categories = questions_base['Category']


questions_base['Number'] = questions_base.groupby(by='Category').cumcount() + 1
questions_base = questions_base.set_index(["Category", "Number"]).sort_index()

categories = sorted(list(set(questions_base.index.get_level_values(0))))

if __name__ == '__main__':
    questions_base.info(memory_usage="deep")


