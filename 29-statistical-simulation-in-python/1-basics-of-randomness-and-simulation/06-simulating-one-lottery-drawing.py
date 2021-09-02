'''
Simulating one lottery drawing

In the last three exercises of this chapter, we will be bringing together everything you've learned so far. We will run a complete simulation, take a decision based on our observed outcomes, and learn to modify inputs to the simulation model.

We will use simulations to figure out whether or not we want to buy a lottery ticket. Suppose you have the opportunity to buy a lottery ticket which gives you a shot at a grand prize of $1 Million. Since there are 1000 tickets in total, your probability of winning is 1 in 1000. Each ticket costs $10. Let's use our understanding of basic simulations to first simulate one drawing of the lottery.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

'''
INSTRUCTIONS

*   Define chance_of_winning as the probability of winning the lottery.
    *   Remember that 1 out of the total number of lottery tickets sold will win.
*   Set the probability list, which includes the probability of winning the lottery, as defined by chance_of_winning and its complement.
*   Use np.random.choice() to perform one simulation of this lottery drawing.
'''

# Pre-defined constant variables
lottery_ticket_cost, num_tickets, grand_prize = 10, 1000, 1000000

# Probability of winning
chance_of_winning = 1/num_tickets

# Simulate a single drawing of the lottery
gains = [-lottery_ticket_cost, grand_prize-lottery_ticket_cost]
probability = [1-chance_of_winning, chance_of_winning]
outcome = np.random.choice(a=gains, size=1, p=probability, replace=True)

print("Outcome of one drawing of the lottery is {}".format(outcome))