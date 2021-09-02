'''
Compare annual stock price trends

In the video, you have seen how to select sub-periods from a time series.

You'll use this to compare the performance for three years of Yahoo stock prices.
'''

import pandas as pd
import matplotlib.pyplot as plt

yahoo = pd.read_csv('../datasets/stock_data/yahoo.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt and we have already loaded the 'yahoo.csv' file in a variable yahoo with DateTimeIndex and a single column price.

*   Create an empty pd.DataFrame() called prices.
*   Iterate over a list containing the three years, 2013, 2014, and 2015, as string, and in each loop:
    *   Use the iteration variable to select the data for this year and the column price.
    *   Use .reset_index() with drop=True to remove the DatetimeIndex.
    *   Rename the column price column to the appropriate year.
    *   Use pd.concat() to combine the yearly data with the data in prices along axis=1.
    *   Plot prices.
'''

# Create dataframe prices here
prices = pd.DataFrame()

# Select data for each year and concatenate with prices here 
for year in ['2013', '2014', '2015']:
    price_per_year = yahoo.loc[year, ['price']].reset_index(drop=True)
    price_per_year.rename(columns={'price': year}, inplace=True)
    prices = pd.concat([prices, price_per_year], axis=1)

# Plot prices
prices.plot(subplots=True)
plt.show()