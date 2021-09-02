'''
Handle missing values

In order to replace missing values in your time series data, you can use the command:

|   df = df.fillna(method="ffill")

where the argument specifies the type of method you want to use. For example, specifying bfill (i.e backfilling) will ensure that missing values are replaced using the next valid observation, while ffill (i.e. forward-filling) ensures that missing values are replaced using the last valid observation.

Recall from the previous exercise that co2_levels has 59 missing values.
'''

import pandas as pd

co2_levels = pd.read_csv('../datasets/ch2_co2_levels.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

*   Impute these missing values in co2_levels by using backfilling.
*   Print the total number of missing values.
'''

# Impute missing values with the next valid observation
co2_levels = co2_levels.fillna(method='bfill')

# Print out the number of missing values
print(co2_levels.isnull().sum())