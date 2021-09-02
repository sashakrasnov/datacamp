'''
Intuition behind statistical significance

In this exercise you will work to gain an intuitive understanding of statistical significance. You will do this by utilizing the get_pvalue() function on a variety of parameter sets that could reasonably arise or be chosen during the course of an A/B test. While doing this you should observing how statistical significance results vary as you change the parameters. This will help build your intuition surrounding this concept, and reveal some of the subtle pitfalls of p-values. As a reminder, this is the get_pvalue() function signature:

|   def get_pvalue(con_conv, test_conv, con_size, test_size):  
|       lift =  - abs(test_conv - con_conv)
|
|       scale_one = con_conv * (1 - con_conv) * (1 / con_size)
|       scale_two = test_conv * (1 - test_conv) * (1 / test_size)
|       scale_val = (scale_one + scale_two)**0.5
|
|       p_value = 2 * stats.norm.cdf(lift, loc = 0, scale = scale_val )
|
|       return p_value
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS 1/3

*   Find the p-value with initial conversion rate of 0.1, test conversion rate of 0.17, and 1000 observations in each group.
'''

# Get the p-value
p_value = get_pvalue(con_conv=0.1, test_conv=0.17, con_size=1000, test_size=1000)
print(p_value)

'''
INSTRUCTIONS 2/3

*   Find the p-value with control conversion of 0.1, test conversion of 0.15, and 100 observations in each group.
'''

# Get the p-value
p_value = get_pvalue(con_conv=0.1, test_conv=0.15, con_size=100, test_size=100)
print(p_value)

'''
INSTRUCTIONS 3/3

*   Now find the p-value with control conversion of 0.48, test conversion of 0.50, and 1000 observations in each group.
'''

# Get the p-value
p_value = get_pvalue(con_conv=0.48, test_conv=0.50, con_size=1000, test_size=1000)
print(p_value)

'''
4.131297741047306e-06
0.28366948940702086
0.370901935824383

To recap we observed that a large lift makes us confident in our observed result, while a small sample size makes us less so, and ultimately high variance can lead to a high p-value!
'''