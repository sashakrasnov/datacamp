'''
Parameter estimation: active bout length

Compute the mean active bout length for wild type and mutant, with 95% bootstrap confidence interval. The data sets are again available in the numpy arrays bout_lengths_wt and bout_lengths_mut. The dc_stat_think module has been imported as dcst.
'''

import pandas as pd
import dc_stat_think as dcst
import numpy as np

df = pd.read_csv('../datasets/gandhi_et_al_bouts.csv', comment='#')

bout_lengths_wt  = df[df.genotype=='wt'].bout_length.values
bout_lengths_mut = df[df.genotype=='mut'].bout_length.values

'''
INSTRUCTIONS

*   Compute the mean active bout length for wild type and mutant using np.mean(). Store the results as mean_wt and mean_mut.
*   Draw 10,000 bootstrap replicates for each using dcst.draw_bs_reps(), storing the results as bs_reps_wt and bs_reps_mut.
*   Compute a 95% confidence interval from the bootstrap replicates using np.percentile(), storing the results as conf_int_wt and conf_int_mut.
*   Print the mean and confidence intervals to the screen.
'''

# Compute mean active bout length
mean_wt = bout_lengths_wt.mean()
mean_mut = bout_lengths_mut.mean()

# Draw bootstrap replicates
bs_reps_wt = dcst.draw_bs_reps(bout_lengths_wt, np.mean, size=10000)
bs_reps_mut = dcst.draw_bs_reps(bout_lengths_mut, np.mean, size=10000)

# Compute 95% confidence intervals
conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])

# Print the results
print("""
wt:  mean = {0:.3f} min., conf. int. = [{1:.1f}, {2:.1f}] min.
mut: mean = {3:.3f} min., conf. int. = [{4:.1f}, {5:.1f}] min.
""".format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))