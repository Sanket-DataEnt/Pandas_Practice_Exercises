'''
20. How to compute difference of differences between consequtive numbers of a series?

Desired Output

[nan, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 8.0]
[nan, nan, 1.0, 1.0, 1.0, 1.0, 0.0, 2.0]
'''

import pandas as pd
import numpy as np

ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])

print(list(ser.diff()))
print(list(ser.diff().diff()))