'''
The standard deviation and the variance

As mentioned in the video, the standard deviation is the square root of the variance. You will see this for yourself by computing the standard deviation using np.std() and comparing it to what you get by computing the variance with np.var() and then computing the square root.
'''

import pandas as pd
import numpy as np

df = pd.read_csv('../datasets/iris.csv')

versicolor_petal_length = df[df.species == 'versicolor']['petal length (cm)'].values

'''
INSTRUCTIONS

*   Compute the variance of the data in the versicolor_petal_length array using np.var().
*   Print the square root of this value.
*   Compute the standard deviation of the data in the versicolor_petal_length array using np.std() and print the result.
'''

# Compute the variance: variance
variance = np.var(versicolor_petal_length)

# Print the square root of the variance
print(np.sqrt(variance))

# Print the standard deviation
print(np.std(versicolor_petal_length))
