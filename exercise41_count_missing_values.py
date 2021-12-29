'''
41. How to count the number of missing values in each column?
'''

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

print(df.isnull().sum()) # Finding missing values in each column

# print(df.isnull().sum().argmax())

print(df.columns[df.isnull().sum().argmax()]) # Finding the column name which has maximum missing values
