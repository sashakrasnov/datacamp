'''
How does the current effect depend on lane position?

To quantify the effect of lane number on performance, perform a linear regression on the f_13 versus lanes data. Do a pairs bootstrap calculation to get a 95% confidence interval. Finally, make a plot of the regression. The arrays lanes and f_13 are in your namespace.

Note that we could compute error bars on the mean fractional differences and use them in the regression, but that is beyond the scope of this course.
'''

import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

# Original datasets

f_13 = np.array([
       -0.01562214, -0.01463810, -0.00977673, -0.00525713,  0.00204104,
        0.00381014,  0.00756640,  0.01525869])

f_15 = np.array([
       -0.00516018, -0.00392952, -0.00099284,  0.00059953, -0.00242400,
       -0.00451099,  0.00047467,  0.00081962])

lanes = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Plot the the fractional difference for 2013 and 2015
_ = plt.plot(lanes, f_13, marker='.', markersize=12, linestyle='none')

# Label axes and show plot
_ = plt.xlabel('lane')
_ = plt.ylabel('frac. diff. (odd - even)')

'''
INSTRUCTIONS

*   Compute the slope and intercept of the f_13 versus lanes line using np.polyfit().
*   Use dcst.draw_bs_pairs_linreg() to get 10,000 bootstrap replicates of the slope and intercept, storing them respectively in bs_reps_slope and bs_reps_int.
*   Use the bootstrap replicates to compute a 95% confidence interval for the slope.
*   Print the slope and 95% confidence interval to the screen. This has been done for you.
*   Using np.array(), generate x-values to use for the plot of the bootstrap lines. x should go from 1 to 8.
*   The plot is already populated with the data. Write a for loop to add 100 bootstrap lines to the plot using the keyword arguments color='red', alpha=0.2, and linewidth=0.5.
'''

# Compute the slope and intercept of the frac diff/lane curve
slope, intercept = np.polyfit(lanes, f_13, 1)

# Compute bootstrap replicates
bs_reps_slope, bs_reps_int = dcst.draw_bs_pairs_linreg(lanes, f_13, size=10000)

# Compute 95% confidence interval of slope
conf_int = np.percentile(bs_reps_slope, [2.5, 97.5])

# Print slope and confidence interval
print("""
slope: {0:.5f} per lane
95% conf int: [{1:.5f}, {2:.5f}] per lane""".format(slope, *conf_int))

# x-values for plotting regression lines
x = np.array([1, 8])

# Plot 100 bootstrap replicate lines
for i in range(100):
    _ = plt.plot(x, bs_reps_slope[i] * x + bs_reps_int[i], 
                 color='red', alpha=0.2, linewidth=0.5)
   
# Update the plot
plt.draw()
plt.show()

'''
slope: 0.00447 per lane
95% conf int: [0.00394, 0.00501] per lane

The slope is a fractional difference of about 0.4% per lane. This is quite a substantial difference at this elite level of swimming where races can be decided by tiny differences.
'''