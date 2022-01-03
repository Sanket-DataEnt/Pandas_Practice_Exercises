'''
43. How to use apply function on existing columns with global variables as additional arguments?

In df, use apply method to replace the missing values in Min.Price with the column’s mean and 
those in Max.Price with the column’s median.
'''

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

min_mean = df['Min.Price'].mean()
max_median = df['Max.Price'].median()
# print(max_median)
# print(min_mean)
df['Min.Price'] = df['Min.Price'].fillna(min_mean)
df['Max.Price'] = df['Max.Price'].fillna(max_median)

print(df.isnull().sum())


