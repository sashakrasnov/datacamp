'''
Plot monthly and yearly trends

Like we saw in Chapter 2, when the index of a DataFrame is of the datetime type, it is possible to directly extract the day, month or year of each date in the index. As a reminder, you can extract the year of each date in the index using the .index.year attribute. You can then use the .groupby() and .mean() methods to compute the mean annual value of each time series in your DataFrame:

|   index_year = df.index.year
|   df_by_year = df.groupby(index_year).mean()

You will now apply what you have learned to display the aggregate mean values of each time series in the jobs DataFrame.
'''

import pandas as pd
import matplotlib.pyplot as plt

jobs = pd.read_csv('../datasets/ch5_employment.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS 1/2

*   Extract the month for each of the dates in the index of jobs and assign them to index_month.
*   Compute the monthly mean unemployment rate in jobs and assign it to jobs_by_month.
*   Plot all the columns of jobs_by_month.
'''

# Extract the month from the index of jobs
index_month = jobs.index.month

# Compute the mean unemployment rate for each month
jobs_by_month = jobs.groupby(index_month).mean()

# Plot the mean unemployment rate for each month
ax = jobs_by_month.plot(fontsize=6, linewidth=1)

# Set axis labels and legend
ax.set_xlabel('Month', fontsize=10)
ax.set_ylabel('Mean unemployment rate', fontsize=10)
ax.legend(bbox_to_anchor=(0.8, 0.6), fontsize=10)
plt.show()

'''
INSTRUCTIONS 2/2

*   Extract the year for each of the dates in the index of jobs and assign them to index_year.
*   Compute the yearly mean unemployment rate in jobs and assign it to jobs_by_year.
*   Plot all the columns of jobs_by_year.
'''

# Extract of the year in each date indices of the jobs DataFrame
index_year = jobs.index.year

# Compute the mean unemployment rate for each year
jobs_by_year = jobs.groupby(index_year).mean()

# Plot the mean unemployment rate for each year
ax = jobs_by_year.plot(fontsize=6, linewidth=1)

# Set axis labels and legend
ax.set_xlabel('Year', fontsize=10)
ax.set_ylabel('Mean unemployment rate', fontsize=10)
ax.legend(bbox_to_anchor=(0.1, 0.5), fontsize=10)
plt.show()