'''
51. How to get the row number of the nth largest value in a column?

Find the row position of the 5th largest value of column 'a' in df
'''

import pandas as pd
import numpy as np

np.random.seed(2022)

df = pd.DataFrame(np.random.randint(1, 30, 30).reshape(10,-1), columns=list('abc'))
# print(df)

df.sort_values(by='a', ascending=False, inplace=True)
# print(df)
print(df.index[4])

# Alternative Solution
df = pd.DataFrame(np.random.randint(1, 30, 30).reshape(10,-1), columns=list('abc'))
print(df['a'].argsort()[::-1][5])
