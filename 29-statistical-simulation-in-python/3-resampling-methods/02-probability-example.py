'''
Probability example

In this exercise, we will review the difference between sampling with and without replacement. We will calculate the probability of an event using simulation, but vary our sampling method to see how it impacts probability.

Consider a bowl filled with colored candies - three blue, two green, and five yellow. Draw three candies at random, with replacement and without replacement. You want to know the probability of drawing a yellow candy on the third draw given that the first candy was blue and the second candy was green.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

'''
INSTRUCTIONS

*   Set up your sample space bowl as a list having three blue 'b', two green 'g' and five yellow 'y' candies.
*   Draw a sample of three candies with replacement (sample_rep) and without replacement (sample_no_rep).
*   Write down the success condition for drawing a yellow candy on the third draw given that the first candy was blue and the second candy was green.
*   Calculate the probability with and without replacement as successes divided by the number of iterations.
'''

# Set up the bowl
success_rep, success_no_rep, sims = 0, 0, 10000
bowl = ['b']*3 + ['g']*2 + ['y']*5

for i in range(sims):
    # Sample with and without replacement & increment success counters
    sample_rep = np.random.choice(bowl, size=3, replace=True)
    sample_no_rep = np.random.choice(bowl, size=3, replace=False)
    if (sample_rep[0] == 'b') & (sample_rep[1] == 'g') & (sample_rep[2] == 'y'): 
        success_rep += 1
    if (sample_no_rep[0] == 'b') & (sample_no_rep[1] == 'g') & (sample_no_rep[2] == 'y'): 
        success_no_rep += 1

# Calculate probabilities
print("Probability with replacement = {}, without replacement = {}".format(success_rep/sims, success_no_rep/sims))