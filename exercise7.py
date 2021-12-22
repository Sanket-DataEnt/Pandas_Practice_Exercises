'''
7. How to get the items not common to both series A and series B?
'''

import pandas as pd
import numpy as np

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Union - Intersecion = > Not Common Items

ser_u = pd.Series(np.union1d(ser1, ser2)) # union
ser_i = pd.Series(np.intersect1d(ser1, ser2)) # intersection

ser_not_common = ser_u[~ser_u.isin(ser_i)]
print(ser_not_common)