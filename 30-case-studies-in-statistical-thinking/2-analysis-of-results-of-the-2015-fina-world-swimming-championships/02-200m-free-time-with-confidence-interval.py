'''
200 m free time with confidence interval

Now, you will practice parameter estimation and computation of confidence intervals by computing the mean and median swim time for the men's 200 freestyle heats. The median is useful because it is immune to heavy tails in the distribution of swim times, such as the slow swimmers in the heats. mens_200_free_heats is still in your namespace.
'''

import numpy as np
import dc_stat_think as dcst

# Original dataset
mens_200_free_heats = np.array([
       118.32, 107.73, 107.00, 106.39, 108.75, 117.74, 108.43, 111.96,
       114.36, 121.77, 108.23, 107.47, 118.41, 108.29, 106.00, 109.32,
       111.49, 112.92, 117.38, 110.95, 108.27, 111.78, 107.87, 110.77,
       109.05, 111.00, 108.77, 106.10, 106.61, 113.68, 108.20, 106.20,
       111.01, 109.25, 112.00, 118.55, 109.56, 108.18, 111.67, 108.09,
       110.04, 113.97, 109.91, 112.12, 111.65, 110.18, 116.36, 124.59,
       115.59, 121.01, 106.88, 108.96, 109.09, 108.67, 109.60, 111.85,
       118.54, 108.12, 124.38, 107.17, 107.48, 106.65, 106.91, 140.68,
       117.93, 120.66, 111.29, 107.10, 108.49, 112.43, 110.61, 110.38,
       109.87, 106.73, 107.18, 110.98, 108.55, 114.31, 112.05])
    
'''
INSTRUCTIONS

*   Compute the mean and median swim times, storing them in variables mean_time and median_time. The swim times are contained in mens_200_free_heats.
*   Draw 10,000 bootstrap replicates each of the mean and median swim time using dcst.draw_bs_reps(). Store the results in bs_reps_mean and bs_reps_median.
*   Compute the 95% confidence intervals for the mean and median using the bootstrap replicates and np.percentile().
*   Hit 'Submit Answer' to print the results to the screen!
'''

# Compute mean and median swim times
mean_time = np.mean(mens_200_free_heats)
median_time = np.median(mens_200_free_heats)

# Draw 10,000 bootstrap replicates of the mean and median
bs_reps_mean = dcst.draw_bs_reps(mens_200_free_heats, np.mean, size=10000)
bs_reps_median = dcst.draw_bs_reps(mens_200_free_heats, np.median, size=10000)

# Compute the 95% confidence intervals
conf_int_mean = np.percentile(bs_reps_mean, [2.5, 97.5])
conf_int_median = np.percentile(bs_reps_median, [2.5, 97.5])

# Print the result to the screen
print("""
mean time: {0:.2f} sec.
95% conf int of mean: [{1:.2f}, {2:.2f}] sec.

median time: {3:.2f} sec.
95% conf int of median: [{4:.2f}, {5:.2f}] sec.
""".format(mean_time, *conf_int_mean, median_time, *conf_int_median))