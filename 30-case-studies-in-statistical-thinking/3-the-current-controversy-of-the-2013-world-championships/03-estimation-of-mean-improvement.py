'''
Estimation of mean improvement

You will now estimate how big this current effect is. Compute the mean fractional improvement for being in a high-numbered lane versus a low-numbered lane, along with a 95% confidence interval of the mean.
'''

import numpy as np
import dc_stat_think as dcst

# Original datasets

swimtime_high_lanes = np.array([
       24.62, 22.9 , 27.05, 24.76, 30.31, 24.54, 26.12, 27.71, 23.15,
       23.11, 21.62, 28.02, 24.73, 24.95, 25.83, 30.61, 27.04, 21.67,
       27.16, 30.23, 21.51, 22.97, 28.05, 21.65, 24.54, 26.06])

swimtime_low_lanes = np.array([
       24.66, 23.28, 27.2 , 24.95, 32.34, 24.66, 26.17, 27.93, 23.35,
       22.93, 21.93, 28.33, 25.14, 25.19, 26.11, 31.31, 27.44, 21.85,
       27.48, 30.66, 21.74, 23.22, 27.93, 21.42, 24.79, 26.46])

# Compute the fractional improvement of being in high lane: f
f = (swimtime_low_lanes - swimtime_high_lanes) / swimtime_low_lanes

'''
INSTRUCTIONS

*   Compute the mean fractional difference using np.mean(). The variable f from the last exercise is already in your namespace.
*   Draw 10,000 bootstrap replicates of the mean fractional difference using dcst.draw_bs_reps(). Store the result in a numpy array named bs_reps.
*   Compute the 95% confidence interval using np.percentile().
*   Hit 'Submit Answer' to print the mean fractional improvement and 95% confidence interval to the screen.
'''

# Compute the mean difference: f_mean
f_mean = np.mean(f)

# Draw 10,000 bootstrap replicates: bs_reps
bs_reps = dcst.draw_bs_reps(f, np.mean, size=10000)

# Compute 95% confidence interval: conf_int
conf_int = np.percentile(bs_reps, [2.5, 97.5])

# Print the result
print("""
mean frac. diff.: {0:.5f}
95% conf int of mean frac. diff.: [{1:.5f}, {2:.5f}]""".format(f_mean, *conf_int))