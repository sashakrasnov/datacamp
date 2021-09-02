'''
Visualize regression coefficients

Now that you've fit the model, let's visualize its coefficients. This is an important part of machine learning because it gives you an idea for how the different features of a model affect the outcome.

The shifted time series DataFrame (prices_perc_shifted) and the regression model (model) are available in your workspace.

In this exercise, you will create a function that, given a set of coefficients and feature names, visualizes the coefficient values.
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

X = prices_perc_shifted.fillna(np.nanmedian(prices_perc_shifted))
y = prices_perc.fillna(np.nanmedian(prices_perc))

model = Ridge()
model.fit(X, y)

'''
INSTRUCTIONS 1/2

*   Define a function (called visualize_coefficients) that takes as input an array of coefficients, an array of each coefficient's name, and an instance of a Matplotlib axis object. It should then generate a bar plot for the input coefficients, with their names on the x-axis.
'''

def visualize_coefficients(coefs, names, ax):
    # Make a bar plot for the coefficients, including their names on the x-axis
    ax.bar(names, coefs)
    ax.set(xlabel='Coefficient name', ylabel='Coefficient value')
    
    # Set formatting so it looks nice
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    return ax

'''
INSTRUCTIONS 2/2

*   Use this function (visualize_coefficients()) with the coefficients contained in the model variable and column names of prices_perc_shifted.
'''

# Visualize the output data up to "2011-01"
fig, axs = plt.subplots(2, 1, figsize=(10, 5))
y.loc[:'2011-01'].plot(ax=axs[0])

# Run the function to visualize model's coefficients
visualize_coefficients(model.coef_, prices_perc_shifted.columns.tolist(), ax=axs[1])
plt.show()