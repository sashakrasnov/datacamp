'''
Grouping & aggregating

You'll be using .groupby() and .agg() a lot in this course, so it's important to become comfortable with them. In this exercise, your job is to calculate a set of summary statistics about the purchase data broken out by 'device' (Android or iOS) and 'gender' (Male or Female).

Following this, you'll compare the values across these subsets, which will give you a baseline for these values as potential KPIs to optimize going forward.

The purchase_data DataFrame from the previous exercise has been pre-loaded for you. As a reminder, it contains purchases merged with user demographics.
'''

import pandas as pd 

customer_data = pd.read_csv('../datasets/customer_data.csv', parse_dates=['reg_date']).rename(columns={'reg_date':'date'})
app_purchases = pd.read_csv('../datasets/inapp_purchases.csv', parse_dates=['date'])

purchase_data = app_purchases.merge(customer_data, on=['uid'], how='inner')
purchase_summary = purchase_data.agg({'price': ['mean', 'median'], 'age': ['mean', 'median']})

'''
INSTRUCTIONS

*   Group the purchase_data DataFrame by 'device' and 'gender' in that order.
*   Aggregate grouped_purchase_data, finding the 'mean', 'median', and standard deviation ('std') of the purchase price, in that order, across these groups.
*   Examine the results. Does the mean differ drastically from the median? How much variability is in each group?
'''

# Group the data 
grouped_purchase_data = purchase_data.groupby(by=['device', 'gender'])

# Aggregate the data
purchase_summary = grouped_purchase_data.agg({'price': ['mean', 'median', 'std']})

# Examine the results
print(purchase_summary)