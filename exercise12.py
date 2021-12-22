'''
12. How to convert a numpy array to a dataframe of given shape? (L1)
'''
import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(1, 10, 35))

print(ser)

b = pd.DataFrame(ser.values.reshape(7, 5))
print(b)