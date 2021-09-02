'''
Load multiple time series

Whether it is during personal projects or your day-to-day work as a Data Scientist, it is likely that you will encounter situations that require the analysis and visualization of multiple time series at the same time.

Provided that the data for each time series is stored in distinct columns of a file, the pandas library makes it easy to work with multiple time series. In the following exercises, you will work with a new time series dataset that contains the amount of different types of meat produced in the USA between 1944 and 2012.
'''

import pandas as pd

url_meat = '../datasets/ch4_meat.csv'

'''
INSTRUCTIONS

We've imported pandas using the pd alias.

*   Read in the the csv file located at url_meat into a DataFrame called meat.
*   Convert the date column in meat to the datetime type.
*   Set the date column as the index of meat.
*   Print the summary statistics of all the numeric columns in meat.
'''

# Read in meat DataFrame
meat = pd.read_csv(url_meat)

# Review the first five lines of the meat DataFrame
print(meat.head(5))

# Convert the date column to a datestamp type
meat['date'] = pd.to_datetime(meat['date'])

# Set the date column as the index of your DataFrame meat
meat = meat.set_index('date')

# Print the summary statistics of the DataFrame
print(meat.describe())