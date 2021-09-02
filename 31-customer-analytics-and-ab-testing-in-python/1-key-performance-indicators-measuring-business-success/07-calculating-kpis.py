'''
Grouping & aggregating

You'll be using .groupby() and .agg() a lot in this course, so it's important to become comfortable with them. In this exercise, your job is to calculate a set of summary statistics about the purchase data broken out by 'device' (Android or iOS) and 'gender' (Male or Female).

Following this, you'll compare the values across these subsets, which will give you a baseline for these values as potential KPIs to optimize going forward.

The purchase_data DataFrame from the previous exercise has been pre-loaded for you. As a reminder, it contains purchases merged with user demographics.
'''

import pandas as pd 

from datetime import timedelta

#customer_data = pd.read_csv('../datasets/customer_data.csv', parse_dates=['reg_date']).rename(columns={'reg_date':'date'})
customer_data = pd.read_csv('../datasets/customer_data.csv', parse_dates=['reg_date'])
app_purchases = pd.read_csv('../datasets/inapp_purchases.csv', parse_dates=['date'])

purchase_data = app_purchases.merge(customer_data, on=['uid'], how='inner')

current_date = pd.Timestamp(2018,3,17)

'''
INSTRUCTIONS 1/4

*   Subtract timedelta(days=28) from current_date to find the last date that we will count purchases from. The current_date variable has already been defined.
'''

# Compute max_purchase_date
max_purchase_date = current_date - timedelta(days=28)

'''
INSTRUCTIONS 2/4

*   Filter out all users in purchase_data who registered in the last 28 days. That is, users whose purchase_data.reg_date is less than max_purchase_date.
'''

# Compute max_purchase_date
max_purchase_date = current_date - timedelta(days=28)

# Filter to only include users who registered before our max date
purchase_data_filt = purchase_data[purchase_data.reg_date < max_purchase_date]

'''
INSTRUCTIONS 3/4

*   Filter this dataset to only include purchases that occured on a date within the first 28 days.
'''

# Compute max_purchase_date
max_purchase_date = current_date - timedelta(days=28)

# Filter to only include users who registered before our max date
purchase_data_filt = purchase_data[purchase_data.reg_date < max_purchase_date]

# Filter to contain only purchases within the first 28 days of registration
purchase_data_filt = purchase_data_filt[(purchase_data_filt.date <
                        purchase_data_filt.reg_date + 
                        timedelta(days=28))]

'''
INSTRUCTIONS 4/4

*   Find the mean of the price paid on purchases in purchase_data_filt.


'''

# Compute max_purchase_date
max_purchase_date = current_date - timedelta(days=28)

# Filter to only include users who registered before our max date
purchase_data_filt = purchase_data[purchase_data.reg_date < max_purchase_date]

# Filter to contain only purchases within the first 28 days of registration
purchase_data_filt = purchase_data_filt[(purchase_data_filt.date <= 
                        purchase_data_filt.reg_date + timedelta(days=28))]

# Output the mean price paid per purchase
print(purchase_data_filt.price.mean())