'''
Converting stop durations to numbers

In the traffic stops dataset, the stop_duration column tells you approximately how long the driver was detained by the officer. Unfortunately, the durations are stored as strings, such as '0-15 Min'. How can you make this data easier to analyze?

In this exercise, you'll convert the stop durations to integers. Because the precise durations are not available, you'll have to estimate the numbers using reasonable values:

*   Convert '0-15 Min' to 8
*   Convert '16-30 Min' to 23
*   Convert '30+ Min' to 45
'''

import pandas as pd

ri = pd.read_csv('../datasets/RI_cleaned.csv', low_memory=False)

ri.drop(['county_name', 'state'], axis='columns', inplace=True)
ri.dropna(subset=['driver_gender'], inplace=True)

ri['is_arrested'] = ri.is_arrested.astype('bool')

combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
ri['stop_datetime'] = pd.to_datetime(combined)

ri.set_index('stop_datetime', inplace=True)

ri.loc[(ri['stop_duration']=='1') | (ri['stop_duration']=='2'), 'stop_duration'] = '0-15 Min'

'''
INSTRUCTIONS

*   Print the unique values in the stop_duration column. (This has been done for you.)
*   Create a dictionary called mapping that maps the stop_duration strings to the integers specified above.
*   Convert the stop_duration strings to integers using the mapping, and store the results in a new column called stop_minutes.
*   Print the unique values in the stop_minutes column, to verify that the durations were properly converted to integers.
'''

# Print the unique values in 'stop_duration'
print(ri.stop_duration.unique())

# Create a dictionary that maps strings to integers
mapping = {'0-15 Min': 8, '16-30 Min':23, '30+ Min': 45}

# Convert the 'stop_duration' strings to integers using the 'mapping'
ri['stop_minutes'] = ri.stop_duration.map(mapping)

# Print the unique values in 'stop_minutes'
print(ri.stop_minutes.unique())