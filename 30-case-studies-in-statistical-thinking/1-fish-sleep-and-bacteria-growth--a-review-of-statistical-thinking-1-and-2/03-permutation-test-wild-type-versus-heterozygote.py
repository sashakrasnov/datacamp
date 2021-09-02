'''
Permutation test: wild type versus heterozygote

Test the hypothesis that the heterozygote and wild type bout lengths are identically distributed using a permutation test.
'''

import pandas as pd
import dc_stat_think as dcst
import numpy as np

df = pd.read_csv('../datasets/gandhi_et_al_bouts.csv', comment='#')

bout_lengths_wt  = df[df.genotype=='wt'].bout_length.values
bout_lengths_het = df[df.genotype=='het'].bout_length.values

'''
INSTRUCTIONS

*   Compute the mean active bout length for wild type and mutant using np.mean(). Store the results as mean_wt and mean_mut.
*   Draw 10,000 bootstrap replicates for each using dcst.draw_bs_reps(), storing the results as bs_reps_wt and bs_reps_mut.
*   Compute a 95% confidence interval from the bootstrap replicates using np.percentile(), storing the results as conf_int_wt and conf_int_mut.
*   Print the mean and confidence intervals to the screen.
'''

# Compute the difference of means: diff_means_exp
diff_means_exp = np.mean(bout_lengths_het) - np.mean(bout_lengths_wt)
#diff_means_exp = dcst.diff_of_means(bout_lengths_het, bout_lengths_wt)

# Draw permutation replicates: perm_reps
perm_reps = dcst.draw_perm_reps(bout_lengths_het, bout_lengths_wt, 
                               dcst.diff_of_means, size=10000)

# Compute the p-value: p-val
p_val = np.sum(perm_reps >= diff_means_exp) / len(perm_reps)

# Print the result
print('p =', p_val)