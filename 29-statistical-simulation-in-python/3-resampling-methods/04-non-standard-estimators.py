'''
Non-standard estimators

In the last exercise, you ran a simple bootstrap that we will now modify for more complicated estimators.

Suppose you are studying the health of students. You are given the height and weight of 1000 students and are interested in the median height as well as the correlation between height and weight and the associated 95% CI for these quantities. Let's use bootstrapping.

Examine the pandas DataFrame df with the heights and weights of 1000 students. Using this, calculate the 95% CI for both the median height as well as the correlation between height and weight.
'''

import numpy as np
import pandas as pd

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

# Default dataset with the heights and weights of 1000 students by DataCamp
df = pd.read_csv('../datasets/heights_weights.csv', index_col=0)

# Randomly generated example with near the same mean values
#df = pd.DataFrame({'heights':np.random.rand(1000)*3+4.5, 'weights':np.random.rand(1000)*150+130})

'''
INSTRUCTIONS

*   Use the .sample() method ondf to generate a sample of the data with replacement and assign it to tmp_df.
*   For each generated dataset in tmp_df, calculate the median heights and correlation between heights and weights using .median() and .corr().
*   Append the median heights to height_medians and correlation to hw_corr.
*   Finally calculate the 95% confidence intervals for each of the above quantities using np.percentile().
'''

# Sample with replacement and calculate quantities of interest
sims, data_size, height_medians, hw_corr = 1000, df.shape[0], [], []
for i in range(sims):
    tmp_df = df.sample(n=data_size, replace=True)
    height_medians.append(tmp_df.heights.median())
    hw_corr.append(tmp_df.corr()['heights']['weights'])

# Calculate confidence intervals
print("Height Median CI = {} \nHeight Weight Correlation CI = {}".format(np.percentile(height_medians, [2.5, 97.5]) , np.percentile(hw_corr, [2.5, 97.5])))