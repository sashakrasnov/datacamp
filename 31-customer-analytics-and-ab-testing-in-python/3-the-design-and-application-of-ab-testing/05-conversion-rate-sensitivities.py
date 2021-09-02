'''
Conversion rate sensitivities

To mix things up, we will spend the next few exercises working with the conversion rate metric we explored in Chapter One. Specifically you will work to examine what that value becomes under different percentage lifts and look at how many more conversions per day this change would result in. First you will find the average number of paywall views and purchases that were made per day in our observed sample. Good luck!
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

*   Merge the paywall_views with demographics_data tables using an 'inner' join. This will limit the result to only include users who appear in both and will remove everyone who did not view a paywall, which is what we want in this scenario.
*   Group purchase_data by 'date'. The result of this is then aggregated for you by summing over the purchase field to find the total number of purchases and counting over it to find the total number of paywall views.
*   Average each of the resulting sum and count fields to find the average number of purchases and paywall views per day.
*   The results reflect a sample of 0.1% of our overall population for ease of use. Multiply each of daily_purchases and daily_paywall_views by 1000 so our result reflects the magnitude change if we had been observing the entire population.
'''

# Merge the datasets and calculate the per day metrics 
purchase_data = demographics_data.merge(paywall_views, how='inner', on=['uid'])
purchase_data.date = purchase_data.date.dt.floor('d')

# Group and aggregate our combined data set 
daily_purchase_data = purchase_data.groupby(by=['date'], as_index=False)
daily_purchase_data = daily_purchase_data.agg({'purchase': ['sum', 'count']})

# Find the mean of each field and then multiply by 1000 to scale the result
daily_purchases = daily_purchase_data.purchase['sum'].mean()
daily_paywall_views = daily_purchase_data.purchase['count'].mean()
daily_purchases = daily_purchases * 1000
daily_paywall_views = daily_paywall_views * 1000

print(daily_purchases)
print(daily_paywall_views)