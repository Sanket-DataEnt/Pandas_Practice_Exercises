'''
38. How to extract the row and column number of a particular cell with given criterion?

Which manufacturer, model and type has the highest Price?
What is the row and column number of the cell with the highest Price value?
'''

import pandas as pd

data = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'

df = pd.read_csv(data)

# print(df.head())

df_h = df[['Manufacturer', 'Model', 'Type','Price']]

# print(df_h.head())

print(df_h[df_h['Price'] == df['Price'].max()])

print(df_h[df_h['Price'] == df['Price'].max()]['Price'])