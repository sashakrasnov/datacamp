'''
Hypothesis test: can this be by chance?

The EDA and linear regression analysis is pretty conclusive. Nonetheless, you will top off the analysis of the zigzag effect by testing the hypothesis that lane assignment has nothing to do with the mean fractional difference between even and odd lanes using a permutation test. You will use the Pearson correlation coefficient, which you can compute with dcst.pearson_r() as the test statistic. The variables lanes and f_13 are already in your namespace.
'''

import numpy as np
import dc_stat_think as dcst

# Original datasets

f_13 = np.array([
       -0.01562214, -0.01463810, -0.00977673, -0.00525713,  0.00204104,
        0.00381014,  0.00756640,  0.01525869])

f_15 = np.array([
       -0.00516018, -0.00392952, -0.00099284,  0.00059953, -0.00242400,
       -0.00451099,  0.00047467,  0.00081962])

lanes = np.array([1, 2, 3, 4, 5, 6, 7, 8])

'''
INSTRUCTIONS

*   Compute the observed Pearson correlation coefficient, storing it as rho.
*   Initialize an array to store the 10,000 permutation replicates of rho using np.empty(). Name the array perm_reps_rho.
*   Write a for loop to draw the permuation replicates.
    *   Scramble the lanes array using np.random.permutation().
    *   Compute the Pearson correlation coefficient between the scrambled lanes array and f_13. Store the result in perm_reps_rho.
*   Compute and print the p-value. Take "at least as extreme as" to be that the Pearson correlation coefficient is greater than or equal to what was observed.
'''

# Compute observed correlation: rho
rho = dcst.pearson_r(lanes, f_13)

# Initialize permutation reps: perm_reps_rho
perm_reps_rho = np.empty(10000)

# Make permutation reps
for i in range(10000):
    # Scramble the lanes array: scrambled_lanes
    scrambled_lanes = np.random.permutation(lanes)
    
    # Compute the Pearson correlation coefficient
    perm_reps_rho[i] = dcst.pearson_r(scrambled_lanes, f_13)
    
# Compute and print p-value
p_val = np.sum(perm_reps_rho >= rho) / 10000
print('p =', p_val)

'''
p = 0.0

The p-value is very small, as you would expect from the confidence interval of the last exercise.
'''