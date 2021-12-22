'''
16. How to get the positions of items of series A in another series B?
Get the positions of items of ser2 in ser1 as a list.
'''

import pandas as pd
import numpy as np

ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])


lst = []


inter = list(np.intersect1d(ser1, ser2))
# print(inter)

for i in inter:
    lst.append(pd.Index(ser1).get_loc(i))
print(lst)

# Solution 2
lst1 = [pd.Index(ser1).get_loc(i) for i in ser2]
print(lst1)
