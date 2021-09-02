'''
Plot all the time series in your dataset

The jobs DataFrame contains 16 time series representing the unemployment rate of various industries between 2001 and 2010. This may seem like a large amount of time series to visualize at the same time, but Chapter 4 introduced you to facetted plots. In this exercise, you will explore some of the time series in the jobs DataFrame and look to extract some meaningful information from these plots.
'''

import pandas as pd
import matplotlib.pyplot as plt

jobs = pd.read_csv('../datasets/ch5_employment.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

*   Review the first 5 rows of jobs_subset.
*   Create a faceted plot of the new jobs_subset DataFrame using a layout of 2 rows and 2 columns. Make sure to also specify that the subgraphs do not share x-axis and y-axis values.
'''

# A subset of the jobs DataFrame
jobs_subset = jobs[['Finance', 'Information', 'Manufacturing', 'Construction']]

# Print the first 5 rows of jobs_subset
print(jobs_subset.head(5))

# Create a facetted graph with 2 rows and 2 columns
ax = jobs_subset.plot(subplots=True,
                      layout=(2,2),
                      sharex=False,
                      sharey=False,
                      linewidth=0.7,
                      fontsize=3,
                      legend=False)

plt.show()