'''
9. How to get frequency counts of unique items of a series?
'''

import numpy as np
import pandas as pd

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

# print(ser)
print(ser.value_counts())