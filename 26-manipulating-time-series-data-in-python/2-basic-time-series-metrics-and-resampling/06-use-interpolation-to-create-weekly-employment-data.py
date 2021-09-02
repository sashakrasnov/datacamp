'''
Use interpolation to create weekly employment data

You have recently used the civilian US unemployment rate, and converted it from monthly to weekly frequency using simple forward or backfill methods.

Compare your previous approach to the new .interpolate() method that you learned about in this video.
'''

import pandas as pd
import matplotlib.pyplot as plt

monthly = pd.read_csv('../datasets/stock_data/unrate.csv', index_col='date', parse_dates=['date'])

'''
INSTRUCTIONS

We have imported pandas as pd and matplotlib.pyplot as plt for you. We have also loaded the monthly unemployment rate from 2010 to 2016 into a variable monthly.

*   Inspect monthly using .info().
*   Create a pd.date_range() with weekly dates, using the .min() and .max() of the index of monthly as start and end, respectively, and assign the result to weekly_dates.
*   Apply .reindex() using weekly_dates to monthly and assign the output to weekly.
*   Create new columns 'ffill' and 'interpolated' by applying .ffill() and .interpolate() to weekly.UNRATE.
*   Show a plot of weekly.
'''

# Inspect data here
print(monthly.info())

# Create weekly dates
weekly_dates = pd.date_range(start=monthly.index.min(), end=monthly.index.max(), freq='W')

# Reindex monthly to weekly data
weekly = monthly.reindex(weekly_dates)

# Create ffill and interpolated columns
weekly['ffill'] = weekly.UNRATE.ffill()
weekly['interpolated'] = weekly.UNRATE.interpolate()

# Plot weekly
weekly.plot()
plt.show()