'''
Bootstrapping regression

Now let's see how bootstrapping works with regression. Bootstrapping helps estimate the uncertainty of non-standard estimators. Consider the R^2 statistic associated with a regression. When you run a simple least squares regression, you get a value for R^2. But let's see how can we get a 95% CI for R^2.

Examine the DataFrame df with a dependent variable y and two independent variables X1 and X2 using df.head(). We've already fit this regression with statsmodels (sm) using:

|   reg_fit = sm.OLS(df['y'], df.iloc[:,1:]).fit()

Examine the result using reg_fit.summary() to find that R^2=0.3504. Use bootstrapping to calculate the 95% CI.
'''

import numpy as np
import pandas as pd
import statsmodels.regression.linear_model as sm

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

# Default dataset with the heights and weights of 1000 students by DataCamp
df = pd.read_csv('../datasets/intercept.csv', index_col=0)

'''
INSTRUCTIONS

*   Use the .sample() method ondf to generate a sample of the data with replacement and assign it to tmp_df.
*   For each generated dataset in tmp_df, calculate the median heights and correlation between heights and weights using .median() and .corr().
*   Append the median heights to height_medians and correlation to hw_corr.
*   Finally calculate the 95% confidence intervals for each of the above quantities using np.percentile().
'''

rsquared_boot, coefs_boot, sims = [], [], 1000
reg_fit = sm.OLS(df['y'], df.iloc[:,1:]).fit()

# Run 1K iterations
for i in range(sims):
    # First create a bootstrap sample with replacement with n=df.shape[0]
    bootstrap = df.sample(n=df.shape[0], replace=True)
    # Fit the regression and append the r square to rsquared_boot
    rsquared_boot.append(sm.OLS(bootstrap['y'],bootstrap.iloc[:,1:]).fit().rsquared)

# Calculate 95% CI on rsquared_boot
print("R Squared 95% CI = {}".format(np.percentile(rsquared_boot, [2.5, 97.5])))