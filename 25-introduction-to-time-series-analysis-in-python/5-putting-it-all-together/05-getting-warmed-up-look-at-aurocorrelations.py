'''
Getting "Warmed" Up: Look at Autocorrelations

Since the temperature series, temp_NY, is a random walk with drift, take first differences to make it stationary. Then compute the sample ACF and PACF. This will provide some guidance on the order of the model.
'''

import pandas as pd
import matplotlib.pyplot as plt

temp_NY = pd.read_csv('../datasets/NOAA_TAVG.csv', index_col=0)

'''
INSTRUCTIONS

*   Import the modules for plotting the sample ACF and PACF
*   Take first differences of the DataFrame temp_NY using the pandas method .diff()
*   Create two subplots for plotting the ACF and PACF
*   Plot the sample ACF of the differenced series
*   Plot the sample PACF of the differenced series
'''

# Import the modules for plotting the sample ACF and PACF
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Take first difference of the temperature Series
chg_temp = temp_NY.diff()
chg_temp = chg_temp.dropna()

# Plot the ACF and PACF on the same page
fig, axes = plt.subplots(2,1)

# Plot the ACF
plot_acf(chg_temp, lags=20, ax=axes[0])

# Plot the PACF
plot_pacf(chg_temp, lags=20, ax=axes[1])
plt.show()