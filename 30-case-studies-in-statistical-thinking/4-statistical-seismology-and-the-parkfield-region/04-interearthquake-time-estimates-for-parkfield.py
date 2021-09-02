'''
Interearthquake time estimates for Parkfield

In this exercise, you will first compute the best estimates for the parameters for the Exponential and Gaussian models for interearthquake times. You will then plot the theoretical CDFs for the respective models along with the formal ECDF of the actual Parkfield interearthquake times.
'''

import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

time_gap = np.array([24.06570842, 20.07665982, 21.01848049, 12.24640657, 32.05475702, 38.2532512])

'''
INSTRUCTIONS

*   Compute the mean interearthquake time and store it as mean_time_gap. The time gaps between the major earthquakes, in units of years, are stored in time_gap.
*   Compute the standard deviation of the interearthquake times and store it as std_time_gap.
*   Use np.random.exponential() to draw 10,000 samples out of an Exponential distribution with the appropriate mean. Store them in the variable time_gap_exp.
*   Use np.random.normal() to draw 10,000 samples out of a Normal distribution with the appropriate mean and standard deviation. Store them in the variable time_gap_norm.
*   Plot the theoretical CDFs in one line each, using the *dcst.ecdf() approach introduced earlier in this chapter.
*   Plot the ECDF using the formal=True, min_x=-10, and max_x=50 keyword arguments.
'''

# Compute the mean time gap: mean_time_gap
mean_time_gap = np.mean(time_gap)

# Standard deviation of the time gap: std_time_gap
std_time_gap = np.std(time_gap)

# Generate theoretical Exponential distribution of timings: time_gap_exp
time_gap_exp = np.random.exponential(mean_time_gap, size=10000)

# Generate theoretical Normal distribution of timings: time_gap_norm
time_gap_norm = np.random.normal(mean_time_gap, std_time_gap, size=10000)

# Plot theoretical CDFs
_ = plt.plot(*dcst.ecdf(time_gap_exp))
_ = plt.plot(*dcst.ecdf(time_gap_norm))

# Plot Parkfield ECDF
_ = plt.plot(*dcst.ecdf(time_gap, formal=True, min_x=-10, max_x=50))

# Add legend
_ = plt.legend(('Exp.', 'Norm.'), loc='upper left')

# Label axes, set limits and show plot
_ = plt.xlabel('time gap (years)')
_ = plt.ylabel('ECDF')
_ = plt.xlim(-10, 50)
plt.show()

'''
By eye, the Gaussian model seems to describe the observed data best. We will investigate the consequences of this in the next exercise, and see if we can reject the Exponential model in coming exercises.
'''