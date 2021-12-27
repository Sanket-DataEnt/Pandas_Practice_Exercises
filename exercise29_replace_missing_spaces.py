'''
29. How to replace missing spaces in a string with the least frequent character?

Replace the spaces in my_str with the least frequent character.

Desired Output

'dbccdebcabedcgade'  # least frequent is 'c'

'''

import pandas as pd

my_str = 'dbc deb abed gade'

my_str_space = my_str.replace(" ","")
print(my_str_space)

## Solution 1
# Method 1 to count each element in string
# my_dict = {}
# for i in my_str_space:
#     if i in my_dict.keys():
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1

# Method 2 to count each element in string
my_dict = {i : my_str_space.count(i) for i in set(my_str_space)}
print(my_dict)

lowest_count = [i for i in my_dict if my_dict[i] == min(my_dict.values())]

print(lowest_count)

for i in range(len(lowest_count)):
    my_str1 = my_str.replace(" ", lowest_count[i])
    print(my_str1)


##  Solution 2

least_freq = pd.Series(list(my_str_space))
least_freq = least_freq.value_counts()
print(least_freq)

least_freq = "".join(least_freq.index)
print(least_freq)

my_res = my_str.replace(" ",least_freq[-1])
print(my_res)