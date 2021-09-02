'''
Computing the Pearson correlation coefficient

As mentioned in the video, the Pearson correlation coefficient, also called the Pearson r, is often easier to interpret than the covariance. It is computed using the np.corrcoef() function. Like np.cov(), it takes two arrays as arguments and returns a 2D array. Entries [0,0] and [1,1] are necessarily equal to 1 (can you think about why?), and the value we are after is entry [0,1].

In this exercise, you will write a function, pearson_r(x, y) that takes in two arrays and returns the Pearson correlation coefficient. You will then use this function to compute it for the petal lengths and widths of I. versicolor.

Again, we include the scatter plot you generated in a previous exercise to remind you how the petal width and length are related.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../datasets/iris.csv')

versicolor_petal_length = df[df.species == 'versicolor']['petal length (cm)'].values
versicolor_petal_width = df[df.species == 'versicolor']['petal width (cm)'].values

'''
INSTRUCTIONS

*   Define a function with signature pearson_r(x, y).
    *   Use np.corrcoef() to compute the correlation matrix of x and y (pass them to np.corrcoef() in that order).
    *   The function returns entry [0,1] of the correlation matrix.
*   Compute the Pearson correlation between the data in the arrays versicolor_petal_length and versicolor_petal_width. Assign the result to r.
*   Print the result.
'''

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0, 1]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)

# Print the result
print(r)
