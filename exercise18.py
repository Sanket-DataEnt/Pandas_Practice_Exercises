'''
18. How to convert the first character of each element in a series to uppercase?
'''

import pandas as pd
import numpy as np
ser = pd.Series(['how', 'to', 'kick', 'ass?'])

ser_c = [i.title() for i in ser]

print(ser_c)