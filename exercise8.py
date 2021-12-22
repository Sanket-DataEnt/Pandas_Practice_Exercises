'''
8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
'''

import numpy as np
import pandas as pd
import random

random.seed(2021)


ser = pd.Series(np.random.normal(10, 5, 25))

# print(ser)

# Doing sorting of the series.
ser = ser.sort_values(ascending=True)
ser = ser.reset_index(drop=True)
print(ser)

ser_min = ser[0] # min
ser_max = ser[len(ser)-1] # max
# ser_median = ser[(len(ser)-1)/2] # median
ser_median = ser.median() # median
ser_25 = np.percentile(ser, 25) # 25th percentile
ser_75 = np.percentile(ser, 75) # 75th percentile


print("Minimum value: ", ser_min)
print("Maximum value: ", ser_max)
print ("Median value: ", ser_median)
print("25 Percentile value: ", ser_25)
print("75 Percentile value: ", ser_75)

# Method 2

'''
np.percentile(ser, q=[0, 25, 50, 75, 100])
'''