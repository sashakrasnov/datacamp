'''
Calculating confidence intervals

Now you will calculate the confidence intervals for the A/B test results.

The four values that have been calculated previously have been loaded for you (cont_conv, test_conv, test_size, cont_size) as variables with those names.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

*   Calculate the mean of the distribution of our lift by subtracting cont_conv from test_conv.
*   Calculate the variance of our lift distribution by completing the calculation. You must complete the control portion of the variance.
*   Find the standard deviation of our lift distribution by taking the square root of the lift_variance
*   Find the confidence bounds for our A/B test with a value equal to our lift_mean, a 0.95 confidence level, and our calculated lift_sd. Pass the arguments in that order.
'''

# Calculate the mean of our lift distribution 
lift_mean = test_conv - cont_conv

# Calculate variance and standard deviation 
lift_variance = (1 - test_conv) * test_conv /test_size + (1 - cont_conv) * cont_conv / cont_size
lift_sd = lift_variance**0.5

# Find the confidence intervals with cl = 0.95
confidence_interval = get_ci(lift_mean, 0.95, lift_sd)
print(confidence_interval)

'''
(0.011039999822042502, 0.011040000177957487)

This really provides great context to our results! Notice that our interval is very narrow thanks to our substantial lift and large sample size.
'''