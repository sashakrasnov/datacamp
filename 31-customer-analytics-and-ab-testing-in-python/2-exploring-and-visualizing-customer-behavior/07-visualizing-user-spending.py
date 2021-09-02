'''
Exponential rolling average & over/under smoothing

In the previous exercise, we saw that our revenue is somewhat flat over time. In this exercise we will dive deeper into the data to see if we can determine why this is the case. We will look at the revenue for a single in-app purchase product we are selling to see if this potentially reveals any trends. As this will have less data then looking at our overall revenue it will be much noisier. To account for this we will smooth the data using an exponential rolling average.

A new daily_revenue dataset has been provided for us, containing the revenue for this product.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

*   Using the .ewm() method, calculate the exponential rolling average with a span of 10 and store it in a column small_scale.
*   Repeat the previous step, now with a span of 100 and store it in a column medium_scale.
*   Finally, calculate the exponential rolling average with a span of 500 and store it in a column large_scale.
*   Plot the three averages, along with the raw data. Examine how clear the trend of the data is.
'''

# Calculate 'small_scale'
daily_revenue['small_scale'] = daily_revenue.revenue.ewm(span=10).mean()

# Calculate 'medium_scale'
daily_revenue['medium_scale'] = daily_revenue.revenue.ewm(span=100).mean()

# Calculate 'large_scale'
daily_revenue['large_scale'] = daily_revenue.revenue.ewm(span=500).mean()

# Plot 'date' on the x-axis and, our three averages and 'revenue'
# on the y-axis
daily_revenue.plot(x='date', y =['revenue', 'small_scale', 'medium_scale', 'large_scale'])
plt.show()