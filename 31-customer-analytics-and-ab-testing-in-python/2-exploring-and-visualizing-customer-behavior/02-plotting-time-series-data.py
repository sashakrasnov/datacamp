'''
Plotting time series data

In trying to boost purchases, we have made some changes to our introductory in-app purchase pricing. In this exercise, you will check if this is having an impact on the number of purchases made by purchasing users during their first week.

The dataset user_purchases has been joined to the demographics data and properly filtered. The column 'first_week_purchases' that is 1 for a first week purchase and 0 otherwise has been added. Additionally, the average amount purchased per user per day has been computed.

We will try to view the impact of this change by looking at a graph of purchases as described in the instructions.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

user_purchases = pd.read_csv('../datasets/user_purchases.csv', parse_dates=['reg_date'])

'''
INSTRUCTIONS

*   Read through and understand code shown and then plot the user_purchases data with 'reg_date' on the x-axis and 'first_week_purchases' on the y-axis.
'''

# Group the data and aggregate first_week_purchases
user_purchases = user_purchases.groupby(by=['reg_date', 'uid']).agg({'first_week_purchases': ['sum']})

# Reset the indexes
user_purchases.columns = user_purchases.columns.droplevel(level=1)
user_purchases.reset_index(inplace=True)

# Find the average amount purchased per user per day
user_purchases = user_purchases.groupby(by=['reg_date']).agg({'first_week_purchases': ['mean']})
user_purchases.columns = user_purchases.columns.droplevel(level=1)
user_purchases.reset_index(inplace=True)

# Plot the results
user_purchases.plot(x='reg_date', y='first_week_purchases')
plt.show()