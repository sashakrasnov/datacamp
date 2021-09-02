'''
Plotting a time series (I)

In this exercise, you'll practice plotting the values of two time series without the time component.

Two DataFrames, data and data2 are available in your workspace.

Unless otherwise noted, assume that all required packages are loaded with their common aliases throughout this course.
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../datasets/data.csv', usecols=[1])
data2 = pd.read_csv('../datasets/data2.csv', usecols=[0])

'''
INSTRUCTIONS 1/3

*   Print the first five rows of data.
'''

# Print the first 5 rows of data
print(data.head())

'''
INSTRUCTIONS 2/3

*   Print the first five rows of data2.
'''

# Print the first 5 rows of data2
print(data2.head())

'''
INSTRUCTIONS 3/3

*   Plot the values column of both the data sets on top of one another, one per axis object.
'''

# Plot the time series in each dataset
fig, axs = plt.subplots(2, 1, figsize=(5, 10))
data.iloc[:1000].plot(y='data_values', ax=axs[0])
data2.iloc[:1000].plot(y='data_values', ax=axs[1])
plt.show()