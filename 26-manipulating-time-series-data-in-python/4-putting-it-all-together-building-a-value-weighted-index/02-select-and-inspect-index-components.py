'''
Select and inspect index components

Now that you have imported and cleaned the listings data, you can proceed to select the index components as the largest company for each sector by market capitalization.

You'll also have the opportunity to take a closer look at the components, their last market value, and last price.
'''

import pandas as pd
import matplotlib.pyplot as plt

listings = pd.read_excel('../datasets/stock_data/listings.xlsx', sheetname='nyse', na_values='n/a')

listings.set_index('Stock Symbol', inplace=True)

# Drop rows with missing 'sector' data
listings.dropna(subset=['Sector'], inplace=True)

# Select companies with IPO Year before 2019
listings = listings[listings['IPO Year'] < 2019]

'''
INSTRUCTIONS

We have already imported pandas as pd, and loaded the listings data with the modifications you made during the last exercise.

*   Use .groupby() and .nlargest() to select the largest company by 'Market Capitalization' for each 'Sector', and assign the result to components.
*   Print components, sorted in descending order by market cap.
*   Select Stock Symbol from the index of components, assign it to tickers and print the result.
*   Create a list info_cols that holds the column names Company Name, Market Capitalization, and Last Sale. Next, use .loc[] with tickers and info_cols to print() more details about the listings sorted in descending order by Market Capitalization).
'''

# Select largest company for each sector
components = listings.groupby(['Sector'])['Market Capitalization'].nlargest(1)

# Print components, sorted by market cap
print(components.sort_values(ascending=False))

# Select stock symbols and print the result
tickers = components.index.get_level_values('Stock Symbol')
print(tickers)

# Print company name, market cap, and last price for each component 
info_cols = ['Company Name', 'Market Capitalization', 'Last Sale']
print(listings.loc[tickers,info_cols].sort_values('Market Capitalization', ascending=False))