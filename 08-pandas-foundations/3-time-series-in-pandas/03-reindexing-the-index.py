'''
Reindexing the Index

Reindexing is useful in preparation for adding or otherwise combining two time series data sets. To reindex the data, we provide a new index and ask pandas to try and match the old data to the new index. If data is unavailable for one of the new index dates or times, you must tell pandas how to fill it in. Otherwise, pandas will fill with NaN by default.

In this exercise, two time series data sets containing daily data have been pre-loaded for you, each indexed by dates. The first, ts1, includes weekends, but the second, ts2, does not. The goal is to combine the two data sets in a sensible way. Your job is to reindex the second data set so that it has weekends as well, and then add it to the first. When you are done, it would be informative to inspect your results.
'''

import pandas as pd

time_format = '%Y-%m-%d %H:%M'

date_list = ['2010-01-01 091234', '2010-02-01 101214', '2010-03-03 191234', '2010-04-08 011234', '2010-05-11 021224', '2010-06-01 071734', '2010-07-04 121212', '2010-07-04 131313', '2010-07-04 141414', '2010-07-04 151515', '2010-08-18 181214', '2010-09-01 091234', '2010-10-11 210000', '2010-10-11 212000', '2010-10-11 213000', '2010-10-11 220000', '2010-11-30 221835', '2010-12-21 231235']

temperature_list = [100, 90, 81, 87, 89, 86, 77, 79, 85, 94, 66, 55, 44, 33, 22, 11, 111, 121]

my_datetimes = pd.to_datetime(date_list, format=time_format)

ts0 = pd.Series(temperature_list, index=my_datetimes)

ts1 = ts0.loc['2010-10-11 21:00:00':'2010-10-11 22:00:00']
ts2 = ts0.loc['2010-07-04']

'''
INSTRUCTIONS

*   Create a new time series ts3 by reindexing ts2 with the index of ts1. To do this, call .reindex() on ts2 and pass in the index of ts1 (ts1.index).
*   Create another new time series, ts4, by calling the same .reindex() as above, but also specifiying a fill method, using the keyword argument method="ffill" to forward-fill values.
*   Add ts1 + ts2. Assign the result to sum12.
*   Add ts1 + ts3. Assign the result to sum13.
*   Add ts1 + ts4, Assign the result to sum14.
'''

# Reindex without fill method: ts3
ts3 = ts2.reindex(ts1.index)

# Reindex with fill method, using forward fill: ts4
ts4 = ts2.reindex(ts1.index, method='ffill')

# Combine ts1 + ts2: sum12
sum12 = ts1 + ts2

# Combine ts1 + ts3: sum13
sum13 = ts1 + ts3

# Combine ts1 + ts4: sum14
sum14 = ts1 + ts4

