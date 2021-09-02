'''
The conditional urn

As we've learned, conditional probability is defined as the probability of an event given another event. To illustrate this concept, let's turn to an urn problem.

We have an urn that contains 7 white and 6 black balls. Four balls are drawn at random. We'd like to know the probability that the first and third balls are white, while the second and the fourth balls are black.

Upon completion, you will learn to manipulate simulations to calculate simple conditional probabilities.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

'''
INSTRUCTIONS

*   Initialize the counter success to 0 and sims to 5000.
*   Define a list, urn, with 7 white balls ('w') and 6 black balls ('b').
*   Draw 4 balls without replacement and check to see if the first and third are white and second and fourth are black.
*   Increment success if the above criterion is met.
'''

# Initialize success, sims and urn
success, sims = 0, 5000
urn = ['w']*7 + ['b']*6

for _ in range(sims):
    # Draw 4 balls without replacement
    draw = np.random.choice(urn, replace=False, size=4)
    # Count the number of successes
    if draw[0]==draw[2]=='w' and draw[1]==draw[3]=='b':
        success += 1

print("Probability of success = {}".format(success/sims))