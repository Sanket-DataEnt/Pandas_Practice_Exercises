'''
44. How to select a specific column from a dataframe as a dataframe instead of a series?

Get the first column (a) in df as a dataframe (rather than as a Series).
'''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

print(df.head())

print(df[['a']])

# Alternative Solutions
print("Solution1: ", type(df[['a']]))
print("Solution2: ",type(df.loc[:, ['a']]))
print("Solution3: ",type(df.iloc[:, [0]]))
