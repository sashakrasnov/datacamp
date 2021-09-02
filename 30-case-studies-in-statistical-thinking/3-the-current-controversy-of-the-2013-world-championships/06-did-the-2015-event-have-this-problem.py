'''
Did the 2015 event have this problem?

You would like to know if this is a typical problem with pools in competitive swimming. To address this question, perform a similar analysis for the results of the 2015 FINA World Championships. That is, compute the mean fractional improvement for going from lanes 1-3 to lanes 6-8 for the 2015 competition, along with a 95% confidence interval on the mean. Also test the hypothesis that the mean fractional improvement is zero.

The arrays swimtime_low_lanes_15 and swimtime_high_lanes_15 have the pertinent data.
'''

import numpy as np
import dc_stat_think as dcst

# Original datasets

swimtime_low_lanes_15 = np.array([
       27.66, 24.69, 23.29, 23.05, 26.87, 31.03, 22.04, 24.51, 21.86,
       25.64, 25.91, 24.77, 30.14, 27.23, 24.31, 30.2 , 26.86])

swimtime_high_lanes_15 = np.array([
       27.7 , 24.64, 23.21, 23.09, 26.87, 30.74, 21.88, 24.50, 21.86,
       25.9 , 26.20, 24.73, 30.13, 26.92, 24.31, 30.25, 26.76])

'''
INSTRUCTIONS

*   Compute the fractional improvement, f using the arrays swimtime_low_lanes_15 and swimtime_high_lanes_15. Also compute the mean of f, storing it as f_mean.
*   Draw 10,000 bootstrap replicates of the mean f.
*   Compute the 95% confidence interval of the mean fractional improvement.
*   Shift f to create f_shift such that its mean is zero.
*   Draw 100,000 bootstrap replicates of the mean of f_shift.
*   Compute the p-value.
'''

# Compute f and its mean
f = (swimtime_low_lanes_15 - swimtime_high_lanes_15) / swimtime_low_lanes_15
f_mean = np.mean(f)

# Draw 10,000 bootstrap replicates
bs_reps = dcst.draw_bs_reps(f, np.mean, size=10000)

# Compute 95% confidence interval
conf_int = np.percentile(bs_reps, [2.5, 97.5])

# Shift f
f_shift = f - f_mean

# Draw 100,000 bootstrap replicates of the mean
bs_reps = dcst.draw_bs_reps(f_shift, np.mean, size=100000)

# Compute the p-value
p_val = np.sum(bs_reps >= f_mean) / 100000

# Print the results
print("""
mean frac. diff.: {0:.5f}
95% conf int of mean frac. diff.: [{1:.5f}, {2:.5f}]
p-value: {3:.5f}""".format(f_mean, *conf_int, p_val))

'''
mean frac. diff.: 0.00079
95% conf int of mean frac. diff.: [-0.00198, 0.00341]
p-value: 0.28179

Both the confidence interval and the p-value suggest that there was no lane bias in 2015.
'''