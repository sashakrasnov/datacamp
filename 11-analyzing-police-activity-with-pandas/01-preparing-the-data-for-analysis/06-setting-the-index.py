'''
The last step that you'll take in this chapter is to set the stop_datetime column as the DataFrame's index. By replacing the default index with a DatetimeIndex, you'll make it easier to analyze the dataset by date and time, which will come in handy later in the course!

INSTRUCTIONS

*   Set stop_datetime as the DataFrame index.
*   Examine the index to verify that it is a DatetimeIndex.
*   Examine the DataFrame columns to confirm that stop_datetime is no longer one of the columns.
'''

import pandas as pd

ri = pd.read_csv('../datasets/RI_cleaned.csv', nrows=100000, low_memory=False)

ri.drop(['county_name', 'state'], axis='columns', inplace=True)
ri.dropna(subset=['driver_gender'], inplace=True)

ri['is_arrested'] = ri.is_arrested.astype('bool')

combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
ri['stop_datetime'] = pd.to_datetime(combined)

# ---

# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Examine the index
print(ri.index)

# Examine the columns
print(ri.columns)