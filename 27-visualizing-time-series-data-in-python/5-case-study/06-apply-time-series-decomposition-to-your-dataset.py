'''
Apply time series decomposition to your dataset

You will now perform time series decomposition on multiple time series. You can achieve this by leveraging the Python dictionary to store the results of each time series decomposition.

In this exercise, you will initialize an empty dictionary with a set of curly braces, {}, use a for loop to iterate through the columns of the DataFrame and apply time series decomposition to each time series. After each time series decomposition, you place the results in the dictionary by using the command my_dict[key] = value, where my_dict is your dictionary, key is the name of the column/time series, and value is the decomposition object of that time series.
'''

import pandas as pd
import statsmodels.api as sm

jobs = pd.read_csv('../datasets/ch5_employment.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

*   Initialize an empty dictionary called jobs_decomp.
*   Extract the column names of the jobs DataFrame and place the results in a list called jobs_names.
*   Iterate through each column in jobs_names and apply time series decomposition to that time series. Place the results in the jobs_decomp dictionary, where the column name is the key, and the value is the decomposition of the time series you just performed.
'''

# Initialize dictionary
jobs_decomp = {}

# Get the names of each time series in the DataFrame
jobs_names = jobs.columns.tolist()

# Run time series decomposition on each time series of the DataFrame
for ts in jobs_names:
    ts_decomposition = sm.tsa.seasonal_decompose(jobs[ts])
    jobs_decomp[ts] = ts_decomposition