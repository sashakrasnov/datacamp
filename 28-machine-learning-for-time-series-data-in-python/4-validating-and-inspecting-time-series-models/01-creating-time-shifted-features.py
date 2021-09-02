'''
Creating time-shifted features

In machine learning for time series, it's common to use information about previous time points to predict a subsequent time point.

In this exercise, you'll "shift" your raw data and visualize the results. You'll use the percent change time series that you calculated in the previous chapter, this time with a very short window. A short window is important because, in a real-world scenario, you want to predict the day-to-day fluctuations of a time series, not its change over a longer window of time.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def percent_change(series):
    # Collect all *but* the last value of this window, then the final value
    previous_values = series[:-1]
    last_value = series[-1]

    # Calculate the % difference between the last value and the mean of earlier values
    percent_change = (last_value - np.mean(previous_values)) / np.mean(previous_values)
    return percent_change


def replace_outliers(series):

    # Calculate a mask for values that are > 3 standard deviations after centering
    this_mask = np.abs(series - np.mean(series)) > (np.std(series) * 3)
    
    # Replace these values with the median accross the data
    #series[this_mask] = np.nanmedian(series)
    return series


prices = pd.read_csv('../datasets/prices_messy.csv', index_col=0, parse_dates=True)[['AAPL']]

prices_perc = prices.rolling(20).apply(percent_change, raw=False)
prices_perc = prices_perc['AAPL'].apply(replace_outliers)

'''
INSTRUCTIONS

*   Use a dictionary comprehension to create multiple time-shifted versions of prices_perc using the lags specified in shifts.
*   Convert the result into a DataFrame.
*   Use the given code to visualize the results.
'''

# These are the "time lags"
shifts = np.arange(1, 11).astype(int)

# Use a dictionary comprehension to create name: value pairs, one pair per shift
shifted_data = {"lag_{}_day".format(day_shift): prices_perc.shift(day_shift) for day_shift in shifts}

# Convert into a DataFrame for subsequent use
prices_perc_shifted = pd.DataFrame(shifted_data)

# Plot the first 100 samples of each
ax = prices_perc_shifted.iloc[:100].plot(cmap=plt.cm.viridis)
prices_perc.iloc[:100].plot(color='r', lw=2)
ax.legend(loc='best')
plt.show()