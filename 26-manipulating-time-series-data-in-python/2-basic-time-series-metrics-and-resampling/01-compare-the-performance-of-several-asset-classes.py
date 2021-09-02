'''
Compare the performance of several asset classes

You have seen in the video how you can easily compare several time series by normalizing their starting points to 100, and plot the result.

To broaden your perspective on financial markets, let's compare four key assets: stocks, bonds, gold, and oil.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt.

*   Import 'asset_classes.csv', using .read_csv() to parse dates in the 'DATE' column and set this column as the index, then assign the result to prices.
*   Select the first price for each series using .iloc[0] on prices and assign the result to first_prices.
*   Divide prices by first_prices, multiply by 100 and assign the result to normalized.
*   Plot normalized.
'''

# Import data here
prices = pd.read_csv('../datasets/stock_data/asset_classes.csv', index_col='DATE', parse_dates=['DATE'])

# Inspect prices here
print(prices.info())

# Select first prices
first_prices = prices.iloc[0]

# Create normalized
normalized = prices.div(first_prices).mul(100)

# Plot normalized
normalized.plot(subplots=True)
plt.show()