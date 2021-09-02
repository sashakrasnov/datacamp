'''
A two-sample bootstrap hypothesis test for difference of means

We now want to test the hypothesis that Frog A and Frog B have the same mean impact force, but not necessarily the same distribution, which is also impossible with a permutation test.

To do the two-sample bootstrap test, we shift both arrays to have the same mean, since we are simulating the hypothesis that their means are, in fact, equal. We then draw bootstrap samples out of the shifted arrays and compute the difference in means. This constitutes a bootstrap replicate, and we generate many of them. The p-value is the fraction of replicates with a difference in means greater than or equal to what was observed.

The objects forces_concat and empirical_diff_means are already in your namespace.
'''

import numpy as np
import pandas as pd

def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))

def draw_bs_reps(data, func, size=1):
    return np.array([bootstrap_replicate_1d(data, func) for _ in range(size)])

def diff_of_means(data_1, data_2):
    return np.mean(data_1) - np.mean(data_2)

df = pd.read_csv('../datasets/frog_tongue.csv', comment='#')

df['impact_force'] = df['impact force (mN)'] / 1000

force_a = df[df.ID == 'II'].impact_force.values
force_b = df[df.ID == 'IV'].impact_force.values

forces_concat = np.concatenate((force_a, force_b))
empirical_diff_means = diff_of_means(force_a, force_b)

'''
INSTRUCTIONS

*   Compute the mean of all forces (from forces_concat) using np.mean().
*   Generate shifted data sets for both force_a and force_b such that the mean of each is the mean of the concatenated array of impact forces.
*   Generate 10,000 bootstrap replicates of the mean each for the two shifted arrays.
*   Compute the bootstrap replicates of the difference of means by subtracting the replicates of the shifted impact force of Frog B from those of Frog A.
*   Compute and print the p-value from your bootstrap replicates.
'''

# Compute mean of all forces: mean_force
mean_force = np.mean(forces_concat)

# Generate shifted arrays
force_a_shifted = force_a - np.mean(force_a) + mean_force
force_b_shifted = force_b - np.mean(force_b) + mean_force

# Compute 10,000 bootstrap replicates from shifted arrays
bs_replicates_a = draw_bs_reps(force_a_shifted, np.mean, size=10000)
bs_replicates_b = draw_bs_reps(force_b_shifted, np.mean, size=10000)

# Get replicates of difference of means: bs_replicates
bs_replicates = bs_replicates_a - bs_replicates_b

# Compute and print p-value: p
p = np.sum(bs_replicates >= empirical_diff_means) / len(bs_replicates)
print('p-value =', p)
