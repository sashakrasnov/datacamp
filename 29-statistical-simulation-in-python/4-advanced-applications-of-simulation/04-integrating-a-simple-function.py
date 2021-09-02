'''
Integrating a Simple Function

This is a simple exercise introducing the concept of Monte Carlo Integration.

Here we will evaluate a simple integral ∫(1,0)x*e^x(dx). We know that the exact answer is 1, but simulation will give us an approximate solution, so we can expect an answer close to 1. As we saw in the video, it's a simple process. For a function of a single variable f(x):

    1. Get the limits of the x-axis (x_min,x_max) and y-axis (max(f(x)),min(min(f(x)),0)).
    2. Generate a number of uniformly distributed point in this box.
    3. Multiply the area of the box ((max(f(x)−min(f(x))*(x_max−x_min)) by the fraction of points that lie below f(x).

Upon completion, you will have a framework for handling definite integrals using Monte Carlo Integration.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

'''
INSTRUCTIONS

*   In the sim_integrate() function, generate uniform random numbers between xmin and xmax and assign to x.
*   Generate uniform random numbers between min(min(f(x)),0) and max(f(x)) and assign to y.
*   Return the fraction of points less than f(x) multiplied by area ((max(f(x)−min(f(x))×(xmax−xmin)) .
*   Finally, use lambda function to define func as x * e^x.
'''

# Define the sim_integrate function
def sim_integrate(func, xmin, xmax, sims):
    x = np.random.uniform(xmin, xmax, sims)
    y = np.random.uniform(min(min(func(x)),0), max(func(x)), sims)
    area = (max(y) - min(y))*(xmax-xmin)
    result = area * sum(abs(y) < abs(func(x)))/sims
    return result
    
# Call the sim_integrate function and print results
result = sim_integrate(func = lambda x: x*np.exp(x), xmin = 0, xmax = 1, sims = 50)
print("Simulated answer = {}, Actual Answer = 1".format(result))