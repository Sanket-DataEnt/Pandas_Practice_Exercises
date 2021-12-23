'''
19. How to calculate the number of characters in each word in a series?
'''
import pandas as pd
import numpy as np

ser = pd.Series(['how', 'to', 'kick', 'ass?'])

y = ser.map(lambda x:len(x))

print(y)