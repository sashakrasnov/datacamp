'''
Quantification of the b-values

Based on the plot you generated in the previous exercise, you can safely use a completeness threshold of mt = 3. Using this threshold, compute b-values for the period between 1980 and 2009 and for 2010 through mid-2017. The function b_value() you wrote last chapter, which computes the b-value and confidence interval from a set of magnitudes and completeness threshold, is available in your namespace, as are the numpy arrays mags_pre and mags_post from the last exercise, and mt.
'''

import numpy as np
import pandas as pd
import dc_stat_think as dcst

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


df = pd.read_csv('../datasets/oklahoma_earthquakes_1950-2017.csv', comment='#', index_col='time', parse_dates=True, usecols=['time','mag'])

time = np.array([d.timestamp() / 31556925.9747 + 1970 for d in df['1980-01':'2017-06'].index.to_pydatetime()])
mags = df['1980-01':'2017-06'].mag.values

mt = 3

# Get magnitudes before and after 2010
mags_pre = mags[time < 2010]
mags_post = mags[time >= 2010]

'''
INSTRUCTIONS

*   Compute the b-value and 95% confidence interval for earthquakes from 1980 through 2009 using 10,000 bootstrap replicates.
*   Compute the b-value and 95% confidence interval for earthquakes from 2010 through mid-2017 using 10,000 bootstrap replicates.
*   Hit 'Submit Answer' to print the results to the screen.
'''

# Compute b-value and confidence interval for pre-2010
b_pre, conf_int_pre = b_value(mags_pre, mt, perc=[2.5, 97.5], n_reps=10000)

# Compute b-value and confidence interval for post-2010
b_post, conf_int_post = b_value(mags_post, mt, perc=[2.5, 97.5], n_reps=10000)

# Report the results
print("""
1980 through 2009
b-value: {0:.2f}
95% conf int: [{1:.2f}, {2:.2f}]

2010 through mid-2017
b-value: {3:.2f}
95% conf int: [{4:.2f}, {5:.2f}]
""".format(b_pre, *conf_int_pre, b_post, *conf_int_post))

'''
1980 through 2009
b-value: 0.74
95% conf int: [0.54, 0.96]
    
2010 through mid-2017
b-value: 0.62
95% conf int: [0.60, 0.65]

The confidence interval for the b-value for recent earthquakes is tighter than for earlier ones because there are many more recent ones. Still, the confidence intervals overlap, and we can perform a hypothesis test to see if we might get these results if the b-values are actually the same.
'''