'''
Plotting the difference distribution

Now lets plot the difference distribution of our results that is, the distribution of our lift.

The cont_var and test_var as well as the cont_conv and test_conv have been loaded for you. Additionally the upper and lower confidence interval bounds of this distribution have been provided as lwr_ci and upr_ci respectively.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

*   Calculate mean of the lift distribution by subtracting the control conversion rate (cont_conv) from the test conversion rate (test_conv)
*   Generate the range of x-values for the difference distribution, making it 3 standard deviations wide.
*   Plot a normal distribution by specifying the calculated lift_mean and lift_sd.
*   Plot a green vertical line at the distributions mean, and a red vertical lines at each of the lower and upper confidence interval bounds. This has been done for you, so hit 'Submit Answer' to see the result!
'''

# Find the lift statistics
lift_mean = test_conv - cont_conv
lift_sd = (test_var + cont_var) ** 0.5

# Generate the range of x-values
lift_line = np.linspace(lift_mean - 3 * lift_sd, lift_mean + 3 * lift_sd, 100)

# Plot the distribution 
plt.plot(lift_line, mlab.normpdf(lift_line, lift_mean, lift_sd))

# Add the annotation lines
plt.axvline(x = lift_mean, color = 'green')
plt.axvline(x = lwr_ci, color = 'red')
plt.axvline(x = upr_ci, color = 'red')
plt.show()

'''
This really contextualizes the lift we observed and provides more information than reporting the numerical point estimate alone would.
'''