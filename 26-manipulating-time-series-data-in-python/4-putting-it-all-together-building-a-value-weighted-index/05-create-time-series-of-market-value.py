'''
Create time series of market value

You can now use the number of shares to calculate the total market capitalization for each component and trading date from the historical price series.

The result will be the key input to construct the value-weighted stock index, which you will complete in the next exercise.
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

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt for you. We have also created the variables components and stock_prices that you worked with in the last exercises.

*   Select the 'Number of Shares' from components, assign to no_shares, and print the sorted result.
*   Multiply stock_prices by no_shares to create a time series of market cap per ticker, and assign it to market_cap.
*   Select the first and the last row of market_cap and assign these to first_value and last_value.
*   Use pd.concat() to concatenate first_value and last_value along axis=1 and plot the result as horizontal bar chart.
'''

# Select the number of shares
no_shares = components['Number of Shares']
print(no_shares.sort_values())

# Create the series of market cap per ticker
market_cap = stock_prices.mul(no_shares)

# Select first and last market cap here
first_value = market_cap.iloc[0]
last_value = market_cap.iloc[-1]

# Concatenate and plot first and last market cap here
pd.concat([first_value, last_value], axis=1).plot(kind='barh')
plt.show()
