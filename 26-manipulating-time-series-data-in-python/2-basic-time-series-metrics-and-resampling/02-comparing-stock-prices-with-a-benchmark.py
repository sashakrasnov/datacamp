'''
Comparing stock prices with a benchmark

You also learned in the video how to compare the performance of various stocks against a benchmark. Now you'll learn more about the stock market by comparing the three largest stocks on the NYSE to the Dow Jones Industrial Average, which contains the 30 largest US companies.

The three largest companies on the NYSE are:

Company             Stock Ticker
----------------------------------
Johnson & Johnson	JNJ
Exxon Mobil	        XOM
JP Morgan Chase	    JPM
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt.

*   Use pd.read_csv() to import 'nyse.csv' and 'dow_jones.csv', creating a DatetimeIndex for each from the 'date' column using parse_dates and index_col, and assign the result to stocks and dow_jones, respectively.
*   Use pd.concat() along axis=1 to combine stocks and dow_jones and assign the result to data. Inspect the .info() of data.
*   Divide data by the first value for each series, multiply by 100 and plot the result.
'''

# Import stock prices and index here
stocks = pd.read_csv('../datasets/stock_data/nyse.csv', index_col='date', parse_dates=['date'])
dow_jones = pd.read_csv('../datasets/stock_data/dow_jones.csv', index_col='date', parse_dates=['date'])

# Concatenate data and inspect result here
data = pd.concat([stocks, dow_jones], axis=1)
print(data.info())

# Normalize and plot your data here
data.div(data.iloc[0]).mul(100).plot(subplots=True)
plt.show()