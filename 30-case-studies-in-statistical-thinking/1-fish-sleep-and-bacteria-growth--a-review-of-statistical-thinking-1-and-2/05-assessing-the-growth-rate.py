'''
Assessing the growth rate

To compute the growth rate, you can do a linear regression of the logarithm of the total bacterial area versus time. Compute the growth rate and get a 95% confidence interval using pairs bootstrap. The time points, in units of hours, are stored in the numpy array t and the bacterial area, in units of square micrometers, is stored in bac_area.
'''

import numpy as np
import dc_stat_think as dcst

bac_area, t = np.loadtxt('../datasets/park_bacterial_growth.csv', delimiter=',', skiprows=3, comments='#').T

'''
INSTRUCTIONS

*   Compute the logarithm of the bacterial area (bac_area) using np.log() and store the result in the variable log_bac_area.
*   Compute the slope and intercept of the semilog growth curve using np.polyfit(). Store the slope in the variable growth_rate and the intercept in log_a0.
*   Draw 10,000 pairs bootstrap replicates of the growth rate and log initial area using dcst.draw_bs_pairs_linreg(). Store the results in growth_rate_bs_reps and log_a0_bs_reps.
*   Use np.percentile() to compute the 95% confidence interval of the growth rate (growth_rate_bs_reps).
*   Print the growth rate and confidence interval to the screen. This has been done for you, so hit 'Submit Answer' to view the results!
'''

# Compute logarithm of the bacterial area: log_bac_area
log_bac_area = np.log(bac_area)

# Compute the slope and intercept: growth_rate, log_a0
growth_rate, log_a0 = np.polyfit(t, log_bac_area, 1)

# Draw 10,000 pairs bootstrap replicates: growth_rate_bs_reps, log_a0_bs_reps
growth_rate_bs_reps, log_a0_bs_reps = dcst.draw_bs_pairs_linreg(t, log_bac_area, size=10000)
    
# Compute confidence intervals: growth_rate_conf_int
growth_rate_conf_int = np.percentile(growth_rate_bs_reps, [2.5, 97.5])

# Print the result to the screen
print("""
Growth rate: {0:.4f} sq. µm/hour
95% conf int: [{1:.4f}, {2:.4f}] sq. µm/hour
""".format(growth_rate, *growth_rate_conf_int))