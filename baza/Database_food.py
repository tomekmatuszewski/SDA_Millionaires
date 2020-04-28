import pandas as pd
import os

pd.set_option('display.max_columns', 10)
path = os.path.join(os.path.dirname(__file__), "food.xlsx")

food = pd.read_excel(path,
                     usecols=['Product', 'Category', 'Kcal', 'Carbo(g)', 'Protein(g)', 'Fats(g)', 'Price[PLN]', 'unit',
                              'Weight[g/ml]', 'Weight_pcs/pack[g]'], )
food = food.fillna(0)

food['Category'] = food['Category'].astype('category')
food['unit'] = food['unit'].astype('category')

food['Number'] = food.groupby(by='Category').cumcount() + 1
food = food.set_index(["Category", "Number"]).sort_index()

categories = sorted(list(set(food.index.get_level_values(0))))

if __name__ == '__main__':
	food.info(memory_usage="deep")