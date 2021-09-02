'''
Assessing the growth rate

To compute the growth rate, you can do a linear regression of the logarithm of the total bacterial area versus time. Compute the growth rate and get a 95% confidence interval using pairs bootstrap. The time points, in units of hours, are stored in the numpy array t and the bacterial area, in units of square micrometers, is stored in bac_area.
'''

import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

bac_area, t = np.loadtxt('../datasets/park_bacterial_growth.csv', delimiter=',', skiprows=3, comments='#').T

# Compute logarithm of the bacterial area: log_bac_area
log_bac_area = np.log(bac_area)

# Draw 10,000 pairs bootstrap replicates: growth_rate_bs_reps, log_a0_bs_reps
growth_rate_bs_reps, log_a0_bs_reps = dcst.draw_bs_pairs_linreg(t, log_bac_area, size=10000)
    
'''
INSTRUCTIONS

*   Compute the logarithm of the bacterial area (bac_area) using np.log() and store the result in the variable log_bac_area.
*   Compute the slope and intercept of the semilog growth curve using np.polyfit(). Store the slope in the variable growth_rate and the intercept in log_a0.
*   Draw 10,000 pairs bootstrap replicates of the growth rate and log initial area using dcst.draw_bs_pairs_linreg(). Store the results in growth_rate_bs_reps and log_a0_bs_reps.
*   Use np.percentile() to compute the 95% confidence interval of the growth rate (growth_rate_bs_reps).
*   Print the growth rate and confidence interval to the screen. This has been done for you, so hit 'Submit Answer' to view the results!
'''

# Plot data points in a semilog-y plot with axis labeles
_ = plt.semilogy(t, bac_area, marker='.', linestyle='none')

# Generate x-values for the bootstrap lines: t_bs
t_bs = np.array([0, 14])

# Plot the first 100 bootstrap lines
for i in range(100):
    y = np.exp(growth_rate_bs_reps[i] * t_bs + log_a0_bs_reps[i])
    _ = plt.semilogy(t_bs, y, linewidth=0.5, alpha=0.05, color='red')
    
# Label axes and show plot
_ = plt.xlabel('time (hr)')
_ = plt.ylabel('area (sq. µm)')
plt.show()
