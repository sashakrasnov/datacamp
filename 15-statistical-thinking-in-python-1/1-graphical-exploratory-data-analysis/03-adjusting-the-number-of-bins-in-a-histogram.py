'''
Adjusting the number of bins in a histogram

The histogram you just made had ten bins. This is the default of matplotlib. The "square root rule" is a commonly-used rule of thumb for choosing number of bins: choose the number of bins to be the square root of the number of samples. Plot the histogram of Iris versicolor petal lengths again, this time using the square root rule for the number of bins. You specify the number of bins using the bins keyword argument of plt.hist().

The plotting utilities are already imported and the seaborn defaults already set. The variable you defined in the last exercise, versicolor_petal_length, is already in your namespace.
'''

import pandas as pd

df = pd.read_csv('../datasets/iris.csv')

versicolor_petal_length = df[df.species=='versicolor']['petal length (cm)'].values

'''
INSTRUCTIONS

*   Import numpy as np. This gives access to the square root function, np.sqrt().
*   Determine how many data points you have using len().
*   Compute the number of bins using the square root rule.
*   Convert the number of bins to an integer using the built in int() function.
*   Generate the histogram and make sure to use the bins keyword argument.
*   Hit 'Submit Answer' to plot the figure and see the fruit of your labors!
'''

# Import numpy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Plot the histogram
_ = plt.hist(versicolor_petal_length, bins=n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()

