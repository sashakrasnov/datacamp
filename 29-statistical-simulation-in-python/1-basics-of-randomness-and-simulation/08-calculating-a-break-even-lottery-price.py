'''
Calculating a break-even lottery price

Simulations allow us to ask more nuanced questions that might not necessarily have an easy analytical solution. Rather than solving a complex mathematical formula, we directly get multiple sample outcomes. We can run experiments by modifying inputs and studying how those changes impact the system. For example, once we have a moderately reasonable model of global weather patterns, we could evaluate the impact of increased greenhouse gas emissions.

In the lottery example, we might want to know how expensive the ticket needs to be for it to not make sense to buy it. To understand this, we need to modify the ticket cost to see when the expected payoff is negative.

grand_prize, num_tickets, and chance_of_winning are loaded in the environment.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(333)

num_tickets, grand_prize = 1000, 1000000
chance_of_winning = 1/num_tickets

'''
INSTRUCTIONS

*   Set sims to 3000 and the lottery_ticket_cost variable to 0.
*   Within the while loop, break if the mean value of outcomes falls below zero.
*   Otherwise, increment lottery_ticket_cost by 1.
'''

# Initialize simulations and cost of ticket
sims, lottery_ticket_cost = 3000, 0

# Use a while loop to increment `lottery_ticket_cost` till average value of outcomes falls below zero
while 1:
    outcomes = np.random.choice([-lottery_ticket_cost, grand_prize-lottery_ticket_cost],
                 size=sims, p=[1-chance_of_winning, chance_of_winning], replace=True)
    if outcomes.mean() < 0:
        break
    else:
        lottery_ticket_cost += 1
answer = lottery_ticket_cost - 1

print("The highest price at which it makes sense to buy the ticket is {}".format(answer))