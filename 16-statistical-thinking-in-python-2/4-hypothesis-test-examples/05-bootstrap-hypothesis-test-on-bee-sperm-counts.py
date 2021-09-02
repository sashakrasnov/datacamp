'''
Bootstrap hypothesis test on bee sperm counts

Now, you will test the following hypothesis: On average, male bees treated with neonicotinoid insecticide have the same number of active sperm per milliliter of semen than do untreated male bees. You will use the difference of means as your test statistic.

For your reference, the call signature for the draw_bs_reps() function you wrote in chapter 2 is draw_bs_reps(data, func, size=1).
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))

def draw_bs_reps(data, func, size=1):
    return np.array([bootstrap_replicate_1d(data, func) for _ in range(size)])

df = pd.read_csv('../datasets/bee_sperm.csv', comment='#', usecols=['Treatment', 'Alive Sperm Millions'])

control = df[df.Treatment == 'Control']['Alive Sperm Millions'].values * 2
treated = df[df.Treatment == 'Pesticide']['Alive Sperm Millions'].values * 2

'''
INSTRUCTIONS

*   Compute the mean alive sperm count of control minus that of treated.
*   Compute the mean of all alive sperm counts. To do this, first concatenate control and treated and take the mean of the concatenated array.
*   Generate shifted data sets for both control and treated such that the shifted data sets have the same mean. This has already been done for you.
*   Generate 10,000 bootstrap replicates of the mean each for the two shifted arrays. Use your draw_bs_reps() function.
*   Compute the bootstrap replicates of the difference of means.
*   The code to compute and print the p-value has been written for you. Hit 'Submit Answer' to see the result!
'''

# Compute the difference in mean sperm count: diff_means
diff_means = np.mean(control) - np.mean(treated)

# Compute mean of pooled data: mean_count
mean_count = np.mean(np.concatenate((control, treated)))

# Generate shifted data sets
control_shifted = control - np.mean(control) + mean_count
treated_shifted = treated - np.mean(treated) + mean_count

# Generate bootstrap replicates
bs_reps_control = draw_bs_reps(control_shifted, np.mean, size=10000)
bs_reps_treated = draw_bs_reps(treated_shifted, np.mean, size=10000)

# Get replicates of difference of means: bs_replicates
bs_replicates = bs_reps_control - bs_reps_treated

# Compute and print p-value: p
p = np.sum(bs_replicates >= np.mean(control) - np.mean(treated)) / len(bs_replicates)
print('p-value =', p)
