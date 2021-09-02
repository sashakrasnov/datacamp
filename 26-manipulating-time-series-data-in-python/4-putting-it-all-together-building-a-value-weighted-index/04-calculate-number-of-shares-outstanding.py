'''
Calculate number of shares outstanding

The next step towards building a value-weighted index is to calculate the number of shares for each index component.

The number of shares will allow you to calculate the total market capitalization for each component given the historical price series in the next exercise.
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../datasets/stock_data/listings.xlsx', sheet_name=['amex' ,'nasdaq', 'nyse'], na_values='n/a')

for e in df.keys():
    df[e]['Exchange'] = e

listings = pd.concat(df).set_index('Stock Symbol')

listings['Market Capitalization'] /= 10**6

listings.dropna(subset=['Sector'], inplace=True)

listings = listings[listings['IPO Year'] < 2010]

# Select stock symbols for largest company for each sector
tickers = listings.groupby(['Sector'])['Market Capitalization'].nlargest(1).index.get_level_values('Stock Symbol')

'''
INSTRUCTIONS

We have already imported pandas as pd, tickers and listings as in the previous exercises.

*   Inspect listings and print tickers.
*   Use .loc[] with the list of tickers to select the index components and the columns 'Market Capitalization' and 'Last Sale'; assign this to components.
*   Print the first five rows of components.
*   Create no_shares by dividing Market Capitalization by 'Last Sale'.
*   Print no_shares in descending order.
'''

# Inspect listings and print tickers
print(listings.info())
print(tickers)

# Select components and relevant columns from listings
components = listings.loc[tickers, ['Market Capitalization', 'Last Sale']]

# Print the first rows of components
print(components.head())

# Calculate the number of shares here
no_shares = components['Market Capitalization'].div(components['Last Sale'])

# Print the sorted no_shares
print(no_shares.sort_values(ascending=False))
