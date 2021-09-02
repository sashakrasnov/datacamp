'''
Which ARMA Model is Best?

Fit the temperature data to an AR(1), AR(2), MA(1), and ARMA(1,1) and see which model is the best fit, using the AIC criterion.
'''

import pandas as pd

temp_NY = pd.read_csv('../datasets/NOAA_TAVG.csv', index_col=0)

chg_temp = temp_NY.diff()
chg_temp = chg_temp.dropna()

'''
INSTRUCTIONS

*   For each ARMA model, create an instance of the ARMA class called mod using the argument order=(p,q)
*   Fit the model mod using the method fit() and save it in a results object called res
*   Print the AIC value, found in res.aic
'''

# Import the module for estimating an ARMA model
from statsmodels.tsa.arima_model import ARMA

# Fit the data to an AR(1) model and print AIC:
mod = ARMA(chg_temp, order=(1,0))
res = mod.fit()
print("The AIC for an AR(1) is: ", res.aic)

# Fit the data to an AR(2) model and print AIC:
mod = ARMA(chg_temp, order=(2,0))
res = mod.fit()
print("The AIC for an AR(2) is: ", res.aic)

# Fit the data to an MA(1) model and print AIC:
mod = ARMA(chg_temp, order=(0,1))
res = mod.fit()
print("The AIC for an MA(1) is: ", res.aic)

# Fit the data to an ARMA(1,1) model and print AIC:
mod = ARMA(chg_temp, order=(1,1))
res = mod.fit()
print("The AIC for an ARMA(1,1) is: ", res.aic)