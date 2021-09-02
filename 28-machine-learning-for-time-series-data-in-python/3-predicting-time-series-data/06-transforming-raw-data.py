'''
Transforming raw data

In the last chapter, you calculated the rolling mean. In this exercise, you will define a function that calculates the percent change of the latest data point from the mean of a window of previous data points. This function will help you calculate the percent change over a rolling window.

This is a more stable kind of time series that is often useful in machine learning.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

prices = pd.read_csv('../datasets/prices_messy.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

*   Define a percent_change function that takes an input time series and does the following:
    *   Extract all but the last value of the input series (assigned to previous_values) and the only the last value of the timeseries ( assigned to last_value)
    *   Calculate the percentage difference between the last value and the mean of earlier values.
*   Using a rolling window of 20, apply this function to prices, and visualize it using the given code.
'''

# Your custom function
def percent_change(series):
    # Collect all *but* the last value of this window, then the final value
    previous_values = series[:-1]
    last_value = series[-1]

    # Calculate the % difference between the last value and the mean of earlier values
    percent_change = (last_value - np.mean(previous_values)) / np.mean(previous_values)
    return percent_change

# Apply your custom function and plot
prices_perc = prices.rolling(20).apply(percent_change)
prices_perc.loc["2014":"2015"].plot()
plt.show()