'''
Compute the ACF for Several MA Time Series

Unlike an AR(1), an MA(1) model has no autocorrelation beyond lag 1, an MA(2) model has no autocorrelation beyond lag 2, etc. The lag-1 autocorrelation for an MA(1) model is not <theta>, but rather <theta> / (1 + <theta>^2). For example, if the MA parameter, <theta>, is = +0.9, the first-lag autocorrelation will be 0.9 / (1 + (0.9)^2) = 0.497, and the autocorrelation at all other lags will be zero. If the MA parameter, <theta>, is -0.9, the first-lag autocorrelation will be -0.9 / (1 +(-0.9)^2) = -0.497.

You will verify these autocorrelation functions for the three time series you generated in the last exercise.
'''

import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.arima_process import ArmaProcess

ar1 = np.array([1])
ma1 = np.array([1, -0.9])
MA_object1 = ArmaProcess(ar1, ma1)
simulated_data_1 = MA_object1.generate_sample(nsample=1000)

ar2 = np.array([1])
ma2 = np.array([1, +0.9])
MA_object2 = ArmaProcess(ar2, ma2)
simulated_data_2 = MA_object2.generate_sample(nsample=1000)

ar3 = np.array([1])
ma3 = np.array([1, -0.3])
MA_object3 = ArmaProcess(ar3, ma3)
simulated_data_3 = MA_object3.generate_sample(nsample=1000)

'''
INSTRUCTIONS

*   simulated_data_1 is the simulated time series with an MA parameter of <theta> = -0.9, simulated_data_2 is for an MA paramter of <theta> = +0.9, and simulated_data_3 is for an MA parameter of <theta> = -0.3.
*   Compute the autocorrelation function for each of the three simulated datasets using the plot_acf function with 20 lags.
'''

# Import the plot_acf module from statsmodels
from statsmodels.graphics.tsaplots import plot_acf

# Plot three ACF on same page for comparison using subplots
fig, axes = plt.subplots(3,1)

# Plot 1: AR parameter = -0.9
plot_acf(simulated_data_1, lags=20, ax=axes[0])
axes[0].set_title("MA Parameter -0.9")

# Plot 2: AR parameter = +0.9
plot_acf(simulated_data_2, lags=20, ax=axes[1])
axes[1].set_title("MA Parameter +0.9")

# Plot 3: AR parameter = -0.3
plot_acf(simulated_data_3, lags=20, ax=axes[2])
axes[2].set_title("MA Parameter -0.3")
plt.show()
