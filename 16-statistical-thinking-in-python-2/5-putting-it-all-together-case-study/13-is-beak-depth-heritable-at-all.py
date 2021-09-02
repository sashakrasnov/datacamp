'''
Is beak depth heritable at all in G. scandens?

The heritability of beak depth in G. scandens seems low. It could be that this observed heritability was just achieved by chance and beak depth is actually not really heritable in the species. You will test that hypothesis here. To do this, you will do a pairs permutation test.
'''

import numpy as np
import pandas as pd

def heritability(parents, offspring):
    """Compute the heritability from parent and offspring samples."""
    covariance_matrix = np.cov(parents, offspring)
    
    return covariance_matrix[0,1] / covariance_matrix[0,0]

fortis = pd.read_csv('../datasets/fortis_beak_depth_heredity.csv')
scandens = pd.read_csv('../datasets/scandens_beak_depth_heredity.csv')

bd_parent_fortis = (fortis['Male BD'].values + fortis['Female BD'].values)/2
bd_offspring_fortis = fortis['Mid-offspr'].values

bd_parent_scandens = scandens['mid_parent'].values
bd_offspring_scandens = scandens['mid_offspring'].values

heritability_scandens = heritability(bd_parent_scandens, bd_offspring_scandens)
heritability_fortis = heritability(bd_parent_fortis, bd_offspring_fortis)

'''
INSTRUCTIONS

*   Initialize your array of replicates of heritability. We will take 10,000 pairs permutation replicates.
*   Write a for loop to generate your replicates.
*   Permute the bd_parent_scandens array using np.random.permutation().
*   Compute the heritability between the permuted array and the bd_offspring_scandens array using the heritability() function you wrote in the last exercise. Store the result in the replicates array.
*   Compute the p-value as the number of replicates that are greater than the observed heritability_scandens you computed in the last exercise.
'''

# Initialize array of replicates: perm_replicates
perm_replicates = np.empty(10000)

# Draw replicates
for i in range(10000):
    # Permute parent beak depths
    bd_parent_permuted = np.random.permutation(bd_parent_scandens)
    perm_replicates[i] = heritability(bd_parent_permuted, bd_offspring_scandens)

# Compute p-value: p
p = np.sum(perm_replicates >= heritability_scandens) / len(perm_replicates)

# Print the p-value
print('p-val =', p)