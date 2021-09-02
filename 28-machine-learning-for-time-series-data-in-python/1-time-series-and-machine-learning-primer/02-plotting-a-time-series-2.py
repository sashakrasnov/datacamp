'''
Plotting a time series (II)

You'll now plot both the datasets again, but with the included time stamps for each (stored in the column called "time"). Let's see if this gives you some more context for understanding each time series data.
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../datasets/data.csv', parse_dates=['time'])
data2 = pd.read_csv('../datasets/data2.csv')

'''
INSTRUCTIONS

*   Plot data and data2 on top of one another, one per axis object.
*   The x-axis should represent the time stamps and the y-axis should represent the dataset values.
'''

# Plot the time series in each dataset
fig, axs = plt.subplots(2, 1, figsize=(5, 10))
data.iloc[:1000].plot(x='time', y='data_values', ax=axs[0])
data2.iloc[:1000].plot(x='time', y='data_values', ax=axs[1])
plt.show()