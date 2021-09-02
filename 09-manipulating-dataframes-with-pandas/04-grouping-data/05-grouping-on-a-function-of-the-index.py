'''
Grouping on a function of the index

Groubpy operations can also be performed on transformations of the index values. In the case of a DateTimeIndex, we can extract portions of the datetime over which to group.

In this exercise you'll read in a set of sample sales data from February 2015 and assign the 'Date' column as the index. Your job is to group the sales data by the day of the week and aggregate the sum of the 'Units' column.

Is there a day of the week that is more popular for customers? To find out, you're going to use .strftime('%a') to transform the index datetime values to abbreviated days of the week.

The sales data CSV file is available to you as 'sales.csv'.

INSTRUCTIONS

*   Read 'sales.csv' into a DataFrame with index_col='Date' and parse_dates=True.
*   Create a groupby object with sales.index.strftime('%a') as input and assign it to by_day.
*   Aggregate the 'Units' column of by_day with the .sum() method. Save the result as units_sum.
*   Print units_sum. This has been done for you, so hit 'Submit Answer' to see the result.
'''

import pandas as pd

# ---

# Read file: sales
sales = pd.read_csv('../datasets/sales-feb-2015.csv', index_col='Date', parse_dates=True)

# Create a groupby object: by_day
by_day = sales.groupby(sales.index.strftime('%a'))

# Create sum: units_sum
units_sum = by_day['Units'].sum()

# Print units_sum
print(units_sum)

'''
> sales
                             Company   Product  Units
Date                                                 
2015-02-02 08:30:00            Hooli  Software      3
2015-02-02 21:00:00        Mediacore  Hardware      9
2015-02-03 14:00:00          Initech  Software     13
2015-02-04 15:30:00        Streeplex  Software     13
2015-02-04 22:00:00  Acme Coporation  Hardware     14
2015-02-05 02:00:00  Acme Coporation  Software     19
2015-02-05 22:00:00            Hooli   Service     10
2015-02-07 23:00:00  Acme Coporation  Hardware      1
2015-02-09 09:00:00        Streeplex   Service     19
2015-02-09 13:00:00        Mediacore  Software      7
2015-02-11 20:00:00          Initech  Software      7
2015-02-11 23:00:00            Hooli  Software      4
2015-02-16 12:00:00            Hooli  Software     10
2015-02-19 11:00:00        Mediacore  Hardware     16
2015-02-19 16:00:00        Mediacore   Service     10
2015-02-21 05:00:00        Mediacore  Software      3
2015-02-21 20:30:00            Hooli  Hardware      3
2015-02-25 00:30:00          Initech   Service     10
2015-02-26 09:00:00        Streeplex   Service      4

> units_sum
Mon    48
Sat     7
Thu    59
Tue    13
Wed    48
Name: Units, dtype: int64
'''