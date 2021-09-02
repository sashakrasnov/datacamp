'''
The b-value for Parkfield

The ECDF is effective at exposing roll-off, as you could see below magnitude 1. Because there are plenty of earthquakes above magnitude 3, you can use Mt = 3 as your completeness threshold. With this completeness threshold, compute the b-value for the Parkfield region from 1950 to 2016, along with the 95% confidence interval. Print the results to the screen. The variable mags with all the magnitudes is in your namespace.

Overlay the theoretical Exponential CDF to verify that the Parkfield region follows the Gutenberg-Richter Law.
'''

import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

def b_value(mags, mt, perc=[2.5, 97.5], n_reps=None):
    """Compute the b-value and optionally its confidence interval."""
    # Extract magnitudes above completeness threshold: m
    m = mags[mags >= mt]

    # Compute b-value: b
    b = (np.mean(m) - mt) * np.log(10)

    # Draw bootstrap replicates
    if n_reps is None:
        return b
    else:
        m_bs_reps = dcst.draw_bs_reps(m, np.mean, size=n_reps)

        # Compute b-value from replicates: b_bs_reps
        b_bs_reps = (m_bs_reps - mt) * np.log(10)

        # Compute confidence interval: conf_int
        conf_int = np.percentile(b_bs_reps, perc)
    
        return b, conf_int


mags = np.loadtxt('../datasets/parkfield_earthquakes_1950-2017.csv', delimiter=',', comments='#', skiprows=3, usecols=4)

mt = 3

'''
INSTRUCTIONS

*   Compute the b-value and the 95% confidence interval using your b_value() function. Use 10,000 bootstrap replicates.
*   Use np.random.exponential() to draw 100,000 samples from the theoretical distribution. Hint: The mean for the distribution is b/np.log(10), and you need to add mt to your samples to appropriately handle the location parameter. Store the result in m_theor.
*   Plot the ECDF of m_theor as a line.
*   Plot the ECDF of all magnitudes above mt as dots. Hint: You need to use Boolean indexing to slice out magnitudes at or above mt from the mags array.
*   Hit 'Submit Answer' to display the plot and print the b-value and confidence interval to the screen.
'''

# Compute b-value and confidence interval
b, conf_int = b_value(mags, mt, perc=[2.5, 97.5], n_reps=10000)

# Generate samples to for theoretical ECDF
m_theor = np.random.exponential(b/np.log(10), size=100000) + mt

# Plot the theoretical CDF
_ = plt.plot(*dcst.ecdf(m_theor))

# Plot the ECDF (slicing mags >= mt)
_ = plt.plot(*dcst.ecdf(mags[mags >= mt]), marker='.', linestyle='none')

# Pretty up and show the plot
_ = plt.xlabel('magnitude')
_ = plt.ylabel('ECDF')
_ = plt.xlim(2.8, 6.2)
plt.show()

# Report the results
print("""
b-value: {0:.2f}
95% conf int: [{1:.2f}, {2:.2f}]""".format(b, *conf_int))

'''
b-value: 1.08
95% conf int: [0.94, 1.24]

Parkfield seems to follow the Gutenberg-Richter law very well. The b-value of about 1 is typical for regions along fault zones.
'''