'''
13. How to find the positions of numbers that are multiples of 3 from a series?
'''
import pandas as pd
import numpy as np
np.random.seed(2021)

ser = pd.Series(np.random.randint(1, 10, 7))
print(ser)

for i in ser.index:
    if ser[i]%3==0:
        print("value: ",ser[i])
        print("index: ",i)


