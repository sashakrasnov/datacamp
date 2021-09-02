'''
Cumulative sum vs .diff()

In the video, you have learned about expanding windows that allow you to run cumulative calculations.

The cumulative sum method has in fact the opposite effect of the .diff() method that you came across in chapter 1.

To illustrate this, let's use the Google stock price time series, create the differences between prices, and reconstruct the series using the cumulative sum.
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../datasets/stock_data/google.csv', index_col='Date', parse_dates=['Date']).dropna()

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt. We have also loaded google stock prices into the variable data

*   Apply .diff() to data, drop missing values, and assign the result to differences.
*   Use .first('D') to select the first price from data, and assign it to start_price.
*   Use .append() to combine start_price and differences, apply .cumsum() and assign this to cumulative_sum.
*   Use .equals() to compare data and cumulative_sum, and print the result.
'''

# Calculate differences
differences = data.diff().dropna()

# Select start price
start_price = data.first('D')

# Calculate cumulative sum
cumulative_sum = start_price.append(differences).cumsum()

# Validate cumulative sum equals data
print(data.equals(cumulative_sum))
