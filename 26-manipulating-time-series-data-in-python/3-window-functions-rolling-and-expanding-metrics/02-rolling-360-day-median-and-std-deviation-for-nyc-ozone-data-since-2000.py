'''
Rolling 360-day median & std. deviation for nyc ozone data since 2000

The last video also showed you how to calculate several rolling statistics using the .agg() method, similar to .groupby().

Let's take a closer look at the air quality history of NYC using the Ozone data you have seen before. The daily data are very volatile, so using a longer term rolling average can help reveal a longer term trend.

You'll be using a 360 day rolling window, and .agg() to calculate the rolling median and standard deviation for the daily average ozone values since 2000.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

We have already imported pandas as pd, and matplotlib.pyplot as plt.

*   Use pd.read_csv() to import 'ozone.csv', creating a DateTimeIndex from the 'date' column using parse_dates and index_col, assign the result to data, and drop missing values using .dropna().
*   Select the 'Ozone' column and create a .rolling() window using 360 periods, apply .agg() to calculate the mean and std, and assign this to rolling_stats.
*   Use .join() to concatenate data with rolling_stats, and assign to stats.
*   Plot stats using subplots.
'''

# Import and inspect ozone data here
data = pd.read_csv('../datasets/air_quality_data/ozone_nyc.csv', index_col='date', parse_dates=['date']).dropna()
print(data.info())

# Calculate the rolling mean and std here
rolling_stats = data.Ozone.rolling(360).agg(['mean','std'])

# Join rolling_stats with ozone data
stats = data.join(rolling_stats)

# Plot stats
stats.plot(subplots=True)
plt.show()
