'''
Birthday problem

Now we'll use simulation to solve a famous probability puzzle - the birthday problem. It sounds quite straightforward - How many people do you need in a room to ensure at least a 50% chance that two of them share the same birthday?

With 366 people in a 365-day year, we are 100% sure that at least two have the same birthday, but we only need to be 50% sure. Simulation gives us an elegant way of solving this problem.

Upon completion of this exercise, you will begin to understand how to cast problems in a simulation framework.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(111)

'''
INSTRUCTIONS 1/2

*   Initialize the sample space days which is an array from 1 - 365.
*   Define a function birthday_sim() that takes as input the number of people and returns the probability that at least two share the same birthday.
'''

# Draw a sample of birthdays & check if each birthday is unique
days = np.arange(1,366)
people = 2

def birthday_sim(people):
    sims, unique_birthdays = 2000, 0 
    for _ in range(sims):
        draw = np.random.choice(days, size=people, replace=True)
        if len(draw) == len(set(draw)): 
            unique_birthdays += 1
    out = 1 - unique_birthdays / sims
    return out

'''
INSTRUCTIONS 2/2

*   Call birthday_sim() in a while loop and break when the probability is greater than 50%.
'''

# Break out of the loop if probability greater than 0.5
while people > 0:
    prop_bds = birthday_sim(people)
    if prop_bds > 0.5: 
        break
    people += 1

print("With {} people, there's a 50% chance that two share a birthday.".format(people))
