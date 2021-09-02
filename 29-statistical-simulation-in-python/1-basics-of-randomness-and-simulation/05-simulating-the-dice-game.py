'''
Simulating the dice game

We now know how to implement the first three steps of a simulation. Now let's consider the next step - repeated random sampling.

Simulating an outcome once doesn't tell us much about how often we can expect to see that outcome. In the case of the dice game from the previous exercise, it's great that we won once. But suppose we want to see how many times we can expect to win if we played this game multiple times, we need to repeat the random sampling process many times. Repeating the process of random sampling is helpful to understand and visualize inherent uncertainty and deciding next steps.

Following this exercise, you will be familiar with implementing the fourth step of running a simulation - sampling repeatedly and generating outcomes.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(223)

'''
INSTRUCTIONS

*   Set sims to 100 repetitions and initialize wins to 0.
*   Write a for loop to repeat throwing the dice.
*   Set outcomes to the outcome of throwing two dice.
*   If the two dice show the same number, increment wins by 1.
'''

# Initialize model parameters & simulate dice throw
die, probabilities, num_dice = [1,2,3,4,5,6], [1/6]*6, 2
sims, wins = 100, 0

for i in range(sims):
    outcomes = np.random.choice(die, size=num_dice, p=probabilities)
    # Increment `wins` by 1 if the dice show same number
    if outcomes[0] == outcomes[1]: 
        wins = wins + 1 

print("In {} games, you win {} times".format(sims, wins))