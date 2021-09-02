'''
Portfolio Simulation - Part III

Previously, we ran a complete simulation to get a distribution for 10-year returns. Now we will use simulation for decision making.

Let's go back to your stock-heavy portfolio with an expected return of 7% and a volatility of 30%. You have the choice of rebalancing your portfolio with some bonds such that the expected return is 4% & volatility is 10%. You have a principal of $10,000. You want to select a strategy based on how much your portfolio will be worth in 10 years. Let's simulate returns for both the portfolios and choose based on the least amount you can expect with 75% probability (25th percentile).

Upon completion, you will know how to use a portfolio simulation for investment decisions.

The portfolio_return() function is again pre-loaded in the environment.
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


sims = 1000
rets_stock = []
rets_bond = []

'''
INSTRUCTIONS

*   Set avg_return and volatility parameters to 0.07 and 0.3, respectively, for the stock portfolio.
*   Set avg_return and volatility parameters to 0.04 and 0.1, respectively, for the bond portfolio.
*   Calculate the 25th percentile of the distribution of returns for the stock and bond portfolios.
*   Calculate and print how much additional returns you would lose or gain by sticking with stocks instead of going to bonds.
'''

for i in range(sims):
    rets_stock.append(portfolio_return(yrs=10, avg_return=0.07, volatility=0.3, principal=10000))
    rets_bond.append(portfolio_return(yrs=10, avg_return=0.04, volatility=0.1, principal=10000))

# Calculate the 25th percentile of the distributions and the amount you'd lose or gain
rets_stock_perc = np.percentile(rets_stock, 25)
rets_bond_perc = np.percentile(rets_bond, 25)
print("Sticking to stocks gets you an additional return of {}".format(rets_stock_perc - rets_bond_perc))