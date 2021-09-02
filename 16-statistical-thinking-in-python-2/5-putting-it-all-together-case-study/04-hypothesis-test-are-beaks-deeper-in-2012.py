'''
Hypothesis test: Are beaks deeper in 2012?

Your plot of the ECDF and determination of the confidence interval make it pretty clear that the beaks of G. scandens on Daphne Major have gotten deeper. But is it possible that this effect is just due to random chance? In other words, what is the probability that we would get the observed difference in mean beak depth if the means were the same?

Be careful! The hypothesis we are testing is not that the beak depths come from the same distribution. For that we could use a permutation test. The hypothesis is that the means are equal. To perform this hypothesis test, we need to shift the two data sets so that they have the same mean and then use bootstrap sampling to compute the difference of means.
'''

import numpy as np
import pandas as pd

def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))

def draw_bs_reps(data, func, size=1):
    return np.array([bootstrap_replicate_1d(data, func) for _ in range(size)])

bd = {}

for y in [1975, 2012]:
    df = pd.read_csv('../datasets/finch_beaks_{}.csv'.format(y), skiprows=1, header=None)

    scns = (df[1] == 'scandens')

    bd[y] = df[scns][3].values

bd_1975 = bd[1975]
bd_2012 = bd[2012]

mean_diff = np.mean(bd_2012) - np.mean(bd_1975)

'''
INSTRUCTIONS

*   Make a concatenated array of the 1975 and 2012 beak depths and compute and store its mean.
*   Shift bd_1975 and bd_2012 such that their means are equal to the one you just computed for the combined data set.
*   Take 10,000 bootstrap replicates of the mean each for the 1975 and 2012 beak depths.
*   Subtract the 1975 replicates from the 2012 replicates to get bootstrap replicates of the difference.
*   Compute and print the p-value. The observed difference in means you computed in the last exercise is still in your namespace as mean_diff.
'''

# Compute mean of combined data set: combined_mean
combined_mean = np.mean(np.concatenate((bd_1975, bd_2012)))

# Shift the samples
bd_1975_shifted = bd_1975 - np.mean(bd_1975) + combined_mean
bd_2012_shifted = bd_2012 - np.mean(bd_2012) + combined_mean

# Get bootstrap replicates of shifted data sets
bs_replicates_1975 = draw_bs_reps(bd_1975_shifted, np.mean, 10000)
bs_replicates_2012 = draw_bs_reps(bd_2012_shifted, np.mean, 10000)

# Compute replicates of difference of means: bs_diff_replicates
bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975

# Compute the p-value: p
p = np.sum(bs_diff_replicates >= mean_diff) / len(bs_diff_replicates)

# Print p-value
print('p =', p)
