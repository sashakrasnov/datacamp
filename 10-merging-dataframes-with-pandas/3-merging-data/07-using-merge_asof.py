'''
Using merge_asof()

Similar to pd.merge_ordered(), the pd.merge_asof() function will also merge values in order using the on column, but for each row in the left DataFrame, only rows from the right DataFrame whose 'on' column values are less than the left value will be kept.

This function can be use to align disparate datetime frequencies without having to first resample.

Here, you'll merge monthly oil prices (US dollars) into a full automobile fuel efficiency dataset. The oil and automobile DataFrames have been pre-loaded as oil and auto. The first 5 rows of each have been printed in the IPython Shell for you to explore.

These datasets will align such that the first price of the year will be broadcast into the rows of the automobiles DataFrame. This is considered correct since by the start of any given year, most automobiles for that year will have already been manufactured.

You'll then inspect the merged DataFrame, resample by year and compute the mean 'Price' and 'mpg'. You should be able to see a trend in these two columns, that you can confirm by computing the Pearson correlation between resampled 'Price' and 'mpg'.

INSTRUCTIONS

*   Merge auto and oil using pd.merge_asof() with left_on='yr' and right_on='Date'. Store the result as merged.
*   Print the tail of merged. This has been done for you.
*   Resample merged using 'A' (annual frequency), and on='Date'. Select [['mpg','Price']] and aggregate the mean. Store the result as yearly.
*   Hit Submit Answer to examine the contents of yearly and yearly.corr(), which shows the Pearson correlation between the resampled 'Price' and 'mpg'.
'''

import pandas as pd

oil = pd.read_csv('../datasets/oil_price.csv', parse_dates=True)
oil['Date'] = pd.to_datetime(oil['Date'])

auto = pd.read_csv('../datasets/automobiles.csv', parse_dates=True)
auto['yr'] = pd.to_datetime(auto['yr'])

# Merge auto and oil: merged
merged = pd.merge_asof(auto, oil, left_on='yr', right_on='Date')

# Print the tail of merged
print(merged.tail())

# Resample merged: yearly
yearly = merged.resample('A',on='Date')[['mpg','Price']].mean()

# Print yearly
print(yearly)

# Print yearly.corr()
print(yearly.corr())

'''
> merged.tail()
      mpg  cyl  displ  hp  weight  accel         yr  origin             name       Date  Price
387  27.0    4  140.0  86    2790   15.6 1982-01-01      US  ford mustang gl 1982-01-01  33.85
388  44.0    4   97.0  52    2130   24.6 1982-01-01  Europe        vw pickup 1982-01-01  33.85
389  32.0    4  135.0  84    2295   11.6 1982-01-01      US    dodge rampage 1982-01-01  33.85
390  28.0    4  120.0  79    2625   18.6 1982-01-01      US      ford ranger 1982-01-01  33.85
391  31.0    4  119.0  82    2720   19.4 1982-01-01      US       chevy s-10 1982-01-01  33.85

> yearly
                  mpg  Price
Date
1970-12-31  17.689655   3.35
1971-12-31  21.111111   3.56
1972-12-31  18.714286   3.56
1973-12-31  17.100000   3.56
1974-12-31  22.769231  10.11
1975-12-31  20.266667  11.16
1976-12-31  21.573529  11.16
1977-12-31  23.375000  13.90
1978-12-31  24.061111  14.85
1979-12-31  25.093103  14.85
1980-12-31  33.803704  32.50
1981-12-31  30.185714  38.00
1982-12-31  32.000000  33.85

> yearly.corr()
            mpg     Price
mpg    1.000000  0.948677
Price  0.948677  1.000000
'''