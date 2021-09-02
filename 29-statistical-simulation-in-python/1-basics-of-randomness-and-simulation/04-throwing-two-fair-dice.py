'''
Throwing two fair dice

We now know how to implement the first two steps of a simulation. Now let's implement the next step - defining the relationship between random variables.

Often times, our simulation will involve not just one, but multiple random variables. Consider a game where throw you two dice and win if each die shows the same number. Here we have two random variables - the two dice - and a relationship between each of them - we win if they show the same number, lose if they don't. In reality, the relationship between random variables can be much more complex, especially when simulating things like weather patterns.

By the end of this exercise, you will be familiar with how to implement the third step of running a simulation - defining relationships between random variables.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(223)

'''
INSTRUCTIONS

*   Set num_dice to 2.
*   Complete the np.random.choice() function to throw two dice and record the outcomes in the outcomes variable.
*   Fill in the Boolean condition to check if the two dice show the same number.
'''

# Initialize number of dice, simulate & record outcome
die, probabilities, num_dice = [1,2,3,4,5,6], [1/6]*6, 2
outcomes = np.random.choice(die, size=num_dice, p=probabilities) 

# Win if the two dice show the same number
if outcomes[0] == outcomes[1]:
    answer = 'win' 
else:
    answer = 'lose'

print("The dice show {} and {}. You {}!".format(outcomes[0], outcomes[1], answer))