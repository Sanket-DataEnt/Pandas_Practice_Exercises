'''
25. How to filter valid emails from a series?

Extract the valid emails from the series emails. 
The regex pattern for valid emails is provided as reference.

1    rameses@egypt.com
2            matt@t.co
3    narendra@modi.com
dtype: object

'''

import pandas as pd
import re

emails = pd.Series(['buying books at amazon.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'

# Solution 1
patt_regex = re.compile(pattern)
email  = emails.map(lambda x:bool(patt_regex.search(x)))
print(emails[email])

# Solution 2
email1 = emails.map(lambda x: bool(re.match(pattern, x)))
print(emails[email1])

