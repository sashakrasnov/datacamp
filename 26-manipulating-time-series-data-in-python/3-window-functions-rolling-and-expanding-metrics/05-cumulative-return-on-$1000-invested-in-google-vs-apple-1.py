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

# Define your investment
investment = 1000

# Calculate the daily returns here
returns = data.pct_change()

# Calculate the cumulative returns here
returns_plus_one = returns + 1
cumulative_return = returns_plus_one.cumprod()

# Calculate and plot the investment return here 
cumulative_return.mul(investment).plot()
plt.show()