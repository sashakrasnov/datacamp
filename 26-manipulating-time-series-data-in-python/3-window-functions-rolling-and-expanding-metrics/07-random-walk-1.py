'''
Random walk I

In the last video, you have seen how to generate a random walk of returns, and how to convert this random return series into a random stock price path.

In this exercise, you'll build your own random walk by drawing random numbers from the normal distribution with the help of numpy.
'''

import pandas as pd
import matplotlib.pyplot as plt

from numpy.random import normal, seed

'''
INSTRUCTIONS

We have already imported pandas as pd, normal and seed from numpy.random, and matplotlib.pyplot as plt.

*   Set seed to 42.
*   Use normal to generate 2,500 random returns with the parameters loc=.001, scale=.01 and assign this to random_walk.
*   Convert random_walk to a pd.Series object and reassign it to random_walk.
*   Create random_prices by adding 1 to random_walk and calculating the cumulative product.
*   Multiply random_prices by 1,000 and plot the result for a price series starting at 1,000.
'''

# Set seed here
seed = 42

# Create random_walk
random_walk = normal(loc=0.001, scale=0.01, size=2500)

# Convert random_walk to pd.series
random_walk = pd.Series(random_walk)

# Create random_prices
random_prices = (random_walk + 1).cumprod()

# Plot random_prices here
random_prices.mul(1000).plot()
plt.show()

