'''
Sensitivity

Continuing with the conversion rate metric, you will now utilize the results from the previous exercise to evaluate a few potential sensitivities that we could make use of in planning our experiment. The baseline conversion_rate has been loaded for you, calculated in the same way we saw in Chapter One. Additionally the daily_paywall_views and daily_purchases values you calculated previously have been loaded.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS 1/3

*   Using the proposed small_sensitivity of 0.1, find the lift in conversion rate and purchasers that would result by applying this sensitivity. Are these resulting values reasonable?
'''

small_sensitivity = 0.1 

# Find the conversion rate when increased by the percentage of the sensitivity above
small_conversion_rate = conversion_rate * (1 + small_sensitivity) 

# Apply the new conversion rate to find how many more users per day that translates to
small_purchasers = daily_paywall_views * small_conversion_rate

# Subtract the initial daily_purcahsers number from this new value to see the lift
purchaser_lift = small_purchasers - daily_purchases

print(small_conversion_rate)
print(small_purchasers)
print(purchaser_lift)

'''
INSTRUCTIONS 2/3

*   Now repeating the steps from before, find the lift in conversion rate and purchasers using the medium_sensitivity. In this exercise you are additionally asked to complete the step to find the increase in purchasers based on this new conversion rate.
'''

medium_sensitivity = 0.2

# Find the conversion rate when increased by the percentage of the sensitivity above
medium_conversion_rate = conversion_rate * (1 + medium_sensitivity) 

# Apply the new conversion rate to find how many more users per day that translates to
medium_purchasers = daily_paywall_views * medium_conversion_rate

# Subtract the initial daily_purcahsers number from this new value to see the lift
purchaser_lift = medium_purchasers - daily_purchases

print(medium_conversion_rate)
print(medium_purchasers)
print(purchaser_lift)

'''
INSTRUCTIONS 3/3

*   Finally repeat the steps from before to find the increase in conversion rate and purchasers when using the very large sensitivity of 0.5. The steps required are the same as the previous exercise. How do the results compare those returned in the previous two exercises?
'''

large_sensitivity = 0.5

# Find the conversion rate lift with the sensitivity above
large_conversion_rate = conversion_rate * (1 + large_sensitivity)

# Find how many more users per day that translates to
large_purchasers = daily_paywall_views * large_conversion_rate
purchaser_lift = large_purchasers - daily_purchases

print(large_conversion_rate)
print(large_purchasers)
print(purchaser_lift)

'''
While it seems that a 50% increase may be too drastic and unreasonable to expect, the small and medium sensitivities both seem very reasonable.
'''