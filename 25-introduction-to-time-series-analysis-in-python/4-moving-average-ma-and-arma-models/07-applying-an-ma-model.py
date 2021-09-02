'''
Applying an MA Model

The bouncing of the stock price between bid and ask induces a negative first order autocorrelation, but no autocorrelations at lags higher than 1. You get the same ACF pattern with an MA(1) model. Therefore, you will fit an MA(1) model to the intraday stock data from the last exercise.

The first step is to compute minute-by-minute returns from the prices in intraday, and plot the autocorrelation function. You should observe that the ACF looks like that for an MA(1) process. Then, fit the data to an MA(1), the same way you did for simulated data.
'''

import pandas as pd
import matplotlib.pyplot as plt

intraday = pd.read_csv('../datasets/Sprint_Intraday.txt', header=None, usecols=[0,1])

intraday.iloc[0,0] = 0
intraday.columns = ['DATE','CLOSE']
intraday['DATE'] = pd.to_numeric(intraday['DATE'])
intraday = intraday.set_index('DATE')

intraday = intraday.reindex(range(391), method='ffill')
intraday.index = pd.date_range(start='2017-08-28 9:30', end='2017-08-28 16:00', freq='1min')

'''
INSTRUCTIONS

*   Import plot_acf and ARMA modules from statsmodels
*   Compute minute-to-minute returns from prices:
    *   Compute returns with the .pct_change() method
    *   Use the pandas method .dropna() to drop the first row of returns, which is NaN
*   Plot the ACF function with lags up to 60 minutes
*   Fit the returns data to an MA(1) model and print out the MA(1) parameter
'''

# Import plot_acf and ARMA modules from statsmodels
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_model import ARMA

# Compute returns from prices and drop the NaN
returns = intraday.pct_change()
returns = returns.dropna()

# Plot ACF of returns with lags up to 60 minutes
plot_acf(returns, lags=60)
plt.show()

# Fit the data to an MA(1) model
mod = ARMA(returns, order=(0,1))
res = mod.fit()
print(res.params)
