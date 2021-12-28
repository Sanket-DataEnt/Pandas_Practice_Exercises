'''
39. How to rename a specific columns in a dataframe?

Rename the column Type as CarType in df and replace the ‘.’ in column names with ‘_’

print(df.columns)
#> Index(['Manufacturer', 'Model', 'CarType', 'Min_Price', 'Price', 'Max_Price',
#>        'MPG_city', 'MPG_highway', 'AirBags', 'DriveTrain', 'Cylinders',
#>        'EngineSize', 'Horsepower', 'RPM', 'Rev_per_mile', 'Man_trans_avail',
#>        'Fuel_tank_capacity', 'Passengers', 'Length', 'Wheelbase', 'Width',
#>        'Turn_circle', 'Rear_seat_room', 'Luggage_room', 'Weight', 'Origin',
#>        'Make'],
#>       dtype='object')

'''

import pandas as pd

data = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'

df = pd.read_csv(data)

# print(df.columns)

df = df.rename({'Type': 'CarType'}, axis=1)
# print(df.columns)

for i in df.columns:
    if '.' in i:
        new_col = i.replace('.', '_')
        df = df.rename({i : new_col}, axis=1)
print(df.columns)
