'''
Modeling Corn Production

Suppose that you manage a small corn farm and are interested in optimizing your costs. In this exercise, we will model the production of corn.

For simplicity, let's assume that corn production depends on only two factors: rain, which you don't control, and cost, which you control. Rain is normally distributed with mean 50 and standard deviation 15. For now, let's fix cost at 5,000. Corn produced in any season is a Poisson random variable while the average corn production is governed by the equation:

100 × (cost)^0.1 × (rain)^0.2

Let's model this production function and simulate one outcome.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(223)

'''
INSTRUCTIONS

*   Initialize rain as a normal random variable with mean 50 and standard deviation 15.
*   In the corn_produced() function, model mean_corn as 100 × cost^0.1 × rain^0.2.
*   Model corn as a Poisson random variable with mean mean_corn.
*   Simulate one outcome by storing the result of calling corn_produced() in corn_result and print your results.
'''

# Initialize variables
cost = 5000
rain = np.random.normal(50, 15)

# Corn production model
def corn_produced(rain, cost):
  mean_corn = 100 * (cost**0.1) * (rain**0.2)
  corn = np.random.poisson(mean_corn)
  return corn

# Simulate and print corn production
corn_result = corn_produced(rain, cost)
print("Simulated Corn Production = {}".format(corn_result))