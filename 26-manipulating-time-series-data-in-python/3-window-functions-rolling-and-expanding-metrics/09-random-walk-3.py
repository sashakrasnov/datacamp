'''
Random walk III

In this exercise, you'll complete your random walk simulation using Facebook stock returns over the last five years. You'll start off with a random sample of returns like the one you've generated during the last exercise and use it to create a random stock price path.
'''

import pandas as pd
import matplotlib.pyplot as plt

from numpy.random import choice, seed

fb = pd.read_csv('../datasets/stock_data/fb.csv', header=None, index_col=0, parse_dates=True, squeeze=True)
fb.index.name = 'date'

# Set seed here
seed = 42

# Calculate daily_returns here
daily_returns = fb.pct_change().dropna()

# Get n_obs
n_obs = daily_returns.count()

# Create random_walk
random_walk = choice(daily_returns, size=n_obs)

# Convert random_walk to pd.series
random_walk = pd.Series(random_walk, index=daily_returns.index)

fb = pd.DataFrame(fb)
fb.columns = ['price']

'''
INSTRUCTIONS

We have already imported pandas as pd, choice and seed from numpy.random, and matplotlib.pyplot as plt. We have loaded the Facebook price as a pd.DataFrame in the variable fb and a random sample of daily FB returns as pd.Series in the variable random_walk.

*   Select the first Facebook price by applying .first('D') to fb.price, and assign to start.
*   Add 1 to random_walk and reassign it to itself, then .append() random_walk to start and assign this to random_price.
*   Apply .cumprod() to random_price and reassign it to itself.
*   Insert random_price as new column labeled random into fb and plot the result.
'''

# Select fb start price here
start = fb.price.first('D')

# Add 1 to random walk and append to start
random_walk = random_walk + 1
random_price = start.append(random_walk)

# Calculate cumulative product here
random_price = random_price.cumprod()

# Insert into fb and plot
fb['random'] =  random_price
fb.plot()

plt.show()
