'''
Comparing arrest rates by weather rating

Do police officers arrest drivers more often when the weather is bad? Find out below!

*   First, you'll calculate the overall arrest rate.
*   Then, you'll calculate the arrest rate for each of the weather ratings you previously assigned.
*   Finally, you'll add violation type as a second factor in the analysis, to see if that accounts for any differences in the arrest rate.

Since you previously defined a logical order for the weather categories, good < bad < worse, they will be sorted that way in the results.
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

'''
INSTRUCTIONS 1/3

Calculate the overall arrest rate by taking the mean of the is_arrested Series.
'''

# Calculate the overall arrest rate
print(ri_weather.is_arrested.mean())

'''
INSTRUCTIONS 2/3

Calculate the arrest rate for each weather rating using a .groupby().
'''

# Calculate the arrest rate for each 'rating'
print(ri_weather.groupby('rating').is_arrested.mean())

'''
INSTRUCTIONS 3/3

Calculate the arrest rate for each combination of violation and rating. How do the arrest rates differ by group?
'''

# Calculate the arrest rate for each 'violation' and 'rating'
print(ri_weather.groupby(['violation', 'rating']).is_arrested.mean())