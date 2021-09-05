'''
Missing values and interpolation

One common application of interpolation in data analysis is to fill in missing data.

In this exercise, noisy measured data that has some dropped or otherwise missing values has been loaded. The goal is to compare two time series, and then look at summary statistics of the differences. The problem is that one of the data sets is missing data at some of the times. The pre-loaded data ts1 has value for all times, yet the data set ts2 does not: it is missing data for the weekends.

Your job is to first interpolate to fill in the data for all days. Then, compute the differences between the two data sets, now that they both have full support for all times. Finally, generate the summary statistics that describe the distribution of differences.
'''

import pandas as pd
import numpy as np

time_format = '%Y-%m-%d %H:%M'

date_list = ['2010-01-01 091234', '2010-02-01 101214', '2010-03-03 191234', '2010-04-08 011234', '2010-05-11 021224', '2010-06-01 071734', '2010-07-04 121212', '2010-07-04 131313', '2010-07-04 141414', '2010-07-04 151515', '2010-08-18 181214', '2010-09-01 091234', '2010-10-11 210000', '2010-10-11 212000', '2010-10-11 213000', '2010-10-11 220000', '2010-11-30 221835', '2010-12-21 231235']

temperature_list = [100, 90, 81, 87, 89, 86, 77, 79, 85, 94, 66, 55, 44, 33, 22, 11, 111, 121]

my_datetimes = pd.to_datetime(date_list, format=time_format)

ts0 = pd.Series(temperature_list, index=my_datetimes)

ts1 = ts0.loc['2010-10-11 21:00:00':'2010-10-11 22:00:00']
ts2 = ts0.loc['2010-09-11':'2010-11-11']

'''
INSTRUCTIONS

*   Replace the index of ts2 with that of ts1, and then fill in the missing values of ts2 by using .interpolate(how='linear'). Save the result as ts2_interp.
*   Compute the difference between ts1 and ts2_interp. Take the absolute value of the difference with np.abs(), and assign the result to differences.
*   Generate and print summary statistics of the differences with .describe() and print().
'''

# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate(how='linear')

# Compute the absolute difference of ts1 and ts2_interp: differences 
differences = np.abs(ts1 - ts2_interp)

# Generate and print summary statistics of the differences
print(differences.describe())
