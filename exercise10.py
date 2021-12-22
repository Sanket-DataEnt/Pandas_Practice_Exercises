'''
10. How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?
'''

import pandas as pd
import numpy as np

np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

# print(ser)
# print(ser.value_counts())

# converting keys to list as per their frequency count
x = ser.value_counts().keys().tolist()

print(x)

# Except top 2 most frequent values replacing else to Other
for i in range(2, len(x)):
    x[i] = 'Other'
print(x)