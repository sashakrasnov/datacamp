'''
Describe time series data with boxplots

You should always explore the distribution of the variables, and because you are working with time series, you will explore their properties using boxplots and numerical summaries. As a reminder, you can plot data in a DataFrame as boxplots with the command:

|   df.boxplot(fontsize=6, vert=False)

Notice the introduction of the new parameter vert, which specifies whether to plot the boxplots horizontally or vertically.
'''

import pandas as pd
import matplotlib.pyplot as plt

jobs = pd.read_csv('../datasets/ch5_employment.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

*   Generate a boxplot of all the time series in jobs.
*   Print out a numerical statistical summary of all the time series in jobs.
*   Review the resuts and print the name of the time series with the highest mean value and with the most variability (i.e. with the highest standard deviation).
'''

# Generate a boxplot
jobs.boxplot(fontsize=6, vert=False)
plt.show()

# Generate numerical summaries
print(jobs.describe())

# Print the name of the time series with the highest mean
print(jobs.describe().loc['mean'][jobs.describe().loc['mean'] == jobs.describe().loc['mean'].max()].index.values[0])

# Print the name of the time series with the highest variability
print(jobs.describe().loc['std'][jobs.describe().loc['std'] == jobs.describe().loc['std'].max()].index.values[0])