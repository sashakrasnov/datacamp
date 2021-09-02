'''
Using "date" information

It's easy to think of timestamps as pure numbers, but don't forget they generally correspond to things that happen in the real world. That means there's often extra information encoded in the data such as "is it a weekday?" or "is it a holiday?". This information is often useful in predicting timeseries data.

In this exercise, you'll extract these date/time based features. A single time series has been loaded in a variable called prices.
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


prices = pd.read_csv('../datasets/prices_messy.csv', index_col=0, parse_dates=True)[['EBAY']]

prices_perc = prices.rolling(20).apply(percent_change, raw=False)
prices_perc = prices_perc.apply(replace_outliers)

'''
INSTRUCTIONS

*   Calculate the day of the week, week number in a year, and month number in a year.
*   Add each one as a column to the prices_perc DataFream, under the names day_of_week, week_of_year and month_of_year, respectively.
'''

# Extract date features from the data, add them as columns
prices_perc['day_of_week'] = prices_perc.index.weekday
prices_perc['week_of_year'] = prices_perc.index.week
prices_perc['month_of_year'] = prices_perc.index.month

# Print prices_perc
print(prices_perc)