'''
Percentiles and partial functions

In this exercise, you'll practice how to pre-choose arguments of a function so that you can pre-configure how it runs. You'll use this to calculate several percentiles of your data using the same percentile() function in numpy.
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
prices_perc = prices_perc['EBAY'].apply(replace_outliers)

'''
INSTRUCTIONS

*   Import partial from functools.
*   Use the partial() function to create several feature generators that calculate percentiles of your data using a list comprehension.
*   Using the rolling window (prices_perc_rolling) we defined for you, calculate the quantiles using percentile_functions.
*   Visualize the results using the code given to you.
'''

# Import partial from functools
from functools import partial
percentiles = [1, 10, 25, 50, 75, 90, 99]

# Use a list comprehension to create a partial function for each quantile
percentile_functions = [partial(np.percentile, q=percentile) for percentile in percentiles]

# Calculate each of these quantiles on the data using a rolling window
prices_perc_rolling = prices_perc.rolling(20, min_periods=5, closed='right')
print(percentile_functions)
features_percentiles = prices_perc_rolling.aggregate(percentile_functions)

print(features_percentiles)
# Plot a subset of the result
ax = features_percentiles.loc[:"2011-01"].plot(cmap=plt.cm.viridis)
ax.legend(percentiles, loc=(1.01, .5))
plt.show()