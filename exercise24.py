'''
24. How to filter words that contain atleast 2 vowels from a series?

Desired Output
0     Apple
1    Orange
4     Money

'''

import pandas as pd
import numpy as np
from collections import Counter

ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])


vowel = ser.map(lambda x: sum([Counter(x.lower()).get(i,0) for i in list('aeiou')]) >= 2)
print(ser[vowel])

