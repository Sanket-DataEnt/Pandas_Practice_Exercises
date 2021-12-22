'''
4. How to combine many series to form a dataframe?
'''

import numpy as np
import pandas as pd

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.DataFrame(dict(ser1=ser1, ser2=ser2))
print(df.head())