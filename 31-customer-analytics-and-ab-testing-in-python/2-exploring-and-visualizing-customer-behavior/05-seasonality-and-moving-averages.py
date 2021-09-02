'''
Seasonality and moving averages

Stepping back, we will now look at the overall revenue data for our meditation app. We saw strong purchase growth in one of our products, and now we want to see if that is leading to a corresponding rise in revenue. As you may expect, revenue is very seasonal, so we want to correct for that and unlock macro trends.

In this exercise, we will correct for weekly, monthly, and yearly seasonality and plot these over our raw data. This can reveal trends in a very powerful way.

The revenue data is loaded for you as daily_revenue.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

*   Using the .rolling() method, find the rolling average of the data with a 7 day window and store it in a column 7_day_rev.
*   Find the monthly (28 days) rolling average and store it in a column 28_day_rev.
*   Find the yearly (365 days) rolling average and store it in a column 365_day_rev.
*   Hit 'Submit Answer' to plot the three calculated rolling averages together along with the raw data.
'''

# Compute 7_day_rev
daily_revenue['7_day_rev'] = daily_revenue.revenue.rolling(window=7,center=False).mean()

# Compute 28_day_rev
daily_revenue['28_day_rev'] = daily_revenue.revenue.rolling(window=28,center=False).mean()
    
# Compute 365_day_rev
daily_revenue['365_day_rev'] = daily_revenue.revenue.rolling(window=365,center=False).mean()
    
# Plot date, and revenue, along with the 3 rolling functions (in order)    
daily_revenue.plot(x='date', y=['revenue', '7_day_rev', '28_day_rev', '365_day_rev', ])
plt.show()