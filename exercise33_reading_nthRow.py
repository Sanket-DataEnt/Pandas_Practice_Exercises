'''
33. How to import only every nth row from a csv file to create a dataframe?

L2 Import every 50th row of BostonHousing dataset as a dataframe.
'''

import pandas as pd

data = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'
n=50
cols = ["crim","zn","indus","chas","nox","rm","age","dis","rad","tax","ptratio","b","lstat","medv"]
df = pd.read_csv(data, skiprows=n)
df.columns = cols

print(df.shape)
print(df.head())