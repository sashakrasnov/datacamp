'''
What are the chances of a horse matching or beating Secretariat's record?

Assume that the Belmont winners' times are Normally distributed (with the 1970 and 1973 years removed), what is the probability that the winner of a given Belmont Stakes will run it as fast or faster than Secretariat?
'''

import numpy as np
import matplotlib.pyplot as plt

belmont_no_outliers = np.array([148.51,  146.65,  148.52,  150.70,  150.42,  150.88,  151.57,
                                147.54,  149.65,  148.74,  147.86,  148.75,  147.50,  148.26,
                                149.71,  146.56,  151.19,  147.88,  149.16,  148.82,  148.96,
                                152.02,  146.82,  149.97,  146.13,  148.10,  147.20,  146.00,
                                146.40,  148.20,  149.80,  147.00,  147.20,  147.80,  148.20,
                                149.00,  149.80,  148.60,  146.80,  149.60,  149.00,  148.20,
                                149.20,  148.00,  150.40,  148.80,  147.20,  148.80,  149.60,
                                148.40,  148.40,  150.20,  148.80,  149.20,  149.20,  148.40,
                                150.20,  146.60,  149.80,  149.00,  150.80,  148.60,  150.20,
                                149.00,  148.60,  150.20,  148.20,  149.40,  150.80,  150.20,
                                152.20,  148.20,  149.20,  151.00,  149.60,  149.60,  149.40,
                                148.60,  150.00,  150.60,  149.20,  152.60,  152.80,  149.60,
                                151.60,  152.80,  153.20,  152.40,  152.20])

mu = np.mean(belmont_no_outliers)
sigma = np.std(belmont_no_outliers)

'''
INSTRUCTIONS

*   Take 1,000,000 samples from the normal distribution using the np.random.normal() function.
*   The mean mu and standard deviation sigma are already loaded into the namespace of your IPython instance.
*   Compute the fraction of samples that have a time less than or equal to Secretariat's time of 144 seconds.
*   Print the result.
'''

# Take a million samples out of the Normal distribution: samples
samples = np.random.normal(mu, sigma, 1000000)

# Compute the fraction that are faster than 144 seconds: prob
prob = len(samples[np.where(samples <= 144)]) / len(samples)

# Print the result
print('Probability of besting Secretariat:', prob)
