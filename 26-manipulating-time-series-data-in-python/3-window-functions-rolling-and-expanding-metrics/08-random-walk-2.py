'''
Random walk II

In the last video, you have also seen how to create a random walk of returns by sampling from actual returns, and how to use this random sample to create a random stock price path.

In this exercise, you'll build a random walk using historical returns from Facebook's stock price since IPO through the end of May 31, 2017. Then you'll simulate an alternative random price path in the next exercise.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from numpy.random import choice, seed

fb = pd.read_csv('../datasets/stock_data/fb.csv', header=None, index_col=0, parse_dates=True, squeeze=True)
fb.index.name = 'date'

'''
INSTRUCTIONS

We have already imported pandas as pd, choice and seed from numpy.random, seaborn as sns, and matplotlib.pyplot as plt. We have also imported the FB stock price series since IPO in May 2012 as the variable fb. Inspect this using .head().

*   Set seed to 42.
*   Apply .pct_change() to generate daily Facebook returns, drop missing values, and assign to daily_returns.
*   Create a variable n_obs that contains the .count() of Facebook daily_returns.
*   Use choice() to randomly select n_obs samples from daily_returns, and assign to random_walk.
*   Convert random_walk to a pd.Series and reassign it to itself.
*   Use sns.distplot() to plot the distribution of random_walk.
'''

# Set seed here
seed = 42

# Calculate daily_returns here
daily_returns = fb.pct_change().dropna()

# Get n_obs
n_obs = daily_returns.count()

# Create random_walk
random_walk = choice(daily_returns, size=n_obs)

# Convert random_walk to pd.series
random_walk = pd.Series(random_walk)

# Plot random_walk distribution
sns.distplot(random_walk)
plt.show()