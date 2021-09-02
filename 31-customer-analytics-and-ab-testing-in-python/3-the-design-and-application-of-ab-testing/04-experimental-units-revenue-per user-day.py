'''
Experimental units: Revenue per user day

We are going to check what happens when we add a consumable paywall to our app. A paywall is a feature of a website or other technology that requires payment from users in order to access additional content or services.

Here, you'll practice calculating experimental units and baseline values related to our consumable paywall. Both measure revenue only among users who viewed a paywall. Your job is to calculate revenue per user-day, with user-day as the experimental unit.

The purchase_data dataset has been loaded for you.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

*   Extract the 'day' value from the date timestamp as you saw in the video: Using .date.dt.floor('d').
*   To make the calculations easier, replace the NaN purchase_data.price values with 0 by using the np.where() method.
*   Finally, find the mean amount paid per user-day among paywall viewers. To do this, you need to first aggregate the data by 'uid' and 'date', which has been done for you.
'''

# Round our timestamp to 'day'
purchase_data.date = purchase_data.date.dt.floor('d')

# Replace the NaN price values with 0 
purchase_data.price = np.where(np.isnan(purchase_data.price), 0, purchase_data.price)

# Aggregate the data by 'uid' & 'date'
purchase_data_agg = purchase_data.groupby(by=['uid', 'date'], as_index=False)
revenue_user_day = purchase_data_agg.price.sum()

# Calculate the final average
revenue_user_day = revenue_user_day.price.mean()
print(revenue_user_day)