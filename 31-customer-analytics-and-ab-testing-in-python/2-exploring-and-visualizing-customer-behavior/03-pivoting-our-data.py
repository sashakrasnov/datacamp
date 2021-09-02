'''
Pivoting our data

As you saw, there does seem to be an increase in the number of purchases by purchasing users within their first week. Let's now confirm that this is not driven only by one segment of users. We'll do this by first pivoting our data by 'country' and then by 'device'. Our change is designed to impact all of these groups equally.

The user_purchases data from before has been grouped and aggregated by the 'country' and 'device' columns. These objects are available in your workspace as user_purchases_country and user_purchases_device.

As a reminder, .pivot_table() has the following signature:

|   pd.pivot_table(data, values, columns, index)
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

user_purchases_country = pd.read_csv('../datasets/user_purchases_country.csv', parse_dates=['reg_date'])
user_purchases_device = pd.read_csv('../datasets/user_purchases_device.csv', parse_dates=['reg_date'])

'''
INSTRUCTIONS 1/2

*   Pivot the user_purchases_country table such that we have our first_week_purchases as our values, the country as the column, and our reg_date as the row.
'''

# Pivot the data
country_pivot = pd.pivot_table(user_purchases_country, values=['first_week_purchases'], columns=['country'], index=['reg_date'])
print(country_pivot.head())

'''
INSTRUCTIONS 2/2

*   Now lets look at our device data. Let us pivot the user_purchases_device table such that we have our first_week_purchases as our values, the device as the column, and our reg_date as the row.
'''

# Pivot the data
device_pivot = pd.pivot_table(user_purchases_device, values=['first_week_purchases'], columns=['device'], index=['reg_date'])
print(device_pivot.head())