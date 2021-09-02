'''
Plot performance difference vs benchmark index

In the video, you learned how to calculate and plot the performance difference of a stock in percentage points relative to a benchmark index.

Let's compare the performance of Microsoft (MSFT) and Apple (AAPL) to the S&P 500 over the last 10 years.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt.

*   Create the list tickers containing the two stock symbols.
*   Use pd.read_csv() to import 'msft_aapl.csv' and 'sp500.csv', creating a DatetimeIndex for each from the 'date' column using parse_dates and index_col, and assign the result to stocks and sp500, respectively.
*   Use pd.concat() to concatenate stocks and sp500 along axis=1, apply .dropna() to drop all missing values, and assign the result to data.
*   Normalize data by dividing by the first price, multiply by 100 and assign the output to normalized.
*   Select tickers from normalized, and subtract normalized['SP500'] with keyword axis=0 to align the indexes, then plot the result.
'''

# Create tickers
tickers = ['MSFT', 'AAPL']

# Import stock data here
stocks = pd.read_csv('../datasets/stock_data/msft_aapl.csv', index_col='date', parse_dates=['date'])

# Import index here
sp500 = pd.read_csv('../datasets/stock_data/sp500.csv', index_col='date', parse_dates=['date'])

# Concatenate stocks and index here
data = pd.concat([stocks, sp500], axis=1).dropna()

# Normalize data
normalized = data.div(data.iloc[0]).mul(100)

# Subtract the normalized index from the normalized stock prices, and plot the result
normalized[tickers].sub(normalized['SP500'], axis=0).plot()
plt.show()
