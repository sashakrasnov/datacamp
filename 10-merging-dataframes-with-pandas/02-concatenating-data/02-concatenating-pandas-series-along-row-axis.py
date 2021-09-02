'''
Concatenating pandas Series along row axis

Having learned how to append Series, you'll now learn how to achieve the same result by concatenating Series instead. You'll continue to work with the sales data you've seen previously. This time, the DataFrames jan, feb, and mar have been pre-loaded.

Your job is to use pd.concat() with a list of Series to achieve the same result that you would get by chaining calls to .append().

You may be wondering about the difference between pd.concat() and pandas' .append() method. One way to think of the difference is that .append() is a specific case of a concatenation, while pd.concat() gives you more flexibility, as you'll see in later exercises.

INSTRUCTIONS

*   Create an empty list called units. This has been done for you.
*   Use a for loop to iterate over [jan, feb, mar]:
    *   In each iteration of the loop, append the 'Units' column of each DataFrame to units.
*   Concatenate the Series contained in the list units into a longer Series called quarter1 using pd.concat().
    *   Specify the keyword argument axis='rows' to stack the Series vertically.
*   Verify that quarter1 has the individual Series stacked vertically by printing slices. This has been done for you, so hit 'Submit Answer' to see the result!
'''

import pandas as pd

jan = pd.read_csv('../datasets/sales/sales-jan-2015.csv', parse_dates=True, index_col='Date')
feb = pd.read_csv('../datasets/sales/sales-feb-2015.csv', parse_dates=True, index_col='Date')
mar = pd.read_csv('../datasets/sales/sales-mar-2015.csv', parse_dates=True, index_col='Date')

# ---

# Initialize empty list: units
units = []

# Build the list of Series
for month in [jan, feb, mar]:
    units.append(month['Units'])

# Concatenate the list: quarter1
quarter1 = pd.concat(units, axis='rows')

# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])

'''
Date
2015-01-27 07:11:55    18
2015-02-02 08:33:01     3
2015-02-02 20:54:49     9
Name: Units, dtype: int64
Date
2015-02-26 08:57:45     4
2015-02-26 08:58:51     1
2015-03-06 10:11:45    17
2015-03-06 02:03:56    17
Name: Units, dtype: int64
'''