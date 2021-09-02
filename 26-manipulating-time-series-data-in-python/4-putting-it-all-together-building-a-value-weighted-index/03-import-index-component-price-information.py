'''
Import index component price information

Now you'll use the stock symbols for the companies you selected in the last exercise to calculate returns for each company.
'''

import pandas as pd
import matplotlib.pyplot as plt

listings = pd.read_excel('../datasets/stock_data/listings.xlsx', sheetname='nyse', na_values='n/a')

listings.set_index('Stock Symbol', inplace=True)

# Drop rows with missing 'sector' data
listings.dropna(subset=['Sector'], inplace=True)

# Select companies with IPO Year before 2019
listings = listings[listings['IPO Year'] < 2019]

# Select stock symbols for largest company for each sector
tickers = listings.groupby(['Sector'])['Market Capitalization'].nlargest(1).index.get_level_values('Stock Symbol')

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt for you. We have also made the variable tickers available to you, which contains the Stock Symbol for each index component as a list.

*   Print tickers to verify the content matches your result from the last exercise.
*   Use pd.read_csv() to import 'stock_prices.csv', parsing the 'Date' column and also setting the 'Date' column as index before assigning the result to stock_prices. Inspect the result using .info().
*   Calculate the price return for the index components by dividing the last row of stock_prices by the first, subtracting 1 and multiplying by 100. Assign the result to price_return.
*   Plot a horizontal bar chart of the sorted returns with the title Stock Price Returns.
'''

# Print tickers
print(tickers)

# Import prices and inspect result
stock_prices = pd.read_csv('../datasets/stock_data/stock_data.csv', index_col='Date', parse_dates=['Date'])
print(stock_prices.info())

# Calculate the returns    
price_return = (stock_prices.iloc[-1] / stock_prices.iloc[0]).sub(1).mul(100)

# Plot horizontal bar chart of sorted price_return   
price_return.sort_values().plot(kind='barh', title='Stock Price Returns')
plt.show()
