'''
37. How to get the nrows, ncolumns, datatype, summary stats of each column of a dataframe? Also get the array and list equivalent.

Get the number of rows, columns, datatype and summary statistics of each column of the Cars93 dataset. 
Also get the numpy array and list equivalent of the dataframe.
'''

import pandas as pd

data = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'

df = pd.read_csv(data)

print(df.head())
print(df.info())

# how many columns under each dtype
print(df.dtypes.value_counts())

# summary statistics
df_stats = df.describe()
print(df_stats)

print("********************* Numpy Array ********************")
# numpy array 
df_arr = df.values
print(df_arr)

print("************************** List **********************")
# list
df_list = df.values.tolist()
print(df_list)