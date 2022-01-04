'''
45. How to change the order of columns of a dataframe?

1. In df, interchange columns 'a' and 'c'.
2. Create a generic function to interchange two columns, without hardcoding column names.
3. Sort the columns in reverse alphabetical order, that is column 'e' first through column 'a' last.
'''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
# print(df)

# df.rename({'a':'c', 'c':'a'}, axis=1, inplace=True)

def column_replace(df, column1, new_col1, column2, new_col2):
    df.rename({column1:new_col1, column2:new_col2}, axis=1, inplace=True)
    return df

df = column_replace(df, 'a', 'c', 'c', 'a')
# print(df)

col = list(df.columns)
# print(col)
col.sort(reverse=True)
# print(col)
df = df[col]
print(df)

