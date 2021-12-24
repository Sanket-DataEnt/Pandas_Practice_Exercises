'''
26. How to get the mean of a series grouped by another series?

Compute the mean of weights of each fruit

Desired output

# values can change due to randomness
apple     6.0
banana    4.0
carrot    5.8
dtype: float64

'''

import numpy as np
import pandas as pd

np.random.seed(2021)

fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
print(weights.tolist())
print(fruit.tolist())
# [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
# ['apple', 'banana', 'banana', 'apple', 'banana', 'carrot', 'carrot', 'apple', 'carrot', 'banana']

print(weights.groupby(fruit).mean())


# >>>>>>> not an ideal way to do this

# fruit_wt = list(zip(fruit, weights))
# print(fruit_wt)

# dic = {}
# cnt_dic = {}
# cnt = 1
# for i,j in fruit_wt:
#     print(i,j)
#     # print (i, j)
#     if i not in dic:
#         dic[i] = j
#         if i not in cnt_dic:
#             cnt_dic[i] = cnt
#     elif i in dic:
#         # print(i,dic[i])
#         dic[i] = dic[i] + j   
#         print(i, dic[i])
#         # print(i,j)
#         # dic[i] += j
#         # dic[i] = dic[i]/cnt
#         cnt += 1
#         if i in cnt_dic:
# print(dic)


