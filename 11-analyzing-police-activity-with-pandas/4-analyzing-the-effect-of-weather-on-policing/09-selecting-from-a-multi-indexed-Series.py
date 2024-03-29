'''
Selecting from a multi-indexed Series

The output of a single .groupby() operation on multiple columns is a Series with a MultiIndex. Working with this type of object is similar to working with a DataFrame:

*   The outer index level is like the DataFrame rows.
*   The inner index level is like the DataFrame columns.

In this exercise, you'll practice accessing data from a multi-indexed Series using the .loc[] accessor.
'''

import pandas as pd

ri = pd.read_csv('../datasets/RI_cleaned.csv', low_memory=False)

ri.drop(['county_name', 'state'], axis='columns', inplace=True)
ri.dropna(subset=['driver_gender'], inplace=True)

ri['is_arrested'] = ri.is_arrested.astype('bool')
ri['stop_datetime'] = pd.to_datetime(ri.stop_date.str.cat(ri.stop_time, sep=' '))

ri.set_index('stop_datetime', inplace=True)

ri.loc[(ri['stop_duration']=='1') | (ri['stop_duration']=='2'), 'stop_duration'] = '0-15 Min'

ri['stop_minutes'] = ri.stop_duration.map({
                        '0-15 Min': 8,
                        '16-30 Min': 23,
                        '30+ Min': 45
                    })

weather = pd.read_csv('../datasets/weather.csv')

WT = weather.loc[:, 'WT01':'WT22']

weather['bad_conditions'] = WT.sum(axis='columns')
weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

mapping = {
    0: 'good',
    1: 'bad',
    2: 'bad',
    3: 'bad',
    4: 'bad',
    5: 'worse',
    6: 'worse',
    7: 'worse',
    8: 'worse',
    9: 'worse'
}

cats = ['good', 'bad', 'worse']

weather['rating'] = pd.Categorical(weather.bad_conditions.map(mapping), ordered=True, categories=cats)

ri.reset_index(inplace=True)

weather_rating = weather[['DATE', 'rating']]

ri_weather = pd.merge(left=ri, right=weather_rating, left_on='stop_date', right_on='DATE', how='left')

ri_weather.set_index('stop_datetime', inplace=True)

'''
INSTRUCTIONS

*   Save the output of the .groupby() operation from the last exercise as a new object, arrest_rate. (This has been done for you.)
*   Print the arrest_rate Series and examine it.
*   Print the arrest rate for moving violations in bad weather.
*   Print the arrest rates for speeding violations in all three weather conditions.
'''

# Save the output of the groupby operation from the last exercise
arrest_rate = ri_weather.groupby(['violation', 'rating']).is_arrested.mean()

# Print the 'arrest_rate' Series
print(arrest_rate)

# Print the arrest rate for moving violations in bad weather
print(arrest_rate['Moving violation', 'bad'])

# Print the arrest rates for speeding violations in all three weather conditions
print(arrest_rate['Speeding'])