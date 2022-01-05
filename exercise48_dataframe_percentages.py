'''
48. How to format all the values in a dataframe as percentages?

Format the values in column 'random' of df as percentages.
'''

import pandas as pd
import numpy as np

np.random.seed(2022)
df = pd.DataFrame(np.random.random(4), columns=['random'])
# print(df)

def percentage(x):
    x = str(np.round((x * 100),2)) + '%'
    return x

df['random'] = df['random'].apply(lambda x : percentage(x))
print(df['random'])

# Alternative Solution
df = pd.DataFrame(np.random.random(4), columns=['random'])
out = df.style.format({
    'random': '{0:.2%}'.format,
})

print(out)