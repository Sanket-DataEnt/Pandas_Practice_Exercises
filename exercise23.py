'''
23. How to convert year-month string to dates corresponding to the 4th day of the month?

0   2010-01-04
1   2011-02-04
2   2012-03-04
dtype: datetime64[ns]

'''

import pandas as pd
import numpy as np

ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])

ser = pd.to_datetime(ser)
print(ser)

day = 4
new_ser = ser.map(lambda x:x.replace(day=day))
print(new_ser)
