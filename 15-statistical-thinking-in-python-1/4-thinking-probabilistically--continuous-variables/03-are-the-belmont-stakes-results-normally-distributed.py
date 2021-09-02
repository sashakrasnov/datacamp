'''
Are the Belmont Stakes results Normally distributed?

Since 1926, the Belmont Stakes is a 1.5 mile-long race of 3-year old thoroughbred horses. Secretariat ran the fastest Belmont Stakes in history in 1973. While that was the fastest year, 1970 was the slowest because of unusually wet and sloppy conditions. With these two  outliers removed from the data set, compute the mean and standard deviation of the Belmont winners' times. Sample out of a Normal distribution with this mean and standard deviation using the np.random.normal() function and plot a CDF. Overlay the ECDF from the winning Belmont times. Are these close to Normally distributed?

Note: Justin scraped the data concerning the Belmont Stakes from the Belmont Wikipedia page at https://en.wikipedia.org/wiki/Belmont_Stakes.
'''

import numpy as np
import matplotlib.pyplot as plt

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y

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

np.random.seed(42)

'''
INSTRUCTIONS

*   Compute mean and standard deviation of Belmont winners' times with the two outliers removed. The NumPy array belmont_no_outliers has these data.
*   Take 10,000 samples out of a normal distribution with this mean and standard deviation using np.random.normal().
*   Compute the CDF of the theoretical samples and the ECDF of the Belmont winners' data, assigning the results to x_theor, y_theor and x, y, respectively.
*   Hit submit to plot the CDF of your samples with the ECDF, label your axes and show the plot.
'''

# Compute mean and standard deviation: mu, sigma
mu = np.mean(belmont_no_outliers)
sigma = np.std(belmont_no_outliers)

# Sample out of a normal distribution with this mu and sigma: samples
samples = np.random.normal(mu, sigma, 10000)

# Get the CDF of the samples and of the data
x_theor, y_theor = ecdf(samples)
x, y = ecdf(belmont_no_outliers)

# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('Belmont winning time (sec.)')
_ = plt.ylabel('CDF')
plt.show()
