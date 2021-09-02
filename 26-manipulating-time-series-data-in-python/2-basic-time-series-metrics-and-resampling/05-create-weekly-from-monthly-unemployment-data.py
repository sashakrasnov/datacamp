'''
Create weekly from monthly unemployment data

The civilian US unemployment rate is reported monthly. You may need more frequent data, but that's no problem because you just learned how to upsample a time series.

You'll work with the time series data for the last 20 years, and apply a few options to fill in missing values before plotting the weekly series.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt.

*   Use pd.read_csv() to import 'unemployment.csv', creating a DateTimeIndex from the 'date' column using parse_dates and index_col, and assign the result to data.
*   Convert data to weekly frequency using .asfreq() with the alias 'W' and show the first five rows.
*   Convert again to weekly frequency, adding the option 'bfill' and show the first five rows.
*   Create weekly series, now adding the option 'ffill', assign to weekly_ffill and show the first five rows.
*   Plot weekly_ffill starting in 2015.
'''

# Import data here
data = pd.read_csv('../datasets/stock_data/unrate.csv', index_col='date', parse_dates=['date'])

# Show first five rows of weekly series
print(data.asfreq('W').head())

# Show first five rows of weekly series with bfill option
print(data.asfreq('W', method='bfill').head())

# Create weekly series with ffill option and show first five rows
weekly_ffill = data.asfreq('W', method='ffill')
print(weekly_ffill.head())

# Plot weekly_fill starting 2015 here 
weekly_ffill['2015':].plot()
plt.show()