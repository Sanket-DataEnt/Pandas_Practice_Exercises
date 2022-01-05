'''
49. How to filter every nth row in a dataframe?

From df, filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).

'''

import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

print(df.iloc[::20, :][['Manufacturer', 'Model', 'Type']])
