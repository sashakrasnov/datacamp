'''
Power Analysis - Part II

Previously, we simulated one instance of the experiment & generated a p-value. We will now use this framework to calculate statistical power. Power of an experiment is the experiment's ability to detect a difference between treatment & control if the difference really exists. It's good statistical hygiene to strive for 80% power.

For our website, we want to know how many people need to visit each variant, such that we can detect a 10% increase in time spent with 80% power. For this, we start with a small sample (50), simulate multiple instances of this experiment & check power. If 80% power is reached, we stop. If not, we increase the sample size & try again.
'''

import numpy as np
import scipy.stats.stats as st

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

# Initialize effect_size, control_mean, control_sd
effect_size, sample_size, control_mean, control_sd = 0.1, 50, 1, 0.5

sims = 1000

'''
INSTRUCTIONS

*   For the time spent random variables, set the size such that it has shape sample_size × sims.
*   Calculate power as a fraction of p-values less than 0.05 (statistically significant).
*   If power is greater than or equal to 80%, break out of the while loop. Else, keep incrementing sample_size by 10.
'''

sample_size = 50

# Keep incrementing sample size by 10 till we reach required power
while 1:
    control_time_spent = np.random.normal(loc=control_mean, scale=control_sd, size=(sample_size, sims))
    treatment_time_spent = np.random.normal(loc=control_mean*(1+effect_size), scale=control_sd, size=(sample_size, sims))
    t, p = st.ttest_ind(treatment_time_spent, control_time_spent)
    
    # Power is the fraction of times in the simulation when the p-value was less than 0.05
    power = (p < 0.05).sum()/sims
    if power >= 0.8: 
        break
    else: 
        sample_size += 10
print("For 80% power, sample size required = {}".format(sample_size))