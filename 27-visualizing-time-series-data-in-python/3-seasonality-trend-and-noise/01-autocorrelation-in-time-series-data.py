'''
Autocorrelation in time series data

In the field of time series analysis, autocorrelation refers to the correlation of a time series with a lagged version of itself. For example, an autocorrelation of order 3 returns the correlation between a time series and its own values lagged by 3 time points.

It is common to use the autocorrelation (ACF) plot, also known as self-autocorrelation, to visualize the autocorrelation of a time-series. The plot_acf() function in the statsmodels library can be used to measure and plot the autocorrelation of a time series.
'''

import pandas as pd
import matplotlib.pyplot as plt

co2_levels = pd.read_csv('../datasets/ch2_co2_levels.csv', index_col=0, parse_dates=True)
co2_levels = co2_levels.fillna(method='bfill')

'''
INSTRUCTIONS

*   Import tsaplots from statsmodels.graphics.
*   Use the plot_acf() function from tsaplots to plot the autocorrelation of the 'co2' column in co2_levels.
*   Specify a maximum lag of 24.
'''

# Import required libraries
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from statsmodels.graphics import tsaplots

# Display the autocorrelation plot of your time series
fig = tsaplots.plot_acf(co2_levels['co2'], lags=24)

# Show plot
plt.show()