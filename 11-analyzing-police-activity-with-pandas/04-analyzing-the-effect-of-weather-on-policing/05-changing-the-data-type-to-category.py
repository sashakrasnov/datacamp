'''
Changing the data type to category

Since the rating column only has a few possible values, you'll change its data type to category in order to store the data more efficiently. You'll also specify a logical order for the categories, which will be useful for future exercises.
'''

import pandas as pd

weather = pd.read_csv('../datasets/weather.csv')

WT = weather.loc[:, 'WT01':'WT22']

weather['bad_conditions'] = WT.sum(axis='columns')
weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

mapping = {0:'good', 1:'bad', 2:'bad', 3:'bad', 4:'bad', 5:'worse', 6:'worse', 7:'worse', 8:'worse', 9:'worse'}

weather['rating'] = weather.bad_conditions.map(mapping)

'''
INSTRUCTIONS

*   Create a list object called cats that lists the weather ratings in a logical order: 'good', 'bad', 'worse'.
*   Change the data type of the rating column from object to category. Make sure to use the cats list to define the category ordering.
*   Examine the head of the rating column to confirm that the categories are logically ordered.
'''

# Create a list of weather ratings in logical order
cats = ['good', 'bad', 'worse']

# Change the data type of 'rating' to category. *) As for now it is depricated
#weather['rating'] = weather.rating.astype('category', ordered=True, categories=cats)
# New, recommended style
weather['rating'] = pd.Categorical(weather['rating'], ordered=True, categories=cats)

# Examine the head of 'rating'
print(weather.rating.head())