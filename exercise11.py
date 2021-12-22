'''
11. How to bin a numeric series to 10 groups of equal size?
'''

import pandas as pd
import numpy as np

ser = pd.Series(np.random.random(20))

print(pd.qcut(ser, q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1], 
        labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']).head())