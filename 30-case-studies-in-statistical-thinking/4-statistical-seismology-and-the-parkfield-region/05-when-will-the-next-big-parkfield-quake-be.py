'''
When will the next big Parkfield quake be?

The last big earthquake in the Parkfield region was on the evening of September 27, 2004 local time. Your task is to get an estimate as to when the next Parkfield quake will be, assuming the Exponential model and also the Gaussian model. In both cases, the best estimate is given by the mean time gap, which you computed in the last exercise to be 24.62 years, meaning that the next earthquake would be in 2029. Compute 95% confidence intervals on when the next earthquake will be assuming an Exponential distribution parametrized by mean_time_gap you computed in the last exercise. Do the same assuming a Normal distribution parametrized by mean_time_gap and std_time_gap.
'''

import numpy as np
import dc_stat_think as dcst

time_gap = np.array([24.06570842, 20.07665982, 21.01848049, 12.24640657, 32.05475702, 38.2532512])
today = 2019.0204192439246
last_quake = 2004.74

# Compute the mean time gap: mean_time_gap
mean_time_gap = np.mean(time_gap)

# Standard deviation of the time gap: std_time_gap
std_time_gap = np.std(time_gap)

'''
INSTRUCTIONS

*   Draw 100,000 sample from an Exponential distribution with a mean given by mean_time_gap. Store the result in exp_samples.
*   Draw 100,000 sample from a Normal distribution with a mean given by mean_time_gap and standard deviation given by std_time_gap. Store the result in norm_samples.
*   Because there has not been a Parkfield earthquake as of today, slice out samples that are greater than today - last_quake, where I have stored the decimal year of today as today, and last_quake = 2004.74, the decimal year of the last Parkfield earthquake. Overwrite the respective exp_samples and norm_samples variables with these sliced arrays.
*   Use np.percentile() to compute the 95% confidence interval for when the next Parkfield earthquake will be. In the same function call, you can also compute the median by including the 50th percentile.
'''

# Draw samples from the Exponential distribution: exp_samples
exp_samples = np.random.exponential(mean_time_gap, size=100000)

# Draw samples from the Normal distribution: norm_samples
norm_samples = np.random.normal(mean_time_gap, std_time_gap, size=100000)

# No earthquake as of today, so only keep samples that are long enough
exp_samples = exp_samples[exp_samples > today - last_quake]
norm_samples = norm_samples[norm_samples > today - last_quake]

# Compute the confidence intervals with medians
conf_int_exp = np.percentile(exp_samples, [2.5, 50, 97.5]) + last_quake
conf_int_norm = np.percentile(norm_samples, [2.5, 50, 97.5]) + last_quake

# Print the results
print('Exponential:', conf_int_exp)
print('     Normal:', conf_int_norm)

'''
Exponential: [2019.65541773 2036.00462663 2109.44537946]
     Normal: [2019.97261641 2030.53638442 2046.37758475]

The models given decidedly different predictions. The Gaussian model says the next earthquake is almost sure to be in the next few decades, but the Exponential model says we may very well have to wait longer.
'''
