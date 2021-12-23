'''
17. How to compute the mean squared error on a truth and predicted series?
'''

import numpy as np
import pandas as pd

truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)

truth_mean = np.mean(truth)
pred_mean = np.mean(pred)
print(truth_mean, pred_mean)
mse = (truth_mean - pred_mean)**2
print(mse)