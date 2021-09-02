'''
Hypothesis test: Does lane assignment affect performance?

Perform a bootstrap hypothesis test of the null hypothesis that the mean fractional improvement going from low-numbered lanes to high-numbered lanes is zero. Take the fractional improvement as your test statistic, and "at least as extreme as" to mean that the test statistic under the null hypothesis is greater than or equal to what was observed.
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

# Compute the mean difference: f_mean
f_mean = np.mean(f)

'''
INSTRUCTIONS

*   Create an array f_shift, by shifting f such that its mean is zero. You can use the variable f_mean computed in previous exercises.
*   Draw 100,000 bootstrap replicates of the mean of the f_shift.
*   Compute and print the p-value.
'''

# Shift f: f_shift
f_shift = f - f_mean

# Draw 100,000 bootstrap replicates of the mean: bs_reps
bs_reps = dcst.draw_bs_reps(f_shift, np.mean, size=100000)

# Compute and report the p-value
p_val = np.sum(bs_reps >= f_mean) / 100000
print('p =', p_val)

'''
p = 0.00033

A p-value of 0.0003 is quite small and suggests that the mean fractional improvment is greater than zero. For fun, I tested the more restrictive hypothesis that lane number has no bearing at all on performance (item (1) in the previous MCQ), and I got an even smaller p-value of about 0.00001. You can perform that test, too, for practice if you like.
'''