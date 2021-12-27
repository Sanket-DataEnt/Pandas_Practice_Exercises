'''
32. How to compute the autocorrelations of a numeric series?

Compute autocorrelations for the first 10 lags of ser. Find out which lag has the largest correlation. 

Desired output

# values will change due to randomness
[0.29999999999999999, -0.11, -0.17000000000000001, 0.46000000000000002, 0.28000000000000003, -0.040000000000000001, -0.37, 0.41999999999999998, 0.47999999999999998, 0.17999999999999999]
Lag having highest correlation:  9

'''
import pandas as pd
import numpy as np

np.random.seed(123)

ser = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))

corr = []

for i in range(10,20):
    corr1 = ser[:i].autocorr()
    corr.append(corr1)
print(corr)

max_value = max(corr)
max_index = corr.index(max_value)
print(f"Index of maximum value {max_value}: ",max_index)
