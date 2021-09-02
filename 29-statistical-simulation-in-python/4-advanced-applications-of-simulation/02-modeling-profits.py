'''
Modeling Profits

In the previous exercise, you built a model of corn production. For a small farm, you typically have no control over the price or demand for corn. Suppose that price is normally distributed with mean 40 and standard deviation 10. You are given a function corn_demanded(), which takes the price and determines the demand for corn. This is reasonable because demand is usually determined by the market and is not in your control.

In this exercise, you will work on a function to calculate the profit by pulling together all the other simulated variables. The only input to this function will be the cost. Upon completion, you will have a function that will give you one simulated profit outcome for a given cost. This function can then be used for planning your costs.
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


# Set random seed to get the same result or remove for different each time
np.random.seed(223)

# Initialize variables
cost = 5000

'''
INSTRUCTIONS

*   Model the price as a normal random variable with mean 40 and standard deviation 10.
*   Get the corn supply by calling the function corn_produced(rain, cost), which you designed in the previous exercise.
*   You are given a corn_demanded() function which takes price as an input. Call this function to get demand.
*   Calculate the profit depending on the relationship between supply and demand of corn.
'''

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
result = profits(cost)
print("Simulated profit = {}".format(result))