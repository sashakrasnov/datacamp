'''
Visualize the seasonality of multiple time series

You will now extract the seasonality component of jobs_decomp to visualize the seasonality in these time series. Note that before plotting, you will have to convert the dictionary of seasonality components into a DataFrame using the pd.DataFrame.from_dict() function.

An empty dictionary jobs_seasonal and the time series decompisiton object jobs_decomp from the previous exercise are available in your workspace.
'''

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

jobs = pd.read_csv('../datasets/ch5_employment.csv', index_col=0, parse_dates=True)

# Initialize dictionary
jobs_decomp = {}

# Get the names of each time series in the DataFrame
jobs_names = jobs.columns.tolist()

# Run time series decomposition on each time series of the DataFrame
for ts in jobs_names:
    ts_decomposition = sm.tsa.seasonal_decompose(jobs[ts])
    jobs_decomp[ts] = ts_decomposition

jobs_seasonal = {}
'''
INSTRUCTIONS

*   Iterate through each column name in jobs_names and extract the corresponding seasonal component from jobs_decomp. Place the results in the jobs_seasonal, where the column name is the name of the time series, and the value is the seasonal component of the time series.
*   Convert jobs_seasonal to a DataFrame and call it seasonality_df.
*   Create a facetted plot of all 16 columns in seasonality_df. Ensure that the subgraphs do not share y-axis.
'''

# Extract the seasonal values for the decomposition of each time series
for ts in jobs_names:
    jobs_seasonal[ts] = jobs_decomp[ts].seasonal
    
# Create a DataFrame from the jobs_seasonal dictionnary
seasonality_df = pd.DataFrame.from_dict(jobs_seasonal)

# Remove the label for the index
seasonality_df.index.name = None

# Create a faceted plot of the seasonality_df DataFrame
seasonality_df.plot(subplots=True,
                   layout=(4,4),
                   sharey=False,
                   fontsize=2,
                   linewidth=0.3,
                   legend=False)

# Show plot
plt.show()