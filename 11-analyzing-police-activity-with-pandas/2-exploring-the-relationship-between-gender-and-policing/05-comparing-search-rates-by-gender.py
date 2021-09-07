'''
Comparing search rates by gender

In this exercise, you'll compare the rates at which female and male drivers are searched during a traffic stop. Remember that the vehicle search rate across all stops is about 3.8%.

First, you'll filter the DataFrame by gender and calculate the search rate for each group separately. Then, you'll perform the same calculation for both genders at once using a .groupby().
'''

import pandas as pd

ri = pd.read_csv('../datasets/RI_cleaned.csv', nrows=100000, low_memory=False)

ri.drop(['county_name', 'state'], axis='columns', inplace=True)
ri.dropna(subset=['driver_gender'], inplace=True)

ri['is_arrested'] = ri.is_arrested.astype('bool')

combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
ri['stop_datetime'] = pd.to_datetime(combined)

ri.set_index('stop_datetime', inplace=True)

'''
INSTRUCTIONS 1/3

*   Filter the DataFrame to only include female drivers, and then calculate the search rate by taking the mean of search_conducted.
'''

# Calculate the search rate for female drivers
print(ri[ri.driver_gender=='F'].search_conducted.mean())

'''
INSTRUCTIONS 2/3

*   Filter the DataFrame to only include male drivers, and then repeat the search rate calculation.
'''

# Calculate the search rate for male drivers
print(ri[ri.driver_gender=='M'].search_conducted.mean())

'''
INSTRUCTIONS 3/3

*   Group by driver gender to calculate the search rate for both groups simultaneously. (It should match the previous results.)
'''

# Calculate the search rate for both groups simultaneously
print(ri.groupby('driver_gender').search_conducted.mean())
