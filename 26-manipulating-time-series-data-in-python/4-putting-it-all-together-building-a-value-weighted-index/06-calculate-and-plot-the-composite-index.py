'''
Calculate & plot the composite index

By now you have all ingredients that you need to calculate the aggregate stock performance for your group of companies.

Use the time series of market capitalization that you created in the last exercise to aggregate the market value for each period, and then normalize this series to convert it to an index.
'''

import pandas as pd
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

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt for you. We have also loaded components and market_cap_series, which you worked with in the last exercise.

*   Aggregate the market cap per trading day by applying .sum() to market_cap_series with axis=1, assign to raw_index and print the result.
*   Normalize the aggregate market cap by dividing by the first value of raw_index and multiplying by 100. Assign this to index and print the result.
*   Plot the index with the title 'Market-Cap Weighted Index'.
'''

# Aggregate and print the market cap per trading day
raw_index = market_cap_series.sum(axis=1)
print(raw_index)

# Normalize the aggregate market cap here 
index = raw_index.div(raw_index.iloc[0]).mul(100)
print(index)

# Plot the index here
index.plot(title='Market-Cap Weighted Index')
plt.show()