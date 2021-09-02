'''
Rating the weather conditions

In the previous exercise, you counted the number of bad weather conditions each day. In this exercise, you'll use the counts to create a rating system for the weather.

The counts range from 0 to 9, and should be converted to ratings as follows:

*   Convert 0 to 'good'
*   Convert 1 through 4 to 'bad'
*   Convert 5 through 9 to 'worse'
'''

import pandas as pd

weather = pd.read_csv('../datasets/weather.csv')

WT = weather.loc[:, 'WT01':'WT22']

weather['bad_conditions'] = WT.sum(axis='columns')
weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

'''
INSTRUCTIONS

*   Count the unique values in the bad_conditions column and sort the index. (This has been done for you.)
*   Create a dictionary called mapping that maps the bad_conditions integers to strings as specified above.
*   Convert the bad_conditions integers to strings using the mapping and store the results in a new column called rating.
*   Count the unique values in rating to verify that the integers were properly converted to strings.
'''

# Count the unique values in 'bad_conditions' and sort the index
print(weather.bad_conditions.value_counts().sort_index())

# Create a dictionary that maps integers to strings
mapping = {0:'good', 1:'bad', 2:'bad', 3:'bad', 4:'bad', 5:'worse', 6:'worse', 7:'worse', 8:'worse', 9:'worse'}

# Convert the 'bad_conditions' integers to strings using the 'mapping'
weather['rating'] = weather.bad_conditions.map(mapping)

# Count the unique values in 'rating'
print(weather.rating.value_counts())