'''
Portfolio Simulation - Part I

In the next few exercises, you will calculate the expected returns of a stock portfolio & characterize its uncertainty.

Suppose you have invested $10,000 in your portfolio comprising of multiple stocks. You want to evaluate the portfolio's performance over 10 years. You can tweak your overall expected rate of return and volatility (standard deviation of the rate of return). Assume the rate of return follows a normal distribution.

First, let's write a function that takes the principal (initial investment), number of years, expected rate of return and volatility as inputs and returns the portfolio's total value after 10 years.

Upon completion of this exercise, you will have a function you can call to determine portfolio performance.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

'''
INSTRUCTIONS

*   For the time spent random variables, set the size such that it has shape sample_size × sims.
*   Calculate power as a fraction of p-values less than 0.05 (statistically significant).
*   If power is greater than or equal to 80%, break out of the while loop. Else, keep incrementing sample_size by 10.
'''

# rates is a Normal random variable and has size equal to number of years
def portfolio_return(yrs, avg_return, sd_of_return, principal):
    np.random.seed(123)
    rates = np.random.normal(loc=avg_return, scale=sd_of_return, size=yrs)
    # Calculate the return at the end of the period
    end_return = principal
    for x in rates:
        end_return = end_return * (1+x)
    return end_return

result = portfolio_return(yrs=5, avg_return=0.07, sd_of_return=0.15, principal=1000)
print("Portfolio return after 5 years = {}".format(result))