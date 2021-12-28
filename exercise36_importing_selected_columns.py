'''
36. How to import only specified columns from a csv file?

Import ‘crim’ and ‘medv’ columns of the BostonHousing dataset as a dataframe.
'''

import pandas as pd

data = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'

df = pd.read_csv(data, usecols = ['crim', 'medv'])

print(df.head())