'''
Throwing a fair die

Once you grasp the basics of designing a simulation, you can apply it to any system or process. Next, we will learn how each step is implemented using some basic examples.

As we have learned, simulation involves repeated random sampling. The first step then is to get one random sample. Once we have that, all we do is repeat the process multiple times. This exercise will focus on understanding how we get one random sample. We will study this in the context of throwing a fair six-sided die.

By the end of this exercise, you will be familiar with how to implement the first two steps of running a simulation - defining a random variable and assigning probabilities.

For the rest of the course, look to the IPython shell to find out what seed has been set.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

'''
INSTRUCTIONS

*   Construct a six-sided die as a list of each of the possible outcomes and assign it to the variable die.
*   Define the probability of each of the six sides having an equal chance of showing up and assign it to the variable probabilities.
*   Finally, use np.random.choice() to simulate a single throw of the die and record its outcome in the outcome variable.
'''

# Define die outcomes and probabilities
die, probabilities, throws = [1,2,3,4,5,6], [1/6]*6, 1

# Use np.random.choice to throw the die once and record the outcome
outcome = np.random.choice(die, size=throws, p=probabilities)
print("Outcome of the throw: {}".format(outcome[0]))