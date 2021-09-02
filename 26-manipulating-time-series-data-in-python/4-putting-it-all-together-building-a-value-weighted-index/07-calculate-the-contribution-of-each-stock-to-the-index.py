'''
Calculate the contribution of each stock to the index

You have successfully built the value-weighted index. Let's now explore how it performed over the 2010-2016 period.

Let's also determine how much each stock has contributed to the index return.
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

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt for you. We have also loaded components and the index you worked with in the last exercise.

*   Divide the last index value by the first, subtract 1 and multiply by 100. Assign the result to index_return and print it.
*   Select the 'Market Capitalization' column from components.
*   Calculate the total market cap for all components and assign this to total_market_cap.
*   Divide the components' market cap by total_market_cap to calculate the component weights, assign it to weights, and print weights with the values sorted.
*   Multiply weights by the index_return to calculate the contribution by component, sort the values, and plot the result as a horizontal bar chart.
'''

# Calculate and print the index return here
index_return = (index.iloc[-1] / index.iloc[0] - 1) * 100
print(index_return)

# Select the market capitalization
market_cap = components['Market Capitalization']

# Calculate the total market cap
total_market_cap = market_cap.sum()

# Calculate the component weights, and print the result
weights = market_cap / total_market_cap
print(weights.sort_values())

# Calculate and plot the contribution by component
weights.mul(index_return).sort_values().plot(kind='barh')
plt.show()