'''
Creating and using a DatetimeIndex

The pandas Index is a powerful way to handle time series data, so it is valuable to know how to build one yourself. Pandas provides the pd.to_datetime() function for just this task. For example, if passed the list of strings ['2010-01-01 091234','2010-01-01 091234'] and a format specification variable, such as format='%Y-%m-%d %H%M%S, pandas will parse the string into the proper datetime elements and build the datetime objects.

In this exercise, a list of temperature data and a list of date strings has been pre-loaded for you as temperature_list and date_list respectively. Your job is to use the .to_datetime() method to build a DatetimeIndex out of the list of date strings, and to then use it along with the list of temperature data to build a pandas Series.
'''

import pandas as pd

date_list = ['2010-01-01 091234', '2010-02-01 101214', '2010-03-03 191234', '2010-04-08 011234', '2010-05-11 021224', '2010-06-01 071734', '2010-07-02 121212', '2010-08-18 181214', '2010-09-01 091234', '2010-10-11 211135', '2010-11-30 221835', '2010-12-21 231235']

temperature_list = [100, 90, 80, 77, 66, 55, 44, 33, 22, 11, 111, 121]

'''
INSTRUCTIONS

*   Prepare a format string, time_format, using '%Y-%m-%d %H:%M' as the desired format.
*   Convert date_list into a datetime object by using the pd.to_datetime() function. Specify the format string you defined above and assign the result to my_datetimes.
*   Construct a pandas Series called time_series using pd.Series() with temperature_list and my_datetimes. Set the index of the Series to be my_datetimes.
'''

# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(date_list, format=time_format)

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list, index=my_datetimes)
