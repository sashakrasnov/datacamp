'''
Fitness goals

Let's model how activity levels impact weight loss using modern fitness trackers. On days when you go to the gym, you average around 15k steps, and around 5k steps otherwise. You go to the gym 40% of the time. Let's model the step counts in a day as a Poisson random variable with a mean <labmda> dependent on whether or not you go to the gym.

For simplicity, let’s say you have an 80% chance of losing 1lb and a 20% chance of gaining 1lb when you get more than 10k steps. The probabilities are reversed when you get less than 8k steps. Otherwise, there's an even chance of gaining or losing 1lb. Given all this, find the probability of losing weight in a month.

Examine the prob variable in the shell, which is the default probability of gaining or losing 1lb.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(222)

sims, days = 1000, 30
outcomes = []

'''
INSTRUCTIONS

*   Simulate steps as a Poisson random variable for a given day based on the value of lam.
*   Set prob to [0.2, 0.8] if steps > 10000 or to [0.8, 0.2] if steps < 8000. Sum up all the weight lost or gained in a month stored in w.
*   Calculate and print the fraction of simulations where total weight for a month in outcomes is less than 0.
'''

# Simulate steps & choose prob 
for _ in range(sims):
    w = []
    for i in range(days):
        lam = np.random.choice([5000, 15000], p=[0.6, 0.4], size=1)
        steps = np.random.poisson(lam)
        if steps > 10000: 
            prob = [0.2, 0.8]
        elif steps < 8000: 
            prob = [0.8, 0.2]
        else:
            prob = [0.5, 0.5]
        w.append(np.random.choice([1, -1], p=prob))
    outcomes.append(sum(w))

# Calculate fraction of outcomes where there was a weight loss
print("Probability of Weight Loss = {}".format(sum([x < 0 for x in outcomes])/len(outcomes)))