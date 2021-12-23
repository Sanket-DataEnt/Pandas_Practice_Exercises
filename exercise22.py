'''
22. How to get the day of month, week number, day of year and day of week from a series of date strings?

Date:  [1, 2, 3, 4, 5, 6]
Week number:  [53, 5, 9, 14, 19, 23]
Day num of year:  [1, 33, 63, 94, 125, 157]
Day of week:  ['Friday', 'Wednesday', 'Saturday', 'Thursday', 'Monday', 'Saturday']

'''
import pandas as pd
import numpy as np
# from datetime import datetime
# import datetime as dt

ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
ser = pd.to_datetime(ser)

Date = list(ser.map(lambda x:x.day))
week = list(ser.map(lambda x:x.weekofyear))
day_year = list(ser.map(lambda x:x.dayofyear))
day = list(ser.map(lambda x:x.day_name()))

print("Date: ", Date)
print("Week Number: ", week)
print("Day num of year: ", day_year)
print("Day of week: ", day)
