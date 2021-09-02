'''
Computing percentage growth of GDP

Your job in this exercise is to compute the yearly percent-change of US GDP (Gross Domestic Product) since 2008.

The data has been obtained from the Federal Reserve Bank of St. Louis and is available in the file GDP.csv, which contains quarterly data; you will resample it to annual sampling and then compute the annual growth of GDP. For a refresher on resampling, check out the relevant material from pandas Foundations.

INSTRUCTIONS

*   Read the file 'GDP.csv' into a DataFrame called gdp.
*   Use parse_dates=True and index_col='DATE'.
*   Create a DataFrame post2008 by slicing gdp such that it comprises all rows from 2008 onward.
*   Print the last 8 rows of the slice post2008. This has been done for you. This data has quarterly frequency so the indices are separated by three-month intervals.
*   Create the DataFrame yearly by resampling the slice post2008 by year. Remember, you need to chain .resample() (using the alias 'A' for annual frequency) with some kind of aggregation; you will use the aggregation method .last() to select the last element when resampling.
*   Compute the percentage growth of the resampled DataFrame yearly with .pct_change() * 100.
'''

import pandas as pd

# Read 'GDP.csv' into a DataFrame: gdp
gdp = pd.read_csv('../datasets/gdp/gdp_usa.csv', parse_dates=True, index_col='DATE')

# Slice all the gdp data from 2008 onward: post2008
post2008 = gdp.loc['2008':]

# Print the last 8 rows of post2008
print(post2008.tail(8))

# Resample post2008 by year, keeping last(): yearly
yearly = post2008.resample('A').last()

# Print yearly
print(yearly)

# Compute percentage growth of yearly: yearly['growth']
yearly['growth'] = yearly.pct_change() * 100

# Print yearly again
print(yearly)

'''
> post2008.tail(8)
              VALUE          
DATE                         
2014-07-01  17569.4          
2014-10-01  17692.2          
2015-01-01  17783.6          
2015-04-01  17998.3          
2015-07-01  18141.9          
2015-10-01  18222.8          
2016-01-01  18281.6          
2016-04-01  18436.5          

> yearly
              VALUE          
DATE                         
2008-12-31  14549.9          
2009-12-31  14566.5          
2010-12-31  15230.2          
2011-12-31  15785.3          
2012-12-31  16297.3          
2013-12-31  16999.9          
2014-12-31  17692.2          
2015-12-31  18222.8          
2016-12-31  18436.5          

> yearly
              VALUE    growth
DATE                         
2008-12-31  14549.9       NaN
2009-12-31  14566.5  0.114090
2010-12-31  15230.2  4.556345
2011-12-31  15785.3  3.644732
2012-12-31  16297.3  3.243524
2013-12-31  16999.9  4.311144
2014-12-31  17692.2  4.072377
2015-12-31  18222.8  2.999062
2016-12-31  18436.5  1.172707
'''