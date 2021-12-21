'''
3. How to convert the index of a series into a column of a dataframe?
'''

import pandas as pd
import numpy as np

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

# df = ser.to_frame()
df = pd.DataFrame(ser)
df = df.reset_index()
print(df.head())