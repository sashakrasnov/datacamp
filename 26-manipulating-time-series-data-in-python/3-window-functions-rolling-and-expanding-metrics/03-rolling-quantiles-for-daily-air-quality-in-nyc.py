'''
Rolling quantiles for daily air quality in nyc

You learned in the last video how to calculate rolling quantiles to describe changes in the dispersion of a time series over time in a way that is less sensitive to outliers than using the mean and standard deviation.

Let's calculate rolling quantiles - at 10%, 50% (median) and 90% - of the distribution of daily average ozone concentration in NYC using a 360-day rolling window.
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../datasets/air_quality_data/ozone_nyc.csv', index_col='date', parse_dates=['date']).dropna()

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt. We have also loaded the ozone data from 2000-2017 into the variable data.

*   Apply .resample() with daily frequency 'D' to data and apply .interpolate() to fill missing values, and reassign to data.
*   Inspect the result using .info().
*   Create a .rolling() window using 360 periods, select the column 'Ozone', and assign the result to rolling.
*   Insert three new columns, 'q10', 'q50' and 'q90' into data, calculating the respective quantiles from rolling.
*   Plot data.
'''

# Resample, interpolate and inspect ozone data here
data = data.resample('D').interpolate()
print(data.info())

# Create the rolling window
rolling = data.Ozone.rolling(360)

# Insert the rolling quantiles to the monthly returns
data['q10'] = rolling.quantile(.1)
data['q50'] = rolling.quantile(.5)
data['q90'] = rolling.quantile(.9)

# Plot monthly returns
data.plot()
plt.show()
