'''
Cumulative return on $1,000 invested in google vs apple I

To put your new ability to do cumulative return calculations to practical use, let's compare how much $1,000 would be worth if invested in Google ('GOOG') or Apple ('AAPL') in 2010.
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../datasets/stock_data/apple_google.csv', index_col='Date', parse_dates=['Date']).dropna()

'''
INSTRUCTIONS

We have already imported pandas as pd, and matplotlib.pyplot as plt. We have also loaded Google and Apple stock prices in a variable data.

*   Define a variable investment with the value 1000.
*   Calculate returns by applying .pct_change() to data.
*   Add 1 to returns and assign this to returns_plus_one, then apply .cumprod() to returns_plus_one and assign the result to cumulative_return.
*   Multiply cumulative_return by investment, and plot the result.
'''

# Import numpy
import numpy as np

# Define a multi_period_return function
def multi_period_return(period_returns):
    return np.prod(period_returns + 1) - 1
    
# Calculate daily returns
daily_returns = data.pct_change()

# Calculate rolling_annual_returns
rolling_annual_returns = daily_returns.rolling('360D').apply(multi_period_return)

# Plot rolling_annual_returns
rolling_annual_returns.mul(100).plot()
plt.show()
