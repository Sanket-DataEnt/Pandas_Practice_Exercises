'''
46. How to set the number of rows and columns displayed in the output?

Change the pandas display settings on printing the dataframe df it shows a maximum of 10 rows and 10 columns.

'''

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')


print(df.shape)
print(df.iloc[0:10,0:10].shape)

# Alternative Solution
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)

print(df)