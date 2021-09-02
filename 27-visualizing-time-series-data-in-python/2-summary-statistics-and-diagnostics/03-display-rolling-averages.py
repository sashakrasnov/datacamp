'''
Display rolling averages

It is also possible to visualize rolling averages of the values in your time series. This is equivalent to "smoothing" your data, and can be particularly useful when your time series contains a lot of noise or outliers. For a given DataFrame df, you can obtain the rolling average of the time series by using the command:

|   df_mean = df.rolling(window=12).mean()

The window parameter should be set according to the granularity of your time series. For example, if your time series contains daily data and you are looking for rolling values over a whole year, you should specify the parameter to window=365. In addition, it is easy to get rolling values for other other metrics, such as the standard deviation (.std()) or variance (.var()).
'''

import pandas as pd
import matplotlib.pyplot as plt

co2_levels = pd.read_csv('../datasets/ch2_co2_levels.csv', index_col=0, parse_dates=True)
co2_levels = co2_levels.fillna(method='bfill')

'''
INSTRUCTIONS

*   Compute the 52 weeks rolling mean of co2_levels and assign it to ma.
*   Compute the 52 weeks rolling standard deviation of co2_levels and assign it to mstd.
*   Calculate the upper bound of time series which can defined as the rolling mean + (2 * rolling standard deviation) and assign it to ma[upper]. Similarly, calculate the lower bound as the rolling mean - (2 * rolling standard deviation) and assign it to ma[lower].
*   Plot the line chart of ma.
'''

# Compute the 52 weeks rolling mean of the co2_levels DataFrame
ma = co2_levels.rolling(window=52).mean()

# Compute the 52 weeks rolling standard deviation of the co2_levels DataFrame
mstd = co2_levels.rolling(window=52).std()

# Add the upper bound column to the ma DataFrame
ma['upper'] = ma['co2'] + (2 * mstd['co2'])

# Add the lower bound column to the ma DataFrame
ma['lower'] = ma['co2'] - (2 * mstd['co2'])

# Plot the content of the ma DataFrame
ax = ma.plot(linewidth=0.8, fontsize=6)

# Specify labels, legend, and show the plot
ax.set_xlabel('Date', fontsize=10)
ax.set_ylabel('CO2 levels in Mauai Hawaii', fontsize=10)
ax.set_title('Rolling mean and variance of CO2 levels\nin Mauai Hawaii from 1958 to 2001', fontsize=10)
plt.show()