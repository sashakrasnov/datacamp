'''
Standard error

Previously we observed how to calculate the standard error using the .std() method. In this exercise, you will explore how to calculate standard error for a conversion rate, which requires a slightly different. You will calculate this step by step in this exercise.

Loaded for you is our inner merged dataset user_purchases as well as the computed conversion_rate value.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

*   Find the number of paywall views in the dataset using .count(). Store this in n.
*   Calculate a quantity we will call v by finding the conversion_rate times the rate of not converting.
*   Now find our variance, var, by dividing v by n. This is the variance of our conversion rate estimate.
*   Finally the square root of var has been taken and stored as the variable se for you. This is the standard error of our estimate.
'''

# Find the n & v quantities
n = purchase_data.purchase.count()

# Calculate the quantitiy "v"
v = conversion_rate * (1 - conversion_rate) 

# Calculate the variance and standard error of the estimate
var = v / n 
se = var**0.5

print(var)
print(se)

'''
3.351780834114284e-07
0.0005789456653360731

Notice how closely the standard error is related to our sample size?
'''