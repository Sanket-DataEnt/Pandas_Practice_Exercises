'''
50. How to create a primary key index by combining relevant columns?

In df, Replace NaNs with ‘missing’ in columns 'Manufacturer', 'Model' and 'Type' 
and create a index as a combination of these three columns and check if the index is a primary key.

Desired Output

                       Manufacturer    Model     Type  Min.Price  Max.Price
Acura_Integra_Small           Acura  Integra    Small       12.9       18.8
missing_Legend_Midsize      missing   Legend  Midsize       29.2       38.7
Audi_90_Compact                Audi       90  Compact       25.9       32.3
Audi_100_Midsize               Audi      100  Midsize        NaN       44.6
BMW_535i_Midsize                BMW     535i  Midsize        NaN        NaN
'''

import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv', usecols=[0,1,2,3,5])

# print(df.head())
print(df.isnull().sum())
values = {'Manufacturer':'missing', 'Model':'missing', 'Type':'missing'}
df.fillna(value=values, inplace=True)
print(df.isnull().sum())
# print(df.head())

df.set_index(df['Manufacturer'] + '_' + df['Model'] + '_' + df['Type'], inplace=True)
print(df.head())