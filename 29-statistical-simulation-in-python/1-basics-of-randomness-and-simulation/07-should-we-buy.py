'''
Should we buy?

In the last exercise, we simulated the random drawing of the lottery ticket once. In this exercise, we complete the simulation process by repeating the process multiple times.

Repeating the process gives us multiple outcomes. We can think of this as multiple universes where the same lottery drawing occurred. We can then determine the average winnings across all these universes. If the average winnings are greater than what we pay for the ticket then it makes sense to buy it, otherwise, we might not want to buy the ticket.

This is typically how simulations are used for evaluating business investments. After completing this exercise, you will have the basic tools required to use simulations for decision-making.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

'''
INSTRUCTIONS

*   Set the size parameter, which controls the number of simulations, to 2000.
*   Set payoffs equal to a list containing how much you could lose and how much you could win.
*   Set probs equal to a list of probabilities of losing and winning.
*   Calculate the mean of outcomes and assign it to answer.
'''

# Initialize size and simulate outcome
lottery_ticket_cost, num_tickets, grand_prize = 10, 1000, 1000000
chance_of_winning = 1/num_tickets
size = 2000
payoffs = [-lottery_ticket_cost, grand_prize-lottery_ticket_cost]
probs = [1-chance_of_winning, chance_of_winning]

outcomes = np.random.choice(a=payoffs, size=size, p=probs, replace=True)

# Mean of outcomes
answer = outcomes.mean()
print("Average payoff from {} simulations = {}".format(size, answer))
