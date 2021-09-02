'''
Running a simple bootstrap

Welcome to the first exercise in the bootstrapping section. We will work through an example where we learn to run a simple bootstrap. As we saw in the video, the main idea behind bootstrapping is sampling with replacement.

Suppose you own a factory that produces wrenches. You want to be able to characterize the average length of the wrenches and ensure that they meet some specifications. Your factory produces thousands of wrenches every day, but it's infeasible to measure the length of each wrench. However, you have access to a representative sample of 100 wrenches. Let's use bootstrapping to get the 95% confidence interval (CI) for the average lengths.

Examine the list wrench_lengths, which has 100 observed lengths of wrenches in the shell.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

# Default set by DataCamp
wrench_lengths = np.array([
        8.91436940, 10.99734545, 10.28297850,  8.49370529,  9.42139975,
       11.65143654,  7.57332076,  9.57108737, 11.26593626,  9.13325960,
        9.32111385,  9.90529103, 11.49138963,  9.36109800,  9.55601804,
        9.56564872, 12.20593008, 12.18678609, 11.00405390, 10.38618640,
       10.73736858, 11.49073203,  9.06416613, 11.17582904,  8.74611933,
        9.36224850, 10.90710520,  8.57131930,  9.85993128,  9.13824510,
        9.74438063,  7.20141089,  8.22846690,  9.30012277, 10.92746243,
        9.82636432, 10.00284592, 10.68822271,  9.12046366, 10.28362732,
        9.19463348,  8.27233051,  9.60910021, 10.57380586, 10.33858905,
        9.98816951, 12.39236527, 10.41291216, 10.97873601, 12.23814334,
        8.70591468,  8.96121179, 11.74371223,  9.20193726, 10.02968323,
       11.06931597, 10.89070639, 11.75488618, 11.49564414, 11.06939267,
        9.22729129, 10.79486267, 10.31427199,  8.67373454, 11.41729905,
       10.80723653, 10.04549008,  9.76690794,  8.80169886, 10.19952407,
       10.46843912,  9.16884502, 11.16220405,  8.90279695,  7.87689965,
       11.03972709,  9.59663396,  9.87397041,  9.16248328,  8.39403724,
       11.25523737,  9.31113102, 11.66095249, 10.80730819,  9.68524185,
        8.91409760,  9.26753801,  8.78747687, 12.08711336, 10.16444123,
       11.15020554,  8.73264795, 10.18103513, 11.17786194,  9.66498924,
       11.03111446,  8.91543209,  8.63652846, 10.37940061,  9.62082357])

# Randomly generated example 1
#wrench_lengths = np.random.rand(100) * 12
# Randomly generated example 2, similar to DataCamp
#wrench_lengths = np.random.rand(100)*4 + 8

'''
INSTRUCTIONS

*   Draw a random sample with replacement from wrench_lengths and store it in temp_sample. Set size = len(wrench_lengths).
*   Calculate the mean length of each sample, assign it to sample_mean, and then append it to mean_lengths.
*   Calculate the bootstrapped mean and bootstrapped 95% confidence interval by using np.percentile().
'''

# Draw some random sample with replacement and append mean to mean_lengths.
mean_lengths, sims = [], 1000
for i in range(sims):
    temp_sample = np.random.choice(wrench_lengths, replace=True, size=len(wrench_lengths))
    sample_mean = temp_sample.mean()
    mean_lengths.append(sample_mean)
    
# Calculate bootstrapped mean and 95% confidence interval.
print("Bootstrapped Mean Length = {}, 95% CI = {}".format(np.mean(mean_lengths), np.percentile(mean_lengths, [2.5, 97.5])))