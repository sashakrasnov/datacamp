'''
Time series decomposition of the airline dataset

In this exercise, you will apply time series decomposition to the airline dataset, and visualize the trend and seasonal componenets.
'''

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

airline = pd.read_csv('../datasets/ch3_airline_passengers.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS 1/2

*   Import statsmodels.api using the alias sm.
*   Perform time series decomposition on the airline DataFrame into a variable called decomposition.
*   Extract the trend and seasonal components.
'''

# Import statsmodels.api as sm
import statsmodels.api as sm

# Perform time series decompositon
decomposition = sm.tsa.seasonal_decompose(airline)

# Extract the trend and seasonal components
trend = decomposition.trend
seasonal = decomposition.seasonal

'''
INSTRUCTIONS 2/2

We placed the trend and seasonal components in the airline_decomposed DataFrame.

*   Print the first 5 rows of airline_decomposed.
*   Plot these two components on the same graph.
'''

# Print the first 5 rows of airline_decomposed
print(airline_decomposed.head())

# Plot the values of the df_decomposed DataFrame
ax = airline_decomposed.plot(figsize=(12, 6), fontsize=15)

# Specify axis labels
ax.set_xlabel('Date', fontsize=15)
plt.legend(fontsize=15)
plt.show()