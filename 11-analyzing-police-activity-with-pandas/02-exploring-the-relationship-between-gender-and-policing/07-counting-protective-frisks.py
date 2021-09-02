'''
Counting protective frisks

During a vehicle search, the police officer may pat down the driver to check if they have a weapon. This is known as a "protective frisk."

In this exercise, you'll first check to see how many times "Protective Frisk" was the only search type. Then, you'll use a string method to locate all instances in which the driver was frisked.
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
INSTRUCTIONS

*   Count the search_type values to see how many times "Protective Frisk" was the only search type.
*   Create a new column, frisk, that is True if search_type contains the string "Protective Frisk" and False otherwise.
*   Check the data type of frisk to confirm that it's a Boolean Series.
*   Take the sum of frisk to count the total number of frisks.
'''

# Count the 'search_type' values
print(ri.search_type.value_counts())

# Check if 'search_type' contains the string 'Protective Frisk'
ri['frisk'] = ri.search_type.str.contains('Protective Frisk', na=False)

# Check the data type of 'frisk'
print(ri.frisk.dtype)

# Take the sum of 'frisk'
print(ri.frisk.sum())

