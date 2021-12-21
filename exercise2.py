'''
2. How to create a series from a list, numpy array and dict?
'''
import pandas as pd
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

# print(mylist)
mylist_s = pd.Series(mylist)
# print(mylist_s)

# print(myarr)
myarr_s = pd.Series(myarr)
# print(myarr_s)

print(mydict)
mydict_s = pd.Series(mydict)
print(mydict_s)
