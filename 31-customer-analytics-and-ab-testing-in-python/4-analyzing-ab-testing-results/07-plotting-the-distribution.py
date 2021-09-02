'''
Plotting the distribution

In this exercise, you will visualize the test and control conversion rates as distributions. It is helpful to practice what was covered in the example, as this may be something you have not applied before. Additionally, viewing the data in this way can give a sense of the variability inherent in our estimation.

Four variables, the test and control variances (test_var, cont_var), and the test and control conversion rates (test_conv and cont_conv) have been loaded for you.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

*   Using the calculated control_sd and test_sd create the range of x values to plot over. It should be 3 standard deviations in either direction from the cont_conv and test_conv respectively.
*   Plot the Normal pdf of the test and control groups by specifying the conversion rate as the mean and the standard deviation in that order in mlab.normpdf()
'''

# Compute the standard deviations
control_sd = cont_var**0.5
test_sd = test_var**0.5

# Create the range of x values 
control_line = np.linspace(cont_conv - 3 * control_sd, cont_conv + 3 * control_sd, 100)
test_line = np.linspace(test_conv - 3 * test_sd ,test_conv +  3 * test_sd, 100)

# Plot the distribution     
plt.plot(control_line, mlab.normpdf(control_line, cont_conv, control_sd))
plt.plot(test_line, mlab.normpdf(test_line, test_conv, test_sd))
plt.show()

'''
We see no overlap, which intuitively implies that our test and control conversion rates are significantly distinct.
'''