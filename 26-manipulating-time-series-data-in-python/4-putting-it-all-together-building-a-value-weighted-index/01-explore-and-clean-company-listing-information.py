'''
Explore and clean company listing information

To get started with the construction of a market-value based index, you'll work with the combined listing info for the three largest US stock exchanges, the NYSE, the NASDAQ and the AMEX.

In this and the next exercise, you will calculate market-cap weights for these stocks.

We have already imported pandas as pd, and loaded the listings data set with listings information from the NYSE, NASDAQ, and AMEX. The column 'Market Capitalization' is already measured in USD mn.
'''

import pandas as pd
import matplotlib.pyplot as plt

listings = pd.read_excel('../datasets/stock_data/listings.xlsx', sheetname='nyse', na_values='n/a')

'''
INSTRUCTIONS

Inspect listings using .info().

*   Move the column 'Stock Symbol' into the index (inplace).
*   Drop all companies with missing 'Sector' information from listings.
*   Select companies with IPO Year before 2019.
*   Inspect the result of the changes you just made using .info().
*   Show the number of companies per 'Sector' using .groupby() and .size(). Sort the output in descending order.
'''

# Inspect listings
print(listings.info())

# Move 'stock symbol' into the index
listings.set_index('Stock Symbol', inplace=True)

# Drop rows with missing 'sector' data
listings.dropna(subset=['Sector'], inplace=True)

# Select companies with IPO Year before 2019
listings = listings[listings['IPO Year'] < 2019]

# Inspect the new listings data
print(listings.info())

# Show the number of companies per sector
print(listings.groupby('Sector').size().sort_values(ascending=False))
