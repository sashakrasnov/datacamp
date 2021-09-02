'''
Examining the different cohorts

To finish this lesson, you're now going to plot by 'country' and then by 'device' and examine the results. Hopefully you will see the observed lift across all groups as designed. This would point to the change being the cause of the lift, not some other event impacting the purchase rate.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

user_purchases_country = pd.read_csv('../datasets/user_purchases_country.csv', parse_dates=['reg_date'])
user_purchases_device = pd.read_csv('../datasets/user_purchases_device.csv', parse_dates=['reg_date'])

country_pivot = pd.pivot_table(user_purchases_country, values=['first_week_purchases'], columns=['country'], index=['reg_date'])
print(country_pivot.head())

device_pivot = pd.pivot_table(user_purchases_device, values=['first_week_purchases'], columns=['device'], index=['reg_date'])
print(device_pivot.head())

'''
INSTRUCTIONS 1/2

*   Plot the average first week purchases for each country by registration date ('reg_date'). There are 6 countries here: 'USA', 'CAN', 'FRA', 'BRA', 'TUR', and 'DEU'. Plot them in the order shown.
'''

# Plot the average first week purchases for each country by registration date
country_pivot.plot(x='reg_date', y=['USA', 'CAN', 'FRA', 'BRA', 'TUR', 'DEU'])
plt.show()

'''
INSTRUCTIONS 2/2

*   Now, plot the average first week purchases for each device ('and' and 'iOS') by registration date ('reg_date'). Plot the devices in the order listed.
'''

# Plot the average first week purchases for each device by registration date
device_pivot.plot(x='reg_date', y=['and', 'iOS'])
plt.show()