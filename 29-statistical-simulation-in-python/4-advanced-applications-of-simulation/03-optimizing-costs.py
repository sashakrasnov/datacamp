'''
Optimizing Costs

Now we will use the functions you've built to optimize our cost of production. We are interested in maximizing average profits. However, our profits depend on a number of factors, but we only control cost. Thus, we can simulate the uncertainty in the other factors and vary cost to see how our profits are impacted.

Since you manage the small corn farm, you have the ability to choose your cost - from $100 to $5,000. You want to choose the cost that gives you the maximum average profit. In this exercise, we will simulate multiple outcomes for each cost level and calculate an average. We will then choose the cost that gives us the maximum mean profit. Upon completion, you will have a framework for selecting optimal inputs for business decisions.
'''

import numpy as np

# Corn production model
def corn_produced(rain, cost):
  mean_corn = 100 * (cost**0.1) * (rain**0.2)
  corn = np.random.poisson(mean_corn)
  return corn


def corn_demanded(price):
    mean_corn = 1000 - 8*price
    corn = np.random.poisson(abs(mean_corn))
    return corn


# Function to calculate profits
def profits(cost):
    rain = np.random.normal(50, 15)
    price = np.random.normal(40, 10)
    supply = corn_produced(rain, cost)
    demand = corn_demanded(price)
    equil_short = supply <= demand
    if equil_short == True:
        tmp = supply*price - cost
        return tmp
    else:
        tmp2 = demand*price - cost
        return tmp2


# Set random seed to get the same result or remove for different each time
np.random.seed(223)

'''
INSTRUCTIONS

*   Initialize the empty dictionary results.
*   For each cost level, simulate profits using the pre-loaded profits() function and append them to tmp_profits.
*   Store the average of tmp_profits for each cost level in the results dictionary.
*   Find the cost level that has the maximum average profit by running results through the list comprehension.
'''

# Initialize results and cost_levels variables
sims, results = 1000, {}
cost_levels = np.arange(100, 5100, 100)

# For each cost level, simulate profits and store mean profit
for cost in cost_levels:
    tmp_profits = []
    for i in range(sims):
        tmp_profits.append(profits(cost))
    results[cost] = np.mean(tmp_profits)
    
# Get the cost that maximizes average profit
print("Average profit is maximized when cost = {}".format([x for x in results.keys() if results[x] == max(results.values())][0]))