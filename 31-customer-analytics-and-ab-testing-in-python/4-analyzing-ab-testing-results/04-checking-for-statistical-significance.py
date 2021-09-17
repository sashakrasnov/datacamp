'''
Checking for statistical significance

Now that you have an intuitive understanding of statistical significance and p-values, you will apply it to your test result data.

The four parameters needed for the p-value function are the two conversion rates - cont_conv and test_conv and the two group sizes - cont_size and test_size. These are available in your workspace, so you have everything you need to check for statistical significance in our experiment results.
'''

import pandas as pd 
from scipy import stats


def get_pvalue(con_conv, test_conv, con_size, test_size):  
    lift =  - abs(test_conv - con_conv)

    scale_one = con_conv * (1 - con_conv) * (1 / con_size)
    scale_two = test_conv * (1 - test_conv) * (1 / test_size)
    scale_val = (scale_one + scale_two)**0.5

    p_value = 2 * stats.norm.cdf(lift, loc = 0, scale = scale_val)

    return p_value


cont_conv = 0.09096495570387314
test_conv = 0.1020053238686779
cont_size = 5329
test_size = 5748

'''
INSTRUCTIONS

*   Find the p-value of our experiment using the loaded variables cont_conv, test_conv, cont_size, test_size calculated from our data. Then determine if our result is statistically significant by running the second section of code.
'''

# Compute the p-value
p_value = get_pvalue(con_conv=cont_conv, test_conv=test_conv, con_size=cont_size, test_size=test_size)

print(p_value)

# Check for statistical significance
if p_value >= 0.05:
    print('Not Significant')
else:
    print('Significant Result')

'''
0.04900185792087508
Significant Result

It looks like our result is significant. Now we can continue on to provide confidence intervals.
'''