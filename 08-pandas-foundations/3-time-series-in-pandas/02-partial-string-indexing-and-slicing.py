'''
Partial string indexing and slicing

Pandas time series support "partial string" indexing. What this means is that even when passed only a portion of the datetime, such as the date but not the time, pandas is remarkably good at doing what one would expect. Pandas datetime indexing also supports a wide variety of commonly used datetime string formats, even when mixed.

In this exercise, a time series that contains hourly weather data has been pre-loaded for you. This data was read using the parse_dates=True option in read_csv() with index_col="Dates" so that the Index is indeed a DatetimeIndex.

All data from the 'Temperature' column has been extracted into the variable ts0. Your job is to use a variety of natural date strings to extract one or more values from ts0.

After you are done, you will have three new variables - ts1, ts2, and ts3. You can slice these further to extract only the first and last entries of each. Try doing this after your submission for more practice.
'''

import pandas as pd

time_format = '%Y-%m-%d %H:%M'

date_list = ['2010-01-01 091234', '2010-02-01 101214', '2010-03-03 191234', '2010-04-08 011234', '2010-05-11 021224', '2010-06-01 071734', '2010-07-04 121212', '2010-08-18 181214', '2010-09-01 091234', '2010-10-11 210000', '2010-10-11 212000', '2010-10-11 213000', '2010-10-11 220000', '2010-11-30 221835', '2010-12-21 231235']

temperature_list = [100, 90, 80, 77, 79, 85, 94, 66, 55, 44, 33, 22, 11, 111, 121]

my_datetimes = pd.to_datetime(date_list, format=time_format)

ts0 = pd.Series(temperature_list, index=my_datetimes)

'''
INSTRUCTIONS

*   Extract data from ts0 for a single hour - the hour from 9pm to 10pm on 2010-10-11. Assign it to ts1.
*   Extract data from ts0 for a single day - July 4th, 2010 - and assign it to ts2.
*   Extract data from ts0 for the second half of December 2010 - 12/15/2010 to 12/31/2010. Assign it to ts3.
'''

# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = ts0.loc['2010-10-11 21:00:00':'2010-10-11 22:00:00']

# Extract '2010-07-04' from ts0: ts2
ts2 = ts0.loc['2010-07-04']

# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = ts0.loc['2010-12-15':'2010-12-31']
