'''
Hypothesis test on Pearson correlation

The observed correlation between female illiteracy and fertility may just be by chance; the fertility of a given country may actually be totally independent of its illiteracy. You will test this hypothesis. To do so, permute the illiteracy values but leave the fertility values fixed. This simulates the hypothesis that they are totally independent of each other. For each permutation, compute the Pearson correlation coefficient and assess how many of your permutation replicates have a Pearson correlation coefficient greater than the observed one.

The function pearson_r() that you wrote in the prequel to this course for computing the Pearson correlation coefficient is already in your name space.
'''

import numpy as np
import pandas as pd

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0,1]

df = pd.read_csv('../datasets/female_literacy_fertility.csv')

fertility = df['fertility'].values
illiteracy = 100 - df['female literacy'].values

'''
Instructions

*   Compute the observed Pearson correlation between illiteracy and fertility.
*   Initialize an array to store your permutation replicates.
*   Write a for loop to draw 10,000 replicates:
    *   Permute the illiteracy measurements using np.random.permutation().
    *   Compute the Pearson correlation between the permuted illiteracy array, illiteracy_permuted, and fertility.
*   Compute and print the p-value from the replicates.
'''

# Compute observed correlation: r_obs
r_obs = pearson_r(illiteracy, fertility)

# Initialize permutation replicates: perm_replicates
perm_replicates = np.empty(10000)

# Draw replicates
for i in range(10000):
    # Permute illiteracy measurments: illiteracy_permuted
    illiteracy_permuted = np.random.permutation(illiteracy)

    # Compute Pearson correlation
    perm_replicates[i] = pearson_r(illiteracy_permuted, fertility)

# Compute p-value: p
p = np.sum(perm_replicates >= r_obs) / len(perm_replicates)
print('p-val =', p)
