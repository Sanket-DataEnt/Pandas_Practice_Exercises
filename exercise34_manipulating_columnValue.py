'''
34. How to change column values when importing csv to a dataframe?

Import the boston housing dataset, but while importing change the 
'medv' (median house value) column so that values < 25 becomes ‘Low’ and > 25 becomes ‘High’.
'''

import pandas as pd

data = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'

df = pd.read_csv(data, 
                converters= {'medv' : lambda x : 'Low' if float(x) < 25 else 'High'})

print(df.shape)
print(df.head())

