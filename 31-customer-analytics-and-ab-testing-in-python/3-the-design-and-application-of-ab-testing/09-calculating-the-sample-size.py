'''
Calculating the sample size

You're now going to utilize the sample size function to determine how many users you need for the test and control groups under various circumstances.

Included is the get_sample_size() function you viewed previously, which takes four primary arguments, power, p1, p2 and cl as described before:

|   def get_sample_size(power, p1, p2, cl, max_n=1000000):
|       n = 1 
|       while n <= max_n:
|           tmp_power = get_power(n, p1, p2, cl)
|
|           if tmp_power >= power: 
|               return n 
|           else: 
|               n = n + 100
|
|       return "Increase Max N Value"

You will continue working with the paywall conversion rate data for this exercise, which has been pre-loaded as purchase_data.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS 1/3

*   Calculate the baseline conversion_rate per paywall view by dividing the total amount spent across all purchase_data.purchase values by the count of purchase_data.purchase values in the dataset.
'''

# Merge the demographics and purchase data to only include paywall views
purchase_data = demographics_data.merge(paywall_views, how='inner', on=['uid'])
                            
# Find the conversion rate
conversion_rate = (sum(purchase_data.purchase) / purchase_data.purchase.count())
            
print(conversion_rate)

'''
INSTRUCTIONS 2/3

Using the conversion_rate value you found, calculate p2, the baseline increased by the percent lift listed.

*   Calculate the sample size needed using the parameters provided in the code comments. Remember the order of the arguments for get_sample_size is power, baseline conversion rate, lifted conversion rate and confidence level.
'''

# Merge the demographics and purchase data to only include paywall views
purchase_data = demographics_data.merge(paywall_views, how='inner', on=['uid'])
                            
# Find the conversion rate
conversion_rate = (sum(purchase_data.purchase) / purchase_data.purchase.count())
            
# Desired Power: 0.8
# CL: 0.90
# Percent Lift: 0.1
p2 = conversion_rate * (1 + 0.1)
sample_size = get_sample_size(0.8, conversion_rate, p2, 0.90)
print(sample_size)

'''
INSTRUCTIONS 3/3

*   Repeat the steps in the previous exercise only now with the new power parameter provided. How does increasing our desired power impact the outputed sample size?
'''

# Merge the demographics and purchase data to only include paywall views
purchase_data = demographics_data.merge(paywall_views, how='inner', on=['uid'])
                            
# Find the conversion rate
conversion_rate = (sum(purchase_data.purchase) / purchase_data.purchase.count())

# Desired Power: 0.95
# CL: 0.90
# Percent Lift: 0.1
p2 = conversion_rate * (1 + 0.1)
sample_size = get_sample_size(0.95, conversion_rate, p2, 0.90)
print(sample_size)

