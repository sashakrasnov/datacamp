'''
Jackknife confidence interval for the median

In this exercise, we will calculate the jackknife 95% CI for a non-standard estimator. Here, we will look at the median. Keep in mind that the variance of a jackknife estimator is n-1 times the variance of the individual jackknife sample estimates where n is the number of observations in the original sample.

Returning to the wrench factory, you are now interested in estimating the median length of the wrenches along with a 95% CI to ensure that the wrenches are within tolerance.

Let's revisit the code from the previous exercise, but this time in the context of median lengths. By the end of this exercise, you will have a much better idea of how to use jackknife resampling to calculate confidence intervals for non-standard estimators.
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

# Randomly generated example similar to DataCamp
#wrench_lengths = np.random.rand(100)*4 + 8

n = len(wrench_lengths)
index = np.arange(n)

'''
INSTRUCTIONS

*   Append the median length of each jackknife sample to median_lengths.
*   Calculate the mean of the jackknife estimate of median_length and assign to jk_median_length.
*   Calculate the upper and lower confidence intervals of the median using 1.96*np.sqrt(jk_var).
'''

# Leave one observation out to get the jackknife sample and store the median length
median_lengths = []
for i in range(n):
    jk_sample = wrench_lengths[index != i]
    median_lengths.append(np.median(jk_sample))

#median_lengths = np.array(median_lengths)

# Calculate jackknife estimate and it's variance
jk_median_length = np.mean(median_lengths)
jk_var = (n-1) * np.var(median_lengths)

# Assuming normality, calculate lower and upper 95% confidence intervals
print("Jackknife 95% CI lower = {}, upper = {}".format(jk_median_length - 1.96*np.sqrt(jk_var), jk_median_length + 1.96*np.sqrt(jk_var)))