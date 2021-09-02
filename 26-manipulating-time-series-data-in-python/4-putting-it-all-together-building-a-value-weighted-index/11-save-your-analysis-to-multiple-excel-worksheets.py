'''
Save your analysis to multiple excel worksheets

Now that you have completed your analysis, you may want to save all results into a single Excel workbook.

Let's practice exporting various DataFrame to multiple Excel worksheets.
'''

import pandas as pd
import seaborn as sns
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
index = raw_index.div(raw_index.iloc[0]).mul(100).to_frame('Index')

'''
INSTRUCTIONS

We have already imported pandas as pd for you. We have also loaded both the historical price series of your index constituents into the variable stock_prices, and the index as index.

*   Inspect both index and stock_prices using .info().
*   Use .join() to combine index with stock_prices, and assign to data.
*   Apply .pct_change() to data and assign to returns.
*   Create pd.ExcelWriter and use with to export data and returns to excel with sheet_names of the same name.
'''

# Inspect index and stock_prices
print(index.info())
print(stock_prices.info())

# Join index to stock_prices, and inspect the result
data = stock_prices.join(index)
print(data.info())

# Create index & stock price returns
returns = data.pct_change()

# Export data and data as returns to excel
with pd.ExcelWriter('../datasets/data.xls') as writer:
    data.to_excel(excel_writer=writer, sheet_name='data')
    returns.to_excel(excel_writer=writer, sheet_name='returns')
