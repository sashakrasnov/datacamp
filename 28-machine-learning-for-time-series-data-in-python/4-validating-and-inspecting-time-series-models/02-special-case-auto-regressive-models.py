'''
Special case: Auto-regressive models

Now that you've created time-shifted versions of a single time series, you can fit an auto-regressive model. This is a regression model where the input features are time-shifted versions of the output time series data. You are using previous values of a timeseries to predict current values of the same timeseries (thus, it is auto-regressive).

By investigating the coefficients of this model, you can explore any repetitive patterns that exist in a timeseries, and get an idea for how far in the past a data point is predictive of the future.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge

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

shifts = np.arange(1, 11).astype(int)
shifted_data = {"lag_{}_day".format(day_shift): prices_perc.shift(day_shift) for day_shift in shifts}

prices_perc_shifted = pd.DataFrame(shifted_data)

'''
INSTRUCTIONS

*   Replace missing values in prices_perc_shifted with the median of the DataFrame and assign it to X.
*   Replace missing values in prices_perc with the median of the series and assign it to y.
*   Fit a regression model using the X and y arrays.
'''

# Replace missing values with the median for each column
X = prices_perc_shifted.fillna(np.nanmedian(prices_perc_shifted))
y = prices_perc.fillna(np.nanmedian(prices_perc))

# Fit the model
model = Ridge()
model.fit(X, y)