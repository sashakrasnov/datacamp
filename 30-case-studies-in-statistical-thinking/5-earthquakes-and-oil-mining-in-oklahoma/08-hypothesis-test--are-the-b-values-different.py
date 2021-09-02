'''
Hypothesis test: are the b-values different?

Perform the hypothesis test sketched out on the previous exercise. The variables mags_pre and mags_post are already loaded into your namespace, as is mt = 3.
'''

import numpy as np
import pandas as pd
import dc_stat_think as dcst

df = pd.read_csv('../datasets/oklahoma_earthquakes_1950-2017.csv', comment='#', index_col='time', parse_dates=True, usecols=['time','mag'])

time = np.array([d.timestamp() / 31556925.9747 + 1970 for d in df['1980-01':'2017-06'].index.to_pydatetime()])
mags = df['1980-01':'2017-06'].mag.values

mt = 3

mags_pre = mags[time < 2010]
mags_post = mags[time >= 2010]

'''
INSTRUCTIONS

*   Slice out the magnitudes of earthquakes before 2010 that have a magnitude above (or equal) the completeness threshold and overwrite mags_pre with the result. Do the same for mags_post.
*   Compute the observed difference in mean magnitudes, subtracting the magnitudes of pre-2010 earthquakes from those of post-2010 earthquakes.
*   Generate 10,000 permutation replicates using dcst.draw_perm_reps(). Use dcst.diff_of_means as the argument for func.
*   Compute and print the p-value taking "at least as extreme as" to mean that the test statistic is smaller than what was observed.
'''

# Only magnitudes above completeness threshold
mags_pre = mags_pre[mags_pre >= mt]
mags_post = mags_post[mags_post >= mt]

# Observed difference in mean magnitudes: diff_obs
diff_obs = np.mean(mags_post) - np.mean(mags_pre)

# Generate permutation replicates: perm_reps
perm_reps = dcst.draw_perm_reps(mags_post, mags_pre, func=dcst.diff_of_means, size=10000)

# Compute and print p-value
p_val = np.sum(perm_reps < diff_obs) / 10000
print('p =', p_val)

'''
p = 0.0993

A p-value around 0.1 suggests that the observed magnitudes are commensurate with there being no change in b-value after wastewater injection began.
'''