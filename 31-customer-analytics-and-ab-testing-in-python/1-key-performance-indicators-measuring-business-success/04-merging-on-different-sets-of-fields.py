'''
Merging on different sets of fields

As you saw in the previous exercise, both customer_data and app_purchases have a common 'uid' column that you can use to combine them. If you explored them further, you would discover that they also have a common date column that is named 'date' in app_purchases and 'reg_date' in customer_data.

In this exercise you will explore merging on both of these columns and looking at how this impacts your final results.

The two datasets from the previous exercise - customer_data and app_purchases- have been loaded for you, with 'reg_date' in customer_data renamed to 'date'.
'''

import pandas as pd 

customer_data = pd.read_csv('../datasets/customer_data.csv', parse_dates=['reg_date']).rename(columns={'reg_date':'date'})
app_purchases = pd.read_csv('../datasets/inapp_purchases.csv', parse_dates=['date'])

'''
INSTRUCTIONS 1/2

*   Merge customer_data with app_purchases, combining on the 'uid' column.
'''

# Merge on the 'uid' field
uid_combined_data = app_purchases.merge(customer_data, on=['uid'], how='inner')

# Examine the results 
print(uid_combined_data.head())
print(len(uid_combined_data))

'''
INSTRUCTIONS 2/2

*   To look at purchases that happened on the date of registration, merge customer_data to app_purchases on 'uid' and 'date'.
'''

# Merge on the 'uid' and 'date' field
uid_date_combined_data = app_purchases.merge(customer_data, on=['uid', 'date'], how='inner')

# Examine the results 
print(uid_date_combined_data.head())
print(len(uid_date_combined_data))