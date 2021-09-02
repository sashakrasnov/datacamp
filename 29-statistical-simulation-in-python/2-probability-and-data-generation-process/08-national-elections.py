'''
National elections

This exercise will give you a taste of how you can model a DGP at different levels of complexity.

Consider national elections in a country with two political parties - Red and Blue. This country has 50 states and the party that wins the most states wins the elections. You have the probability p of Red winning in each individual state and want to know the probability of Red winning nationally.

Let's model the DGP to understand the distribution. Suppose the election outcome in each state follows a binomial distribution with probability p such that 0 indicates a loss for Red and 1 indicates a win. We then simulate a number of election outcomes. Finally, we can ask rich questions like what is the probability of Red winning less than 45% of the states?
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(224)

# Elections for Red
p = np.random.rand(50)

'''
INSTRUCTIONS

*   Simulate one election using np.random.binomial() with p = probs and n=1. Assign it to election.
*   Append the average of Red's wins in election to outcomes.
*   Calculate the fraction of outcomes where Red won less than 45% of the states.
'''

outcomes, sims, probs = [], 1000, p

for _ in range(sims):
    # Simulate elections in the 50 states
    election = np.random.binomial(p=probs, n=1)
    # Get average of Red wins and add to `outcomes`
    outcomes.append(election.mean())

# Calculate probability of Red winning in less than 45% of the states
print("Probability of Red winning in less than 45% of the states = {}".format(sum(np.array(outcomes) < 0.45)/sims))