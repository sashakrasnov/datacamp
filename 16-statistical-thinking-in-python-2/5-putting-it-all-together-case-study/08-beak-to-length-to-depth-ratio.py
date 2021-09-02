'''
Beak length to depth ratio

The linear regressions showed interesting information about the beak geometry. The slope was the same in 1975 and 2012, suggesting that for every millimeter gained in beak length, the birds gained about half a millimeter in depth in both years. However, if we are interested in the shape of the beak, we want to compare the ratio of beak length to beak depth. Let's make that comparison.

Remember, the data are stored in bd_1975, bd_2012, bl_1975, and bl_2012.
'''

import numpy as np
import pandas as pd

def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))

def draw_bs_reps(data, func, size=1):
    return np.array([bootstrap_replicate_1d(data, func) for _ in range(size)])

bd = {}
bl = {}

for y in [1975, 2012]:
    df = pd.read_csv('../datasets/finch_beaks_{}.csv'.format(y), skiprows=1, header=None)

    scns = (df[1] == 'scandens')

    bl[y] = df[scns][2].values
    bd[y] = df[scns][3].values

bl_1975 = bl[1975]
bd_1975 = bd[1975]

bl_2012 = bl[2012]
bd_2012 = bd[2012]

'''
INSTRUCTIONS

*   Make arrays of the beak length to depth ratio of each bird for 1975 and for 2012.
*   Compute the mean of the length to depth ratio for 1975 and for 2012.
*   Generate 10,000 bootstrap replicates each for the mean ratio for 1975 and 2012 using your draw_bs_reps() function.
*   Get a 99% bootstrap confidence interval for the length to depth ratio for 1975 and 2012.
*   Print the results.
'''

# Compute length-to-depth ratios
ratio_1975 = bl_1975 / bd_1975
ratio_2012 = bl_2012 / bd_2012

# Compute means
mean_ratio_1975 = np.mean(ratio_1975)
mean_ratio_2012 = np.mean(ratio_2012)

# Generate bootstrap replicates of the means
bs_replicates_1975 = draw_bs_reps(ratio_1975, np.mean, size=10000)
bs_replicates_2012 = draw_bs_reps(ratio_2012, np.mean, size=10000)

# Compute the 99% confidence intervals
conf_int_1975 = np.percentile(bs_replicates_1975, [0.5, 99.5])
conf_int_2012 = np.percentile(bs_replicates_2012, [0.5, 99.5])

# Print the results
print('1975: mean ratio =', mean_ratio_1975, 'conf int =', conf_int_1975)
print('2012: mean ratio =', mean_ratio_2012, 'conf int =', conf_int_2012)
      