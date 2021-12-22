'''
14. How to extract items at given positions from a series
From ser, extract the items at positions in list pos. Input
'''

import pandas as pd
import numpy as np

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

for i in pos:
    print(ser[i])

