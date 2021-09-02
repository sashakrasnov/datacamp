'''
Portfolio Simulation - Part II

Now we will use the simulation function you built to evaluate 10-year returns.

Your stock-heavy portfolio has an initial investment of $10,000, an expected return of 7% and a volatility of 30%. You want to get a 95% confidence interval of what your investment will be worth in 10 years. We will simulate multiple samples of 10-year returns and calculate the confidence intervals on the distribution of returns.

By the end of this exercise, you will have run a complete portfolio simulation.

The function portfolio_return() from the previous exercise is already initialized in the environment.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

# rates is a Normal random variable and has size equal to number of years
def portfolio_return(yrs, avg_return, volatility, principal):
    rates = np.random.normal(loc=avg_return, scale=volatility, size=yrs)
    end_return = principal
    for x in rates:
        end_return = end_return * (1+x)
    return end_return


'''
INSTRUCTIONS

*   Initialize sims to 1,000.
*   Enter the appropriate values for the portfolio_return() function parameters.
*   Calculate the 95% confidence interval lower and upper limits.
'''

# Run 1,000 iterations and store the results
sims = 1000
rets = []

for i in range(sims):
    rets.append(portfolio_return(yrs = 10,
                                 avg_return = 0.07, 
                                 volatility = 0.3, 
                                 principal = 10000))

# Calculate the 95% CI
print("95% CI of Returns: Lower = {}, Upper = {}".format(np.percentile(rets, 2.5), np.percentile(rets, 97.5)))