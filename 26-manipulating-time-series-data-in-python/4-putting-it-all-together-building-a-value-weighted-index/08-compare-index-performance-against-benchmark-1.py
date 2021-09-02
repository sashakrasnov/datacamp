'''
Compare index performance against benchmark I

The next step in analyzing the performance of your index is to compare it against a benchmark.

In the video, we used the S&P 500 as benchmark. You can also use the Dow Jones Industrial Average, which contains the 30 largest stocks, and would also be a reasonable benchmark for the largest stocks from all sectors across the three exchanges.
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

raw_index = market_cap_series.sum(axis=1)
index = raw_index.div(raw_index.iloc[0]).mul(100)

djia = pd.read_csv('../datasets/stock_data/djia.csv', index_col='date', parse_dates=['date'])

'''
INSTRUCTIONS

We have already imported pandas as pd, matplotlib.pyplot as plt for you. We have also loaded your index and the DJIA data into variables index and djia, respectively, both as a pd.Series().

*   Convert index to a pd.DataFrame with the column name 'Index' and assign the result to data.
*   Normalize djia to start at 100 and add it as new column to data.
*   Show the total return for both index and djia by dividing the last row of data by the first, subtracting 1 and multiplying by 100.
*   Show a plot of both of the series in data.
'''

# Convert index series to dataframe here
data = index.to_frame('Index')

# Normalize djia series and add as new column to data
djia = djia.div(djia.iloc[0]).mul(100)
data['DJIA'] = djia

# Show total return for both index and djia
print(data.iloc[-1].div(data.iloc[0]).sub(1).mul(100))

# Plot both series
data.plot()
plt.show()
