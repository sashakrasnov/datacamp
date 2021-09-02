'''
Practicing aggregations

It's time to begin exploring the in-app purchase data in more detail. Here, you will practice aggregating the dataset in various ways using the .agg() method and then examine the results to get an understanding of the overall data, as well as a feel for how to aggregate data using pandas.

Loaded for you is a DataFrame named purchase_data which is the dataset of in-app purchase data merged with the user demographics data from earlier.

Before getting started, it's good practice to explore this purchase_data DataFrame in the IPython Shell. In particular, notice the price column: You'll examine it further in this exercise.
'''

import pandas as pd 

customer_data = pd.read_csv('../datasets/customer_data.csv', parse_dates=['reg_date']).rename(columns={'reg_date':'date'})
app_purchases = pd.read_csv('../datasets/inapp_purchases.csv', parse_dates=['date'])

purchase_data = app_purchases.merge(customer_data, on=['uid'], how='inner')

'''
INSTRUCTIONS 1/3

*   Find the 'mean' purchase price paid across our dataset. Then examine the output before moving on.
'''

# Calculate the mean purchase price 
purchase_price_mean = purchase_data.price.agg('mean')

# Examine the output 
print(purchase_price_mean)

'''
INSTRUCTIONS 2/3

*   Now, use the .agg() method to find the 'mean' and 'median' prices together.
'''

# Calculate the mean and median purchase price 
purchase_price_summary = purchase_data.price.agg(['mean', 'median'])

# Examine the output 
print(purchase_price_summary)

'''
INSTRUCTIONS 3/3

*   Now, use the .agg() method to find the 'mean' and 'median' prices together.
'''

# Calculate the mean and median of price and age
purchase_summary = purchase_data.agg({'price': ['mean', 'median'], 'age': ['mean', 'median']})

# Examine the output 
print(purchase_summary)