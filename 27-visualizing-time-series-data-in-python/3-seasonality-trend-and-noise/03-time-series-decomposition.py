'''
Time series decomposition

When visualizing time series data, you should look out for some distinguishable patterns:

*   seasonality: does the data display a clear periodic pattern?
*   trend: does the data follow a consistent upwards or downward slope?
*   noise: are there any outlier points or missing values that are not consistent with the rest of the data?

You can rely on a method known as time-series decomposition to automatically extract and quantify the structure of time-series data. The statsmodels library provides the seasonal_decompose() function to perform time series decomposition out of the box.

|   decomposition = sm.tsa.seasonal_decompose(time_series)

You can extract a specific component, for example seasonality, by accessing the seasonal attribute of the decomposition object.
'''

import pandas as pd
import matplotlib.pyplot as plt

co2_levels = pd.read_csv('../datasets/ch2_co2_levels.csv', index_col=0, parse_dates=True)
co2_levels = co2_levels.fillna(method='bfill')

'''
INSTRUCTIONS

*   Import statsmodels.api using the alias sm.
*   Perform time series decomposition on the co2_levels DataFrame into a variable called decomposition.
*   Print the seasonality component of your time series decomposition.
'''

# Import statsmodels.api as sm
import statsmodels.api as sm

# Perform time series decompositon
decomposition = sm.tsa.seasonal_decompose(co2_levels)

# Print the seasonality component
print(decomposition.seasonal)