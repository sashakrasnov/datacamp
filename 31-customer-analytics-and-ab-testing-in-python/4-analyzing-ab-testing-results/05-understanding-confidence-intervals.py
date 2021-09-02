'''
Understanding confidence intervals

In this exercise, you'll develop your intuition for how various parameter values impact confidence intervals. Specifically, you will explore through the get_ci() function how changes widen or tighten the confidence interval. This is the function signature, where cl is the confidence level and sd is the standard deviation.

|   def get_ci(value, cl, sd):
|     loc = sci.norm.ppf(1 - cl/2)
|     rng_val = sci.norm.cdf(loc - value/sd)
|
|     lwr_bnd = value - rng_val
|     upr_bnd = value + rng_val 
|
|     return_val = (lwr_bnd, upr_bnd)
|     return(return_val)
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS 1/3

*   Find the confidence interval with a value of 1, a confidence level of 0.975 and a standard deviation of 0.5.
'''

# Compute and print the confidence interval
confidence_interval  = get_ci(1, 0.975, 0.5)
print(confidence_interval)

'''
INSTRUCTIONS 2/3

*   Repeat the calculation, updating the confidence level to 0.95 and the standard deviation to 2. Leave the value as 1
'''

# Compute and print the confidence interval
confidence_interval  = get_ci(1, 0.95, 2)
print(confidence_interval)

'''
INSTRUCTIONS 3/3

*   Finally, update your code such that the standard deviation is 0.001 while leaving the confidence level and value the same as the previous exercise part. Compare the three confidence intervals outputted. How do they seem to relate to the parameters used?
'''

# Compute and print the confidence interval
confidence_interval  = get_ci(1, 0.95, 0.001)
print(confidence_interval)

'''
(0.9755040421682947, 1.0244959578317054)
(0.6690506448818785, 1.3309493551181215)
(1.0, 1.0)

As our standard deviation decreases so too does the width of our confidence interval. Great work!
'''