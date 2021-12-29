'''
40. How to check if a dataframe has any missing values?
'''

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# print(df.isnull().sum())

print(df.isnull().values.any())