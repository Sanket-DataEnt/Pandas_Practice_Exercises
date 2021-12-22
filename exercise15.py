'''
15. How to stack two series vertically and horizontally ?
Stack ser1 and ser2 vertically and horizontally (to form a dataframe). Input
'''

import pandas as pd
import numpy as np

ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

vertical = pd.concat([ser1, ser2], ignore_index=True)

horizontal = pd.concat([ser1, ser2], ignore_index=True, axis=1)

print("vertical: ", vertical)
print("horizontal: ", horizontal)

