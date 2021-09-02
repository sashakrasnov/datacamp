'''
Bootstrap hypothesis test

The permutation test has a pretty restrictive hypothesis, that the heterozygotic and wild type bout lengths are identically distributed. Now, use a bootstrap hypothesis test to test the hypothesis that the means are equal, making no assumptions about the distributions.
'''

import pandas as pd
import dc_stat_think as dcst
import numpy as np

df = pd.read_csv('../datasets/gandhi_et_al_bouts.csv', comment='#')

bout_lengths_wt  = df[df.genotype=='wt'].bout_length.values
bout_lengths_het = df[df.genotype=='het'].bout_length.values

# Compute the difference of means: diff_means_exp
diff_means_exp = np.mean(bout_lengths_het) - np.mean(bout_lengths_wt)

'''
INSTRUCTIONS

*   Make an array, bout_lengths_concat, that contains all of the bout lengths for both wild type (bout_lengths_wt) and heterozygote (bout_lengths_het) using np.concatenate().
*   Compute the mean of all bout lengths from this concatenated array (bout_lengths_concat), storing the results in the variable mean_bout_length.
*   Shift both data sets such that they both have the same mean, namely mean_bout_length. Store the shifted arrays in variables wt_shifted and het_shifted.
*   Use dcst.draw_bs_reps() to draw 10,000 bootstrap replicates of the mean for each of the shifted data sets. Store the respective replicates in bs_reps_wt and bs_reps_het.
*   Subtract bs_reps_wt from bs_reps_het to get the bootstrap replicates of the difference of means. Store the results in the variable bs_reps.
*   Compute the p-value, defining "at least as extreme as" to be that the difference of means under the null hypothesis is greater than or equal to that which was observed experimentally. The variable diff_means_exp from the last exercise is already in your namespace.
'''

# Concatenate arrays: bout_lengths_concat
bout_lengths_concat = np.concatenate((bout_lengths_wt, bout_lengths_het))

# Compute mean of all bout_lengths: mean_bout_length
mean_bout_length = np.mean(bout_lengths_concat)

# Generate shifted arrays
wt_shifted = bout_lengths_wt - np.mean(bout_lengths_wt) + mean_bout_length
het_shifted = bout_lengths_het - np.mean(bout_lengths_het) + mean_bout_length

# Compute 10,000 bootstrap replicates from shifted arrays
bs_reps_wt = dcst.draw_bs_reps(wt_shifted, np.mean, size=10000)
bs_reps_het = dcst.draw_bs_reps(het_shifted, np.mean, size=10000)

# Get replicates of difference of means: bs_replicates
bs_reps = bs_reps_het - bs_reps_wt

# Compute and print p-value: p
p = np.sum(bs_reps >= diff_means_exp) / len(bs_reps)
print('p-value =', p)