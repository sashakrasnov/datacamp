'''
Preparing the DataFrames

In this exercise, you'll prepare the traffic stop and weather rating DataFrames so that they're ready to be merged:

1.  With the ri DataFrame, you'll move the stop_datetime index to a column since the index will be lost during the merge.
2.  With the weather DataFrame, you'll select the DATE and rating columns and put them in a new DataFrame.
'''

import pandas as pd

ri = pd.read_csv('../datasets/RI_cleaned.csv', low_memory=False)

ri.drop(['county_name', 'state'], axis='columns', inplace=True)
ri.dropna(subset=['driver_gender'], inplace=True)

ri['is_arrested'] = ri.is_arrested.astype('bool')
ri['stop_datetime'] = pd.to_datetime(ri.stop_date.str.cat(ri.stop_time, sep=' '))

ri.set_index('stop_datetime', inplace=True)

ri.loc[(ri['stop_duration']=='1') | (ri['stop_duration']=='2'), 'stop_duration'] = '0-15 Min'

ri['stop_minutes'] = ri.stop_duration.map({'0-15 Min': 8, '16-30 Min':23, '30+ Min': 45})

weather = pd.read_csv('../datasets/weather.csv')

WT = weather.loc[:, 'WT01':'WT22']

weather['bad_conditions'] = WT.sum(axis='columns')
weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

mapping = {0:'good', 1:'bad', 2:'bad', 3:'bad', 4:'bad', 5:'worse', 6:'worse', 7:'worse', 8:'worse', 9:'worse'}
cats = ['good', 'bad', 'worse']

weather['rating'] = pd.Categorical(weather.bad_conditions.map(mapping), ordered=True, categories=cats)

'''
INSTRUCTIONS

*   Reset the index of the ri DataFrame.
*   Examine the head of ri to verify that stop_datetime is now a DataFrame column, and the index is now the default integer index.
*   Create a new DataFrame named weather_rating that contains only the DATE and rating columns from the weather DataFrame.
*   Examine the head of weather_rating to verify that it contains the proper columns.
'''

# Reset the index of 'ri'
ri.reset_index(inplace=True)

# Examine the head of 'ri'
print(ri.head())

# Create a DataFrame from the 'DATE' and 'rating' columns
weather_rating = weather[['DATE', 'rating']]

# Examine the head of 'weather_rating'
print(weather_rating.head())
