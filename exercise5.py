'''
5. How to assign name to the series’ index?
'''

import pandas as pd

ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))

ser.name = 'name'

print(ser.head())
