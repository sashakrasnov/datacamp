'''
Exploring the power calculation

As discussed, power is the probability of rejecting the null hypothesis when the alternative hypothesis is true. Here you will explore some properties of the power function and see how it relates to sample size among other parameters. The get_power() function has been included and takes the following arguments in the listed order n for sample size, p1 as the baseline value, p2 as the value with lift included, and cl as the confidence level.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

*   Calculate the power using n = 1000 and n = 2000 in that order, along with the pre-loaded parameters, p1, p2, and cl.
*   Using the variable n1 for the sample size, find the power with a confidence level of cl = 0.8 and cl = 0.95 in that order.
*   Hit 'Submit Answer' to compare the ratios. Which change has the bigger impact, increasing the confidence level or the sample size?
'''

# Look at the impact of sample size increase on power
n_param_one = get_power(n=1000, p1=p1, p2=p2, cl=cl)
n_param_two = get_power(n=2000, p1=p1, p2=p2, cl=cl)

# Look at the impact of confidence level increase on power
alpha_param_one = get_power(n=n1, p1=p1, p2=p2, cl=0.8)
alpha_param_two = get_power(n=n1, p1=p1, p2=p2, cl=0.95)
    
# Compare the ratios
print(n_param_two / n_param_one)
print(alpha_param_one / alpha_param_two)

'''
1.7596440001351992
1.8857367092232278

With these particular values it looks like decreasing our confidence level has a slightly larger impact on the power than increasing our sample size
'''