'''
28. How to find all the local maxima (or peaks) and local maxima in a numeric series?

Get the positions of peaks (values surrounded by smaller values on both sides) in

Desired output

array([1, 5, 7])
'''

import pandas as pd
import numpy as np
from scipy.signal import argrelextrema

ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])

# for local maxima
maxima = argrelextrema(ser.values, np.greater)

# for local minima
minima = argrelextrema(ser.values, np.less)

print("Local maxima: ", maxima)
print("Local minima: ", minima)