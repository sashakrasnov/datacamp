'''
Compare index performance against benchmark II

The next step in analyzing the performance of your index is to compare it against a benchmark.

In the video, we have use the S&P 500 as benchmark. You can also use the Dow Jones Industrial Average, which contains the 30 largest stocks, and would also be a reasonable benchmark for the largest stocks from all sectors across the three exchanges.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stock_prices = pd.read_csv('../datasets/stock_data/stock_data.csv', index_col='Date', parse_dates=['Date'])

df = pd.read_excel('../datasets/stock_data/listings.xlsx', sheet_name=['amex' ,'nasdaq', 'nyse'], na_values='n/a')

for e in df.keys():
    df[e]['Exchange'] = e

listings = pd.concat(df).set_index('Stock Symbol')

listings['Market Capitalization'] /= 10**6

listings.dropna(subset=['Sector'], inplace=True)

listings = listings[listings['IPO Year'] < 2010]

tickers = listings.groupby(['Sector'])['Market Capitalization'].nlargest(1).index.get_level_values('Stock Symbol')

components = listings.loc[tickers, ['Market Capitalization', 'Last Sale']]
components['Number of Shares'] = components['Market Capitalization'].div(components['Last Sale'])

market_cap_series = stock_prices.mul(components['Number of Shares'])

raw_index = market_cap_series.sum(axis=1)
index = raw_index.div(raw_index.iloc[0]).mul(100)

djia = pd.read_csv('../datasets/stock_data/djia.csv', index_col='date', parse_dates=['date'])

data = index.to_frame('Index')

djia = djia.div(djia.iloc[0]).mul(100)
data['DJIA'] = djia

'''
INSTRUCTIONS

We have already imported numpy as np, pandas as pd, matplotlib.pyplot as plt for you. We have also loaded your Index and the Dow Jones Industrial Average (normalized) in a variable called data.

*   Inspect data and print the first five rows.
*   Define a function multi_period_return that takes a numpy array of period returns as input, and returns the total return for the period. Use the formula from the video - add 1 to the input, pass the result to np.prod(), subtract 1 and multiply by 100.
*   Create a .rolling() window of length '360D' from data, and apply multi_period_return. Assign to rolling_return_360.
*   Plot rolling_return_360 using the title 'Rolling 360D Return'.
'''

# Inspect data
print(data.info())
print(data.head())

# Create multi_period_return function here
def multi_period_return(r):
    return (np.prod(r + 1) - 1) * 100

# Calculate rolling_return_360
rolling_return_360 = data.pct_change().rolling('360D').apply(multi_period_return)

# Plot rolling_return_360 here
rolling_return_360.plot(title='Rolling 360D Return')
plt.show()
