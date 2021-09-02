'''
Compare quarterly GDP growth rate and stock returns

With your new skill to downsample and aggregate time series, you can compare higher-frequency stock price series to lower-frequency economic time series.

As a first example, let's compare the quarterly GDP growth rate to the quarterly rate of return on the (resampled) Dow Jones Industrial index of 30 large US stocks.

GDP growth is reported at the beginning of each quarter for the previous quarter. To calculate matching stock returns, you'll resample the stock index to quarter start frequency using the alias 'QS', and aggregating using the .first() observations.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

As usual, we have imported pandas as pd and matplotlib.pyplot as plt for you.

*   Use pd.read_csv() to import 'gdp_growth.csv' and 'djia.csv', for both set a DateTimeIndex based on the 'date' column using parse_dates and index_col, and assign the results to gdp_growth and djia respectively, then inspect using .info().
*   Resample djia using frequency alias 'QS', aggregate using .first(), and assign to djia_quarterly.
*   Apply .pct_change() to djia_quarterly and .mul() by 100 to obtain djia_quarterly_return.
*   Use pd.concat() to concatenate gdp_growth and djia_quarterly_return along axis=1, and assign to data. * Rename the columns using .columns and the new labels 'gdp' and 'djia', then .plot() the results.
'''

# Import and inspect gdp_growth here
gdp_growth = pd.read_csv('../datasets/stock_data/gdp_growth.csv', index_col='date', parse_dates=['date'])
print(gdp_growth.info())

# Import and inspect djia here
djia = pd.read_csv('../datasets/stock_data/djia.csv', index_col='date', parse_dates=['date'])
print(djia.info())

# Calculate djia quarterly returns here 
djia_quarterly = djia.resample('QS').first()
djia_quarterly_return = djia_quarterly.pct_change().mul(100)

# Concatenate, rename and plot djia_quarterly_return and gdp_growth here 
data = pd.concat([gdp_growth,djia_quarterly_return], axis=1)
data.columns = ['gdp', 'djia']
data.plot()

plt.show()
