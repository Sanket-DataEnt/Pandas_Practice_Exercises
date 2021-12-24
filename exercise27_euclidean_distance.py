'''
27. How to compute the euclidean distance between two series?

Compute the euclidean distance between series (points) p and q, without using a packaged formula.

Desired Output

18.165

'''

import numpy as np
import pandas as pd

p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

def euclidean(p, q):
    num = np.sqrt(np.sum(np.subtract(p, q)**2))
    return num

print(euclidean(p, q))