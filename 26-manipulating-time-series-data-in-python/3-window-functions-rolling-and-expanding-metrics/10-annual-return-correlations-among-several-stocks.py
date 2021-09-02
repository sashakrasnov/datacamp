'''
Annual return correlations among several stocks

You have seen in the video how to calculate correlations, and visualize the result.

In this exercise, we have provided you with the historical stock prices for Apple (AAPL), Amazon (AMZN), IBM (IBM), WalMart (WMT), and Exxon Mobile (XOM) for the last 4,000 trading days from July 2001 until the end of May 2017.

You'll calculate the year-end returns, the pairwise correlations among all stocks, and visualize the result as an annotated heatmap.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../datasets/stock_data/5_stocks.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

We have already imported pandas as pd, seaborn as sns, and matplotlib.pyplot as plt. We have loaded the daily close price for the five stocks in a variable called data.

*   Inspect using .info().
*   Apply .resample() with year-end frequency (alias: 'A') to data and select the .last() price from each subperiod; assign this to annual_prices.
*   Calculate annual_returns by applying .pct_change() to annual_prices.
*   Calculate correlations by applying .corr() to annual_returns and print the result.
*   Visualize correlations as an annotated sns.heatmap().
'''

# Inspect data here
print(data.info())

# Calculate year-end prices here
annual_prices = data.resample('A').last()

# Calculate annual returns here
annual_returns = annual_prices.pct_change()

# Calculate and print the correlation matrix here
correlations = annual_returns.corr()
print(correlations)

# Visualize the correlations as heatmap here
sns.heatmap(correlations, annot=True)
plt.show()