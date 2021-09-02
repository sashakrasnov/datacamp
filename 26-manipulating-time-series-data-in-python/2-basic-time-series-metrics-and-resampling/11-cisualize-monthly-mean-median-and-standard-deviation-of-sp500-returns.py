'''
Visualize monthly mean, median and standard deviation of S&P500 returns

You have also learned how to calculate several aggregate statistics from upsampled data.

Let's use this to explore how the monthly mean, median and standard deviation of daily S&P500 returns have trended over the last 10 years.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

As usual, we have imported pandas as pd and matplotlib.pyplot as plt for you.

*   Use pd.read_csv() to import 'sp500.csv', set a DateTimeIndex based on the 'date' column using parse_dates and index_col, assign the results to sp500, and inspect using .info().
*   Convert sp500 to a pd.Series() using .squeeze(), and apply .pct_change() to calculate daily_returns.
*   .resample() daily_returns to month-end frequency (alias: 'M'), and apply .agg() to calculate 'mean', 'median', and 'std'. Assign the result to stats.
*   .plot() stats.
'''

# Import data here
sp500 = pd.read_csv('../datasets/stock_data/sp500.csv', index_col='date', parse_dates=['date'])
print(sp500.info())

# Calculate daily returns here
daily_returns = sp500.squeeze().pct_change()

# Resample and calculate statistics
stats = daily_returns.resample('M').agg(['mean', 'median', 'std'])

# Plot stats here
stats.plot()
plt.show()
