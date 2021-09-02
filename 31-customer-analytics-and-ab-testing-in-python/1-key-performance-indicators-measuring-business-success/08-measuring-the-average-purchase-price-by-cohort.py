'''
Measuring the average purchase price by cohort

Building on the previous exercise, let's look at the same KPI, average purchase price, and a similar one, median purchase price, within the first 28 days. Additionally, let's look at these metrics not limited to 28 days to compare.

We can calculate these metrics across a set of cohorts and see what differences emerge. This is a useful task as it can help us understand how behaviors vary across cohorts.

Note that in our data the price variable is given in cents.
'''

import pandas as pd 
import numpy as np

from datetime import timedelta

#customer_data = pd.read_csv('../datasets/customer_data.csv', parse_dates=['reg_date']).rename(columns={'reg_date':'date'})
customer_data = pd.read_csv('../datasets/customer_data.csv', parse_dates=['reg_date'])
app_purchases = pd.read_csv('../datasets/inapp_purchases.csv', parse_dates=['date'])

purchase_data = app_purchases.merge(customer_data, on=['uid'], how='inner')

current_date = pd.Timestamp(2018,3,17)

'''
INSTRUCTIONS 1/3

Compute month1

The price for purchases where:
    (1) purchase_data.reg_date is less than max_reg_date
    (2) purchase_data.date is less than purchase_data.reg_date plus 28 days and np.NaN for purchases that don't meet these conditions.
'''

# Set the max registration date to be one month before today
max_reg_date = current_date - timedelta(days=28)

# Find the month 1 values
month1 = np.where((purchase_data.reg_date < max_reg_date) &
                 (purchase_data.date < purchase_data.reg_date + timedelta(days=28)),
                 purchase_data.price, np.NaN)
                 
# Update the value in the DataFrame
purchase_data['month1'] = month1

'''
INSTRUCTIONS 2/3

*   Now, group purchase_data by gender then device using the .groupby() method.
'''

# Set the max registration date to be one month before today
max_reg_date = current_date - timedelta(days=28)

# Find the month 1 values 
month1 = np.where((purchase_data.reg_date < max_reg_date) &
                 (purchase_data.date <= purchase_data.reg_date + timedelta(days=28)),
                 purchase_data.price, np.NaN)
                 
# Update the value in the DataFrame 
purchase_data['month1'] = month1

# Group the data by gender and device 
purchase_data_upd = purchase_data.groupby(by=['gender', 'device'], as_index=False)

'''
INSTRUCTIONS 3/3

*   Aggregate the "mean" and "median" of 'month1' and'price' using the .agg() method in the listed order of aggregations and fields.
'''

# Set the max registration date to be one month before today
max_purchase_date = current_date - timedelta(days=28)

# Find the Month 1 Values using the conditions provided in the instructions 
month1 = np.where((purchase_data.reg_date < max_purchase_date) &
                 (purchase_data.date <= purchase_data.reg_date + timedelta(days=28)),
                 purchase_data.price, np.NaN)

# Update the value in the DataFrame 
purchase_data['month1'] = month1

# Group the data by gender and device 
purchase_data_upd = purchase_data.groupby(by=['gender', 'device'], as_index=False) 

# Aggregate the month1 and price data 
purchase_summary = purchase_data_upd.agg(
                        {'month1': ['mean', 'median'],
                        'price': ['mean', 'median']})

# Examine the results 
print(purchase_summary)