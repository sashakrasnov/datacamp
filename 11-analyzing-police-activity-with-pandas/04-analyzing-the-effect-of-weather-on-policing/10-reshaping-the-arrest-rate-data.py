'''
Reshaping the arrest rate data

In this exercise, you'll start by reshaping the arrest_rate Series into a DataFrame. This is a useful step when working with any multi-indexed Series, since it enables you to access the full range of DataFrame methods.

Then, you'll create the exact same DataFrame using a pivot table. This is a great example of how pandas often gives you more than one way to reach the same result!
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

ri.reset_index(inplace=True)

weather_rating = weather[['DATE', 'rating']]

ri_weather = pd.merge(left=ri, right=weather_rating, left_on='stop_date', right_on='DATE', how='left')

ri_weather.set_index('stop_datetime', inplace=True)

arrest_rate = ri_weather.groupby(['violation', 'rating']).is_arrested.mean()

'''
INSTRUCTIONS

*   Unstack the arrest_rate Series to reshape it into a DataFrame.
*   Create the exact same DataFrame using a pivot table! Each of the three .pivot_table() parameters should be specified as one of the ri_weather columns.
'''

# Unstack the 'arrest_rate' Series into a DataFrame
print(arrest_rate.unstack())

# Create the same DataFrame using a pivot table
print(ri_weather.pivot_table(index='violation', columns='rating', values='is_arrested'))