'''
42. How to replace missing values of multiple numeric columns with the mean?

Replace missing values in Min.Price and Max.Price columns with their respective mean.
'''

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

print(df.isnull().sum())

df[['Min.Price', 'Max.Price']] = df[['Min.Price', 'Max.Price']].apply(lambda x:x.fillna(x.mean()))

print(df.isnull().sum())

