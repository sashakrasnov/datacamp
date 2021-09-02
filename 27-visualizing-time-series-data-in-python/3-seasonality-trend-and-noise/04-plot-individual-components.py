'''
Plot individual components

It is also possible to extract other inferred quantities from your time-series decomposition object. The following code shows you how to extract the observed, trend and noise (or residual, resid) components.

|   observed = decomposition.observed
|   trend = decomposition.trend
|   residuals = decomposition.resid

You can then use the extracted components and plot them individually.

The decomposition object you created in the last exercise is available in your workspace.
'''

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

co2_levels = pd.read_csv('../datasets/ch2_co2_levels.csv', index_col=0, parse_dates=True)
co2_levels = co2_levels.fillna(method='bfill')

decomposition = sm.tsa.seasonal_decompose(co2_levels)

'''
INSTRUCTIONS

*   Extract the trend component from the decomposition object.
*   Plot this trend component.
'''

# Extract the trend component
trend = decomposition.trend

# Plot the values of the trend
ax = trend.plot(figsize=(12, 6), fontsize=6)

# Specify axis labels
ax.set_xlabel('Date', fontsize=10)
ax.set_title('Seasonal component the CO2 time-series', fontsize=10)
plt.show()