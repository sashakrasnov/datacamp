'''
Computing the b-value

The b-value is a common metric for the seismicity of a region. You can imagine you would like to calculate it often when working with earthquake data. For tasks like this that you will do often, it is best to write a function! So, write a function with signature b_value(mags, mt, perc=[2.5, 97.5], n_reps=None) that returns the b-value and (optionally, if n_reps is not None) its confidence interval for a set of magnitudes, mags. The completeness threshold is given by mt. The perc keyword argument gives the percentiles for the lower and upper bounds of the confidence interval, and n_reps is the number of bootstrap replicates to use in computing the confidence interval.
'''

import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

mags = np.loadtxt('../datasets/parkfield_earthquakes_1950-2017.csv', delimiter=',', comments='#', skiprows=3, usecols=4)

'''
INSTRUCTIONS

*   Define a function with signature b_value(mags, mt, perc=[2.5, 97.5], n_reps=None) that does the following:
    *   Slice magnitudes out of mags at and above the completeness threshold mt using Boolean indexing. Store the result in the variable m.
    *   Compute the best estimate of the b-value. Remember, the best estimate for the b-value is b = (M_mean - Mt)·ln(10). Store the result in the variable b.
    *   if n_reps is not None, do the following.
        *   Draw n_reps bootstrap replicates of the mean of m. Store the result in the variable m_bs_reps.
        *   Convert the bootstrap replicates of the mean of m to replicates of the b-value. Store the result in b_bs_reps.
        *   Compute the confidence interval from the bootstrap replicates of the b-value. Store the result in conf_int.
    *   Return b and conf_int, or just b if n_reps is None.
'''

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